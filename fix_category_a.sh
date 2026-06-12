#!/bin/bash
# Category A fixer: Remove dirt_provider and force_dirt from tree configs

cd "c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7"

# Find all configured_feature/placed_feature files with dirt_provider or force_dirt
files=$(grep -r "dirt_provider\|force_dirt" data/ --include="*.json" -l)

count=0
for file in $files; do
  # Use jq to remove the keys at all levels
  # This handles nested structures by recursively removing dirt_provider and force_dirt
  jq 'walk(if type == "object" then del(.dirt_provider, .force_dirt) else . end)' "$file" > "$file.tmp"

  # Check if anything changed
  if ! diff -q "$file" "$file.tmp" > /dev/null 2>&1; then
    mv "$file.tmp" "$file"
    git add "$file"
    git commit -m "Remove dirt_provider and force_dirt from $(basename "$file")"
    count=$((count + 1))

    # Every 50 commits, run verification
    if [ $((count % 50)) -eq 0 ]; then
      echo "Processed $count files, running verification..."
      grep -r "dirt_provider" data/ --include="*.json" -l | wc -l
      grep -r "force_dirt" data/ --include="*.json" -l | wc -l
    fi
  else
    rm "$file.tmp"
  fi
done

echo "Total files processed: $count"
