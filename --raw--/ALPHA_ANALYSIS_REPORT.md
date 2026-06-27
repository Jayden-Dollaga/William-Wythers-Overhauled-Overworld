# Alpha Analysis Report: wwoo-26.2-port-fixed

Date: 2026-06-25
Scope: Read-only analysis of [wwoo-26.2-port-fixed](wwoo-26.2-port-fixed) versus [WWOO_ORIGINAL](WWOO_ORIGINAL) and [26.1.2](26.1.2).

## Executive summary

The 26.2 alpha is best understood as a selective rewrite and pruning pass rather than a drop-in compatibility port. It removes the old random-patch wrapper entirely, keeps the biome-stage layout intact, and trims a large amount of older feature content. However, it still produces many schema issues when checked against the 26.1.2 reference, so copying the whole folder into the current port would be unsafe.

The main lesson is that Cristelknight’s approach was to simplify the feature tree and preserve the biome customizations, not to preserve every legacy feature file verbatim.

## 1. Folder structure and counts

- Total JSON files in the 26.2 alpha datapack: 1667
- Top-level namespaces under data/: `minecraft`, `wythers`
- New top-level namespaces compared with the original: none

## 2. How random_patch was handled

- `minecraft:random_patch` references in the alpha: 0
- Conclusion: the old wrapper was removed rather than translated into a 26.1.2-compatible pattern.

Example before/after pattern:

Before, [WWOO_ORIGINAL/data/wythers/worldgen/placed_feature/decor/sparse_steam.json](WWOO_ORIGINAL/data/wythers/worldgen/placed_feature/decor/sparse_steam.json) used a feature wrapper around a simple block placement.

After, [wwoo-26.2-port-fixed/data/wythers/worldgen/placed_feature/decor/sparse_steam.json](wwoo-26.2-port-fixed/data/wythers/worldgen/placed_feature/decor/sparse_steam.json) uses a direct simple-block placed feature with the placement rules moved out to the surrounding placement list. The older `random_patch` structure is gone.

This is the clearest pattern: replace the legacy patch wrapper with a simpler direct feature definition and place the scatter/placement logic in the placement list.

## 3. Tree-key compatibility

Counts found in the alpha datapack:

- `dirt_provider`: 0
- `force_dirt`: 0
- `exclusion_radius_xz`: 124
- `waterlogged`: 405
- `extra_branch_steps`: 14

Interpretation:

- The alpha removed the old dirt-provider and force-dirt vocabulary entirely.
- It still keeps several other tree-related keys, especially `exclusion_radius_xz`, `waterlogged`, and `extra_branch_steps`, which appear in tree-like or branch-heavy feature files.

## 4. Biome structure comparison

Forest biome comparison:

| Source | Feature stages | Total features |
| --- | ---: | ---: |
| [WWOO_ORIGINAL/data/minecraft/worldgen/biome/forest.json](WWOO_ORIGINAL/data/minecraft/worldgen/biome/forest.json) | 11 | 84 |
| [wwoo-26.2-port-fixed/data/minecraft/worldgen/biome/forest.json](wwoo-26.2-port-fixed/data/minecraft/worldgen/biome/forest.json) | 11 | 84 |
| [26.1.2/data/minecraft/worldgen/biome/forest.json](26.1.2/data/minecraft/worldgen/biome/forest.json) | 11 | 48 |

Conclusion:

- The 26.2 alpha does not replace biome definitions wholesale.
- It preserves the vanilla-style stage structure and injects Wythers content into it.
- Vanilla ore and structure features are still present in the stage list, so the biome files are functioning as a vanilla base plus extra Wythers features.

## 5. Files deleted vs. added

File-set comparison between [WWOO_ORIGINAL](WWOO_ORIGINAL) and [wwoo-26.2-port-fixed](wwoo-26.2-port-fixed):

- Deleted in the alpha: 118 JSON files
- Added in the alpha: 13 JSON files

The deleted files are mostly older tags, legacy terrain/feature variants, and old structure-exclusivity files. The added files are mostly newer support files and a small number of feature/test definitions.

## 6. Schema scanner results for the alpha

Running the scanner over the alpha produced:

- Files scanned: 1648
- Files with issues: 1264
- Unbound or dangling references: 1581

Issue categories reported:

- `leaf_blockstate_keys`: 2687
- `misc_removed_keys`: 1085
- `missing_type_field`: 912
- `column_placer_keys`: 903
- `foliage_placer_keys`: 48

This means the alpha is not schema-clean for the 26.1.2 reference. It still contains patterns that 26.1.2 would reject, even though the alpha is targeting a newer schema baseline.

## 7. What can be copied and what needs adaptation

### Direct-copy candidates

A wholesale copy of [wwoo-26.2-port-fixed/data](wwoo-26.2-port-fixed/data) into the 26.1.2 port is not safe.

The only realistic direct-copy candidates are very small, simple files that do not use the flagged key vocabulary and do not reference missing placed features. In practice, that is a narrow subset rather than the whole datapack.

### Files that need adaptation

These categories need adaptation before they can be used in the 26.1.2 port:

- Any feature that previously used the old `minecraft:random_patch` wrapper and was rewritten as a direct block/placement structure.
- Any feature using the removed tree keys `dirt_provider` or `force_dirt`.
- Any file with a missing `type` field or with structure that the 26.1.2 schema does not accept.
- Any biome or placed-feature file that references features not available in the 26.1.2 set.

## Recommendation

The 26.2 alpha is useful as a design reference, but it should not be treated as a direct source for the 26.1.2 port. The best approach is to borrow the overall pattern:

1. Keep the biome-based customizations.
2. Simplify and prune the feature tree.
3. Replace or remove anything that depends on 26.2-only or 26.1.2-incompatible structures.

In short: use the alpha to learn the migration strategy, not to copy the data wholesale.
