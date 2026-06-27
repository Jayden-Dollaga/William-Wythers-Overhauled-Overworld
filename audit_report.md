# Git History Audit — Debunked Category Commits

These commits removed keys that were LATER confirmed (via official
Minecraft changelog) to still be valid in 26.1.2. They were removed
based on unverified round-report claims, not actual schema checks.

**This report does not auto-revert anything.** Each commit needs manual
review — some may have also done other legitimate work in the same file.

**Total commits scanned**: 3391
**Commits flagged**: 1876

## Commits Per Debunked Category

| Category | Commits |
|---|---|
| waterlogged | 882 |
| missing_type_field (heuristic match) | 689 |
| persistent | 680 |
| distance | 680 |
| required_empty_blocks | 255 |
| exclusion_radius_xz | 253 |
| exclusion_radius_y | 253 |
| heightmap | 172 |
| can_grow_through | 108 |
| snowy | 53 |
| extra_branch_steps | 45 |
| extra_branch_length | 45 |
| place_branch_per_log_probability | 45 |

## Flagged Commits (Detail)

### `fc381b6388` — Upload All For Debugging

- **Removed debunked keys**: heightmap, snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt, below_trunk_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 775
  - `---NOTES---.txt`
  - `Blueprint Promp analyzing.txt`
  - `Log_Error23.txt`
  - `WWOO_NF/data/minecraft/worldgen/biome/bamboo_jungle.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/beach.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/birch_forest.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/cold_ocean.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/dark_forest.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/deep_cold_ocean.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/deep_frozen_ocean.json`
  - ... +765 more
- **Revert command** (review diff first!): `git show fc381b6388` then `git revert fc381b6388` if confirmed safe

### `adefc8d4c9` — fix: restore valid configured_features from WWOO_ORIGINAL

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 746
  - `Log_Error21.txt`
  - `Log_Error22.txt`
  - `WWOO_NF/data/minecraft/worldgen/biome/badlands.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/bamboo_jungle.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/basalt_deltas.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/beach.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/birch_forest.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/cherry_grove.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/cold_ocean.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/crimson_forest.json`
  - ... +736 more
- **Revert command** (review diff first!): `git show adefc8d4c9` then `git revert adefc8d4c9` if confirmed safe

### `20fc5e22ad` — fix: delete remaining wythers files with 26.1.2 breaking changes - Removed 43 configured_features with random_patch type - Removed 258 files with inline random_patch features - Removed 2 files with malformed rule structures - Total: 303 files deleted for 26.1.2 compatibility

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 177
  - `data/minecraft/worldgen/configured_feature/disk_grass.json`
  - `data/minecraft/worldgen/configured_feature/disk_sand.json`
  - `data/minecraft/worldgen/configured_feature/patch_dead_bush.json`
  - `data/minecraft/worldgen/configured_feature/patch_grass.json`
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/decor/stumps.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - ... +167 more
- **Revert command** (review diff first!): `git show 20fc5e22ad` then `git revert 20fc5e22ad` if confirmed safe

### `561f826d83` — fix: delete wythers placed_features with malformed rule structures - Found 162 files with 'rules' structures missing 'type' field - These were invalid in 26.1.2 serialization format - Deleted to resolve datapack loading failures

- **Removed debunked keys**: heightmap, snowy, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 162
  - `data/wythers/worldgen/configured_feature/terrain/local/cold_island_processor.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/fan_corals.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/giant_mushrooms.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_island.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_island_2.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_ocean_caves.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/mushroom_spires.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/volcanic_flooded_cavern_mud.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/warm_island.json`
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_24.json`
  - ... +152 more
- **Revert command** (review diff first!): `git show 561f826d83` then `git revert 561f826d83` if confirmed safe

### `ac9f887ac3` — fix: delete wythers placed_features with inline random_patch - Found 98 placed_feature files that defined inline random_patch features - These are invalid in 26.1.2; removed to allow datapack loading

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1218
  - `Log_Error20.txt`
  - `WWOO_NF/data/minecraft/worldgen/biome/badlands.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/bamboo_jungle.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/beach.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/birch_forest.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/cherry_grove.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/cold_ocean.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/dark_forest.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/deep_cold_ocean.json`
  - `WWOO_NF/data/minecraft/worldgen/biome/deep_dark.json`
  - ... +1208 more
- **Revert command** (review diff first!): `git show ac9f887ac3` then `git revert ac9f887ac3` if confirmed safe

### `1d1c981af5` — restore: integrity check after Round 16 agent deletions

- **Removed debunked keys**: required_empty_blocks, can_grow_through, snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 377
  - `data/minecraft/worldgen/configured_feature/patch_dead_bush.json`
  - `data/minecraft/worldgen/configured_feature/patch_grass.json`
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/decor/stumps.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes_1.json`
  - ... +367 more
- **Revert command** (review diff first!): `git show 1d1c981af5` then `git revert 1d1c981af5` if confirmed safe

### `fdafe4259a` — fix: delete random_patch configured_features (removed in 26.1.2) - These 41 wythers decorative features used removed random_patch type - Deleted to allow datapack to load; core world gen unaffected - Can be re-implemented with 26.1.2-compatible feature types later

- **Removed debunked keys**: required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy
- **Files touched**: 278
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/decor/stumps.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes_1.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes_2.json`
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes_3.json`
  - ... +268 more
- **Revert command** (review diff first!): `git show fdafe4259a` then `git revert fdafe4259a` if confirmed safe

### `afce317978` — fix: remove 26.1.2 deprecated keys from wythers features - Removed waterlogged, persistent, distance, exclusion_radius_xz/y - Removed dirt_provider, force_dirt from all wythers worldgen files - Preserves all feature definitions and placements

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 407
  - `data/wythers/worldgen/configured_feature/decor/campfires.json`
  - `data/wythers/worldgen/configured_feature/decor/floating_lantern.json`
  - `data/wythers/worldgen/configured_feature/decor/scarecrow.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
  - `data/wythers/worldgen/configured_feature/other/small_tubeworm.json`
  - `data/wythers/worldgen/configured_feature/other/tubeworm.json`
  - ... +397 more
- **Revert command** (review diff first!): `git show afce317978` then `git revert afce317978` if confirmed safe

### `b4bd7ae1d7` — restore: all wythers customizations from WWOO_ORIGINAL - Restored all wythers configured_features, placed_features, and tags - These contain WWOO's custom world generation features and decorations

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1092
  - `data/wythers/tags/block/air_and_plants.json`
  - `data/wythers/tags/block/palm_tree_replaceable.json`
  - `data/wythers/tags/block/tree_replaceable.json`
  - `data/wythers/worldgen/configured_feature/decor/campfires.json`
  - `data/wythers/worldgen/configured_feature/decor/floating_lantern.json`
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/decor/scarecrow.json`
  - `data/wythers/worldgen/configured_feature/decor/stumps.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - ... +1082 more
- **Revert command** (review diff first!): `git show b4bd7ae1d7` then `git revert b4bd7ae1d7` if confirmed safe

### `392400d109` — Update

- **Removed debunked keys**: heightmap, snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: below_trunk_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1688
  - `---NOTES---.txt`
  - `.Blueprint_Prompt_Full_Sweep_v2.txt`
  - `Blueprint Prompt Error Template.txt`
  - `Blueprint Prompt Template.txt`
  - `Blueprint Prompt11.txt`
  - `Blueprint Prompt12.txt`
  - `Blueprint Prompt13.txt`
  - `Blueprint_Prompt_Auto.txt`
  - `Blueprint_Prompt_Full_Sweep.txt`
  - `Log_Error13.txt`
  - ... +1678 more
- **Revert command** (review diff first!): `git show 392400d109` then `git revert 392400d109` if confirmed safe

### `a0c9b73c80` — fix(configured_feature): remove malformed patch_dead_bush and patch_grass using removed random_patch type

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt, below_trunk_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 22
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/acacia.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/azalea_tree.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/birch.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/birch_bees_005.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/cherry.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/cherry_bees_005.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/dark_oak.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/fancy_oak.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/fancy_oak_bees_005.json`
  - `WWOO_NF/data/minecraft/worldgen/configured_feature/mangrove.json`
  - ... +12 more
- **Revert command** (review diff first!): `git show a0c9b73c80` then `git revert a0c9b73c80` if confirmed safe

### `694c3a2d4a` — chore(vanilla): replace all minecraft/worldgen, minecraft/tags with authoritative 26.1.2 reference

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt, below_trunk_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1730
  - `data/minecraft/chicken_variant/cold.json`
  - `data/minecraft/chicken_variant/temperate.json`
  - `data/minecraft/chicken_variant/warm.json`
  - `data/minecraft/tags/banner_pattern/no_item_required.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/bordure_indented.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/creeper.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/field_masoned.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/flow.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/flower.json`
  - `data/minecraft/tags/banner_pattern/pattern_item/globe.json`
  - ... +1720 more
- **Revert command** (review diff first!): `git show 694c3a2d4a` then `git revert 694c3a2d4a` if confirmed safe

### `bda8f14d8e` — Update

- **Removed debunked keys**: heightmap
- **Files touched**: 66
  - `---NOTES---.txt`
  - `Blueprint Prompt10.txt`
  - `GROUNDSEL_FIX_LOG.txt`
  - `Log_Error10.txt`
  - `Log_Error11.txt`
  - `Log_Error12.txt`
  - `WWOO_NF/data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `WWOO_NF/data/wythers/worldgen/configured_feature/other/stone_forest_rock.json`
  - `WWOO_NF/data/wythers/worldgen/configured_feature/vegetation/floating_vegetation_plants.json`
  - `WWOO_NF/data/wythers/worldgen/configured_feature/vegetation/fungus/patch_morel.json`
  - ... +56 more
- **Revert command** (review diff first!): `git show bda8f14d8e` then `git revert bda8f14d8e` if confirmed safe

### `6ad8d9f495` — fix(worldgen): add simple_random_selector wrapper to configured_feature files (melon, wheat, bamboo patches)

- **Removed debunked keys**: heightmap
- **Files touched**: 3
  - `data/wythers/worldgen/configured_feature/vegetation/melon_patch.json`
  - `data/wythers/worldgen/configured_feature/vegetation/patch_wheat_farmed.json`
  - `data/wythers/worldgen/configured_feature/vegetation/thin_jungle_bamboo_patch.json`
- **Revert command** (review diff first!): `git show 6ad8d9f495` then `git revert 6ad8d9f495` if confirmed safe

### `0b991edf38` — Export all

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 2237
  - `---NOTES---.txt`
  - `Blueprint Prompt6 - Part 1.txt`
  - `Blueprint Prompt6 - Part 2.txt`
  - `Blueprint Prompt6 - Part 3.txt`
  - `Blueprint Prompt6 - Part 4.txt`
  - `Blueprint Prompt6.txt`
  - `Blueprint Prompt7.txt`
  - `GROUNDSEL_FIX_LOG.txt`
  - `Log_Error5.txt`
  - `Log_Error6.txt`
  - ... +2227 more
- **Revert command** (review diff first!): `git show 0b991edf38` then `git revert 0b991edf38` if confirmed safe

### `f39c887a7e` — fix(worldgen): Round 9 pass 2 - remaining 20 nested random_patch cleared

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 20
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/banyan.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_1.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_2.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_3.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_4.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
  - ... +10 more
- **Revert command** (review diff first!): `git show f39c887a7e` then `git revert f39c887a7e` if confirmed safe

### `6b80209d6e` — fix(worldgen): Round 9 - fix nested random_patch (221 files)

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 221
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/deep_lukewarm_island.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/giant_mushrooms.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/iceland.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/island.json`
  - `data/wythers/worldgen/configured_feature/terrain/local/mushroom_island.json`
  - ... +211 more
- **Revert command** (review diff first!): `git show 6b80209d6e` then `git revert 6b80209d6e` if confirmed safe

### `b353b2f16b` — fix(worldgen): Round 8 — unwrap remaining random_patch

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 30
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spikes.json`
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
  - `data/wythers/worldgen/configured_feature/vegetation/patch/sea_vines.json`
  - `data/wythers/worldgen/configured_feature/vegetation/patch/seagrass_mixed.json`
  - `data/wythers/worldgen/configured_feature/vegetation/patch_pumpkin_farmed.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/rooted_dirt/1.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/rooted_dirt/2.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/rooted_dirt/3.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/rooted_dirt/1.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/rooted_dirt/2.json`
  - ... +20 more
- **Revert command** (review diff first!): `git show b353b2f16b` then `git revert b353b2f16b` if confirmed safe

### `1ea29e79d3` — fix(worldgen): Round 6 Part 4 — random_patch conversion and vanilla feature updates

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, heightmap, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 380
  - `WWOO/data/minecraft/cow_variant/cold.json`
  - `WWOO/data/minecraft/cow_variant/temperate.json`
  - `WWOO/data/minecraft/cow_variant/warm.json`
  - `WWOO/data/minecraft/pig_variant/cold.json`
  - `WWOO/data/minecraft/pig_variant/temperate.json`
  - `WWOO/data/minecraft/pig_variant/warm.json`
  - `WWOO/data/minecraft/wolf_variant/ashen.json`
  - `WWOO/data/minecraft/wolf_variant/black.json`
  - `WWOO/data/minecraft/wolf_variant/chestnut.json`
  - `WWOO/data/minecraft/wolf_variant/pale.json`
  - ... +370 more
- **Revert command** (review diff first!): `git show 1ea29e79d3` then `git revert 1ea29e79d3` if confirmed safe

### `d0b25cd5bc` — fix(worldgen): patch_enoki.json — convert random_patch

- **Removed debunked keys**: waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 2
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
  - `WWOO/data/wythers/worldgen/placed_feature/vegetation/fungus/patch_enoki_pf.json`
- **Revert command** (review diff first!): `git show d0b25cd5bc` then `git revert d0b25cd5bc` if confirmed safe

### `6dc833aa32` — fix: cherry_maple.json — remove wrongly added type field

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_maple.json`
- **Revert command** (review diff first!): `git show 6dc833aa32` then `git revert 6dc833aa32` if confirmed safe

### `060554fa62` — fix: cherry_huangshan_pine.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_huangshan_pine.json`
- **Revert command** (review diff first!): `git show 060554fa62` then `git revert 060554fa62` if confirmed safe

### `242e6adb33` — fix: cherry_maple_snowy.json — remove wrongly added type field

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_maple_snowy.json`
- **Revert command** (review diff first!): `git show 242e6adb33` then `git revert 242e6adb33` if confirmed safe

### `8bd4cdcb5c` — fix: cherry_huangshan_pine_snowy.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_huangshan_pine_snowy.json`
- **Revert command** (review diff first!): `git show 8bd4cdcb5c` then `git revert 8bd4cdcb5c` if confirmed safe

### `b56c31d64a` — fix: tundra_spruce.json — remove wrongly added type field

- **Removed debunked keys**: persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/tundra_spruce.json`
- **Revert command** (review diff first!): `git show b56c31d64a` then `git revert b56c31d64a` if confirmed safe

### `5238af07eb` — fix: tundra_bush.json — remove wrongly added type field

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/tundra_bush.json`
- **Revert command** (review diff first!): `git show 5238af07eb` then `git revert 5238af07eb` if confirmed safe

### `342bd7e86f` — fix: teak.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/teak.json`
- **Revert command** (review diff first!): `git show 342bd7e86f` then `git revert 342bd7e86f` if confirmed safe

### `aae3b31c55` — fix: stick_plant.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant.json`
- **Revert command** (review diff first!): `git show aae3b31c55` then `git revert aae3b31c55` if confirmed safe

### `7784e58e50` — fix: stick_plant_small.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant_small.json`
- **Revert command** (review diff first!): `git show 7784e58e50` then `git revert 7784e58e50` if confirmed safe

### `253b4c0661` — fix: scrub_spruce.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_spruce.json`
- **Revert command** (review diff first!): `git show 253b4c0661` then `git revert 253b4c0661` if confirmed safe

### `7c76d03c15` — fix: scrub_oak.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_oak.json`
- **Revert command** (review diff first!): `git show 7c76d03c15` then `git revert 7c76d03c15` if confirmed safe

### `7e733b0ea8` — fix: scrub_jungle.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_jungle.json`
- **Revert command** (review diff first!): `git show 7e733b0ea8` then `git revert 7e733b0ea8` if confirmed safe

### `06ab6c489b` — fix: scrub_flowering_azalea.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_flowering_azalea.json`
- **Revert command** (review diff first!): `git show 06ab6c489b` then `git revert 06ab6c489b` if confirmed safe

### `d55f337323` — fix: scrub_dark_oak.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_dark_oak.json`
- **Revert command** (review diff first!): `git show d55f337323` then `git revert d55f337323` if confirmed safe

### `728805cd33` — fix: scrub_birch.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_birch.json`
- **Revert command** (review diff first!): `git show 728805cd33` then `git revert 728805cd33` if confirmed safe

### `31dafcf7ae` — fix: scrub_azalea.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_azalea.json`
- **Revert command** (review diff first!): `git show 31dafcf7ae` then `git revert 31dafcf7ae` if confirmed safe

### `d796390f84` — fix: scrub_acacia.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_acacia.json`
- **Revert command** (review diff first!): `git show d796390f84` then `git revert d796390f84` if confirmed safe

### `ac9cbefa83` — fix: savanna_oak.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/savanna_oak.json`
- **Revert command** (review diff first!): `git show ac9cbefa83` then `git revert ac9cbefa83` if confirmed safe

### `50e03a5aae` — fix: sandalwood.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/sandalwood.json`
- **Revert command** (review diff first!): `git show 50e03a5aae` then `git revert 50e03a5aae` if confirmed safe

### `de64ebaa43` — fix: rosewood.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/rosewood.json`
- **Revert command** (review diff first!): `git show de64ebaa43` then `git revert de64ebaa43` if confirmed safe

### `f75faf15ce` — fix: red_ivorywood.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/red_ivorywood.json`
- **Revert command** (review diff first!): `git show f75faf15ce` then `git revert f75faf15ce` if confirmed safe

### `ade19471a8` — fix: ponderosa_pine.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_pine.json`
- **Revert command** (review diff first!): `git show ade19471a8` then `git revert ade19471a8` if confirmed safe

### `a1be1b2a28` — fix: pine.json — remove wrongly added type field

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pine.json`
- **Revert command** (review diff first!): `git show a1be1b2a28` then `git revert a1be1b2a28` if confirmed safe

### `e73ab7fb21` — fix: olive.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/olive.json`
- **Revert command** (review diff first!): `git show e73ab7fb21` then `git revert e73ab7fb21` if confirmed safe

### `d56248ff87` — fix: oak.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/oak.json`
- **Revert command** (review diff first!): `git show d56248ff87` then `git revert d56248ff87` if confirmed safe

### `8a3289512e` — fix: oak_bush.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/oak_bush.json`
- **Revert command** (review diff first!): `git show 8a3289512e` then `git revert 8a3289512e` if confirmed safe

### `bc4c216a1a` — fix: mpingo.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mpingo.json`
- **Revert command** (review diff first!): `git show bc4c216a1a` then `git revert bc4c216a1a` if confirmed safe

### `34380a5c75` — fix: maple_tall.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/maple_tall.json`
- **Revert command** (review diff first!): `git show 34380a5c75` then `git revert 34380a5c75` if confirmed safe

### `f312a34eb7` — fix: mahogany.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mahogany.json`
- **Revert command** (review diff first!): `git show f312a34eb7` then `git revert f312a34eb7` if confirmed safe

### `3f798a90c5` — fix: huangshan_pine.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/huangshan_pine.json`
- **Revert command** (review diff first!): `git show 3f798a90c5` then `git revert 3f798a90c5` if confirmed safe

### `e774c74a0f` — fix: ground_pine.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ground_pine.json`
- **Revert command** (review diff first!): `git show e774c74a0f` then `git revert e774c74a0f` if confirmed safe

### `8bedf643e9` — fix: flowering_azalea_bush.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/flowering_azalea_bush.json`
- **Revert command** (review diff first!): `git show 8bedf643e9` then `git revert 8bedf643e9` if confirmed safe

### `9fab2e715e` — fix: fir_medium.json — remove wrongly added type field

- **Removed debunked keys**: persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/fir_medium.json`
- **Revert command** (review diff first!): `git show 9fab2e715e` then `git revert 9fab2e715e` if confirmed safe

### `3105e62885` — fix: ebony.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ebony.json`
- **Revert command** (review diff first!): `git show 3105e62885` then `git revert 3105e62885` if confirmed safe

### `90abc73617` — fix: corymbia_aparrerinja.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/corymbia_aparrerinja.json`
- **Revert command** (review diff first!): `git show 90abc73617` then `git revert 90abc73617` if confirmed safe

### `c4aa25f6b9` — fix: cold_pine_medium.json — remove wrongly added type field

- **Removed debunked keys**: persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/cold_pine_medium.json`
- **Revert command** (review diff first!): `git show c4aa25f6b9` then `git revert c4aa25f6b9` if confirmed safe

### `15615ba71f` — fix: birch.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/birch.json`
- **Revert command** (review diff first!): `git show 15615ba71f` then `git revert 15615ba71f` if confirmed safe

### `ad9c9f28e0` — fix: bamboo_palm.json — remove wrongly added type field

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bamboo_palm.json`
- **Revert command** (review diff first!): `git show ad9c9f28e0` then `git revert ad9c9f28e0` if confirmed safe

### `c5ec200086` — fix: azalea_conifer.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/azalea_conifer.json`
- **Revert command** (review diff first!): `git show c5ec200086` then `git revert c5ec200086` if confirmed safe

### `b4e4a0f2c5` — fix: azalea_birch.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/azalea_birch.json`
- **Revert command** (review diff first!): `git show b4e4a0f2c5` then `git revert b4e4a0f2c5` if confirmed safe

### `a4e92a90b9` — fix: aspen.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/aspen.json`
- **Revert command** (review diff first!): `git show a4e92a90b9` then `git revert a4e92a90b9` if confirmed safe

### `831fa387d9` — fix: acacia_plains.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/acacia_plains.json`
- **Revert command** (review diff first!): `git show 831fa387d9` then `git revert 831fa387d9` if confirmed safe

### `4ea1b7f88f` — fix: acacia_forest.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/acacia_forest.json`
- **Revert command** (review diff first!): `git show 4ea1b7f88f` then `git revert 4ea1b7f88f` if confirmed safe

### `929027a37b` — fix: pale.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/pale.json`
- **Revert command** (review diff first!): `git show 929027a37b` then `git revert 929027a37b` if confirmed safe

### `cd09a92420` — fix: jungle.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/jungle.json`
- **Revert command** (review diff first!): `git show cd09a92420` then `git revert cd09a92420` if confirmed safe

### `4760dad197` — fix: acacia.json — remove wrongly added type field

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/acacia.json`
- **Revert command** (review diff first!): `git show 4760dad197` then `git revert 4760dad197` if confirmed safe

### `566ad77226` — fix(Round6Fix6): remove sapling_provider — fir_tall.json

- **Removed debunked keys**: persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/fir_tall.json`
- **Revert command** (review diff first!): `git show 566ad77226` then `git revert 566ad77226` if confirmed safe

### `710076ec6c` — fix(Round6Fix6): remove placement — baobab_small.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/baobab_small.json`
- **Revert command** (review diff first!): `git show 710076ec6c` then `git revert 710076ec6c` if confirmed safe

### `0c1a122de6` — fix(Round6Fix6): remove blocks — coastal_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 0c1a122de6` then `git revert 0c1a122de6` if confirmed safe

### `f87fcd1113` — fix(Round6Fix6): remove blocks — coastal_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show f87fcd1113` then `git revert f87fcd1113` if confirmed safe

### `46e1359e04` — fix(Round6Fix6): remove blocks — coastal_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 46e1359e04` then `git revert 46e1359e04` if confirmed safe

### `182ec3f8f3` — fix(Round6Fix6): remove blocks — coastal_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 182ec3f8f3` then `git revert 182ec3f8f3` if confirmed safe

### `cede4a1346` — fix(Round6Fix6): remove blocks — bent_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_west.json`
- **Revert command** (review diff first!): `git show cede4a1346` then `git revert cede4a1346` if confirmed safe

### `9d73a88b89` — fix(Round6Fix6): remove blocks — bent_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_south.json`
- **Revert command** (review diff first!): `git show 9d73a88b89` then `git revert 9d73a88b89` if confirmed safe

### `527f7b33a7` — fix(Round6Fix6): remove blocks — bent_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_north.json`
- **Revert command** (review diff first!): `git show 527f7b33a7` then `git revert 527f7b33a7` if confirmed safe

### `a71a919e02` — fix(Round6Fix6): remove blocks — bent_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_east.json`
- **Revert command** (review diff first!): `git show a71a919e02` then `git revert a71a919e02` if confirmed safe

### `14e3f7e11c` — fix(Round6Fix6): remove snowy — sea_cliff.json

- **Removed debunked keys**: snowy
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/terrain/local/sea_cliff.json`
- **Revert command** (review diff first!): `git show 14e3f7e11c` then `git revert 14e3f7e11c` if confirmed safe

### `8e7d32f6b0` — fix(Round6Fix6): remove snowy — packed_mud_canyons.json

- **Removed debunked keys**: snowy
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/terrain/local/packed_mud_canyons.json`
- **Revert command** (review diff first!): `git show 8e7d32f6b0` then `git revert 8e7d32f6b0` if confirmed safe

### `0482abc012` — fix(Round6Fix6): remove snowy — dripstone_cliff.json

- **Removed debunked keys**: snowy
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/placed_feature/terrain/extended/dripstone_cliff.json`
- **Revert command** (review diff first!): `git show 0482abc012` then `git revert 0482abc012` if confirmed safe

### `649b5a3822` — fix(Round6Fix6): remove snowy — ancient_pale_oak.json

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ancient_pale_oak.json`
- **Revert command** (review diff first!): `git show 649b5a3822` then `git revert 649b5a3822` if confirmed safe

### `3cc4396b62` — fix(Round6Fix6): remove snowy — ancient_dead_pale_oak.json

- **Removed debunked keys**: snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dead_pale_oak.json`
- **Revert command** (review diff first!): `git show 3cc4396b62` then `git revert 3cc4396b62` if confirmed safe

### `5be86a30bb` — fix(Round6Fix6): remove heightmap — island.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/local/island.json`
- **Revert command** (review diff first!): `git show 5be86a30bb` then `git revert 5be86a30bb` if confirmed safe

### `d25a8496f2` — fix(Round6Fix6): remove heightmap — deep_lukewarm_island.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/local/deep_lukewarm_island.json`
- **Revert command** (review diff first!): `git show d25a8496f2` then `git revert d25a8496f2` if confirmed safe

### `6daf095524` — fix(Round6Fix5): remove ColumnPlacer keys — giant_omphalotus_illudens.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json`
- **Revert command** (review diff first!): `git show 6daf095524` then `git revert 6daf095524` if confirmed safe

### `0798965036` — fix(Round6Fix5): remove ColumnPlacer keys — fungal_forest_orange.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json`
- **Revert command** (review diff first!): `git show 0798965036` then `git revert 0798965036` if confirmed safe

### `7c798fe71e` — fix(Round6Fix4): remove trunk placer keys — elephant_bamboo_tropical.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 7c798fe71e` then `git revert 7c798fe71e` if confirmed safe

### `f10c605715` — fix(Round6Fix4): remove trunk placer keys — elephant_bamboo_tropical_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show f10c605715` then `git revert f10c605715` if confirmed safe

### `e9e5760177` — fix(Round6Fix4): remove trunk placer keys — elephant_bamboo_temperate.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show e9e5760177` then `git revert e9e5760177` if confirmed safe

### `168d2671ad` — fix(Round6Fix4): remove trunk placer keys — elephant_bamboo_temperate_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show 168d2671ad` then `git revert 168d2671ad` if confirmed safe

### `c861b78c57` — fix(Round6Fix3): remove blockstate keys — terracotta_mound_yellow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show c861b78c57` then `git revert c861b78c57` if confirmed safe

### `5683d56503` — fix(Round6Fix3): remove blockstate keys — terracotta_mound_red.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show 5683d56503` then `git revert 5683d56503` if confirmed safe

### `fc4c2aca66` — fix(Round6Fix3): remove blockstate keys — terracotta_mound_orange.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json`
- **Revert command** (review diff first!): `git show fc4c2aca66` then `git revert fc4c2aca66` if confirmed safe

### `71368c4b4a` — fix(Round6Fix2): remove dirt_provider+force_dirt — young_mega_jungle.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json`
- **Revert command** (review diff first!): `git show 71368c4b4a` then `git revert 71368c4b4a` if confirmed safe

### `1db140b812` — fix(Round6Fix2): remove dirt_provider+force_dirt — young_kapok.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json`
- **Revert command** (review diff first!): `git show 1db140b812` then `git revert 1db140b812` if confirmed safe

### `e03c930fa6` — fix(Round6Fix2): remove dirt_provider+force_dirt — young_brazilwood.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json`
- **Revert command** (review diff first!): `git show e03c930fa6` then `git revert e03c930fa6` if confirmed safe

### `08335978ca` — fix(Round6Fix2): remove dirt_provider+force_dirt — swamp_gum.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json`
- **Revert command** (review diff first!): `git show 08335978ca` then `git revert 08335978ca` if confirmed safe

### `d628b05fa6` — fix(Round6Fix2): remove dirt_provider+force_dirt — swamp_forest_oak.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json`
- **Revert command** (review diff first!): `git show d628b05fa6` then `git revert d628b05fa6` if confirmed safe

### `d6d847f424` — fix(Round6Fix2): remove dirt_provider+force_dirt — swamp_forest_birch.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json`
- **Revert command** (review diff first!): `git show d6d847f424` then `git revert d6d847f424` if confirmed safe

### `c22664fe29` — fix(Round6Fix2): remove dirt_provider+force_dirt — pandanus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show c22664fe29` then `git revert c22664fe29` if confirmed safe

### `45ab7b0373` — fix(Round6Fix2): remove dirt_provider+force_dirt — mega_jungle.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 45ab7b0373` then `git revert 45ab7b0373` if confirmed safe

### `8668bc6ba2` — fix(Round6Fix2): remove dirt_provider+force_dirt — kapok.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show 8668bc6ba2` then `git revert 8668bc6ba2` if confirmed safe

### `c91094dbef` — fix(Round6Fix2): remove dirt_provider+force_dirt — jungle_mangrove.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show c91094dbef` then `git revert c91094dbef` if confirmed safe

### `2e46178038` — fix(Round6Fix2): remove dirt_provider+force_dirt — eucalyptus_deanei_white.json

- **Removed debunked keys**: can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json`
- **Revert command** (review diff first!): `git show 2e46178038` then `git revert 2e46178038` if confirmed safe

### `3e2e7c58d3` — fix(Round6Fix2): remove dirt_provider+force_dirt — elephant_bamboo_tropical.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 3e2e7c58d3` then `git revert 3e2e7c58d3` if confirmed safe

### `8e99c16ff8` — fix(Round6Fix2): remove dirt_provider+force_dirt — elephant_bamboo_tropical_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show 8e99c16ff8` then `git revert 8e99c16ff8` if confirmed safe

### `1a5f86a1ed` — fix(Round6Fix2): remove dirt_provider+force_dirt — elephant_bamboo_temperate.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show 1a5f86a1ed` then `git revert 1a5f86a1ed` if confirmed safe

### `49fa2c3e8a` — fix(Round6Fix2): remove dirt_provider+force_dirt — elephant_bamboo_temperate_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show 49fa2c3e8a` then `git revert 49fa2c3e8a` if confirmed safe

### `bfa3667d88` — fix(Round6Fix2): remove dirt_provider+force_dirt — complex_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show bfa3667d88` then `git revert bfa3667d88` if confirmed safe

### `43d5675f0c` — fix(Round6Fix2): remove dirt_provider+force_dirt — complex_dark_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 43d5675f0c` then `git revert 43d5675f0c` if confirmed safe

### `491eb28f0b` — fix(Round6Fix2): remove dirt_provider+force_dirt — brazilwood.json

- **Removed debunked keys**: can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json`
- **Revert command** (review diff first!): `git show 491eb28f0b` then `git revert 491eb28f0b` if confirmed safe

### `5710dd306e` — fix(Round6Fix2): remove dirt_provider+force_dirt — bayou_cypress_surface.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json`
- **Revert command** (review diff first!): `git show 5710dd306e` then `git revert 5710dd306e` if confirmed safe

### `79f6d945ee` — fix(Round6Fix2): remove dirt_provider+force_dirt — bayou_cypress_surface_2.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json`
- **Revert command** (review diff first!): `git show 79f6d945ee` then `git revert 79f6d945ee` if confirmed safe

### `e6c9c57183` — fix(Round6Fix2): remove dirt_provider+force_dirt — bayou_cypress_shallow.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json`
- **Revert command** (review diff first!): `git show e6c9c57183` then `git revert e6c9c57183` if confirmed safe

### `47a82fca27` — fix(Round6Fix2): remove dirt_provider+force_dirt — bayou_cypress_middle.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
- **Revert command** (review diff first!): `git show 47a82fca27` then `git revert 47a82fca27` if confirmed safe

### `f595651955` — fix(Round6Fix2): remove dirt_provider+force_dirt — bayou_cypress_deep.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
- **Revert command** (review diff first!): `git show f595651955` then `git revert f595651955` if confirmed safe

### `df323e0950` — fix(Round6Fix2): remove dirt_provider+force_dirt — terracotta_mound_yellow.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show df323e0950` then `git revert df323e0950` if confirmed safe

### `a8102c17d0` — fix(Round6Fix2): remove dirt_provider+force_dirt — terracotta_mound_red.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show a8102c17d0` then `git revert a8102c17d0` if confirmed safe

### `9a17fb83c2` — fix(Round6Fix2): remove dirt_provider+force_dirt — terracotta_mound_orange.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json`
- **Revert command** (review diff first!): `git show 9a17fb83c2` then `git revert 9a17fb83c2` if confirmed safe

### `0f5fcbd78d` — fix(Round6Fix2): remove dirt_provider+force_dirt — mega_jungle.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 0f5fcbd78d` then `git revert 0f5fcbd78d` if confirmed safe

### `ad864ce97c` — fix(Round6Fix2): remove dirt_provider+force_dirt — jungle_mangrove.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show ad864ce97c` then `git revert ad864ce97c` if confirmed safe

### `d2e0fc2b13` — fix(configured_feature): add missing state provider type fields — Round 6

- **Removed debunked keys**: heightmap, snowy
- **Files touched**: 435
  - `data/minecraft/worldgen/configured_feature/ore_andesite.json`
  - `data/minecraft/worldgen/configured_feature/ore_diorite.json`
  - `data/minecraft/worldgen/configured_feature/ore_dirt.json`
  - `data/minecraft/worldgen/configured_feature/ore_granite.json`
  - `data/minecraft/worldgen/configured_feature/ore_gravel.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
  - ... +425 more
- **Revert command** (review diff first!): `git show d2e0fc2b13` then `git revert d2e0fc2b13` if confirmed safe

### `aeead3fa06` — fix(worldgen): Round 5 — Categories 1-3, 5, 7 complete

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, heightmap, snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 82
  - `data/minecraft/worldgen/configured_feature/mangrove.json`
  - `data/minecraft/worldgen/configured_feature/tall_mangrove.json`
  - `data/minecraft/worldgen/placed_feature/mangrove_checked.json`
  - `data/minecraft/worldgen/placed_feature/tall_mangrove_checked.json`
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json`
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
  - ... +72 more
- **Revert command** (review diff first!): `git show aeead3fa06` then `git revert aeead3fa06` if confirmed safe

### `f8c7f93192` — fix: convert integer spreads to IntProvider — white_bracket_fungi.json

- **Removed debunked keys**: heightmap
- **Files touched**: 16
  - `data/wythers/worldgen/placed_feature/terrain/extended/beach_cliffs.json`
  - `data/wythers/worldgen/placed_feature/terrain/extended/scree_spread.json`
  - `data/wythers/worldgen/placed_feature/terrain/extended/stony_desert_cliffs.json`
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_dripstone_spikes.json`
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_geodes.json`
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mangrove_swamp.json`
  - `data/wythers/worldgen/placed_feature/terrain/local/base_wooded_badlands.json`
  - `data/wythers/worldgen/placed_feature/terrain/local/cave_ice.json`
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_basalt_cliffs.json`
  - `data/wythers/worldgen/placed_feature/terrain/local/highland_stone_cliffs.json`
  - ... +6 more
- **Revert command** (review diff first!): `git show f8c7f93192` then `git revert f8c7f93192` if confirmed safe

### `bd38a95d2e` — fix: convert integer spreads to IntProvider — base_mangrove_swamp_savanna.json

- **Removed debunked keys**: heightmap
- **Files touched**: 2
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_savanna.json`
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_sparse_jungle.json`
- **Revert command** (review diff first!): `git show bd38a95d2e` then `git revert bd38a95d2e` if confirmed safe

### `6128d2ed69` — fix: IntProvider spreads — base_mangrove_swamp_forest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_forest.json`
- **Revert command** (review diff first!): `git show 6128d2ed69` then `git revert 6128d2ed69` if confirmed safe

### `7e6f807b1a` — fix: convert integer spreads to IntProvider — base_frozen_peaks_snow.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_frozen_peaks_snow.json`
- **Revert command** (review diff first!): `git show 7e6f807b1a` then `git revert 7e6f807b1a` if confirmed safe

### `8956835d4c` — fix: remove extra branch keys — young_mega_jungle.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json`
- **Revert command** (review diff first!): `git show 8956835d4c` then `git revert 8956835d4c` if confirmed safe

### `d3ce88ce28` — fix: remove extra branch keys — young_kapok.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json`
- **Revert command** (review diff first!): `git show d3ce88ce28` then `git revert d3ce88ce28` if confirmed safe

### `0c1e12d97c` — fix: remove extra branch keys — young_brazilwood.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json`
- **Revert command** (review diff first!): `git show 0c1e12d97c` then `git revert 0c1e12d97c` if confirmed safe

### `f0b459288f` — fix: remove extra branch keys — swamp_gum.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json`
- **Revert command** (review diff first!): `git show f0b459288f` then `git revert f0b459288f` if confirmed safe

### `e7e0dc03a7` — fix: remove extra branch keys — swamp_forest_oak.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json`
- **Revert command** (review diff first!): `git show e7e0dc03a7` then `git revert e7e0dc03a7` if confirmed safe

### `810ab5344e` — fix: remove extra branch keys — swamp_forest_birch.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json`
- **Revert command** (review diff first!): `git show 810ab5344e` then `git revert 810ab5344e` if confirmed safe

### `c5b40b3bcd` — fix: remove extra branch keys — pandanus.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show c5b40b3bcd` then `git revert c5b40b3bcd` if confirmed safe

### `24b844f82a` — fix: remove extra branch keys — pale_acacia_stump.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_acacia_stump.json`
- **Revert command** (review diff first!): `git show 24b844f82a` then `git revert 24b844f82a` if confirmed safe

### `a674bca420` — fix: remove extra branch keys — old_swamp_oak.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json`
- **Revert command** (review diff first!): `git show a674bca420` then `git revert a674bca420` if confirmed safe

### `d2d207de59` — fix: remove extra branch keys — mega_jungle.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show d2d207de59` then `git revert d2d207de59` if confirmed safe

### `fad1b389bb` — fix: remove extra branch keys — live_oak_dark_swamp.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json`
- **Revert command** (review diff first!): `git show fad1b389bb` then `git revert fad1b389bb` if confirmed safe

### `31de15907b` — fix: remove extra branch keys — kapok.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show 31de15907b` then `git revert 31de15907b` if confirmed safe

### `574208475f` — fix: remove extra branch keys — jungle_mangrove.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show 574208475f` then `git revert 574208475f` if confirmed safe

### `cee132901a` — fix: remove extra branch keys — eucalyptus_deanei_white.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json`
- **Revert command** (review diff first!): `git show cee132901a` then `git revert cee132901a` if confirmed safe

### `fce95a22b4` — fix: remove extra branch keys — elephant_bamboo_tropical_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show fce95a22b4` then `git revert fce95a22b4` if confirmed safe

### `7321eab064` — fix: remove extra branch keys — elephant_bamboo_tropical.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 7321eab064` then `git revert 7321eab064` if confirmed safe

### `dd02a5b01b` — fix: remove extra branch keys — elephant_bamboo_temperate_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show dd02a5b01b` then `git revert dd02a5b01b` if confirmed safe

### `32e8a606cd` — fix: remove extra branch keys — elephant_bamboo_temperate.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show 32e8a606cd` then `git revert 32e8a606cd` if confirmed safe

### `9bf07bc4aa` — fix: remove extra branch keys — complex_oak_1.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show 9bf07bc4aa` then `git revert 9bf07bc4aa` if confirmed safe

### `720152155d` — fix: remove extra branch keys — complex_dark_oak_1.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 720152155d` then `git revert 720152155d` if confirmed safe

### `ff6f9c569e` — fix: remove extra branch keys — brazilwood.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json`
- **Revert command** (review diff first!): `git show ff6f9c569e` then `git revert ff6f9c569e` if confirmed safe

### `f7bb58a09c` — fix: remove extra branch keys — bayou_cypress_surface_2.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json`
- **Revert command** (review diff first!): `git show f7bb58a09c` then `git revert f7bb58a09c` if confirmed safe

### `29bd9487e7` — fix: remove extra branch keys — bayou_cypress_surface.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json`
- **Revert command** (review diff first!): `git show 29bd9487e7` then `git revert 29bd9487e7` if confirmed safe

### `164824a578` — fix: remove extra branch keys — bayou_cypress_shallow.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json`
- **Revert command** (review diff first!): `git show 164824a578` then `git revert 164824a578` if confirmed safe

### `9dc2387e00` — fix: remove extra branch keys — bayou_cypress_middle.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
- **Revert command** (review diff first!): `git show 9dc2387e00` then `git revert 9dc2387e00` if confirmed safe

### `7f5101099a` — fix: remove extra branch keys — bayou_cypress_deep.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
- **Revert command** (review diff first!): `git show 7f5101099a` then `git revert 7f5101099a` if confirmed safe

### `1c9a8e35d0` — fix: remove extra branch keys — ancient_swamp_oak.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
- **Revert command** (review diff first!): `git show 1c9a8e35d0` then `git revert 1c9a8e35d0` if confirmed safe

### `aa3f40fbf9` — fix: remove extra branch keys — terracotta_mound_yellow.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show aa3f40fbf9` then `git revert aa3f40fbf9` if confirmed safe

### `f08ea424b7` — fix: remove extra branch keys — terracotta_mound_red.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show f08ea424b7` then `git revert f08ea424b7` if confirmed safe

### `439d27a649` — fix: remove extra branch keys — terracotta_mound_orange.json

- **Removed debunked keys**: can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json`
- **Revert command** (review diff first!): `git show 439d27a649` then `git revert 439d27a649` if confirmed safe

### `08e7c6d3be` — fix: remove extra branch keys — tall_mangrove_checked.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/tall_mangrove_checked.json`
- **Revert command** (review diff first!): `git show 08e7c6d3be` then `git revert 08e7c6d3be` if confirmed safe

### `ce1af262f6` — fix: remove extra branch keys — mangrove_checked.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/mangrove_checked.json`
- **Revert command** (review diff first!): `git show ce1af262f6` then `git revert ce1af262f6` if confirmed safe

### `3f7d4236d4` — fix: remove extra branch keys — tall_mangrove.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/tall_mangrove.json`
- **Revert command** (review diff first!): `git show 3f7d4236d4` then `git revert 3f7d4236d4` if confirmed safe

### `12ccad3b70` — fix: remove extra branch keys — mangrove.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/mangrove.json`
- **Revert command** (review diff first!): `git show 12ccad3b70` then `git revert 12ccad3b70` if confirmed safe

### `b18ab9fdf8` — fix: remove leaf blockstate keys — white_bracket_fungi.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show b18ab9fdf8` then `git revert b18ab9fdf8` if confirmed safe

### `9e5bf87a74` — fix: remove leaf blockstate keys — fungal_savanna_vegetation.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_savanna_vegetation.json`
- **Revert command** (review diff first!): `git show 9e5bf87a74` then `git revert 9e5bf87a74` if confirmed safe

### `3e3b455e2f` — fix: remove leaf blockstate keys — fungal_powder_spores.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show 3e3b455e2f` then `git revert 3e3b455e2f` if confirmed safe

### `076603ba27` — fix: remove leaf blockstate keys — fungal_jungle_vegetation.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_vegetation.json`
- **Revert command** (review diff first!): `git show 076603ba27` then `git revert 076603ba27` if confirmed safe

### `e95913e221` — fix: remove leaf blockstate keys — pamukkale_pools.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_pools.json`
- **Revert command** (review diff first!): `git show e95913e221` then `git revert e95913e221` if confirmed safe

### `6415b05fa4` — fix: remove leaf blockstate keys — deglaciator_01.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_01.json`
- **Revert command** (review diff first!): `git show 6415b05fa4` then `git revert 6415b05fa4` if confirmed safe

### `622a48d6d1` — fix: remove leaf blockstate keys — danakil_water.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_water.json`
- **Revert command** (review diff first!): `git show 622a48d6d1` then `git revert 622a48d6d1` if confirmed safe

### `8aa0871103` — fix: remove leaf blockstate keys — tepui_plants.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_plants.json`
- **Revert command** (review diff first!): `git show 8aa0871103` then `git revert 8aa0871103` if confirmed safe

### `795b349199` — fix: remove leaf blockstate keys — tepui_falls.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_falls.json`
- **Revert command** (review diff first!): `git show 795b349199` then `git revert 795b349199` if confirmed safe

### `1e9ce576b5` — fix: remove leaf blockstate keys — tepui_crystals.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_crystals.json`
- **Revert command** (review diff first!): `git show 1e9ce576b5` then `git revert 1e9ce576b5` if confirmed safe

### `7d1b2752bb` — fix: remove leaf blockstate keys — tepui_chasms.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_chasms.json`
- **Revert command** (review diff first!): `git show 7d1b2752bb` then `git revert 7d1b2752bb` if confirmed safe

### `0fa0dcb256` — fix: remove leaf blockstate keys — tepui_cavern_lakes.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_lakes.json`
- **Revert command** (review diff first!): `git show 0fa0dcb256` then `git revert 0fa0dcb256` if confirmed safe

### `9e1e968f56` — fix: remove leaf blockstate keys — onsen_pools.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_pools.json`
- **Revert command** (review diff first!): `git show 9e1e968f56` then `git revert 9e1e968f56` if confirmed safe

### `28ae073c79` — fix: remove leaf blockstate keys — sunflower_plains.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/sunflower_plains.json`
- **Revert command** (review diff first!): `git show 28ae073c79` then `git revert 28ae073c79` if confirmed safe

### `52c81f883c` — fix: remove leaf blockstate keys — cherry_grove.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/cherry_grove.json`
- **Revert command** (review diff first!): `git show 52c81f883c` then `git revert 52c81f883c` if confirmed safe

### `628377e22b` — fix: remove leaf blockstate keys — bamboo_jungle.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle.json`
- **Revert command** (review diff first!): `git show 628377e22b` then `git revert 628377e22b` if confirmed safe

### `7f27aa8865` — fix: remove leaf blockstate keys — andesite.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/andesite.json`
- **Revert command** (review diff first!): `git show 7f27aa8865` then `git revert 7f27aa8865` if confirmed safe

### `63a1619636` — fix: remove leaf blockstate keys — coastal_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 63a1619636` then `git revert 63a1619636` if confirmed safe

### `a2d1a9fbd1` — fix: remove leaf blockstate keys — coastal_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show a2d1a9fbd1` then `git revert a2d1a9fbd1` if confirmed safe

### `689d6b531e` — fix: remove leaf blockstate keys — coastal_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 689d6b531e` then `git revert 689d6b531e` if confirmed safe

### `b8e1617505` — fix: remove leaf blockstate keys — coastal_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show b8e1617505` then `git revert b8e1617505` if confirmed safe

### `c4f1c74a8b` — fix: remove leaf blockstate keys — paddy_leaf.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/paddy_leaf.json`
- **Revert command** (review diff first!): `git show c4f1c74a8b` then `git revert c4f1c74a8b` if confirmed safe

### `74968de550` — fix: remove leaf blockstate keys — sparse_steam.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/sparse_steam.json`
- **Revert command** (review diff first!): `git show 74968de550` then `git revert 74968de550` if confirmed safe

### `6f53effc6d` — fix: remove leaf blockstate keys — dense_steam.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/dense_steam.json`
- **Revert command** (review diff first!): `git show 6f53effc6d` then `git revert 6f53effc6d` if confirmed safe

### `208b73666b` — fix: remove leaf blockstate keys — willow_large.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow_large.json`
- **Revert command** (review diff first!): `git show 208b73666b` then `git revert 208b73666b` if confirmed safe

### `6d1310d91e` — fix: remove leaf blockstate keys — willow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow.json`
- **Revert command** (review diff first!): `git show 6d1310d91e` then `git revert 6d1310d91e` if confirmed safe

### `1efe266c9b` — fix: remove leaf blockstate keys — straight_cocoa_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/straight_cocoa_palm.json`
- **Revert command** (review diff first!): `git show 1efe266c9b` then `git revert 1efe266c9b` if confirmed safe

### `a4f379d9c7` — fix: remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show a4f379d9c7` then `git revert a4f379d9c7` if confirmed safe

### `a12f24346a` — fix: remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show a12f24346a` then `git revert a12f24346a` if confirmed safe

### `d280604561` — fix: remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show d280604561` then `git revert d280604561` if confirmed safe

### `aabf96dc4e` — fix: remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show aabf96dc4e` then `git revert aabf96dc4e` if confirmed safe

### `3d063261c9` — fix: remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 3d063261c9` then `git revert 3d063261c9` if confirmed safe

### `699a2518d7` — fix: remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 699a2518d7` then `git revert 699a2518d7` if confirmed safe

### `d5e24b0611` — fix: remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show d5e24b0611` then `git revert d5e24b0611` if confirmed safe

### `b9a23e46fc` — fix: remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show b9a23e46fc` then `git revert b9a23e46fc` if confirmed safe

### `61fbe1de70` — fix: remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/8.json`
- **Revert command** (review diff first!): `git show 61fbe1de70` then `git revert 61fbe1de70` if confirmed safe

### `7eba4fb0a1` — fix: remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/7.json`
- **Revert command** (review diff first!): `git show 7eba4fb0a1` then `git revert 7eba4fb0a1` if confirmed safe

### `7f77f569bd` — fix: remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/6.json`
- **Revert command** (review diff first!): `git show 7f77f569bd` then `git revert 7f77f569bd` if confirmed safe

### `83d217291d` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/5.json`
- **Revert command** (review diff first!): `git show 83d217291d` then `git revert 83d217291d` if confirmed safe

### `8eef5f17e5` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/4.json`
- **Revert command** (review diff first!): `git show 8eef5f17e5` then `git revert 8eef5f17e5` if confirmed safe

### `337983e958` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/3.json`
- **Revert command** (review diff first!): `git show 337983e958` then `git revert 337983e958` if confirmed safe

### `da894ff972` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/2.json`
- **Revert command** (review diff first!): `git show da894ff972` then `git revert da894ff972` if confirmed safe

### `1eef66bdf8` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/1.json`
- **Revert command** (review diff first!): `git show 1eef66bdf8` then `git revert 1eef66bdf8` if confirmed safe

### `eb387132bc` — fix: remove leaf blockstate keys — riverside_jungle_tree.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/riverside_jungle_tree.json`
- **Revert command** (review diff first!): `git show eb387132bc` then `git revert eb387132bc` if confirmed safe

### `b0d031cb60` — fix: remove leaf blockstate keys — pink_lapacho.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pink_lapacho.json`
- **Revert command** (review diff first!): `git show b0d031cb60` then `git revert b0d031cb60` if confirmed safe

### `42bb7dae75` — fix: remove leaf blockstate keys — pandanus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show 42bb7dae75` then `git revert 42bb7dae75` if confirmed safe

### `0acd568960` — fix: remove leaf blockstate keys — pale_shroom.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom.json`
- **Revert command** (review diff first!): `git show 0acd568960` then `git revert 0acd568960` if confirmed safe

### `6b04b2fbd7` — fix: remove leaf blockstate keys — pale_dark_eucalyptus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_dark_eucalyptus.json`
- **Revert command** (review diff first!): `git show 6b04b2fbd7` then `git revert 6b04b2fbd7` if confirmed safe

### `10c4b5ac28` — fix: remove leaf blockstate keys — old_willow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_willow.json`
- **Revert command** (review diff first!): `git show 10c4b5ac28` then `git revert 10c4b5ac28` if confirmed safe

### `090d024831` — fix: remove leaf blockstate keys — old_swamp_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json`
- **Revert command** (review diff first!): `git show 090d024831` then `git revert 090d024831` if confirmed safe

### `80ae85c056` — fix: remove leaf blockstate keys — mega_jungle.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 80ae85c056` then `git revert 80ae85c056` if confirmed safe

### `d25356c53c` — fix: remove leaf blockstate keys — mediterranean_cypress.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mediterranean_cypress.json`
- **Revert command** (review diff first!): `git show d25356c53c` then `git revert d25356c53c` if confirmed safe

### `033471e01d` — fix: remove leaf blockstate keys — marula.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/marula.json`
- **Revert command** (review diff first!): `git show 033471e01d` then `git revert 033471e01d` if confirmed safe

### `895ac9454d` — fix: remove leaf blockstate keys — live_oak_dark_swamp.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json`
- **Revert command** (review diff first!): `git show 895ac9454d` then `git revert 895ac9454d` if confirmed safe

### `6d7102bf63` — fix: remove leaf blockstate keys — live_oak_dark.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark.json`
- **Revert command** (review diff first!): `git show 6d7102bf63` then `git revert 6d7102bf63` if confirmed safe

### `5e98a9c9b7` — fix: remove leaf blockstate keys — live_oak_bright.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_bright.json`
- **Revert command** (review diff first!): `git show 5e98a9c9b7` then `git revert 5e98a9c9b7` if confirmed safe

### `f866375515` — fix: remove leaf blockstate keys — live_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak.json`
- **Revert command** (review diff first!): `git show f866375515` then `git revert f866375515` if confirmed safe

### `c17fc70149` — fix: remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show c17fc70149` then `git revert c17fc70149` if confirmed safe

### `0a0b7975d6` — fix: remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show 0a0b7975d6` then `git revert 0a0b7975d6` if confirmed safe

### `1256585947` — fix: remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show 1256585947` then `git revert 1256585947` if confirmed safe

### `1779857621` — fix: remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show 1779857621` then `git revert 1779857621` if confirmed safe

### `ad7ef4fea2` — fix: remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show ad7ef4fea2` then `git revert ad7ef4fea2` if confirmed safe

### `259186dfa4` — fix: remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 259186dfa4` then `git revert 259186dfa4` if confirmed safe

### `aba90c85a1` — fix: remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show aba90c85a1` then `git revert aba90c85a1` if confirmed safe

### `cfbad6c7ed` — fix: remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show cfbad6c7ed` then `git revert cfbad6c7ed` if confirmed safe

### `0e62ed01ea` — fix: remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/8.json`
- **Revert command** (review diff first!): `git show 0e62ed01ea` then `git revert 0e62ed01ea` if confirmed safe

### `9f53ea453f` — fix: remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/7.json`
- **Revert command** (review diff first!): `git show 9f53ea453f` then `git revert 9f53ea453f` if confirmed safe

### `98e10267bc` — fix: remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/6.json`
- **Revert command** (review diff first!): `git show 98e10267bc` then `git revert 98e10267bc` if confirmed safe

### `194c4acfed` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/5.json`
- **Revert command** (review diff first!): `git show 194c4acfed` then `git revert 194c4acfed` if confirmed safe

### `c41b2c6478` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/4.json`
- **Revert command** (review diff first!): `git show c41b2c6478` then `git revert c41b2c6478` if confirmed safe

### `66fab05ab8` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/3.json`
- **Revert command** (review diff first!): `git show 66fab05ab8` then `git revert 66fab05ab8` if confirmed safe

### `77d263838b` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/2.json`
- **Revert command** (review diff first!): `git show 77d263838b` then `git revert 77d263838b` if confirmed safe

### `f8d8b77920` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/1.json`
- **Revert command** (review diff first!): `git show f8d8b77920` then `git revert f8d8b77920` if confirmed safe

### `34642b2859` — fix: remove leaf blockstate keys — kapok.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show 34642b2859` then `git revert 34642b2859` if confirmed safe

### `e4536ab5a7` — fix: remove leaf blockstate keys — jungle_mangrove.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show e4536ab5a7` then `git revert e4536ab5a7` if confirmed safe

### `86c91e913d` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/5.json`
- **Revert command** (review diff first!): `git show 86c91e913d` then `git revert 86c91e913d` if confirmed safe

### `6613be537b` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/4.json`
- **Revert command** (review diff first!): `git show 6613be537b` then `git revert 6613be537b` if confirmed safe

### `a17d2d0c92` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/3.json`
- **Revert command** (review diff first!): `git show a17d2d0c92` then `git revert a17d2d0c92` if confirmed safe

### `12bc262500` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/2.json`
- **Revert command** (review diff first!): `git show 12bc262500` then `git revert 12bc262500` if confirmed safe

### `deb229f243` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/1.json`
- **Revert command** (review diff first!): `git show deb229f243` then `git revert deb229f243` if confirmed safe

### `c683e4209c` — fix: remove leaf blockstate keys — leaves_2_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show c683e4209c` then `git revert c683e4209c` if confirmed safe

### `50c27125e1` — fix: remove leaf blockstate keys — leaves_2_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show 50c27125e1` then `git revert 50c27125e1` if confirmed safe

### `7a09f7a45b` — fix: remove leaf blockstate keys — leaves_1_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show 7a09f7a45b` then `git revert 7a09f7a45b` if confirmed safe

### `24dee361d4` — fix: remove leaf blockstate keys — leaves_1_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 24dee361d4` then `git revert 24dee361d4` if confirmed safe

### `816d487eee` — fix: remove leaf blockstate keys — 4_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_west.json`
- **Revert command** (review diff first!): `git show 816d487eee` then `git revert 816d487eee` if confirmed safe

### `f163c4cb68` — fix: remove leaf blockstate keys — 4_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_south.json`
- **Revert command** (review diff first!): `git show f163c4cb68` then `git revert f163c4cb68` if confirmed safe

### `5690b832e1` — fix: remove leaf blockstate keys — 4_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_north.json`
- **Revert command** (review diff first!): `git show 5690b832e1` then `git revert 5690b832e1` if confirmed safe

### `bb920c58f8` — fix: remove leaf blockstate keys — 4_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_east.json`
- **Revert command** (review diff first!): `git show bb920c58f8` then `git revert bb920c58f8` if confirmed safe

### `0edcb0cfac` — fix: remove leaf blockstate keys — 9.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 0edcb0cfac` then `git revert 0edcb0cfac` if confirmed safe

### `2d0e255ee6` — fix: remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show 2d0e255ee6` then `git revert 2d0e255ee6` if confirmed safe

### `a3fd0257af` — fix: remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show a3fd0257af` then `git revert a3fd0257af` if confirmed safe

### `299aa3dc10` — fix: remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show 299aa3dc10` then `git revert 299aa3dc10` if confirmed safe

### `56a66a78f2` — fix: remove leaf blockstate keys — 10.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show 56a66a78f2` then `git revert 56a66a78f2` if confirmed safe

### `02d6ab4217` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/5.json`
- **Revert command** (review diff first!): `git show 02d6ab4217` then `git revert 02d6ab4217` if confirmed safe

### `a57447c2c5` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/4.json`
- **Revert command** (review diff first!): `git show a57447c2c5` then `git revert a57447c2c5` if confirmed safe

### `ca3744a045` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/3.json`
- **Revert command** (review diff first!): `git show ca3744a045` then `git revert ca3744a045` if confirmed safe

### `0c98bb40c4` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/2.json`
- **Revert command** (review diff first!): `git show 0c98bb40c4` then `git revert 0c98bb40c4` if confirmed safe

### `c9e6907b3e` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/1.json`
- **Revert command** (review diff first!): `git show c9e6907b3e` then `git revert c9e6907b3e` if confirmed safe

### `b7ff4eea35` — fix: remove leaf blockstate keys — leaves_2_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show b7ff4eea35` then `git revert b7ff4eea35` if confirmed safe

### `4bfa9b976b` — fix: remove leaf blockstate keys — leaves_2_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show 4bfa9b976b` then `git revert 4bfa9b976b` if confirmed safe

### `aa4c552116` — fix: remove leaf blockstate keys — leaves_1_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show aa4c552116` then `git revert aa4c552116` if confirmed safe

### `3825f8dc1c` — fix: remove leaf blockstate keys — leaves_1_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 3825f8dc1c` then `git revert 3825f8dc1c` if confirmed safe

### `d7b19b3593` — fix: remove leaf blockstate keys — 4_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_west.json`
- **Revert command** (review diff first!): `git show d7b19b3593` then `git revert d7b19b3593` if confirmed safe

### `943a5212b8` — fix: remove leaf blockstate keys — 4_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_south.json`
- **Revert command** (review diff first!): `git show 943a5212b8` then `git revert 943a5212b8` if confirmed safe

### `fb90ca440d` — fix: remove leaf blockstate keys — 4_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_north.json`
- **Revert command** (review diff first!): `git show fb90ca440d` then `git revert fb90ca440d` if confirmed safe

### `1aaee5233b` — fix: remove leaf blockstate keys — 4_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_east.json`
- **Revert command** (review diff first!): `git show 1aaee5233b` then `git revert 1aaee5233b` if confirmed safe

### `7316cfaf3c` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show 7316cfaf3c` then `git revert 7316cfaf3c` if confirmed safe

### `52b95db8df` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show 52b95db8df` then `git revert 52b95db8df` if confirmed safe

### `f7c7dae514` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show f7c7dae514` then `git revert f7c7dae514` if confirmed safe

### `a5d663f806` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show a5d663f806` then `git revert a5d663f806` if confirmed safe

### `8a59a8e768` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show 8a59a8e768` then `git revert 8a59a8e768` if confirmed safe

### `052fe32e42` — fix: remove leaf blockstate keys — extra_leaf.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/extra_leaf.json`
- **Revert command** (review diff first!): `git show 052fe32e42` then `git revert 052fe32e42` if confirmed safe

### `d9bb1221c2` — fix: remove leaf blockstate keys — branch_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show d9bb1221c2` then `git revert d9bb1221c2` if confirmed safe

### `bc44546585` — fix: remove leaf blockstate keys — branch_sw.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_sw.json`
- **Revert command** (review diff first!): `git show bc44546585` then `git revert bc44546585` if confirmed safe

### `8cc44b871b` — fix: remove leaf blockstate keys — branch_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show 8cc44b871b` then `git revert 8cc44b871b` if confirmed safe

### `6427e81149` — fix: remove leaf blockstate keys — branch_se.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_se.json`
- **Revert command** (review diff first!): `git show 6427e81149` then `git revert 6427e81149` if confirmed safe

### `856d4d91a9` — fix: remove leaf blockstate keys — branch_nw.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_nw.json`
- **Revert command** (review diff first!): `git show 856d4d91a9` then `git revert 856d4d91a9` if confirmed safe

### `2ce2f075ba` — fix: remove leaf blockstate keys — branch_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 2ce2f075ba` then `git revert 2ce2f075ba` if confirmed safe

### `bd7b1847dd` — fix: remove leaf blockstate keys — branch_ne.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_ne.json`
- **Revert command** (review diff first!): `git show bd7b1847dd` then `git revert bd7b1847dd` if confirmed safe

### `68a1c35334` — fix: remove leaf blockstate keys — branch_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show 68a1c35334` then `git revert 68a1c35334` if confirmed safe

### `f60bc35358` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show f60bc35358` then `git revert f60bc35358` if confirmed safe

### `b913f5ba0e` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show b913f5ba0e` then `git revert b913f5ba0e` if confirmed safe

### `67403a8639` — fix: remove leaf blockstate keys — glow_banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/glow_banyan.json`
- **Revert command** (review diff first!): `git show 67403a8639` then `git revert 67403a8639` if confirmed safe

### `fb1787709f` — fix: remove leaf blockstate keys — flowering_cassia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_cassia.json`
- **Revert command** (review diff first!): `git show fb1787709f` then `git revert fb1787709f` if confirmed safe

### `5319429989` — fix: remove leaf blockstate keys — eucalyptus_salubris.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_salubris.json`
- **Revert command** (review diff first!): `git show 5319429989` then `git revert 5319429989` if confirmed safe

### `74ef751398` — fix: remove leaf blockstate keys — desert_fan_palm_tall.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_tall.json`
- **Revert command** (review diff first!): `git show 74ef751398` then `git revert 74ef751398` if confirmed safe

### `11b62afd55` — fix: remove leaf blockstate keys — desert_fan_palm_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_2.json`
- **Revert command** (review diff first!): `git show 11b62afd55` then `git revert 11b62afd55` if confirmed safe

### `93081868e6` — fix: remove leaf blockstate keys — desert_fan_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm.json`
- **Revert command** (review diff first!): `git show 93081868e6` then `git revert 93081868e6` if confirmed safe

### `eb3cfdcf87` — fix: remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show eb3cfdcf87` then `git revert eb3cfdcf87` if confirmed safe

### `b050a0e84f` — fix: remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show b050a0e84f` then `git revert b050a0e84f` if confirmed safe

### `b39f69a4e6` — fix: remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show b39f69a4e6` then `git revert b39f69a4e6` if confirmed safe

### `c9d287b220` — fix: remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show c9d287b220` then `git revert c9d287b220` if confirmed safe

### `f6a3d718f3` — fix: remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show f6a3d718f3` then `git revert f6a3d718f3` if confirmed safe

### `312817526a` — fix: remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 312817526a` then `git revert 312817526a` if confirmed safe

### `fab3b07089` — fix: remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show fab3b07089` then `git revert fab3b07089` if confirmed safe

### `2a7d0eff99` — fix: remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 2a7d0eff99` then `git revert 2a7d0eff99` if confirmed safe

### `c0c13bf64d` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/5.json`
- **Revert command** (review diff first!): `git show c0c13bf64d` then `git revert c0c13bf64d` if confirmed safe

### `e0db92f79a` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/4.json`
- **Revert command** (review diff first!): `git show e0db92f79a` then `git revert e0db92f79a` if confirmed safe

### `a0318d6454` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/3.json`
- **Revert command** (review diff first!): `git show a0318d6454` then `git revert a0318d6454` if confirmed safe

### `9d8f6f70f9` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/2.json`
- **Revert command** (review diff first!): `git show 9d8f6f70f9` then `git revert 9d8f6f70f9` if confirmed safe

### `14b497d60b` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/1.json`
- **Revert command** (review diff first!): `git show 14b497d60b` then `git revert 14b497d60b` if confirmed safe

### `74aaeddefc` — fix: remove leaf blockstate keys — dark_banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dark_banyan.json`
- **Revert command** (review diff first!): `git show 74aaeddefc` then `git revert 74aaeddefc` if confirmed safe

### `bac64b3cb3` — fix: remove leaf blockstate keys — complex_oak_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show bac64b3cb3` then `git revert bac64b3cb3` if confirmed safe

### `e5f1f30f9f` — fix: remove leaf blockstate keys — complex_oak_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show e5f1f30f9f` then `git revert e5f1f30f9f` if confirmed safe

### `e1ffba4b46` — fix: remove leaf blockstate keys — complex_dark_oak_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show e1ffba4b46` then `git revert e1ffba4b46` if confirmed safe

### `278106de27` — fix: remove leaf blockstate keys — complex_dark_oak_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 278106de27` then `git revert 278106de27` if confirmed safe

### `f86787ce01` — fix: remove leaf blockstate keys — coastal_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show f86787ce01` then `git revert f86787ce01` if confirmed safe

### `87cbc9a27c` — fix: remove leaf blockstate keys — coastal_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show 87cbc9a27c` then `git revert 87cbc9a27c` if confirmed safe

### `8594848845` — fix: remove leaf blockstate keys — coastal_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 8594848845` then `git revert 8594848845` if confirmed safe

### `f180087a78` — fix: remove leaf blockstate keys — coastal_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show f180087a78` then `git revert f180087a78` if confirmed safe

### `1a7420f944` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show 1a7420f944` then `git revert 1a7420f944` if confirmed safe

### `6aeb75e2d9` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show 6aeb75e2d9` then `git revert 6aeb75e2d9` if confirmed safe

### `3ca2580565` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show 3ca2580565` then `git revert 3ca2580565` if confirmed safe

### `ca7670c767` — fix: remove leaf blockstate keys — bent_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_west.json`
- **Revert command** (review diff first!): `git show ca7670c767` then `git revert ca7670c767` if confirmed safe

### `a45ad7ec92` — fix: remove leaf blockstate keys — bent_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_south.json`
- **Revert command** (review diff first!): `git show a45ad7ec92` then `git revert a45ad7ec92` if confirmed safe

### `5019924bac` — fix: remove leaf blockstate keys — bent_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_north.json`
- **Revert command** (review diff first!): `git show 5019924bac` then `git revert 5019924bac` if confirmed safe

### `fabb0eafa0` — fix: remove leaf blockstate keys — bent_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_east.json`
- **Revert command** (review diff first!): `git show fabb0eafa0` then `git revert fabb0eafa0` if confirmed safe

### `3f8d8e3852` — fix: remove leaf blockstate keys — bayou_cypress_4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_4.json`
- **Revert command** (review diff first!): `git show 3f8d8e3852` then `git revert 3f8d8e3852` if confirmed safe

### `7fe67899c2` — fix: remove leaf blockstate keys — bayou_cypress_3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_3.json`
- **Revert command** (review diff first!): `git show 7fe67899c2` then `git revert 7fe67899c2` if confirmed safe

### `4111e2fe0a` — fix: remove leaf blockstate keys — bayou_cypress_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_2.json`
- **Revert command** (review diff first!): `git show 4111e2fe0a` then `git revert 4111e2fe0a` if confirmed safe

### `af9605167d` — fix: remove leaf blockstate keys — bayou_cypress_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_1.json`
- **Revert command** (review diff first!): `git show af9605167d` then `git revert af9605167d` if confirmed safe

### `d96ff0ad08` — fix: remove leaf blockstate keys — bayou_cypress.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress.json`
- **Revert command** (review diff first!): `git show d96ff0ad08` then `git revert d96ff0ad08` if confirmed safe

### `8d6ff272b2` — fix: remove leaf blockstate keys — bayou.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou.json`
- **Revert command** (review diff first!): `git show 8d6ff272b2` then `git revert 8d6ff272b2` if confirmed safe

### `bb3e990d67` — fix: remove leaf blockstate keys — baobab_short.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_short.json`
- **Revert command** (review diff first!): `git show bb3e990d67` then `git revert bb3e990d67` if confirmed safe

### `b24d444d3f` — fix: remove leaf blockstate keys — baobab.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab.json`
- **Revert command** (review diff first!): `git show b24d444d3f` then `git revert b24d444d3f` if confirmed safe

### `9ee98e9344` — fix: remove leaf blockstate keys — banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/banyan.json`
- **Revert command** (review diff first!): `git show 9ee98e9344` then `git revert 9ee98e9344` if confirmed safe

### `9686f0980c` — fix: remove leaf blockstate keys — ancient_swamp_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
- **Revert command** (review diff first!): `git show 9686f0980c` then `git revert 9686f0980c` if confirmed safe

### `8e5f73cede` — fix: remove leaf blockstate keys — ancient_pale_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_pale_oak.json`
- **Revert command** (review diff first!): `git show 8e5f73cede` then `git revert 8e5f73cede` if confirmed safe

### `6c0363f9ea` — fix: remove leaf blockstate keys — ancient_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_oak.json`
- **Revert command** (review diff first!): `git show 6c0363f9ea` then `git revert 6c0363f9ea` if confirmed safe

### `572430f56f` — fix: remove leaf blockstate keys — ancient_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak.json`
- **Revert command** (review diff first!): `git show 572430f56f` then `git revert 572430f56f` if confirmed safe

### `889ebcdb00` — fix: remove leaf blockstate keys — ancient_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_birch.json`
- **Revert command** (review diff first!): `git show 889ebcdb00` then `git revert 889ebcdb00` if confirmed safe

### `a13eae7c00` — fix: remove leaf blockstate keys — ancient_azalea.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_azalea.json`
- **Revert command** (review diff first!): `git show a13eae7c00` then `git revert a13eae7c00` if confirmed safe

### `1503b2379f` — fix: remove leaf blockstate keys — waterlily_pink.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_pink.json`
- **Revert command** (review diff first!): `git show 1503b2379f` then `git revert 1503b2379f` if confirmed safe

### `8af143799e` — fix: remove leaf blockstate keys — waterlily_magenta.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_magenta.json`
- **Revert command** (review diff first!): `git show 8af143799e` then `git revert 8af143799e` if confirmed safe

### `d3d804bfe5` — fix: remove leaf blockstate keys — waterlily_blue.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_blue.json`
- **Revert command** (review diff first!): `git show d3d804bfe5` then `git revert d3d804bfe5` if confirmed safe

### `c279bdc790` — fix: remove leaf blockstate keys — water_grass_with_lily.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_lily.json`
- **Revert command** (review diff first!): `git show c279bdc790` then `git revert c279bdc790` if confirmed safe

### `8f814709c7` — fix: remove leaf blockstate keys — water_grass_with_blue_orchids.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_blue_orchids.json`
- **Revert command** (review diff first!): `git show 8f814709c7` then `git revert 8f814709c7` if confirmed safe

### `f26b3a9c8b` — fix: remove leaf blockstate keys — water_grass_with_azure_bluets.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_azure_bluets.json`
- **Revert command** (review diff first!): `git show f26b3a9c8b` then `git revert f26b3a9c8b` if confirmed safe

### `6d8787836a` — fix: remove leaf blockstate keys — water_grass.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass.json`
- **Revert command** (review diff first!): `git show 6d8787836a` then `git revert 6d8787836a` if confirmed safe

### `8eaf19ac62` — fix: remove leaf blockstate keys — oasis_pool.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/oasis_pool.json`
- **Revert command** (review diff first!): `git show 8eaf19ac62` then `git revert 8eaf19ac62` if confirmed safe

### `ee72efce46` — fix: remove leaf blockstate keys — agave_spiking_large.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_spiking_large.json`
- **Revert command** (review diff first!): `git show ee72efce46` then `git revert ee72efce46` if confirmed safe

### `0413d09a5c` — fix: remove leaf blockstate keys — agave_spiking.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_spiking.json`
- **Revert command** (review diff first!): `git show 0413d09a5c` then `git revert 0413d09a5c` if confirmed safe

### `edab4f0b47` — fix: remove leaf blockstate keys — agave_flowering_large.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_large.json`
- **Revert command** (review diff first!): `git show edab4f0b47` then `git revert edab4f0b47` if confirmed safe

### `a1d35058e1` — fix: remove leaf blockstate keys — agave_flowering_dead.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_dead.json`
- **Revert command** (review diff first!): `git show a1d35058e1` then `git revert a1d35058e1` if confirmed safe

### `f32e331f21` — fix: remove leaf blockstate keys — agave_flowering_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_2.json`
- **Revert command** (review diff first!): `git show f32e331f21` then `git revert f32e331f21` if confirmed safe

### `bd912b41cd` — fix: remove leaf blockstate keys — agave_flowering.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering.json`
- **Revert command** (review diff first!): `git show bd912b41cd` then `git revert bd912b41cd` if confirmed safe

### `aabd7b41f0` — fix: remove leaf blockstate keys — agave.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave.json`
- **Revert command** (review diff first!): `git show aabd7b41f0` then `git revert aabd7b41f0` if confirmed safe

### `c3aa600ca7` — fix: remove leaf blockstate keys — groundsel_leaves.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/groundsel_leaves.json`
- **Revert command** (review diff first!): `git show c3aa600ca7` then `git revert c3aa600ca7` if confirmed safe

### `4727343505` — fix: remove leaf blockstate keys — patch_enoki.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
- **Revert command** (review diff first!): `git show 4727343505` then `git revert 4727343505` if confirmed safe

### `df527ccc6c` — fix: remove leaf blockstate keys — medium_muscaria.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/medium_muscaria.json`
- **Revert command** (review diff first!): `git show df527ccc6c` then `git revert df527ccc6c` if confirmed safe

### `af476ab042` — fix: remove leaf blockstate keys — giant_omphalotus_illudens.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json`
- **Revert command** (review diff first!): `git show af476ab042` then `git revert af476ab042` if confirmed safe

### `987cfc6300` — fix: remove leaf blockstate keys — giant_muscaria.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_muscaria.json`
- **Revert command** (review diff first!): `git show 987cfc6300` then `git revert 987cfc6300` if confirmed safe

### `f86b82ae90` — fix: remove leaf blockstate keys — giant_morel.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_morel.json`
- **Revert command** (review diff first!): `git show f86b82ae90` then `git revert f86b82ae90` if confirmed safe

### `952391dcc1` — fix: remove leaf blockstate keys — giant_matsutake.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show 952391dcc1` then `git revert 952391dcc1` if confirmed safe

### `1b74148fad` — fix: remove leaf blockstate keys — giant_enoki.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 1b74148fad` then `git revert 1b74148fad` if confirmed safe

### `d3408f19a4` — fix: remove leaf blockstate keys — fungal_forest_red.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_red.json`
- **Revert command** (review diff first!): `git show d3408f19a4` then `git revert d3408f19a4` if confirmed safe

### `c67bec3ccc` — fix: remove leaf blockstate keys — fungal_forest_orange.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json`
- **Revert command** (review diff first!): `git show c67bec3ccc` then `git revert c67bec3ccc` if confirmed safe

### `c992fc30eb` — fix: remove leaf blockstate keys — fungal_forest_brown.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_brown.json`
- **Revert command** (review diff first!): `git show c992fc30eb` then `git revert c992fc30eb` if confirmed safe

### `29bb8ca45b` — fix: remove leaf blockstate keys — bracket_fungus.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show 29bb8ca45b` then `git revert 29bb8ca45b` if confirmed safe

### `a817748d4d` — fix: remove leaf blockstate keys — twisting_rose.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/twisting_rose.json`
- **Revert command** (review diff first!): `git show a817748d4d` then `git revert a817748d4d` if confirmed safe

### `3e634c41a8` — fix: remove leaf blockstate keys — spanish_moss.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/spanish_moss.json`
- **Revert command** (review diff first!): `git show 3e634c41a8` then `git revert 3e634c41a8` if confirmed safe

### `90865ce3ba` — fix: remove leaf blockstate keys — 9.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/9.json`
- **Revert command** (review diff first!): `git show 90865ce3ba` then `git revert 90865ce3ba` if confirmed safe

### `11099b01da` — fix: remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/8.json`
- **Revert command** (review diff first!): `git show 11099b01da` then `git revert 11099b01da` if confirmed safe

### `7ed6517cfa` — fix: remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/7.json`
- **Revert command** (review diff first!): `git show 7ed6517cfa` then `git revert 7ed6517cfa` if confirmed safe

### `8dd9ad3586` — fix: remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/6.json`
- **Revert command** (review diff first!): `git show 8dd9ad3586` then `git revert 8dd9ad3586` if confirmed safe

### `ff3ca1441b` — fix: remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/5.json`
- **Revert command** (review diff first!): `git show ff3ca1441b` then `git revert ff3ca1441b` if confirmed safe

### `7b85dc2c40` — fix: remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/4.json`
- **Revert command** (review diff first!): `git show 7b85dc2c40` then `git revert 7b85dc2c40` if confirmed safe

### `bede5c69b9` — fix: remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/3.json`
- **Revert command** (review diff first!): `git show bede5c69b9` then `git revert bede5c69b9` if confirmed safe

### `c7f258f283` — fix: remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/2.json`
- **Revert command** (review diff first!): `git show c7f258f283` then `git revert c7f258f283` if confirmed safe

### `d383bbeccb` — fix: remove leaf blockstate keys — 14.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/14.json`
- **Revert command** (review diff first!): `git show d383bbeccb` then `git revert d383bbeccb` if confirmed safe

### `c2b182b541` — fix: remove leaf blockstate keys — 13.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/13.json`
- **Revert command** (review diff first!): `git show c2b182b541` then `git revert c2b182b541` if confirmed safe

### `6359c0be10` — fix: remove leaf blockstate keys — 12.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/12.json`
- **Revert command** (review diff first!): `git show 6359c0be10` then `git revert 6359c0be10` if confirmed safe

### `73abe3f7c5` — fix: remove leaf blockstate keys — 11.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/11.json`
- **Revert command** (review diff first!): `git show 73abe3f7c5` then `git revert 73abe3f7c5` if confirmed safe

### `5287773574` — fix: remove leaf blockstate keys — 10.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/10.json`
- **Revert command** (review diff first!): `git show 5287773574` then `git revert 5287773574` if confirmed safe

### `d32d1d376a` — fix: remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/1.json`
- **Revert command** (review diff first!): `git show d32d1d376a` then `git revert d32d1d376a` if confirmed safe

### `fc7a17987c` — fix: remove leaf blockstate keys — bamboo_shoot.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/bamboo_shoot.json`
- **Revert command** (review diff first!): `git show fc7a17987c` then `git revert fc7a17987c` if confirmed safe

### `24872842fe` — fix: remove leaf blockstate keys — desert.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/desert.json`
- **Revert command** (review diff first!): `git show 24872842fe` then `git revert 24872842fe` if confirmed safe

### `d0776cd86e` — fix: remove leaf blockstate keys — birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/birch.json`
- **Revert command** (review diff first!): `git show d0776cd86e` then `git revert d0776cd86e` if confirmed safe

### `ae8db91607` — fix: remove leaf blockstate keys — fan_corals.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/fan_corals.json`
- **Revert command** (review diff first!): `git show ae8db91607` then `git revert ae8db91607` if confirmed safe

### `74209f83fa` — fix: remove leaf blockstate keys — coral_air_pockets.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/coral_air_pockets.json`
- **Revert command** (review diff first!): `git show 74209f83fa` then `git revert 74209f83fa` if confirmed safe

### `b1a9490400` — fix: remove leaf blockstate keys — dripstone_spike_3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_3.json`
- **Revert command** (review diff first!): `git show b1a9490400` then `git revert b1a9490400` if confirmed safe

### `340dd364dc` — fix: remove leaf blockstate keys — dripstone_spike_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_2.json`
- **Revert command** (review diff first!): `git show 340dd364dc` then `git revert 340dd364dc` if confirmed safe

### `da7f5c0d4e` — fix: remove leaf blockstate keys — dripstone_spike_1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_1.json`
- **Revert command** (review diff first!): `git show da7f5c0d4e` then `git revert da7f5c0d4e` if confirmed safe

### `d04a396c54` — fix: remove leaf blockstate keys — tall_top.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/palm/branch/tall_top.json`
- **Revert command** (review diff first!): `git show d04a396c54` then `git revert d04a396c54` if confirmed safe

### `2f442dec2f` — fix: remove leaf blockstate keys — tubeworm.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/tubeworm.json`
- **Revert command** (review diff first!): `git show 2f442dec2f` then `git revert 2f442dec2f` if confirmed safe

### `bc1a33a51f` — fix: remove leaf blockstate keys — small_tubeworm.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/small_tubeworm.json`
- **Revert command** (review diff first!): `git show bc1a33a51f` then `git revert bc1a33a51f` if confirmed safe

### `e4d7b249ac` — fix: remove leaf blockstate keys — hydrothermal_vent.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
- **Revert command** (review diff first!): `git show e4d7b249ac` then `git revert e4d7b249ac` if confirmed safe

### `09e7339489` — fix: remove leaf blockstate keys — giant_tubeworm_4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
- **Revert command** (review diff first!): `git show 09e7339489` then `git revert 09e7339489` if confirmed safe

### `a4b9502c4f` — fix: remove leaf blockstate keys — giant_tubeworm_3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
- **Revert command** (review diff first!): `git show a4b9502c4f` then `git revert a4b9502c4f` if confirmed safe

### `ec5fdaee13` — fix: remove leaf blockstate keys — giant_tubeworm_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
- **Revert command** (review diff first!): `git show ec5fdaee13` then `git revert ec5fdaee13` if confirmed safe

### `4c4ecd973e` — fix: remove leaf blockstate keys — giant_tubeworm_1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
- **Revert command** (review diff first!): `git show 4c4ecd973e` then `git revert 4c4ecd973e` if confirmed safe

### `a75d8aef12` — fix: remove leaf blockstate keys — scarecrow.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/decor/scarecrow.json`
- **Revert command** (review diff first!): `git show a75d8aef12` then `git revert a75d8aef12` if confirmed safe

### `a10c4471ba` — fix: remove leaf blockstate keys — floating_lantern.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/decor/floating_lantern.json`
- **Revert command** (review diff first!): `git show a10c4471ba` then `git revert a10c4471ba` if confirmed safe

### `51526ec5e7` — fix: remove dirt_provider and force_dirt — white_bracket_fungi.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show 51526ec5e7` then `git revert 51526ec5e7` if confirmed safe

### `d2074bcea0` — fix: remove dirt_provider and force_dirt — fungal_powder_spores.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show d2074bcea0` then `git revert d2074bcea0` if confirmed safe

### `c61f8683c2` — fix: remove dirt_provider and force_dirt — coastal_palm_west.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show c61f8683c2` then `git revert c61f8683c2` if confirmed safe

### `edce125761` — fix: remove dirt_provider and force_dirt — coastal_palm_south.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show edce125761` then `git revert edce125761` if confirmed safe

### `574856b30f` — fix: remove dirt_provider and force_dirt — coastal_palm_north.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 574856b30f` then `git revert 574856b30f` if confirmed safe

### `2aff052ecf` — fix: remove dirt_provider and force_dirt — coastal_palm_east.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 2aff052ecf` then `git revert 2aff052ecf` if confirmed safe

### `01c0511708` — fix: remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 01c0511708` then `git revert 01c0511708` if confirmed safe

### `6fab0940ab` — fix: remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 6fab0940ab` then `git revert 6fab0940ab` if confirmed safe

### `c7f94a538e` — fix: remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show c7f94a538e` then `git revert c7f94a538e` if confirmed safe

### `0f8b876b64` — fix: remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 0f8b876b64` then `git revert 0f8b876b64` if confirmed safe

### `f503030a65` — fix: remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show f503030a65` then `git revert f503030a65` if confirmed safe

### `54eed85c63` — fix: remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 54eed85c63` then `git revert 54eed85c63` if confirmed safe

### `1cca69272f` — fix: remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 1cca69272f` then `git revert 1cca69272f` if confirmed safe

### `d57483eea7` — fix: remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show d57483eea7` then `git revert d57483eea7` if confirmed safe

### `befbc1241b` — fix: remove dirt_provider and force_dirt — pandanus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show befbc1241b` then `git revert befbc1241b` if confirmed safe

### `a683e4ae30` — fix: remove dirt_provider and force_dirt — mega_jungle.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show a683e4ae30` then `git revert a683e4ae30` if confirmed safe

### `473c60097b` — fix: remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show 473c60097b` then `git revert 473c60097b` if confirmed safe

### `0cd4dcb75e` — fix: remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show 0cd4dcb75e` then `git revert 0cd4dcb75e` if confirmed safe

### `e3030f27d4` — fix: remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show e3030f27d4` then `git revert e3030f27d4` if confirmed safe

### `3a53d87c4f` — fix: remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show 3a53d87c4f` then `git revert 3a53d87c4f` if confirmed safe

### `543382e93d` — fix: remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show 543382e93d` then `git revert 543382e93d` if confirmed safe

### `9de5fc10a0` — fix: remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 9de5fc10a0` then `git revert 9de5fc10a0` if confirmed safe

### `6f7d239b5f` — fix: remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show 6f7d239b5f` then `git revert 6f7d239b5f` if confirmed safe

### `70d4a70e79` — fix: remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show 70d4a70e79` then `git revert 70d4a70e79` if confirmed safe

### `7bd9b890a3` — fix: remove dirt_provider and force_dirt — kapok.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show 7bd9b890a3` then `git revert 7bd9b890a3` if confirmed safe

### `90e3b612cb` — fix: remove dirt_provider and force_dirt — jungle_mangrove.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show 90e3b612cb` then `git revert 90e3b612cb` if confirmed safe

### `4d9473fa44` — fix: remove dirt_provider and force_dirt — 9.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 4d9473fa44` then `git revert 4d9473fa44` if confirmed safe

### `68dfb868e0` — fix: remove dirt_provider and force_dirt — 8.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show 68dfb868e0` then `git revert 68dfb868e0` if confirmed safe

### `413d10367c` — fix: remove dirt_provider and force_dirt — 7.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show 413d10367c` then `git revert 413d10367c` if confirmed safe

### `706f51bf27` — fix: remove dirt_provider and force_dirt — 6.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show 706f51bf27` then `git revert 706f51bf27` if confirmed safe

### `e6591dd0ea` — fix: remove dirt_provider and force_dirt — 10.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show e6591dd0ea` then `git revert e6591dd0ea` if confirmed safe

### `a298888266` — fix: remove dirt_provider and force_dirt — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show a298888266` then `git revert a298888266` if confirmed safe

### `2aca6d4d41` — fix: remove dirt_provider and force_dirt — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show 2aca6d4d41` then `git revert 2aca6d4d41` if confirmed safe

### `3ef2c5e8b7` — fix: remove dirt_provider and force_dirt — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show 3ef2c5e8b7` then `git revert 3ef2c5e8b7` if confirmed safe

### `214a8da9a0` — fix: remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show 214a8da9a0` then `git revert 214a8da9a0` if confirmed safe

### `e53d3ba05f` — fix: remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show e53d3ba05f` then `git revert e53d3ba05f` if confirmed safe

### `2c38a2b7aa` — fix: remove dirt_provider and force_dirt — branch_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show 2c38a2b7aa` then `git revert 2c38a2b7aa` if confirmed safe

### `0328e21aba` — fix: remove dirt_provider and force_dirt — branch_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show 0328e21aba` then `git revert 0328e21aba` if confirmed safe

### `04cbc015bd` — fix: remove dirt_provider and force_dirt — branch_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 04cbc015bd` then `git revert 04cbc015bd` if confirmed safe

### `e7b8c119b9` — fix: remove dirt_provider and force_dirt — branch_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show e7b8c119b9` then `git revert e7b8c119b9` if confirmed safe

### `a9176ada70` — fix: remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show a9176ada70` then `git revert a9176ada70` if confirmed safe

### `ebe63e11e2` — fix: remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show ebe63e11e2` then `git revert ebe63e11e2` if confirmed safe

### `d6a55cadd4` — fix: remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show d6a55cadd4` then `git revert d6a55cadd4` if confirmed safe

### `8c947c25a4` — fix: remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 8c947c25a4` then `git revert 8c947c25a4` if confirmed safe

### `ec6722b9e9` — fix: remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show ec6722b9e9` then `git revert ec6722b9e9` if confirmed safe

### `25751037c9` — fix: remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 25751037c9` then `git revert 25751037c9` if confirmed safe

### `cb8b24998f` — fix: remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show cb8b24998f` then `git revert cb8b24998f` if confirmed safe

### `b006d05147` — fix: remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show b006d05147` then `git revert b006d05147` if confirmed safe

### `589758464e` — fix: remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 589758464e` then `git revert 589758464e` if confirmed safe

### `49f089e1ce` — fix: remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 49f089e1ce` then `git revert 49f089e1ce` if confirmed safe

### `f9ef3c95eb` — fix: remove dirt_provider and force_dirt — complex_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show f9ef3c95eb` then `git revert f9ef3c95eb` if confirmed safe

### `5bd6420467` — fix: remove dirt_provider and force_dirt — complex_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show 5bd6420467` then `git revert 5bd6420467` if confirmed safe

### `ef8448f806` — fix: remove dirt_provider and force_dirt — complex_dark_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show ef8448f806` then `git revert ef8448f806` if confirmed safe

### `fa17068171` — fix: remove dirt_provider and force_dirt — complex_dark_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show fa17068171` then `git revert fa17068171` if confirmed safe

### `ab965fdb7e` — fix: remove dirt_provider and force_dirt — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show ab965fdb7e` then `git revert ab965fdb7e` if confirmed safe

### `8137b925d2` — fix: remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show 8137b925d2` then `git revert 8137b925d2` if confirmed safe

### `a4dd7a3486` — fix: remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show a4dd7a3486` then `git revert a4dd7a3486` if confirmed safe

### `353202a09d` — fix: remove dirt_provider and force_dirt — baobab_short.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_short.json`
- **Revert command** (review diff first!): `git show 353202a09d` then `git revert 353202a09d` if confirmed safe

### `16aa9d8f16` — fix: remove dirt_provider and force_dirt — ancient_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak.json`
- **Revert command** (review diff first!): `git show 16aa9d8f16` then `git revert 16aa9d8f16` if confirmed safe

### `c0b3cc11bc` — fix: remove dirt_provider and force_dirt — giant_matsutake.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show c0b3cc11bc` then `git revert c0b3cc11bc` if confirmed safe

### `25ec0578dd` — fix: remove dirt_provider and force_dirt — giant_enoki.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 25ec0578dd` then `git revert 25ec0578dd` if confirmed safe

### `c80084ab16` — fix: remove dirt_provider and force_dirt — bracket_fungus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show c80084ab16` then `git revert c80084ab16` if confirmed safe

### `b25fcfa6f6` — restore: fix 740 files with wrong matching_blocks type from Cat 4 inference

- **Removed debunked keys**: can_grow_through, heightmap, snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 845
  - `data/wythers/worldgen/configured_feature/decor/floating_lantern.json`
  - `data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json`
  - `data/wythers/worldgen/configured_feature/decor/scarecrow.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
  - `data/wythers/worldgen/configured_feature/other/small_tubeworm.json`
  - `data/wythers/worldgen/configured_feature/other/tubeworm.json`
  - ... +835 more
- **Revert command** (review diff first!): `git show b25fcfa6f6` then `git revert b25fcfa6f6` if confirmed safe

### `991e738022` — restore: jungle_mangrove.json — Cat 3 incorrectly removed required exclusion_radius keys

- **Removed debunked keys**: can_grow_through
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show 991e738022` then `git revert 991e738022` if confirmed safe

### `e838c923d0` — fix: convert random_patch — pale_acacia_stump.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_acacia_stump.json`
- **Revert command** (review diff first!): `git show e838c923d0` then `git revert e838c923d0` if confirmed safe

### `b094b1382b` — fix: add missing type field — palm_nuts.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/part/palm_nuts.json`
- **Revert command** (review diff first!): `git show b094b1382b` then `git revert b094b1382b` if confirmed safe

### `a5bb2fe670` — fix: add missing type field — palm_leaves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/part/palm_leaves.json`
- **Revert command** (review diff first!): `git show a5bb2fe670` then `git revert a5bb2fe670` if confirmed safe

### `ae09a9fb75` — fix: add missing type field — savanna_mossy.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/savanna_mossy.json`
- **Revert command** (review diff first!): `git show ae09a9fb75` then `git revert ae09a9fb75` if confirmed safe

### `9b6c41a5c3` — fix: add missing type field — oasis_palms.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/oasis_palms.json`
- **Revert command** (review diff first!): `git show 9b6c41a5c3` then `git revert 9b6c41a5c3` if confirmed safe

### `5419f1c7de` — fix: add missing type field — cherry_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_pools.json`
- **Revert command** (review diff first!): `git show 5419f1c7de` then `git revert 5419f1c7de` if confirmed safe

### `1aca378bf3` — fix: add missing type field — cherry_maple.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_maple.json`
- **Revert command** (review diff first!): `git show 1aca378bf3` then `git revert 1aca378bf3` if confirmed safe

### `21fb66dd09` — fix: add missing type field — cherry_huangshan_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_huangshan_pine.json`
- **Revert command** (review diff first!): `git show 21fb66dd09` then `git revert 21fb66dd09` if confirmed safe

### `79f97f0045` — fix: add missing type field — salt_lake_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/salt_lake_grass.json`
- **Revert command** (review diff first!): `git show 79f97f0045` then `git revert 79f97f0045` if confirmed safe

### `a6f3736954` — fix: add missing type field — white_bracket_fungi.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show a6f3736954` then `git revert a6f3736954` if confirmed safe

### `0610ef389e` — fix: add missing type field — fungal_weeping_growths.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_weeping_growths.json`
- **Revert command** (review diff first!): `git show 0610ef389e` then `git revert 0610ef389e` if confirmed safe

### `99d8967d1d` — fix: add missing type field — fungal_sculk_trees.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_sculk_trees.json`
- **Revert command** (review diff first!): `git show 99d8967d1d` then `git revert 99d8967d1d` if confirmed safe

### `1cc6fac399` — fix: add missing type field — fungal_savanna_vegetation.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_savanna_vegetation.json`
- **Revert command** (review diff first!): `git show 1cc6fac399` then `git revert 1cc6fac399` if confirmed safe

### `0a45174218` — fix: add missing type field — fungal_powder_spores.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show 0a45174218` then `git revert 0a45174218` if confirmed safe

### `5952ba89fc` — fix: add missing type field — fungal_moss_sprouts.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_moss_sprouts.json`
- **Revert command** (review diff first!): `git show 5952ba89fc` then `git revert 5952ba89fc` if confirmed safe

### `039bc52e87` — fix: add missing type field — fungal_jungle_vegetation.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_vegetation.json`
- **Revert command** (review diff first!): `git show 039bc52e87` then `git revert 039bc52e87` if confirmed safe

### `92bf3fe4b8` — fix: add missing type field — fungal_blood_woods.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_blood_woods.json`
- **Revert command** (review diff first!): `git show 92bf3fe4b8` then `git revert 92bf3fe4b8` if confirmed safe

### `33366f6721` — fix: add missing type field — creaking_heart.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/creaking_heart.json`
- **Revert command** (review diff first!): `git show 33366f6721` then `git revert 33366f6721` if confirmed safe

### `dc0f3199b7` — fix: add missing type field — coral_disks_small.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/coral_disks_small.json`
- **Revert command** (review diff first!): `git show dc0f3199b7` then `git revert dc0f3199b7` if confirmed safe

### `ce558f06a5` — fix: add missing type field — coral_disks_ranged.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/coral_disks_ranged.json`
- **Revert command** (review diff first!): `git show ce558f06a5` then `git revert ce558f06a5` if confirmed safe

### `5bf57bb5a3` — fix: add missing type field — coral_disks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/coral_disks.json`
- **Revert command** (review diff first!): `git show 5bf57bb5a3` then `git revert 5bf57bb5a3` if confirmed safe

### `a9f0bf37a2` — fix: add missing type field — coral_blobs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/coral_blobs.json`
- **Revert command** (review diff first!): `git show a9f0bf37a2` then `git revert a9f0bf37a2` if confirmed safe

### `7735311707` — fix: add missing type field — cocoanuts.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/cocoanuts.json`
- **Revert command** (review diff first!): `git show 7735311707` then `git revert 7735311707` if confirmed safe

### `9573799c4d` — fix: add missing type field — baobab_interior.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/baobab_interior.json`
- **Revert command** (review diff first!): `git show 9573799c4d` then `git revert 9573799c4d` if confirmed safe

### `672f2f2437` — fix: add missing type field — cherry_maple_snowy.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_maple_snowy.json`
- **Revert command** (review diff first!): `git show 672f2f2437` then `git revert 672f2f2437` if confirmed safe

### `ee97167eb5` — fix: add missing type field — cherry_huangshan_pine_snowy.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_huangshan_pine_snowy.json`
- **Revert command** (review diff first!): `git show ee97167eb5` then `git revert ee97167eb5` if confirmed safe

### `4b19813641` — fix: add missing type field — yellowstone_white.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_white.json`
- **Revert command** (review diff first!): `git show 4b19813641` then `git revert 4b19813641` if confirmed safe

### `428648a56f` — fix: add missing type field — yellowstone_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_pools.json`
- **Revert command** (review diff first!): `git show 428648a56f` then `git revert 428648a56f` if confirmed safe

### `4d8bb19aa6` — fix: add missing type field — yellowstone_path.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_path.json`
- **Revert command** (review diff first!): `git show 4d8bb19aa6` then `git revert 4d8bb19aa6` if confirmed safe

### `4209080389` — fix: add missing type field — yellowstone_orange.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_orange.json`
- **Revert command** (review diff first!): `git show 4209080389` then `git revert 4209080389` if confirmed safe

### `7c9661110b` — fix: add missing type field — yellowstone_dripstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_dripstone.json`
- **Revert command** (review diff first!): `git show 7c9661110b` then `git revert 7c9661110b` if confirmed safe

### `2cac99d911` — fix: add missing type field — yellowstone_colours.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/yellowstone_colours.json`
- **Revert command** (review diff first!): `git show 2cac99d911` then `git revert 2cac99d911` if confirmed safe

### `44c64a593a` — fix: add missing type field — volcano_high_snow_blocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/volcano_high_snow_blocks.json`
- **Revert command** (review diff first!): `git show 44c64a593a` then `git revert 44c64a593a` if confirmed safe

### `6a7631685f` — fix: add missing type field — volcanic_pools.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/volcanic_pools.json`
- **Revert command** (review diff first!): `git show 6a7631685f` then `git revert 6a7631685f` if confirmed safe

### `bb9a9e2f3a` — fix: add missing type field — underground_volcanifier.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/underground_volcanifier.json`
- **Revert command** (review diff first!): `git show bb9a9e2f3a` then `git revert bb9a9e2f3a` if confirmed safe

### `b7e9eaded5` — fix: add missing type field — tundra_light.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/tundra_light.json`
- **Revert command** (review diff first!): `git show b7e9eaded5` then `git revert b7e9eaded5` if confirmed safe

### `e34f6707e9` — fix: add missing type field — thermal_vents_floor.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_vents_floor.json`
- **Revert command** (review diff first!): `git show e34f6707e9` then `git revert e34f6707e9` if confirmed safe

### `f502da4f6d` — fix: add missing type field — thermal_taiga_white.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_taiga_white.json`
- **Revert command** (review diff first!): `git show f502da4f6d` then `git revert f502da4f6d` if confirmed safe

### `12b9284d2e` — fix: add missing type field — thermal_taiga_disk_terracotta_yellow.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_taiga_disk_terracotta_yellow.json`
- **Revert command** (review diff first!): `git show 12b9284d2e` then `git revert 12b9284d2e` if confirmed safe

### `085fb21d1a` — fix: add missing type field — thermal_taiga_disk_terracotta_white.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_taiga_disk_terracotta_white.json`
- **Revert command** (review diff first!): `git show 085fb21d1a` then `git revert 085fb21d1a` if confirmed safe

### `d6d60da70b` — fix: add missing type field — thermal_taiga_disk_terracotta_orange.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_taiga_disk_terracotta_orange.json`
- **Revert command** (review diff first!): `git show d6d60da70b` then `git revert d6d60da70b` if confirmed safe

### `01993609e8` — fix: add missing type field — thermal_steppe_soul.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_soul.json`
- **Revert command** (review diff first!): `git show 01993609e8` then `git revert 01993609e8` if confirmed safe

### `279188ecba` — fix: add missing type field — thermal_steppe_mud.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_mud.json`
- **Revert command** (review diff first!): `git show 279188ecba` then `git revert 279188ecba` if confirmed safe

### `5255fd8687` — fix: add missing type field — thermal_steppe_gray.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_gray.json`
- **Revert command** (review diff first!): `git show 5255fd8687` then `git revert 5255fd8687` if confirmed safe

### `c4b6c8ac50` — fix: add missing type field — thermal_steppe_dripstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_dripstone.json`
- **Revert command** (review diff first!): `git show c4b6c8ac50` then `git revert c4b6c8ac50` if confirmed safe

### `d4cf2db763` — fix: add missing type field — thermal_steppe_dirt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_dirt.json`
- **Revert command** (review diff first!): `git show d4cf2db763` then `git revert d4cf2db763` if confirmed safe

### `a2f164430b` — fix: add missing type field — thermal_steppe_brown.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_steppe_brown.json`
- **Revert command** (review diff first!): `git show a2f164430b` then `git revert a2f164430b` if confirmed safe

### `9095f6ae2e` — fix: add missing type field — thermal_savanna_soul.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_soul.json`
- **Revert command** (review diff first!): `git show 9095f6ae2e` then `git revert 9095f6ae2e` if confirmed safe

### `1321508aea` — fix: add missing type field — thermal_savanna_mud.json

- **Removed debunked keys**: heightmap, snowy
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_mud.json`
- **Revert command** (review diff first!): `git show 1321508aea` then `git revert 1321508aea` if confirmed safe

### `605695cd18` — fix: add missing type field — thermal_savanna_gray.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_gray.json`
- **Revert command** (review diff first!): `git show 605695cd18` then `git revert 605695cd18` if confirmed safe

### `79103c9520` — fix: add missing type field — thermal_savanna_dripstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_dripstone.json`
- **Revert command** (review diff first!): `git show 79103c9520` then `git revert 79103c9520` if confirmed safe

### `f26f66689b` — fix: add missing type field — thermal_savanna_dirt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_dirt.json`
- **Revert command** (review diff first!): `git show f26f66689b` then `git revert f26f66689b` if confirmed safe

### `f7d73c66fa` — fix: add missing type field — thermal_savanna_brown.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/thermal_savanna_brown.json`
- **Revert command** (review diff first!): `git show f7d73c66fa` then `git revert f7d73c66fa` if confirmed safe

### `4580e05190` — fix: add missing type field — swamp_stone_replacer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_stone_replacer.json`
- **Revert command** (review diff first!): `git show 4580e05190` then `git revert 4580e05190` if confirmed safe

### `6ffea0e4b3` — fix: add missing type field — swamp_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_pools.json`
- **Revert command** (review diff first!): `git show 6ffea0e4b3` then `git revert 6ffea0e4b3` if confirmed safe

### `bbde50d4c2` — fix: add missing type field — swamp_hills.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_hills.json`
- **Revert command** (review diff first!): `git show bbde50d4c2` then `git revert bbde50d4c2` if confirmed safe

### `2247b1c0d9` — fix: add missing type field — swamp_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_ground.json`
- **Revert command** (review diff first!): `git show 2247b1c0d9` then `git revert 2247b1c0d9` if confirmed safe

### `ef418398c1` — fix: add missing type field — swamp_carver_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_carver_2.json`
- **Revert command** (review diff first!): `git show ef418398c1` then `git revert ef418398c1` if confirmed safe

### `a4a156d939` — fix: add missing type field — swamp_carver.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/swamp_carver.json`
- **Revert command** (review diff first!): `git show a4a156d939` then `git revert a4a156d939` if confirmed safe

### `1c9d6fd8eb` — fix: add missing type field — sunken_soil.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sunken_soil.json`
- **Revert command** (review diff first!): `git show 1c9d6fd8eb` then `git revert 1c9d6fd8eb` if confirmed safe

### `6188f7f2ab` — fix: add missing type field — sudd_marsh_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sudd_marsh_ground.json`
- **Revert command** (review diff first!): `git show 6188f7f2ab` then `git revert 6188f7f2ab` if confirmed safe

### `f08af3cb4b` — fix: add missing type field — stony_shore_tuff.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stony_shore_tuff.json`
- **Revert command** (review diff first!): `git show f08af3cb4b` then `git revert f08af3cb4b` if confirmed safe

### `4ec8cd5933` — fix: add missing type field — stone_cliffs_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs_surface.json`
- **Revert command** (review diff first!): `git show 4ec8cd5933` then `git revert 4ec8cd5933` if confirmed safe

### `41fcd2a0e5` — fix: add missing type field — stone_cliffs_sheer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs_sheer.json`
- **Revert command** (review diff first!): `git show 41fcd2a0e5` then `git revert 41fcd2a0e5` if confirmed safe

### `0c714f5d93` — fix: add missing type field — stone_cliffs_plus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs_plus.json`
- **Revert command** (review diff first!): `git show 0c714f5d93` then `git revert 0c714f5d93` if confirmed safe

### `1884a6eb92` — fix: add missing type field — stone_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs.json`
- **Revert command** (review diff first!): `git show 1884a6eb92` then `git revert 1884a6eb92` if confirmed safe

### `e9eeec4417` — fix: add missing type field — sponge_disks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sponge_disks.json`
- **Revert command** (review diff first!): `git show e9eeec4417` then `git revert e9eeec4417` if confirmed safe

### `a8cf9d47a2` — fix: add missing type field — sparse_jungle_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sparse_jungle_shore.json`
- **Revert command** (review diff first!): `git show a8cf9d47a2` then `git revert a8cf9d47a2` if confirmed safe

### `1a1f83fd46` — fix: add missing type field — snowy_leaves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snowy_leaves.json`
- **Revert command** (review diff first!): `git show 1a1f83fd46` then `git revert 1a1f83fd46` if confirmed safe

### `8d68bf39af` — fix: add missing type field — snowy_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snowy_ground.json`
- **Revert command** (review diff first!): `git show 8d68bf39af` then `git revert 8d68bf39af` if confirmed safe

### `0f92a604b9` — fix: add missing type field — snowy_edges.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snowy_edges.json`
- **Revert command** (review diff first!): `git show 0f92a604b9` then `git revert 0f92a604b9` if confirmed safe

### `910f12f7a3` — fix: add missing type field — snow_blocks_disk.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snow_blocks_disk.json`
- **Revert command** (review diff first!): `git show 910f12f7a3` then `git revert 910f12f7a3` if confirmed safe

### `8fe6d823d3` — fix: add missing type field — snow_blocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snow_blocks.json`
- **Revert command** (review diff first!): `git show 8fe6d823d3` then `git revert 8fe6d823d3` if confirmed safe

### `1813ec506b` — fix: add missing type field — shield.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/shield.json`
- **Revert command** (review diff first!): `git show 1813ec506b` then `git revert 1813ec506b` if confirmed safe

### `1d5b83ccbe` — fix: add missing type field — shadow_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/shadow_snow.json`
- **Revert command** (review diff first!): `git show 1d5b83ccbe` then `git revert 1d5b83ccbe` if confirmed safe

### `e3e4600e10` — fix: add missing type field — sea_cliff.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sea_cliff.json`
- **Revert command** (review diff first!): `git show e3e4600e10` then `git revert e3e4600e10` if confirmed safe

### `cad1f8c06f` — fix: add missing type field — savanna_sandy_wash_x.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/savanna_sandy_wash_x.json`
- **Revert command** (review diff first!): `git show cad1f8c06f` then `git revert cad1f8c06f` if confirmed safe

### `67243ccda4` — fix: add missing type field — savanna_sandy_wash.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/savanna_sandy_wash.json`
- **Revert command** (review diff first!): `git show 67243ccda4` then `git revert 67243ccda4` if confirmed safe

### `479a869268` — fix: add missing type field — sandy_marsh_hills.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_marsh_hills.json`
- **Revert command** (review diff first!): `git show 479a869268` then `git revert 479a869268` if confirmed safe

### `8236fcde6d` — fix: add missing type field — sandy_marsh_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_marsh_ground.json`
- **Revert command** (review diff first!): `git show 8236fcde6d` then `git revert 8236fcde6d` if confirmed safe

### `59bc1c37f9` — fix: add missing type field — sandy_jungle_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_jungle_2.json`
- **Revert command** (review diff first!): `git show 59bc1c37f9` then `git revert 59bc1c37f9` if confirmed safe

### `c7227ea791` — fix: add missing type field — sandy_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_jungle.json`
- **Revert command** (review diff first!): `git show c7227ea791` then `git revert c7227ea791` if confirmed safe

### `9475972dfa` — fix: add missing type field — sandy_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_forest.json`
- **Revert command** (review diff first!): `git show 9475972dfa` then `git revert 9475972dfa` if confirmed safe

### `7a4addaae9` — fix: add missing type field — sandy_floor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_floor.json`
- **Revert command** (review diff first!): `git show 7a4addaae9` then `git revert 7a4addaae9` if confirmed safe

### `f38524159a` — fix: add missing type field — rooted_cave_floor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/rooted_cave_floor.json`
- **Revert command** (review diff first!): `git show f38524159a` then `git revert f38524159a` if confirmed safe

### `3a08a3fbc7` — fix: add missing type field — riverbank_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/riverbank_sand.json`
- **Revert command** (review diff first!): `git show 3a08a3fbc7` then `git revert 3a08a3fbc7` if confirmed safe

### `8d1758ab7e` — fix: add missing type field — riverbank_red_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/riverbank_red_sand.json`
- **Revert command** (review diff first!): `git show 8d1758ab7e` then `git revert 8d1758ab7e` if confirmed safe

### `ee88c1ee07` — fix: add missing type field — riverbank_plains.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/riverbank_plains.json`
- **Revert command** (review diff first!): `git show ee88c1ee07` then `git revert ee88c1ee07` if confirmed safe

### `d266e25d8c` — fix: add missing type field — riverbank_packed_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/riverbank_packed_mud.json`
- **Revert command** (review diff first!): `git show d266e25d8c` then `git revert d266e25d8c` if confirmed safe

### `7985b5c9cc` — fix: add missing type field — riverbank_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/riverbank_gravel.json`
- **Revert command** (review diff first!): `git show 7985b5c9cc` then `git revert 7985b5c9cc` if confirmed safe

### `2f03f2b9fb` — fix: add missing type field — river_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/river_grass.json`
- **Revert command** (review diff first!): `git show 2f03f2b9fb` then `git revert 2f03f2b9fb` if confirmed safe

### `f980bfb750` — fix: add missing type field — river_clay.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/river_clay.json`
- **Revert command** (review diff first!): `git show f980bfb750` then `git revert f980bfb750` if confirmed safe

### `b0c7c12963` — fix: add missing type field — replace_volcanics_flower_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_volcanics_flower_forest.json`
- **Revert command** (review diff first!): `git show b0c7c12963` then `git revert b0c7c12963` if confirmed safe

### `75a862cf9d` — fix: add missing type field — replace_coarse_dirt_to_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_coarse_dirt_to_moss.json`
- **Revert command** (review diff first!): `git show 75a862cf9d` then `git revert 75a862cf9d` if confirmed safe

### `e25f265666` — fix: add missing type field — rainforest_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/rainforest_ground.json`
- **Revert command** (review diff first!): `git show e25f265666` then `git revert e25f265666` if confirmed safe

### `4f018169fc` — fix: add missing type field — rainforest_carver_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/rainforest_carver_2.json`
- **Revert command** (review diff first!): `git show 4f018169fc` then `git revert 4f018169fc` if confirmed safe

### `69b3b1a069` — fix: add missing type field — rainforest_carver.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/rainforest_carver.json`
- **Revert command** (review diff first!): `git show 69b3b1a069` then `git revert 69b3b1a069` if confirmed safe

### `9ee010e803` — fix: add missing type field — pelagic_clay.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pelagic_clay.json`
- **Revert command** (review diff first!): `git show 9ee010e803` then `git revert 9ee010e803` if confirmed safe

### `d84eb45964` — fix: add missing type field — pamukkale_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_pools.json`
- **Revert command** (review diff first!): `git show d84eb45964` then `git revert d84eb45964` if confirmed safe

### `ef09eca91b` — fix: add missing type field — pamukkale_diorite.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_diorite.json`
- **Revert command** (review diff first!): `git show ef09eca91b` then `git revert ef09eca91b` if confirmed safe

### `974942e314` — fix: add missing type field — pamukkale_calcite.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_calcite.json`
- **Revert command** (review diff first!): `git show 974942e314` then `git revert 974942e314` if confirmed safe

### `f82af6eb57` — fix: add missing type field — packed_mud_canyons.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/packed_mud_canyons.json`
- **Revert command** (review diff first!): `git show f82af6eb57` then `git revert f82af6eb57` if confirmed safe

### `0743bef7f0` — fix: add missing type field — pack_ice_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pack_ice_snow.json`
- **Revert command** (review diff first!): `git show 0743bef7f0` then `git revert 0743bef7f0` if confirmed safe

### `e63fb40d00` — fix: add missing type field — oasis_water.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/oasis_water.json`
- **Revert command** (review diff first!): `git show e63fb40d00` then `git revert e63fb40d00` if confirmed safe

### `049f9d0bc9` — fix: add missing type field — oasis_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/oasis_moss.json`
- **Revert command** (review diff first!): `git show 049f9d0bc9` then `git revert 049f9d0bc9` if confirmed safe

### `d26813eca8` — fix: add missing type field — oasis_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/oasis_grass.json`
- **Revert command** (review diff first!): `git show d26813eca8` then `git revert d26813eca8` if confirmed safe

### `19ca156e95` — fix: add missing type field — oasis_clay.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/oasis_clay.json`
- **Revert command** (review diff first!): `git show 19ca156e95` then `git revert 19ca156e95` if confirmed safe

### `15001c088b` — fix: add missing type field — mushroom_spires_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_spires_grass.json`
- **Revert command** (review diff first!): `git show 15001c088b` then `git revert 15001c088b` if confirmed safe

### `6afcecbbf5` — fix: add missing type field — mushroom_plateau_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_plateau_cliffs.json`
- **Revert command** (review diff first!): `git show 6afcecbbf5` then `git revert 6afcecbbf5` if confirmed safe

### `9516305148` — fix: add missing type field — mushroom_mycelium.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_mycelium.json`
- **Revert command** (review diff first!): `git show 9516305148` then `git revert 9516305148` if confirmed safe

### `e6e6a455d7` — fix: add missing type field — mushroom_fields_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_fields_shore.json`
- **Revert command** (review diff first!): `git show e6e6a455d7` then `git revert e6e6a455d7` if confirmed safe

### `2f76cea184` — fix: add missing type field — mushroom_fields_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_fields_sand.json`
- **Revert command** (review diff first!): `git show 2f76cea184` then `git revert 2f76cea184` if confirmed safe

### `b6557444c9` — fix: add missing type field — mushroom_fields_grass_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_fields_grass_surface.json`
- **Revert command** (review diff first!): `git show b6557444c9` then `git revert b6557444c9` if confirmed safe

### `a2a79146c6` — fix: add missing type field — mushroom_fields_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_fields_grass.json`
- **Revert command** (review diff first!): `git show a2a79146c6` then `git revert a2a79146c6` if confirmed safe

### `c077524c6c` — fix: add missing type field — mushroom_chasms.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mushroom_chasms.json`
- **Revert command** (review diff first!): `git show c077524c6c` then `git revert c077524c6c` if confirmed safe

### `ed9ef1f2a7` — fix: add missing type field — mudflat.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mudflat.json`
- **Revert command** (review diff first!): `git show ed9ef1f2a7` then `git revert ed9ef1f2a7` if confirmed safe

### `002534ea61` — fix: add missing type field — mangrove_swamp_stone_replacer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mangrove_swamp_stone_replacer.json`
- **Revert command** (review diff first!): `git show 002534ea61` then `git revert 002534ea61` if confirmed safe

### `9a0d15b84e` — fix: add missing type field — mangrove_swamp_hills.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mangrove_swamp_hills.json`
- **Revert command** (review diff first!): `git show 9a0d15b84e` then `git revert 9a0d15b84e` if confirmed safe

### `fbcef02877` — fix: add missing type field — mangrove_swamp_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mangrove_swamp_ground.json`
- **Revert command** (review diff first!): `git show fbcef02877` then `git revert fbcef02877` if confirmed safe

### `b873588339` — fix: add missing type field — mangrove_swamp_carver_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mangrove_swamp_carver_2.json`
- **Revert command** (review diff first!): `git show b873588339` then `git revert b873588339` if confirmed safe

### `e55b23cae6` — fix: add missing type field — mangrove_swamp_carver.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/mangrove_swamp_carver.json`
- **Revert command** (review diff first!): `git show e55b23cae6` then `git revert e55b23cae6` if confirmed safe

### `cdd3fbd027` — fix: add missing type field — jungle_floor_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/jungle_floor_3.json`
- **Revert command** (review diff first!): `git show cdd3fbd027` then `git revert cdd3fbd027` if confirmed safe

### `8fbd7c01d9` — fix: add missing type field — jungle_floor_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/jungle_floor_2.json`
- **Revert command** (review diff first!): `git show 8fbd7c01d9` then `git revert 8fbd7c01d9` if confirmed safe

### `28bf9f26da` — fix: add missing type field — jungle_floor_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/jungle_floor_1.json`
- **Revert command** (review diff first!): `git show 28bf9f26da` then `git revert 28bf9f26da` if confirmed safe

### `d701d4ec74` — fix: add missing type field — jungle_floor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/jungle_floor.json`
- **Revert command** (review diff first!): `git show d701d4ec74` then `git revert d701d4ec74` if confirmed safe

### `2f259147dd` — fix: add missing type field — icelandifier_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/icelandifier_2.json`
- **Revert command** (review diff first!): `git show 2f259147dd` then `git revert 2f259147dd` if confirmed safe

### `9ef6f2a251` — fix: add missing type field — iceland_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/iceland_snow.json`
- **Revert command** (review diff first!): `git show 9ef6f2a251` then `git revert 9ef6f2a251` if confirmed safe

### `bd0283b1de` — fix: add missing type field — iceland_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/iceland_moss.json`
- **Revert command** (review diff first!): `git show bd0283b1de` then `git revert bd0283b1de` if confirmed safe

### `de603bb1b7` — fix: add missing type field — ice_spikes_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_grass.json`
- **Revert command** (review diff first!): `git show de603bb1b7` then `git revert de603bb1b7` if confirmed safe

### `d26cf9278b` — fix: add missing type field — ice_spikes_glacial_stone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_stone.json`
- **Revert command** (review diff first!): `git show d26cf9278b` then `git revert d26cf9278b` if confirmed safe

### `194a50ebd6` — fix: add missing type field — ice_spikes_glacial_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_gravel.json`
- **Revert command** (review diff first!): `git show 194a50ebd6` then `git revert 194a50ebd6` if confirmed safe

### `936e28d10f` — fix: add missing type field — ice_spikes_glacial_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_grass.json`
- **Revert command** (review diff first!): `git show 936e28d10f` then `git revert 936e28d10f` if confirmed safe

### `e836981342` — fix: add missing type field — ice_spikes_glacial_dirt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_dirt.json`
- **Revert command** (review diff first!): `git show e836981342` then `git revert e836981342` if confirmed safe

### `88bc3fa5f5` — fix: add missing type field — ice_shelf_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_shelf_4.json`
- **Revert command** (review diff first!): `git show 88bc3fa5f5` then `git revert 88bc3fa5f5` if confirmed safe

### `8ea41213dd` — fix: add missing type field — ice_shelf_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_shelf_3.json`
- **Revert command** (review diff first!): `git show 8ea41213dd` then `git revert 8ea41213dd` if confirmed safe

### `967267f4af` — fix: add missing type field — ice_shelf_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_shelf_2.json`
- **Revert command** (review diff first!): `git show 967267f4af` then `git revert 967267f4af` if confirmed safe

### `d9da2bb2c6` — fix: add missing type field — ice_shelf_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_shelf_1.json`
- **Revert command** (review diff first!): `git show d9da2bb2c6` then `git revert d9da2bb2c6` if confirmed safe

### `f1efd14e28` — fix: add missing type field — ice_shelf_0.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_shelf_0.json`
- **Revert command** (review diff first!): `git show f1efd14e28` then `git revert f1efd14e28` if confirmed safe

### `b427965d2d` — fix: add missing type field — huangshan_spires_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/huangshan_spires_grass.json`
- **Revert command** (review diff first!): `git show b427965d2d` then `git revert b427965d2d` if confirmed safe

### `f9d8a12971` — fix: add missing type field — highland_stone_cliffs_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/highland_stone_cliffs_surface.json`
- **Revert command** (review diff first!): `git show f9d8a12971` then `git revert f9d8a12971` if confirmed safe

### `014d2fbddf` — fix: add missing type field — highland_stone_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/highland_stone_cliffs.json`
- **Revert command** (review diff first!): `git show 014d2fbddf` then `git revert 014d2fbddf` if confirmed safe

### `aca83f27a6` — fix: add missing type field — grove_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/grove_cliffs.json`
- **Revert command** (review diff first!): `git show aca83f27a6` then `git revert aca83f27a6` if confirmed safe

### `2e7d974983` — fix: add missing type field — gravelly_beach_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/gravelly_beach_snow.json`
- **Revert command** (review diff first!): `git show 2e7d974983` then `git revert 2e7d974983` if confirmed safe

### `af13634885` — fix: add missing type field — grass_spread_badlands.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/grass_spread_badlands.json`
- **Revert command** (review diff first!): `git show af13634885` then `git revert af13634885` if confirmed safe

### `19b359f172` — fix: add missing type field — grass_spread.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/grass_spread.json`
- **Revert command** (review diff first!): `git show 19b359f172` then `git revert 19b359f172` if confirmed safe

### `eb1e22768c` — fix: add missing type field — glacier_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacier_1.json`
- **Revert command** (review diff first!): `git show eb1e22768c` then `git revert eb1e22768c` if confirmed safe

### `f75e1fdcce` — fix: add missing type field — glacier_0.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacier_0.json`
- **Revert command** (review diff first!): `git show f75e1fdcce` then `git revert f75e1fdcce` if confirmed safe

### `a1974fdda8` — fix: add missing type field — glacial_scree.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacial_scree.json`
- **Revert command** (review diff first!): `git show a1974fdda8` then `git revert a1974fdda8` if confirmed safe

### `1b97b3b74c` — fix: add missing type field — glacial_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacial_pools.json`
- **Revert command** (review diff first!): `git show 1b97b3b74c` then `git revert 1b97b3b74c` if confirmed safe

### `2c31259a39` — fix: add missing type field — fungal_sculk_infection.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_sculk_infection.json`
- **Revert command** (review diff first!): `git show 2c31259a39` then `git revert 2c31259a39` if confirmed safe

### `c87b47ee17` — fix: add missing type field — fungal_savanna_floor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_savanna_floor.json`
- **Revert command** (review diff first!): `git show c87b47ee17` then `git revert c87b47ee17` if confirmed safe

### `0fce9bccc3` — fix: add missing type field — fungal_prismarine_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_prismarine_shore.json`
- **Revert command** (review diff first!): `git show 0fce9bccc3` then `git revert 0fce9bccc3` if confirmed safe

### `16ca9902b9` — fix: add missing type field — fungal_powder.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_powder.json`
- **Revert command** (review diff first!): `git show 16ca9902b9` then `git revert 16ca9902b9` if confirmed safe

### `0f5d979a9e` — fix: add missing type field — fungal_mossy_shore_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_mossy_shore_2.json`
- **Revert command** (review diff first!): `git show 0f5d979a9e` then `git revert 0f5d979a9e` if confirmed safe

### `8f9fa530d0` — fix: add missing type field — fungal_mossy_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_mossy_shore.json`
- **Revert command** (review diff first!): `git show 8f9fa530d0` then `git revert 8f9fa530d0` if confirmed safe

### `aeff5e1244` — fix: add missing type field — fungal_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_moss.json`
- **Revert command** (review diff first!): `git show aeff5e1244` then `git revert aeff5e1244` if confirmed safe

### `0d3961b416` — fix: add missing type field — fungal_fire_coral_shore_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_fire_coral_shore_2.json`
- **Revert command** (review diff first!): `git show 0d3961b416` then `git revert 0d3961b416` if confirmed safe

### `70d70d9102` — fix: add missing type field — fungal_fire_coral_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_fire_coral_shore.json`
- **Revert command** (review diff first!): `git show 70d70d9102` then `git revert 70d70d9102` if confirmed safe

### `661063fbc3` — fix: add missing type field — fungal_coral_mycelium.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral_mycelium.json`
- **Revert command** (review diff first!): `git show 661063fbc3` then `git revert 661063fbc3` if confirmed safe

### `5befb440ed` — fix: add missing type field — fungal_coral_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral_2.json`
- **Revert command** (review diff first!): `git show 5befb440ed` then `git revert 5befb440ed` if confirmed safe

### `2b8b02a69d` — fix: add missing type field — fungal_coral.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral.json`
- **Revert command** (review diff first!): `git show 2b8b02a69d` then `git revert 2b8b02a69d` if confirmed safe

### `eebaad097d` — fix: add missing type field — frozen_river.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/frozen_river.json`
- **Revert command** (review diff first!): `git show eebaad097d` then `git revert eebaad097d` if confirmed safe

### `8ea8c6a093` — fix: add missing type field — frozen_ocean_land_replacer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/frozen_ocean_land_replacer.json`
- **Revert command** (review diff first!): `git show 8ea8c6a093` then `git revert 8ea8c6a093` if confirmed safe

### `fc3592a744` — fix: add missing type field — forest_snow_blocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/forest_snow_blocks.json`
- **Revert command** (review diff first!): `git show fc3592a744` then `git revert fc3592a744` if confirmed safe

### `b074ef1a35` — fix: add missing type field — forest_floor_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/forest_floor_grass.json`
- **Revert command** (review diff first!): `git show b074ef1a35` then `git revert b074ef1a35` if confirmed safe

### `2a4b99b9af` — fix: add missing type field — forest_floor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/forest_floor.json`
- **Revert command** (review diff first!): `git show 2a4b99b9af` then `git revert 2a4b99b9af` if confirmed safe

### `78e1b22b1f` — fix: add missing type field — fen_ground.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fen_ground.json`
- **Revert command** (review diff first!): `git show 78e1b22b1f` then `git revert 78e1b22b1f` if confirmed safe

### `41296c790f` — fix: add missing type field — disk_sand_tropical_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_sand_tropical_shore.json`
- **Revert command** (review diff first!): `git show 41296c790f` then `git revert 41296c790f` if confirmed safe

### `c7992e4139` — fix: add missing type field — disk_sand_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_sand_shore.json`
- **Revert command** (review diff first!): `git show c7992e4139` then `git revert c7992e4139` if confirmed safe

### `7d2d128424` — fix: add missing type field — disk_sand_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_sand_forest.json`
- **Revert command** (review diff first!): `git show 7d2d128424` then `git revert 7d2d128424` if confirmed safe

### `3697d8dcc9` — fix: add missing type field — disk_packed_mud_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_packed_mud_shore.json`
- **Revert command** (review diff first!): `git show 3697d8dcc9` then `git revert 3697d8dcc9` if confirmed safe

### `dbdf8da241` — fix: add missing type field — disk_muddy_roots_in_podzol.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_muddy_roots_in_podzol.json`
- **Revert command** (review diff first!): `git show dbdf8da241` then `git revert dbdf8da241` if confirmed safe

### `4397300e1e` — fix: add missing type field — disk_mud_swamp.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_mud_swamp.json`
- **Revert command** (review diff first!): `git show 4397300e1e` then `git revert 4397300e1e` if confirmed safe

### `0737ef6ae4` — fix: add missing type field — disk_mud_shore_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_mud_shore_jungle.json`
- **Revert command** (review diff first!): `git show 0737ef6ae4` then `git revert 0737ef6ae4` if confirmed safe

### `db9e29ac68` — fix: add missing type field — disk_mud_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_mud_shore.json`
- **Revert command** (review diff first!): `git show db9e29ac68` then `git revert db9e29ac68` if confirmed safe

### `7d34002ba9` — fix: add missing type field — disk_mud_in_muddy_roots.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_mud_in_muddy_roots.json`
- **Revert command** (review diff first!): `git show 7d34002ba9` then `git revert 7d34002ba9` if confirmed safe

### `bd98cda550` — fix: add missing type field — disk_mossy_cobblestone_in_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_mossy_cobblestone_in_gravel.json`
- **Revert command** (review diff first!): `git show bd98cda550` then `git revert bd98cda550` if confirmed safe

### `ff3410c47b` — fix: add missing type field — disk_moss_in_mossy_cobblestone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_moss_in_mossy_cobblestone.json`
- **Revert command** (review diff first!): `git show ff3410c47b` then `git revert ff3410c47b` if confirmed safe

### `58f50336f6` — fix: add missing type field — disk_gravel_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_gravel_shore.json`
- **Revert command** (review diff first!): `git show 58f50336f6` then `git revert 58f50336f6` if confirmed safe

### `032c303c63` — fix: add missing type field — disk_gravel_river.json

- **Removed debunked keys**: heightmap
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_gravel_river.json`
- **Revert command** (review diff first!): `git show 032c303c63` then `git revert 032c303c63` if confirmed safe

### `fae392a192` — fix: add missing type field — disk_gravel_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_gravel_forest.json`
- **Revert command** (review diff first!): `git show fae392a192` then `git revert fae392a192` if confirmed safe

### `dc07c8f60d` — fix: add missing type field — disk_gravel_birch_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_gravel_birch_forest.json`
- **Revert command** (review diff first!): `git show dc07c8f60d` then `git revert dc07c8f60d` if confirmed safe

### `6548adef41` — fix: add missing type field — disk_dead_coral_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_dead_coral_shore.json`
- **Revert command** (review diff first!): `git show 6548adef41` then `git revert 6548adef41` if confirmed safe

### `7a946183c0` — fix: add missing type field — disk_beach_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/disk_beach_sand.json`
- **Revert command** (review diff first!): `git show 7a946183c0` then `git revert 7a946183c0` if confirmed safe

### `8ce92e809a` — fix: add missing type field — deglaciator_9.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_9.json`
- **Revert command** (review diff first!): `git show 8ce92e809a` then `git revert 8ce92e809a` if confirmed safe

### `b49a956415` — fix: add missing type field — deglaciator_8.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_8.json`
- **Revert command** (review diff first!): `git show b49a956415` then `git revert b49a956415` if confirmed safe

### `7376b07e53` — fix: add missing type field — deglaciator_7.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_7.json`
- **Revert command** (review diff first!): `git show 7376b07e53` then `git revert 7376b07e53` if confirmed safe

### `7401701112` — fix: add missing type field — deglaciator_6.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_6.json`
- **Revert command** (review diff first!): `git show 7401701112` then `git revert 7401701112` if confirmed safe

### `4f70372ff5` — fix: add missing type field — deglaciator_5.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_5.json`
- **Revert command** (review diff first!): `git show 4f70372ff5` then `git revert 4f70372ff5` if confirmed safe

### `b941e6b06e` — fix: add missing type field — deglaciator_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_4.json`
- **Revert command** (review diff first!): `git show b941e6b06e` then `git revert b941e6b06e` if confirmed safe

### `ad53e31225` — fix: add missing type field — deglaciator_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_3.json`
- **Revert command** (review diff first!): `git show ad53e31225` then `git revert ad53e31225` if confirmed safe

### `df487be743` — fix: add missing type field — deglaciator_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_2.json`
- **Revert command** (review diff first!): `git show df487be743` then `git revert df487be743` if confirmed safe

### `5436e59486` — fix: add missing type field — deglaciator_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_1.json`
- **Revert command** (review diff first!): `git show 5436e59486` then `git revert 5436e59486` if confirmed safe

### `8c9e96199d` — fix: add missing type field — deglaciator_01.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_01.json`
- **Revert command** (review diff first!): `git show 8c9e96199d` then `git revert 8c9e96199d` if confirmed safe

### `09615e4771` — fix: add missing type field — deglaciator_00.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_00.json`
- **Revert command** (review diff first!): `git show 09615e4771` then `git revert 09615e4771` if confirmed safe

### `75dd8f02f8` — fix: add missing type field — deglaciator_0.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_0.json`
- **Revert command** (review diff first!): `git show 75dd8f02f8` then `git revert 75dd8f02f8` if confirmed safe

### `cfd12d251f` — fix: add missing type field — deepslate_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deepslate_cliffs.json`
- **Revert command** (review diff first!): `git show cfd12d251f` then `git revert cfd12d251f` if confirmed safe

### `670adffdd0` — fix: add missing type field — deep_dark_placer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deep_dark_placer.json`
- **Revert command** (review diff first!): `git show 670adffdd0` then `git revert 670adffdd0` if confirmed safe

### `38afa2d470` — fix: add missing type field — de_snowify_stone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/de_snowify_stone.json`
- **Revert command** (review diff first!): `git show 38afa2d470` then `git revert 38afa2d470` if confirmed safe

### `cc1949ef77` — fix: add missing type field — danakil_yellow_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_yellow_2.json`
- **Revert command** (review diff first!): `git show cc1949ef77` then `git revert cc1949ef77` if confirmed safe

### `0e43e8bf07` — fix: add missing type field — danakil_yellow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_yellow.json`
- **Revert command** (review diff first!): `git show 0e43e8bf07` then `git revert 0e43e8bf07` if confirmed safe

### `5c1ba7c45f` — fix: add missing type field — danakil_water.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_water.json`
- **Revert command** (review diff first!): `git show 5c1ba7c45f` then `git revert 5c1ba7c45f` if confirmed safe

### `813157e2a9` — fix: add missing type field — danakil_terracotta.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_terracotta.json`
- **Revert command** (review diff first!): `git show 813157e2a9` then `git revert 813157e2a9` if confirmed safe

### `902f94d4da` — fix: add missing type field — danakil_red.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_red.json`
- **Revert command** (review diff first!): `git show 902f94d4da` then `git revert 902f94d4da` if confirmed safe

### `a69b8f509c` — fix: add missing type field — danakil_orange.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_orange.json`
- **Revert command** (review diff first!): `git show a69b8f509c` then `git revert a69b8f509c` if confirmed safe

### `156060b0f4` — fix: add missing type field — danakil_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_mud.json`
- **Revert command** (review diff first!): `git show 156060b0f4` then `git revert 156060b0f4` if confirmed safe

### `08e188bc45` — fix: add missing type field — crust_salt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crust_salt.json`
- **Revert command** (review diff first!): `git show 08e188bc45` then `git revert 08e188bc45` if confirmed safe

### `261a4b5755` — fix: add missing type field — crust_packed_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crust_packed_mud.json`
- **Revert command** (review diff first!): `git show 261a4b5755` then `git revert 261a4b5755` if confirmed safe

### `dc1e2f8193` — fix: add missing type field — crust_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crust_grass.json`
- **Revert command** (review diff first!): `git show dc1e2f8193` then `git revert dc1e2f8193` if confirmed safe

### `d66957057d` — fix: add missing type field — crimson_patch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crimson_patch.json`
- **Revert command** (review diff first!): `git show d66957057d` then `git revert d66957057d` if confirmed safe

### `e118b76f1b` — fix: add missing type field — crack_ice.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crack_ice.json`
- **Revert command** (review diff first!): `git show e118b76f1b` then `git revert e118b76f1b` if confirmed safe

### `727552a474` — fix: add missing type field — cold_ocean_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cold_ocean_gravel.json`
- **Revert command** (review diff first!): `git show 727552a474` then `git revert 727552a474` if confirmed safe

### `01837a31f9` — fix: add missing type field — cold_island_mossy_cobblestone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cold_island_mossy_cobblestone.json`
- **Revert command** (review diff first!): `git show 01837a31f9` then `git revert 01837a31f9` if confirmed safe

### `9a96e1cf2f` — fix: add missing type field — cloud_forest_terrain.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cloud_forest_terrain.json`
- **Revert command** (review diff first!): `git show 9a96e1cf2f` then `git revert 9a96e1cf2f` if confirmed safe

### `6697366d6b` — fix: add missing type field — cloud_forest_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cloud_forest_surface.json`
- **Revert command** (review diff first!): `git show 6697366d6b` then `git revert 6697366d6b` if confirmed safe

### `c98a674cf3` — fix: add missing type field — cherry_pools_edge.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cherry_pools_edge.json`
- **Revert command** (review diff first!): `git show c98a674cf3` then `git revert c98a674cf3` if confirmed safe

### `9c63b86b4b` — fix: add missing type field — cherry_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cherry_pools.json`
- **Revert command** (review diff first!): `git show 9c63b86b4b` then `git revert 9c63b86b4b` if confirmed safe

### `d1f2bb78f4` — fix: add missing type field — cave_ice.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cave_ice.json`
- **Revert command** (review diff first!): `git show d1f2bb78f4` then `git revert d1f2bb78f4` if confirmed safe

### `35da102b7d` — fix: add missing type field — cave_disk_magma.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cave_disk_magma.json`
- **Revert command** (review diff first!): `git show 35da102b7d` then `git revert 35da102b7d` if confirmed safe

### `250a433971` — fix: add missing type field — cave_disk_blackstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cave_disk_blackstone.json`
- **Revert command** (review diff first!): `git show 250a433971` then `git revert 250a433971` if confirmed safe

### `f613afe7ee` — fix: add missing type field — cave_disk_basalt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cave_disk_basalt.json`
- **Revert command** (review diff first!): `git show f613afe7ee` then `git revert f613afe7ee` if confirmed safe

### `06347adfad` — fix: add missing type field — bore_hole_corals.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/bore_hole_corals.json`
- **Revert command** (review diff first!): `git show 06347adfad` then `git revert 06347adfad` if confirmed safe

### `942f5c87a6` — fix: add missing type field — boggy_moss_shore.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/boggy_moss_shore.json`
- **Revert command** (review diff first!): `git show 942f5c87a6` then `git revert 942f5c87a6` if confirmed safe

### `19c58d6b51` — fix: add missing type field — boggy_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/boggy_moss.json`
- **Revert command** (review diff first!): `git show 19c58d6b51` then `git revert 19c58d6b51` if confirmed safe

### `14facce587` — fix: add missing type field — beach_mossy_stone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/beach_mossy_stone.json`
- **Revert command** (review diff first!): `git show 14facce587` then `git revert 14facce587` if confirmed safe

### `ce130feca5` — fix: add missing type field — base_wooded_badlands.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_wooded_badlands.json`
- **Revert command** (review diff first!): `git show ce130feca5` then `git revert ce130feca5` if confirmed safe

### `0bcc4baa14` — fix: add missing type field — base_snowy_beach.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_snowy_beach.json`
- **Revert command** (review diff first!): `git show 0bcc4baa14` then `git revert 0bcc4baa14` if confirmed safe

### `900a86301f` — fix: add missing type field — base_mushroom_fields.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mushroom_fields.json`
- **Revert command** (review diff first!): `git show 900a86301f` then `git revert 900a86301f` if confirmed safe

### `c18f970556` — fix: add missing type field — base_mangrove_swamp_bayou_hills.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mangrove_swamp_bayou_hills.json`
- **Revert command** (review diff first!): `git show c18f970556` then `git revert c18f970556` if confirmed safe

### `f649c870a4` — fix: add missing type field — base_mangrove_swamp.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mangrove_swamp.json`
- **Revert command** (review diff first!): `git show f649c870a4` then `git revert f649c870a4` if confirmed safe

### `6f194cc7c0` — fix: add missing type field — base_jagged_peaks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_jagged_peaks.json`
- **Revert command** (review diff first!): `git show 6f194cc7c0` then `git revert 6f194cc7c0` if confirmed safe

### `7aab729ac8` — fix: add missing type field — base_grove.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_grove.json`
- **Revert command** (review diff first!): `git show 7aab729ac8` then `git revert 7aab729ac8` if confirmed safe

### `4ae4823cf2` — fix: add missing type field — base_dark_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_dark_forest.json`
- **Revert command** (review diff first!): `git show 4ae4823cf2` then `git revert 4ae4823cf2` if confirmed safe

### `d7f5faf90a` — fix: add missing type field — badlands_snow_blocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_snow_blocks.json`
- **Revert command** (review diff first!): `git show d7f5faf90a` then `git revert d7f5faf90a` if confirmed safe

### `3344210611` — fix: add missing type field — badlands_replace_all_red_sand_to_grass_block.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_replace_all_red_sand_to_grass_block.json`
- **Revert command** (review diff first!): `git show 3344210611` then `git revert 3344210611` if confirmed safe

### `e6ed9f5cb0` — fix: add missing type field — badlands_plateau_red_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_plateau_red_sand.json`
- **Revert command** (review diff first!): `git show e6ed9f5cb0` then `git revert e6ed9f5cb0` if confirmed safe

### `692967eb0c` — fix: add missing type field — badlands_plateau_packed_mud_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_plateau_packed_mud_2.json`
- **Revert command** (review diff first!): `git show 692967eb0c` then `git revert 692967eb0c` if confirmed safe

### `ca65c40f43` — fix: add missing type field — badlands_plateau_packed_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_plateau_packed_mud.json`
- **Revert command** (review diff first!): `git show ca65c40f43` then `git revert ca65c40f43` if confirmed safe

### `3a64b4f807` — fix: add missing type field — badlands_alpine_grassland.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/badlands_alpine_grassland.json`
- **Revert command** (review diff first!): `git show 3a64b4f807` then `git revert 3a64b4f807` if confirmed safe

### `5baf98bfef` — fix: add missing type field — atoll_grass.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/atoll_grass.json`
- **Revert command** (review diff first!): `git show 5baf98bfef` then `git revert 5baf98bfef` if confirmed safe

### `a3605cb40f` — fix: add missing type field — arroyo_extension.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/arroyo_extension.json`
- **Revert command** (review diff first!): `git show a3605cb40f` then `git revert a3605cb40f` if confirmed safe

### `5cc71d1b3b` — fix: add missing type field — thermal_vents_soul.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/thermal_vents_soul.json`
- **Revert command** (review diff first!): `git show 5cc71d1b3b` then `git revert 5cc71d1b3b` if confirmed safe

### `a8e7a55710` — fix: add missing type field — thermal_vents_iron.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/thermal_vents_iron.json`
- **Revert command** (review diff first!): `git show a8e7a55710` then `git revert a8e7a55710` if confirmed safe

### `8060a7b516` — fix: add missing type field — tepui_tuff_layer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_tuff_layer.json`
- **Revert command** (review diff first!): `git show 8060a7b516` then `git revert 8060a7b516` if confirmed safe

### `5effc858e2` — fix: add missing type field — tepui_terrain.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_terrain.json`
- **Revert command** (review diff first!): `git show 5effc858e2` then `git revert 5effc858e2` if confirmed safe

### `e1f1f9cef6` — fix: add missing type field — tepui_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_surface.json`
- **Revert command** (review diff first!): `git show e1f1f9cef6` then `git revert e1f1f9cef6` if confirmed safe

### `6937383a82` — fix: add missing type field — tepui_lowland_for_glacier.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_lowland_for_glacier.json`
- **Revert command** (review diff first!): `git show 6937383a82` then `git revert 6937383a82` if confirmed safe

### `48d5212cfa` — fix: add missing type field — tepui_filler.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_filler.json`
- **Revert command** (review diff first!): `git show 48d5212cfa` then `git revert 48d5212cfa` if confirmed safe

### `2fad20488f` — fix: add missing type field — tepui_falls.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_falls.json`
- **Revert command** (review diff first!): `git show 2fad20488f` then `git revert 2fad20488f` if confirmed safe

### `27ad17b394` — fix: add missing type field — tepui_chasms.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_chasms.json`
- **Revert command** (review diff first!): `git show 27ad17b394` then `git revert 27ad17b394` if confirmed safe

### `376b64a2d3` — fix: add missing type field — tepui_caverns.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_caverns.json`
- **Revert command** (review diff first!): `git show 376b64a2d3` then `git revert 376b64a2d3` if confirmed safe

### `9e777e34e4` — fix: add missing type field — tepui_cavern_moss.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_moss.json`
- **Revert command** (review diff first!): `git show 9e777e34e4` then `git revert 9e777e34e4` if confirmed safe

### `799b0dc0ae` — fix: add missing type field — tepui_cavern_lakes.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_lakes.json`
- **Revert command** (review diff first!): `git show 799b0dc0ae` then `git revert 799b0dc0ae` if confirmed safe

### `41ddcdd96d` — fix: add missing type field — tepui_cavern_dripstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_dripstone.json`
- **Revert command** (review diff first!): `git show 41ddcdd96d` then `git revert 41ddcdd96d` if confirmed safe

### `a1d246bf07` — fix: add missing type field — tepui_base.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_base.json`
- **Revert command** (review diff first!): `git show a1d246bf07` then `git revert a1d246bf07` if confirmed safe

### `273c96f131` — fix: add missing type field — tepui_basalt_layer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_basalt_layer.json`
- **Revert command** (review diff first!): `git show 273c96f131` then `git revert 273c96f131` if confirmed safe

### `9f8bf8a253` — fix: add missing type field — tepui.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui.json`
- **Revert command** (review diff first!): `git show 9f8bf8a253` then `git revert 9f8bf8a253` if confirmed safe

### `79cabe48a0` — fix: add missing type field — ice_tunnel_mid.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/ice_tunnel_mid.json`
- **Revert command** (review diff first!): `git show 79cabe48a0` then `git revert 79cabe48a0` if confirmed safe

### `191ce9c4ef` — fix: add missing type field — ice_tunnel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/ice_tunnel.json`
- **Revert command** (review diff first!): `git show 191ce9c4ef` then `git revert 191ce9c4ef` if confirmed safe

### `063f7f6817` — fix: add missing type field — crevasse.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/crevasse.json`
- **Revert command** (review diff first!): `git show 063f7f6817` then `git revert 063f7f6817` if confirmed safe

### `3be3198f87` — fix: add missing type field — wooded_badlands_extender.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/wooded_badlands_extender.json`
- **Revert command** (review diff first!): `git show 3be3198f87` then `git revert 3be3198f87` if confirmed safe

### `3f4b6d96bd` — fix: add missing type field — windswept_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/windswept_snow.json`
- **Revert command** (review diff first!): `git show 3f4b6d96bd` then `git revert 3f4b6d96bd` if confirmed safe

### `c78bfcf6a5` — fix: add missing type field — volcano_snow_blocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/volcano_snow_blocks.json`
- **Revert command** (review diff first!): `git show c78bfcf6a5` then `git revert c78bfcf6a5` if confirmed safe

### `8ef01b00a3` — fix: add missing type field — volcanic_jungle_muddy_roots_on_basalt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/volcanic_jungle_muddy_roots_on_basalt.json`
- **Revert command** (review diff first!): `git show 8ef01b00a3` then `git revert 8ef01b00a3` if confirmed safe

### `0aa4a6061c` — fix: add missing type field — volcanic_jungle_mud_in_basalt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/volcanic_jungle_mud_in_basalt.json`
- **Revert command** (review diff first!): `git show 0aa4a6061c` then `git revert 0aa4a6061c` if confirmed safe

### `94e3948c61` — fix: add missing type field — thermal_savanna_forest_base.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/thermal_savanna_forest_base.json`
- **Revert command** (review diff first!): `git show 94e3948c61` then `git revert 94e3948c61` if confirmed safe

### `68fab50af7` — fix: add missing type field — stony_shore_placer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/stony_shore_placer.json`
- **Revert command** (review diff first!): `git show 68fab50af7` then `git revert 68fab50af7` if confirmed safe

### `799e5397ed` — fix: add missing type field — sea_cliff.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/sea_cliff.json`
- **Revert command** (review diff first!): `git show 799e5397ed` then `git revert 799e5397ed` if confirmed safe

### `6ac8ac78da` — fix: add missing type field — scree.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/scree.json`
- **Revert command** (review diff first!): `git show 6ac8ac78da` then `git revert 6ac8ac78da` if confirmed safe

### `2c04fc61fb` — fix: add missing type field — river_soil.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/river_soil.json`
- **Revert command** (review diff first!): `git show 2c04fc61fb` then `git revert 2c04fc61fb` if confirmed safe

### `75db404412` — fix: add missing type field — river_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/river_gravel.json`
- **Revert command** (review diff first!): `git show 75db404412` then `git revert 75db404412` if confirmed safe

### `354098b4dd` — fix: add missing type field — replace_mud_to_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_mud_to_sand.json`
- **Revert command** (review diff first!): `git show 354098b4dd` then `git revert 354098b4dd` if confirmed safe

### `70a885ac7d` — fix: add missing type field — replace_gravel_to_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_gravel_to_sand.json`
- **Revert command** (review diff first!): `git show 70a885ac7d` then `git revert 70a885ac7d` if confirmed safe

### `fe4deec141` — fix: add missing type field — replace_gravel_to_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_gravel_to_mud.json`
- **Revert command** (review diff first!): `git show fe4deec141` then `git revert fe4deec141` if confirmed safe

### `9bb8beae4a` — fix: add missing type field — replace_dirt_to_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_dirt_to_sand.json`
- **Revert command** (review diff first!): `git show 9bb8beae4a` then `git revert 9bb8beae4a` if confirmed safe

### `203c01acdc` — fix: add missing type field — onsen_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_pools.json`
- **Revert command** (review diff first!): `git show 203c01acdc` then `git revert 203c01acdc` if confirmed safe

### `3ee6303479` — fix: add missing type field — onsen_deepslate.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_deepslate.json`
- **Revert command** (review diff first!): `git show 3ee6303479` then `git revert 3ee6303479` if confirmed safe

### `62334be6d3` — fix: add missing type field — onsen_calcite.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_calcite.json`
- **Revert command** (review diff first!): `git show 62334be6d3` then `git revert 62334be6d3` if confirmed safe

### `53e060811e` — fix: add missing type field — ocean_beach_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/ocean_beach_sand.json`
- **Revert command** (review diff first!): `git show 53e060811e` then `git revert 53e060811e` if confirmed safe

### `9d0cdc8b6b` — fix: add missing type field — ocean_beach_gravel_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/ocean_beach_gravel_2.json`
- **Revert command** (review diff first!): `git show 9d0cdc8b6b` then `git revert 9d0cdc8b6b` if confirmed safe

### `1f78d13a50` — fix: add missing type field — ocean_beach_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/ocean_beach_gravel.json`
- **Revert command** (review diff first!): `git show 1f78d13a50` then `git revert 1f78d13a50` if confirmed safe

### `1aab5fbcaf` — fix: add missing type field — mudify_rooted_dirt.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/mudify_rooted_dirt.json`
- **Revert command** (review diff first!): `git show 1aab5fbcaf` then `git revert 1aab5fbcaf` if confirmed safe

### `63eff349a9` — fix: add missing type field — mangrove_swamp_savanna_filler.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/mangrove_swamp_savanna_filler.json`
- **Revert command** (review diff first!): `git show 63eff349a9` then `git revert 63eff349a9` if confirmed safe

### `b146950055` — fix: add missing type field — estuary_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/estuary_mud.json`
- **Revert command** (review diff first!): `git show b146950055` then `git revert b146950055` if confirmed safe

### `2edd8c4944` — fix: add missing type field — dripstone_cliff.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/dripstone_cliff.json`
- **Revert command** (review diff first!): `git show 2edd8c4944` then `git revert 2edd8c4944` if confirmed safe

### `10ff8514d2` — fix: add missing type field — dover_cliffs.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/dover_cliffs.json`
- **Revert command** (review diff first!): `git show 10ff8514d2` then `git revert 10ff8514d2` if confirmed safe

### `ec86fd1407` — fix: add missing type field — disk_clay_dirt_only.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/disk_clay_dirt_only.json`
- **Revert command** (review diff first!): `git show ec86fd1407` then `git revert ec86fd1407` if confirmed safe

### `ceefd0884f` — fix: add missing type field — desert_swamp_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/desert_swamp_sand.json`
- **Revert command** (review diff first!): `git show ceefd0884f` then `git revert ceefd0884f` if confirmed safe

### `09334c9d10` — fix: add missing type field — desert_extender.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/desert_extender.json`
- **Revert command** (review diff first!): `git show 09334c9d10` then `git revert 09334c9d10` if confirmed safe

### `cce27b98ca` — fix: add missing type field — desert_edge.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/desert_edge.json`
- **Revert command** (review diff first!): `git show cce27b98ca` then `git revert cce27b98ca` if confirmed safe

### `e4793e52f1` — fix: add missing type field — dead_coral_stone_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/dead_coral_stone_2.json`
- **Revert command** (review diff first!): `git show e4793e52f1` then `git revert e4793e52f1` if confirmed safe

### `263cc9cd58` — fix: add missing type field — dead_coral_stone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/dead_coral_stone.json`
- **Revert command** (review diff first!): `git show 263cc9cd58` then `git revert 263cc9cd58` if confirmed safe

### `9a18a93e2d` — fix: add missing type field — coral_pools_edge.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coral_pools_edge.json`
- **Revert command** (review diff first!): `git show 9a18a93e2d` then `git revert 9a18a93e2d` if confirmed safe

### `ff2bc94641` — fix: add missing type field — coral_pools.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coral_pools.json`
- **Revert command** (review diff first!): `git show ff2bc94641` then `git revert ff2bc94641` if confirmed safe

### `52811e175f` — fix: add missing type field — cold_ocean_gravel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/cold_ocean_gravel.json`
- **Revert command** (review diff first!): `git show 52811e175f` then `git revert 52811e175f` if confirmed safe

### `e6715f2999` — fix: add missing type field — coastal_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coastal_sand.json`
- **Revert command** (review diff first!): `git show e6715f2999` then `git revert e6715f2999` if confirmed safe

### `ee959720bb` — fix: add missing type field — coastal_forest_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coastal_forest_sand.json`
- **Revert command** (review diff first!): `git show ee959720bb` then `git revert ee959720bb` if confirmed safe

### `23658d47be` — fix: add missing type field — base_taiga.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_taiga.json`
- **Revert command** (review diff first!): `git show 23658d47be` then `git revert 23658d47be` if confirmed safe

### `2c7bc04a2b` — fix: add missing type field — base_savanna.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_savanna.json`
- **Revert command** (review diff first!): `git show 2c7bc04a2b` then `git revert 2c7bc04a2b` if confirmed safe

### `d53a387a1f` — fix: add missing type field — base_mangrove_swamp_sudd.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_sudd.json`
- **Revert command** (review diff first!): `git show d53a387a1f` then `git revert d53a387a1f` if confirmed safe

### `dd42314dbf` — fix: add missing type field — base_mangrove_swamp_sparse_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_sparse_jungle.json`
- **Revert command** (review diff first!): `git show dd42314dbf` then `git revert dd42314dbf` if confirmed safe

### `f674f2e624` — fix: add missing type field — base_mangrove_swamp_savanna.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_savanna.json`
- **Revert command** (review diff first!): `git show f674f2e624` then `git revert f674f2e624` if confirmed safe

### `1a7ed2b0c1` — fix: add missing type field — base_mangrove_swamp_plains.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_plains.json`
- **Revert command** (review diff first!): `git show 1a7ed2b0c1` then `git revert 1a7ed2b0c1` if confirmed safe

### `f528a80e3a` — fix: add missing type field — base_mangrove_swamp_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_jungle.json`
- **Revert command** (review diff first!): `git show f528a80e3a` then `git revert f528a80e3a` if confirmed safe

### `dce684236f` — fix: add missing type field — base_mangrove_swamp_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_forest.json`
- **Revert command** (review diff first!): `git show dce684236f` then `git revert dce684236f` if confirmed safe

### `d450954288` — fix: add missing type field — base_mangrove_swamp_arid.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_arid.json`
- **Revert command** (review diff first!): `git show d450954288` then `git revert d450954288` if confirmed safe

### `b555f31dc6` — fix: add missing type field — base_frozen_peaks_snow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_frozen_peaks_snow.json`
- **Revert command** (review diff first!): `git show b555f31dc6` then `git revert b555f31dc6` if confirmed safe

### `c73424ec4c` — fix: add missing type field — base_frozen_peaks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_frozen_peaks.json`
- **Revert command** (review diff first!): `git show c73424ec4c` then `git revert c73424ec4c` if confirmed safe

### `01f7cb96de` — fix: add missing type field — badlands_stone_fix.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/badlands_stone_fix.json`
- **Revert command** (review diff first!): `git show 01f7cb96de` then `git revert 01f7cb96de` if confirmed safe

### `ff1a685094` — fix: add missing type field — badlands_muddy_canyon.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/badlands_muddy_canyon.json`
- **Revert command** (review diff first!): `git show ff1a685094` then `git revert ff1a685094` if confirmed safe

### `27bd5f7511` — fix: add missing type field — badlands_extender.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/badlands_extender.json`
- **Revert command** (review diff first!): `git show 27bd5f7511` then `git revert 27bd5f7511` if confirmed safe

### `94351d6afe` — fix: add missing type field — badlands_edge.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/badlands_edge.json`
- **Revert command** (review diff first!): `git show 94351d6afe` then `git revert 94351d6afe` if confirmed safe

### `50867da800` — fix: add missing type field — arroyo_red_sandify.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/arroyo_red_sandify.json`
- **Revert command** (review diff first!): `git show 50867da800` then `git revert 50867da800` if confirmed safe

### `965521f08a` — fix: add missing type field — arroyo_red_salt_pan_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/arroyo_red_salt_pan_2.json`
- **Revert command** (review diff first!): `git show 965521f08a` then `git revert 965521f08a` if confirmed safe

### `97e0435107` — fix: add missing type field — arroyo_red_salt_pan.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/arroyo_red_salt_pan.json`
- **Revert command** (review diff first!): `git show 97e0435107` then `git revert 97e0435107` if confirmed safe

### `dcd137a84a` — fix: add missing type field — arroyo_extender.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/arroyo_extender.json`
- **Revert command** (review diff first!): `git show dcd137a84a` then `git revert dcd137a84a` if confirmed safe

### `a53a69c6bd` — fix: add missing type field — river_water.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/carver/river_water.json`
- **Revert command** (review diff first!): `git show a53a69c6bd` then `git revert a53a69c6bd` if confirmed safe

### `1aaf77c4ef` — fix: add missing type field — river.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/carver/river.json`
- **Revert command** (review diff first!): `git show 1aaf77c4ef` then `git revert 1aaf77c4ef` if confirmed safe

### `4633c2370c` — fix: add missing type field — ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/carver/ocean.json`
- **Revert command** (review diff first!): `git show 4633c2370c` then `git revert 4633c2370c` if confirmed safe

### `cb88231005` — fix: add missing type field — sparse_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/sparse_jungle.json`
- **Revert command** (review diff first!): `git show cb88231005` then `git revert cb88231005` if confirmed safe

### `b187e73dac` — fix: add missing type field — rainforest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/rainforest.json`
- **Revert command** (review diff first!): `git show b187e73dac` then `git revert b187e73dac` if confirmed safe

### `d8f9c4ecc6` — fix: add missing type field — jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/jungle.json`
- **Revert command** (review diff first!): `git show d8f9c4ecc6` then `git revert d8f9c4ecc6` if confirmed safe

### `8c0027924c` — fix: add missing type field — harvest_fields_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_4.json`
- **Revert command** (review diff first!): `git show 8c0027924c` then `git revert 8c0027924c` if confirmed safe

### `b678d74070` — fix: add missing type field — harvest_fields_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_3.json`
- **Revert command** (review diff first!): `git show b678d74070` then `git revert b678d74070` if confirmed safe

### `dd75a26d8a` — fix: add missing type field — harvest_fields_2b.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_2b.json`
- **Revert command** (review diff first!): `git show dd75a26d8a` then `git revert dd75a26d8a` if confirmed safe

### `772c2b70af` — fix: add missing type field — harvest_fields_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_2.json`
- **Revert command** (review diff first!): `git show 772c2b70af` then `git revert 772c2b70af` if confirmed safe

### `0f66fc1894` — fix: add missing type field — harvest_fields_1b.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_1b.json`
- **Revert command** (review diff first!): `git show 0f66fc1894` then `git revert 0f66fc1894` if confirmed safe

### `6d847ea3b8` — fix: add missing type field — harvest_fields_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_1.json`
- **Revert command** (review diff first!): `git show 6d847ea3b8` then `git revert 6d847ea3b8` if confirmed safe

### `ad44553ef3` — fix: add missing type field — cherry_grove.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/cherry_grove.json`
- **Revert command** (review diff first!): `git show ad44553ef3` then `git revert ad44553ef3` if confirmed safe

### `990007643f` — fix: add missing type field — bamboo_jungle_old_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle_old_2.json`
- **Revert command** (review diff first!): `git show 990007643f` then `git revert 990007643f` if confirmed safe

### `2b857be379` — fix: add missing type field — bamboo_jungle_old_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle_old_1.json`
- **Revert command** (review diff first!): `git show 2b857be379` then `git revert 2b857be379` if confirmed safe

### `5a2ef8bead` — fix: add missing type field — bamboo_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle.json`
- **Revert command** (review diff first!): `git show 5a2ef8bead` then `git revert 5a2ef8bead` if confirmed safe

### `2182ecdd56` — fix: add missing type field — wooded_badlands.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/wooded_badlands.json`
- **Revert command** (review diff first!): `git show 2182ecdd56` then `git revert 2182ecdd56` if confirmed safe

### `7bed9fa766` — fix: add missing type field — warm_ocean_extender_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/warm_ocean_extender_3.json`
- **Revert command** (review diff first!): `git show 7bed9fa766` then `git revert 7bed9fa766` if confirmed safe

### `321c939ff8` — fix: add missing type field — warm_ocean_extender_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/warm_ocean_extender_2.json`
- **Revert command** (review diff first!): `git show 321c939ff8` then `git revert 321c939ff8` if confirmed safe

### `cfcde11cd7` — fix: add missing type field — warm_ocean_extender_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/warm_ocean_extender_1.json`
- **Revert command** (review diff first!): `git show cfcde11cd7` then `git revert cfcde11cd7` if confirmed safe

### `22c753cce6` — fix: add missing type field — warm_ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/warm_ocean.json`
- **Revert command** (review diff first!): `git show 22c753cce6` then `git revert 22c753cce6` if confirmed safe

### `596007d9d5` — fix: add missing type field — taiga.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/taiga.json`
- **Revert command** (review diff first!): `git show 596007d9d5` then `git revert 596007d9d5` if confirmed safe

### `d159544566` — fix: add missing type field — swamp.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/swamp.json`
- **Revert command** (review diff first!): `git show d159544566` then `git revert d159544566` if confirmed safe

### `50c9a9800b` — fix: add missing type field — sunflower_plains.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/sunflower_plains.json`
- **Revert command** (review diff first!): `git show 50c9a9800b` then `git revert 50c9a9800b` if confirmed safe

### `c5646809d6` — fix: add missing type field — stony_peaks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/stony_peaks.json`
- **Revert command** (review diff first!): `git show c5646809d6` then `git revert c5646809d6` if confirmed safe

### `3679cebd8f` — fix: add missing type field — sparse_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/sparse_jungle.json`
- **Revert command** (review diff first!): `git show 3679cebd8f` then `git revert 3679cebd8f` if confirmed safe

### `fc30fd7186` — fix: add missing type field — snowy_taiga.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/snowy_taiga.json`
- **Revert command** (review diff first!): `git show fc30fd7186` then `git revert fc30fd7186` if confirmed safe

### `5da40775c4` — fix: add missing type field — savanna.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/savanna.json`
- **Revert command** (review diff first!): `git show 5da40775c4` then `git revert 5da40775c4` if confirmed safe

### `7a38ed0d10` — fix: add missing type field — river_extended.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/river_extended.json`
- **Revert command** (review diff first!): `git show 7a38ed0d10` then `git revert 7a38ed0d10` if confirmed safe

### `0861fbe621` — fix: add missing type field — river.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/river.json`
- **Revert command** (review diff first!): `git show 0861fbe621` then `git revert 0861fbe621` if confirmed safe

### `f1ddc68fc6` — fix: add missing type field — plains.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/plains.json`
- **Revert command** (review diff first!): `git show f1ddc68fc6` then `git revert f1ddc68fc6` if confirmed safe

### `8f06efa9b2` — fix: add missing type field — mushroom_fields.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/mushroom_fields.json`
- **Revert command** (review diff first!): `git show 8f06efa9b2` then `git revert 8f06efa9b2` if confirmed safe

### `2f2e34413f` — fix: add missing type field — mangrove_swamp.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/mangrove_swamp.json`
- **Revert command** (review diff first!): `git show 2f2e34413f` then `git revert 2f2e34413f` if confirmed safe

### `49a9d4779f` — fix: add missing type field — lush_caves_deep.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/lush_caves_deep.json`
- **Revert command** (review diff first!): `git show 49a9d4779f` then `git revert 49a9d4779f` if confirmed safe

### `46c05ae379` — fix: add missing type field — lush_caves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/lush_caves.json`
- **Revert command** (review diff first!): `git show 46c05ae379` then `git revert 46c05ae379` if confirmed safe

### `ad2e6f9628` — fix: add missing type field — lukewarm_ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/lukewarm_ocean.json`
- **Revert command** (review diff first!): `git show ad2e6f9628` then `git revert ad2e6f9628` if confirmed safe

### `730f3016d9` — fix: add missing type field — jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/jungle.json`
- **Revert command** (review diff first!): `git show 730f3016d9` then `git revert 730f3016d9` if confirmed safe

### `2b6db6cb70` — fix: add missing type field — ice_spikes.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/ice_spikes.json`
- **Revert command** (review diff first!): `git show 2b6db6cb70` then `git revert 2b6db6cb70` if confirmed safe

### `9b6cbc797c` — fix: add missing type field — frozen_ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/frozen_ocean.json`
- **Revert command** (review diff first!): `git show 9b6cbc797c` then `git revert 9b6cbc797c` if confirmed safe

### `0c9de163fe` — fix: add missing type field — forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/forest.json`
- **Revert command** (review diff first!): `git show 0c9de163fe` then `git revert 0c9de163fe` if confirmed safe

### `34ae7faeac` — fix: add missing type field — flower_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/flower_forest.json`
- **Revert command** (review diff first!): `git show 34ae7faeac` then `git revert 34ae7faeac` if confirmed safe

### `e21c5ce485` — fix: add missing type field — dripstone_caves_deep.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/dripstone_caves_deep.json`
- **Revert command** (review diff first!): `git show e21c5ce485` then `git revert e21c5ce485` if confirmed safe

### `64501d00d1` — fix: add missing type field — dripstone_caves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/dripstone_caves.json`
- **Revert command** (review diff first!): `git show 64501d00d1` then `git revert 64501d00d1` if confirmed safe

### `dcc29a964b` — fix: add missing type field — desert.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/desert.json`
- **Revert command** (review diff first!): `git show dcc29a964b` then `git revert dcc29a964b` if confirmed safe

### `fbee1373b9` — fix: add missing type field — deep_frozen_ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/deep_frozen_ocean.json`
- **Revert command** (review diff first!): `git show fbee1373b9` then `git revert fbee1373b9` if confirmed safe

### `934ee01857` — fix: add missing type field — deep_dark_extended.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/deep_dark_extended.json`
- **Revert command** (review diff first!): `git show 934ee01857` then `git revert 934ee01857` if confirmed safe

### `3d57711193` — fix: add missing type field — deep_dark.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/deep_dark.json`
- **Revert command** (review diff first!): `git show 3d57711193` then `git revert 3d57711193` if confirmed safe

### `40df120618` — fix: add missing type field — deep_cold_ocean.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/deep_cold_ocean.json`
- **Revert command** (review diff first!): `git show 40df120618` then `git revert 40df120618` if confirmed safe

### `7b9747489d` — fix: add missing type field — dark_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/dark_forest.json`
- **Revert command** (review diff first!): `git show 7b9747489d` then `git revert 7b9747489d` if confirmed safe

### `c753e1334e` — fix: add missing type field — birch_forests.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/birch_forests.json`
- **Revert command** (review diff first!): `git show c753e1334e` then `git revert c753e1334e` if confirmed safe

### `a417a26e35` — fix: add missing type field — bedrock_sealer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/bedrock_sealer.json`
- **Revert command** (review diff first!): `git show a417a26e35` then `git revert a417a26e35` if confirmed safe

### `861d136109` — fix: add missing type field — beach.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/beach.json`
- **Revert command** (review diff first!): `git show 861d136109` then `git revert 861d136109` if confirmed safe

### `671ee94895` — fix: add missing type field — bamboo_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/bamboo_jungle.json`
- **Revert command** (review diff first!): `git show 671ee94895` then `git revert 671ee94895` if confirmed safe

### `5c37be4c72` — fix: add missing type field — badlands.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/placer/badlands.json`
- **Revert command** (review diff first!): `git show 5c37be4c72` then `git revert 5c37be4c72` if confirmed safe

### `08d5ceef06` — fix: add missing type field — coastal_palm_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 08d5ceef06` then `git revert 08d5ceef06` if confirmed safe

### `8953443d13` — fix: add missing type field — coastal_palm_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show 8953443d13` then `git revert 8953443d13` if confirmed safe

### `0e2a4a6b87` — fix: add missing type field — coastal_palm_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 0e2a4a6b87` then `git revert 0e2a4a6b87` if confirmed safe

### `f8412477d2` — fix: add missing type field — coastal_palm_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show f8412477d2` then `git revert f8412477d2` if confirmed safe

### `e6af4e2173` — fix: add missing type field — paddy_water_highlands.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/paddy_water_highlands.json`
- **Revert command** (review diff first!): `git show e6af4e2173` then `git revert e6af4e2173` if confirmed safe

### `7cc571c9bf` — fix: add missing type field — paddy_water.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/paddy_water.json`
- **Revert command** (review diff first!): `git show 7cc571c9bf` then `git revert 7cc571c9bf` if confirmed safe

### `844851ddee` — fix: add missing type field — harvest_fields_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/harvest_fields_3.json`
- **Revert command** (review diff first!): `git show 844851ddee` then `git revert 844851ddee` if confirmed safe

### `8a614663aa` — fix: add missing type field — harvest_fields_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/harvest_fields_2.json`
- **Revert command** (review diff first!): `git show 8a614663aa` then `git revert 8a614663aa` if confirmed safe

### `9ff2d1c4ee` — fix: add missing type field — harvest_fields_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/harvest_fields_1.json`
- **Revert command** (review diff first!): `git show 9ff2d1c4ee` then `git revert 9ff2d1c4ee` if confirmed safe

### `2c2af55882` — fix: add missing type field — young_mega_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json`
- **Revert command** (review diff first!): `git show 2c2af55882` then `git revert 2c2af55882` if confirmed safe

### `0b058e1555` — fix: add missing type field — young_kapok.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json`
- **Revert command** (review diff first!): `git show 0b058e1555` then `git revert 0b058e1555` if confirmed safe

### `f7ae26d377` — fix: add missing type field — young_brazilwood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json`
- **Revert command** (review diff first!): `git show f7ae26d377` then `git revert f7ae26d377` if confirmed safe

### `00c4a390f0` — fix: add missing type field — witch_tree.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/witch_tree.json`
- **Revert command** (review diff first!): `git show 00c4a390f0` then `git revert 00c4a390f0` if confirmed safe

### `e8da366efa` — fix: add missing type field — willow_large.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow_large.json`
- **Revert command** (review diff first!): `git show e8da366efa` then `git revert e8da366efa` if confirmed safe

### `4a2e33c523` — fix: add missing type field — willow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow.json`
- **Revert command** (review diff first!): `git show 4a2e33c523` then `git revert 4a2e33c523` if confirmed safe

### `df7c204433` — fix: add missing type field — wierwood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/wierwood.json`
- **Revert command** (review diff first!): `git show df7c204433` then `git revert df7c204433` if confirmed safe

### `0efe614d19` — fix: add missing type field — tundra_spruce.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_spruce.json`
- **Revert command** (review diff first!): `git show 0efe614d19` then `git revert 0efe614d19` if confirmed safe

### `f8f7c5bc7f` — fix: add missing type field — tundra_bush.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_bush.json`
- **Revert command** (review diff first!): `git show f8f7c5bc7f` then `git revert f8f7c5bc7f` if confirmed safe

### `ea1f5bb96b` — fix: add missing type field — teak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/teak.json`
- **Revert command** (review diff first!): `git show ea1f5bb96b` then `git revert ea1f5bb96b` if confirmed safe

### `f04be13121` — fix: add missing type field — swamp_gum.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json`
- **Revert command** (review diff first!): `git show f04be13121` then `git revert f04be13121` if confirmed safe

### `b370c8a191` — fix: add missing type field — swamp_forest_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json`
- **Revert command** (review diff first!): `git show b370c8a191` then `git revert b370c8a191` if confirmed safe

### `eeb6b5da4a` — fix: add missing type field — swamp_forest_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json`
- **Revert command** (review diff first!): `git show eeb6b5da4a` then `git revert eeb6b5da4a` if confirmed safe

### `df23b5bf40` — fix: add missing type field — straight_cocoa_palm.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/straight_cocoa_palm.json`
- **Revert command** (review diff first!): `git show df23b5bf40` then `git revert df23b5bf40` if confirmed safe

### `c200920503` — fix: add missing type field — stick_plant_small.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant_small.json`
- **Revert command** (review diff first!): `git show c200920503` then `git revert c200920503` if confirmed safe

### `1b04144e47` — fix: add missing type field — stick_plant.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant.json`
- **Revert command** (review diff first!): `git show 1b04144e47` then `git revert 1b04144e47` if confirmed safe

### `b81568c842` — fix: add missing type field — 2_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show b81568c842` then `git revert b81568c842` if confirmed safe

### `44862a3a95` — fix: add missing type field — 2_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 44862a3a95` then `git revert 44862a3a95` if confirmed safe

### `8759c301b8` — fix: add missing type field — 2_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show 8759c301b8` then `git revert 8759c301b8` if confirmed safe

### `578ecdd88a` — fix: add missing type field — 2_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 578ecdd88a` then `git revert 578ecdd88a` if confirmed safe

### `ff024f1819` — fix: add missing type field — 1_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show ff024f1819` then `git revert ff024f1819` if confirmed safe

### `59bef2acc8` — fix: add missing type field — 1_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 59bef2acc8` then `git revert 59bef2acc8` if confirmed safe

### `a757db34a7` — fix: add missing type field — 1_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show a757db34a7` then `git revert a757db34a7` if confirmed safe

### `853d5a1c53` — fix: add missing type field — 1_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 853d5a1c53` then `git revert 853d5a1c53` if confirmed safe

### `7f13db9c07` — fix: add missing type field — 8.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/8.json`
- **Revert command** (review diff first!): `git show 7f13db9c07` then `git revert 7f13db9c07` if confirmed safe

### `7915a626cb` — fix: add missing type field — 7.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/7.json`
- **Revert command** (review diff first!): `git show 7915a626cb` then `git revert 7915a626cb` if confirmed safe

### `a62d51c258` — fix: add missing type field — 6.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/6.json`
- **Revert command** (review diff first!): `git show a62d51c258` then `git revert a62d51c258` if confirmed safe

### `6acd8e69f9` — fix: add missing type field — 5.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/5.json`
- **Revert command** (review diff first!): `git show 6acd8e69f9` then `git revert 6acd8e69f9` if confirmed safe

### `4b6bdacb77` — fix: add missing type field — 4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/4.json`
- **Revert command** (review diff first!): `git show 4b6bdacb77` then `git revert 4b6bdacb77` if confirmed safe

### `16b554376a` — fix: add missing type field — 3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/3.json`
- **Revert command** (review diff first!): `git show 16b554376a` then `git revert 16b554376a` if confirmed safe

### `2aa4a0aa2a` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/2.json`
- **Revert command** (review diff first!): `git show 2aa4a0aa2a` then `git revert 2aa4a0aa2a` if confirmed safe

### `1d169f4c62` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/1.json`
- **Revert command** (review diff first!): `git show 1d169f4c62` then `git revert 1d169f4c62` if confirmed safe

### `ef679c4ea1` — fix: add missing type field — sparse_jungle_palm.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sparse_jungle_palm.json`
- **Revert command** (review diff first!): `git show ef679c4ea1` then `git revert ef679c4ea1` if confirmed safe

### `7924a4ad3f` — fix: add missing type field — scrub_spruce.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_spruce.json`
- **Revert command** (review diff first!): `git show 7924a4ad3f` then `git revert 7924a4ad3f` if confirmed safe

### `9388b77136` — fix: add missing type field — scrub_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_oak.json`
- **Revert command** (review diff first!): `git show 9388b77136` then `git revert 9388b77136` if confirmed safe

### `d2776de07e` — fix: add missing type field — scrub_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_jungle.json`
- **Revert command** (review diff first!): `git show d2776de07e` then `git revert d2776de07e` if confirmed safe

### `b79cdd25f3` — fix: add missing type field — scrub_flowering_azalea.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_flowering_azalea.json`
- **Revert command** (review diff first!): `git show b79cdd25f3` then `git revert b79cdd25f3` if confirmed safe

### `a32029c075` — fix: add missing type field — scrub_dark_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_dark_oak.json`
- **Revert command** (review diff first!): `git show a32029c075` then `git revert a32029c075` if confirmed safe

### `eb17e6b1d7` — fix: add missing type field — scrub_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_birch.json`
- **Revert command** (review diff first!): `git show eb17e6b1d7` then `git revert eb17e6b1d7` if confirmed safe

### `fc9fa3122e` — fix: add missing type field — scrub_azalea.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_azalea.json`
- **Revert command** (review diff first!): `git show fc9fa3122e` then `git revert fc9fa3122e` if confirmed safe

### `17f16e8b1c` — fix: add missing type field — scrub_acacia.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_acacia.json`
- **Revert command** (review diff first!): `git show 17f16e8b1c` then `git revert 17f16e8b1c` if confirmed safe

### `ebb4909124` — fix: add missing type field — sclerophylous_tall.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous_tall.json`
- **Revert command** (review diff first!): `git show ebb4909124` then `git revert ebb4909124` if confirmed safe

### `c11c3a98a9` — fix: add missing type field — sclerophylous_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous_birch.json`
- **Revert command** (review diff first!): `git show c11c3a98a9` then `git revert c11c3a98a9` if confirmed safe

### `be4086f590` — fix: add missing type field — sclerophylous.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous.json`
- **Revert command** (review diff first!): `git show be4086f590` then `git revert be4086f590` if confirmed safe

### `d4a981157a` — fix: add missing type field — savanna_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/savanna_oak.json`
- **Revert command** (review diff first!): `git show d4a981157a` then `git revert d4a981157a` if confirmed safe

### `960183b448` — fix: add missing type field — sandalwood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sandalwood.json`
- **Revert command** (review diff first!): `git show 960183b448` then `git revert 960183b448` if confirmed safe

### `ba4dec628a` — fix: add missing type field — rosewood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/rosewood.json`
- **Revert command** (review diff first!): `git show ba4dec628a` then `git revert ba4dec628a` if confirmed safe

### `6ae4ee9682` — fix: add missing type field — riverside_jungle_tree.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/riverside_jungle_tree.json`
- **Revert command** (review diff first!): `git show 6ae4ee9682` then `git revert 6ae4ee9682` if confirmed safe

### `f4dc7c13ff` — fix: add missing type field — red_ivorywood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/red_ivorywood.json`
- **Revert command** (review diff first!): `git show f4dc7c13ff` then `git revert f4dc7c13ff` if confirmed safe

### `a7b7e1e2fe` — fix: add missing type field — ponderosa_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_pine.json`
- **Revert command** (review diff first!): `git show a7b7e1e2fe` then `git revert a7b7e1e2fe` if confirmed safe

### `80c12d9c4c` — fix: add missing type field — ponderosa_blackjack.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_blackjack.json`
- **Revert command** (review diff first!): `git show 80c12d9c4c` then `git revert 80c12d9c4c` if confirmed safe

### `7c10574ede` — fix: add missing type field — ponderosa_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_2.json`
- **Revert command** (review diff first!): `git show 7c10574ede` then `git revert 7c10574ede` if confirmed safe

### `2c49ca90ee` — fix: add missing type field — ponderosa_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_1.json`
- **Revert command** (review diff first!): `git show 2c49ca90ee` then `git revert 2c49ca90ee` if confirmed safe

### `bed77d2711` — fix: add missing type field — pinyon_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pinyon_1.json`
- **Revert command** (review diff first!): `git show bed77d2711` then `git revert bed77d2711` if confirmed safe

### `e6ad9266aa` — fix: add missing type field — pink_lapacho.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pink_lapacho.json`
- **Revert command** (review diff first!): `git show e6ad9266aa` then `git revert e6ad9266aa` if confirmed safe

### `ea0c337c77` — fix: add missing type field — pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pine.json`
- **Revert command** (review diff first!): `git show ea0c337c77` then `git revert ea0c337c77` if confirmed safe

### `03a393b225` — fix: add missing type field — pandanus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show 03a393b225` then `git revert 03a393b225` if confirmed safe

### `d97ba9aa05` — fix: add missing type field — pale_shroom_forked.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom_forked.json`
- **Revert command** (review diff first!): `git show d97ba9aa05` then `git revert d97ba9aa05` if confirmed safe

### `fcd3123632` — fix: add missing type field — pale_shroom.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom.json`
- **Revert command** (review diff first!): `git show fcd3123632` then `git revert fcd3123632` if confirmed safe

### `534e238038` — fix: add missing type field — pale_dark_eucalyptus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_dark_eucalyptus.json`
- **Revert command** (review diff first!): `git show 534e238038` then `git revert 534e238038` if confirmed safe

### `c21bb2e496` — fix: add missing type field — pale_acacia_stump.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_acacia_stump.json`
- **Revert command** (review diff first!): `git show c21bb2e496` then `git revert c21bb2e496` if confirmed safe

### `93847dc2ea` — fix: add missing type field — olive.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/olive.json`
- **Revert command** (review diff first!): `git show 93847dc2ea` then `git revert 93847dc2ea` if confirmed safe

### `2754245ab3` — fix: add missing type field — old_willow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_willow.json`
- **Revert command** (review diff first!): `git show 2754245ab3` then `git revert 2754245ab3` if confirmed safe

### `65bb67d3eb` — fix: add missing type field — old_swamp_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json`
- **Revert command** (review diff first!): `git show 65bb67d3eb` then `git revert 65bb67d3eb` if confirmed safe

### `e27fb6e478` — fix: add missing type field — old_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_oak.json`
- **Revert command** (review diff first!): `git show e27fb6e478` then `git revert e27fb6e478` if confirmed safe

### `bf67d3b555` — fix: add missing type field — old_dark_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_dark_oak.json`
- **Revert command** (review diff first!): `git show bf67d3b555` then `git revert bf67d3b555` if confirmed safe

### `880d48bee2` — fix: add missing type field — oak_bush.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/oak_bush.json`
- **Revert command** (review diff first!): `git show 880d48bee2` then `git revert 880d48bee2` if confirmed safe

### `3b029b1d07` — fix: add missing type field — oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/oak.json`
- **Revert command** (review diff first!): `git show 3b029b1d07` then `git revert 3b029b1d07` if confirmed safe

### `d5f0ad0620` — fix: add missing type field — mpingo.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mpingo.json`
- **Revert command** (review diff first!): `git show d5f0ad0620` then `git revert d5f0ad0620` if confirmed safe

### `4d5d93b7fe` — fix: add missing type field — moss_tree.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/moss_tree.json`
- **Revert command** (review diff first!): `git show 4d5d93b7fe` then `git revert 4d5d93b7fe` if confirmed safe

### `4cdf20b729` — fix: add missing type field — montane_forest_spruce.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/montane_forest_spruce.json`
- **Revert command** (review diff first!): `git show 4cdf20b729` then `git revert 4cdf20b729` if confirmed safe

### `0b0dfaeec0` — fix: add missing type field — mega_jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 0b0dfaeec0` then `git revert 0b0dfaeec0` if confirmed safe

### `0300e90a9f` — fix: add missing type field — mediterranean_cypress.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mediterranean_cypress.json`
- **Revert command** (review diff first!): `git show 0300e90a9f` then `git revert 0300e90a9f` if confirmed safe

### `3b04145382` — fix: add missing type field — marula.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/marula.json`
- **Revert command** (review diff first!): `git show 3b04145382` then `git revert 3b04145382` if confirmed safe

### `79b78c17fa` — fix: add missing type field — maple_tall.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/maple_tall.json`
- **Revert command** (review diff first!): `git show 79b78c17fa` then `git revert 79b78c17fa` if confirmed safe

### `9709eeaf98` — fix: add missing type field — mahogany.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mahogany.json`
- **Revert command** (review diff first!): `git show 9709eeaf98` then `git revert 9709eeaf98` if confirmed safe

### `c138b7b31c` — fix: add missing type field — live_oak_dark_swamp.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json`
- **Revert command** (review diff first!): `git show c138b7b31c` then `git revert c138b7b31c` if confirmed safe

### `df42ddbf2d` — fix: add missing type field — live_oak_dark.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark.json`
- **Revert command** (review diff first!): `git show df42ddbf2d` then `git revert df42ddbf2d` if confirmed safe

### `663077d15d` — fix: add missing type field — live_oak_bright.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_bright.json`
- **Revert command** (review diff first!): `git show 663077d15d` then `git revert 663077d15d` if confirmed safe

### `446537393a` — fix: add missing type field — live_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak.json`
- **Revert command** (review diff first!): `git show 446537393a` then `git revert 446537393a` if confirmed safe

### `8e80d5c93c` — fix: add missing type field — 2_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show 8e80d5c93c` then `git revert 8e80d5c93c` if confirmed safe

### `b12f69a965` — fix: add missing type field — 2_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show b12f69a965` then `git revert b12f69a965` if confirmed safe

### `f0ec94d44a` — fix: add missing type field — 2_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show f0ec94d44a` then `git revert f0ec94d44a` if confirmed safe

### `3233783ff5` — fix: add missing type field — 2_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show 3233783ff5` then `git revert 3233783ff5` if confirmed safe

### `fe936cba66` — fix: add missing type field — 1_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show fe936cba66` then `git revert fe936cba66` if confirmed safe

### `3eee0b202c` — fix: add missing type field — 1_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 3eee0b202c` then `git revert 3eee0b202c` if confirmed safe

### `dfdfc0d95d` — fix: add missing type field — 1_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show dfdfc0d95d` then `git revert dfdfc0d95d` if confirmed safe

### `b484b725b8` — fix: add missing type field — 1_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show b484b725b8` then `git revert b484b725b8` if confirmed safe

### `649aa44bc5` — fix: add missing type field — 8.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/8.json`
- **Revert command** (review diff first!): `git show 649aa44bc5` then `git revert 649aa44bc5` if confirmed safe

### `66cbdc8772` — fix: add missing type field — 7.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/7.json`
- **Revert command** (review diff first!): `git show 66cbdc8772` then `git revert 66cbdc8772` if confirmed safe

### `82e88ef587` — fix: add missing type field — 6.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/6.json`
- **Revert command** (review diff first!): `git show 82e88ef587` then `git revert 82e88ef587` if confirmed safe

### `c12ae3d8e7` — fix: add missing type field — 5.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/5.json`
- **Revert command** (review diff first!): `git show c12ae3d8e7` then `git revert c12ae3d8e7` if confirmed safe

### `b18d4884db` — fix: add missing type field — 4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/4.json`
- **Revert command** (review diff first!): `git show b18d4884db` then `git revert b18d4884db` if confirmed safe

### `9e10e21175` — fix: add missing type field — 3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/3.json`
- **Revert command** (review diff first!): `git show 9e10e21175` then `git revert 9e10e21175` if confirmed safe

### `29a08ab551` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/2.json`
- **Revert command** (review diff first!): `git show 29a08ab551` then `git revert 29a08ab551` if confirmed safe

### `303d247c68` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/1.json`
- **Revert command** (review diff first!): `git show 303d247c68` then `git revert 303d247c68` if confirmed safe

### `a6bf8535c9` — fix: add missing type field — kapok.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show a6bf8535c9` then `git revert a6bf8535c9` if confirmed safe

### `d7eebf2274` — fix: add missing type field — jungle_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_pine.json`
- **Revert command** (review diff first!): `git show d7eebf2274` then `git revert d7eebf2274` if confirmed safe

### `34692e876c` — fix: add missing type field — jungle_palm.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_palm.json`
- **Revert command** (review diff first!): `git show 34692e876c` then `git revert 34692e876c` if confirmed safe

### `0414492ae6` — fix: add missing type field — jungle_mangrove.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show 0414492ae6` then `git revert 0414492ae6` if confirmed safe

### `8671fc47b5` — fix: add missing type field — dead.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/dead.json`
- **Revert command** (review diff first!): `git show 8671fc47b5` then `git revert 8671fc47b5` if confirmed safe

### `6f191d04ec` — fix: add missing type field — leaves_2_z.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show 6f191d04ec` then `git revert 6f191d04ec` if confirmed safe

### `0edefb4e9e` — fix: add missing type field — leaves_2_x.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show 0edefb4e9e` then `git revert 0edefb4e9e` if confirmed safe

### `b581a03963` — fix: add missing type field — leaves_1_z.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show b581a03963` then `git revert b581a03963` if confirmed safe

### `beff4dc7fa` — fix: add missing type field — leaves_1_x.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show beff4dc7fa` then `git revert beff4dc7fa` if confirmed safe

### `1c4729f7c1` — fix: add missing type field — 9.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 1c4729f7c1` then `git revert 1c4729f7c1` if confirmed safe

### `8cad3c1dc7` — fix: add missing type field — 8.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show 8cad3c1dc7` then `git revert 8cad3c1dc7` if confirmed safe

### `824e37d62f` — fix: add missing type field — 7.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show 824e37d62f` then `git revert 824e37d62f` if confirmed safe

### `1e380d9ce5` — fix: add missing type field — 6.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show 1e380d9ce5` then `git revert 1e380d9ce5` if confirmed safe

### `c383ac8188` — fix: add missing type field — 10.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show c383ac8188` then `git revert c383ac8188` if confirmed safe

### `954de15288` — fix: add missing type field — dead.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/dead.json`
- **Revert command** (review diff first!): `git show 954de15288` then `git revert 954de15288` if confirmed safe

### `9039a5973f` — fix: add missing type field — leaves_2_z.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show 9039a5973f` then `git revert 9039a5973f` if confirmed safe

### `2c89dc88da` — fix: add missing type field — leaves_2_x.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show 2c89dc88da` then `git revert 2c89dc88da` if confirmed safe

### `eccf012b57` — fix: add missing type field — leaves_1_z.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show eccf012b57` then `git revert eccf012b57` if confirmed safe

### `0c40e90575` — fix: add missing type field — leaves_1_x.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 0c40e90575` then `git revert 0c40e90575` if confirmed safe

### `db66ee7f81` — fix: add missing type field — 5.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show db66ee7f81` then `git revert db66ee7f81` if confirmed safe

### `2dccf97d65` — fix: add missing type field — 4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show 2dccf97d65` then `git revert 2dccf97d65` if confirmed safe

### `807c6b108d` — fix: add missing type field — 3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show 807c6b108d` then `git revert 807c6b108d` if confirmed safe

### `975ce0b34c` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show 975ce0b34c` then `git revert 975ce0b34c` if confirmed safe

### `cef6f6d04a` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show cef6f6d04a` then `git revert cef6f6d04a` if confirmed safe

### `4468fd1d1f` — fix: add missing type field — branch_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show 4468fd1d1f` then `git revert 4468fd1d1f` if confirmed safe

### `5de2f47c27` — fix: add missing type field — branch_sw.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_sw.json`
- **Revert command** (review diff first!): `git show 5de2f47c27` then `git revert 5de2f47c27` if confirmed safe

### `841b4f8dc8` — fix: add missing type field — branch_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show 841b4f8dc8` then `git revert 841b4f8dc8` if confirmed safe

### `2898b2335c` — fix: add missing type field — branch_se.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_se.json`
- **Revert command** (review diff first!): `git show 2898b2335c` then `git revert 2898b2335c` if confirmed safe

### `5dbd427aee` — fix: add missing type field — branch_nw.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_nw.json`
- **Revert command** (review diff first!): `git show 5dbd427aee` then `git revert 5dbd427aee` if confirmed safe

### `55940e95a9` — fix: add missing type field — branch_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 55940e95a9` then `git revert 55940e95a9` if confirmed safe

### `3b8018e89c` — fix: add missing type field — branch_ne.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_ne.json`
- **Revert command** (review diff first!): `git show 3b8018e89c` then `git revert 3b8018e89c` if confirmed safe

### `69cb00b1bf` — fix: add missing type field — branch_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show 69cb00b1bf` then `git revert 69cb00b1bf` if confirmed safe

### `c19f68a04d` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show c19f68a04d` then `git revert c19f68a04d` if confirmed safe

### `87cf0f5a1a` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show 87cf0f5a1a` then `git revert 87cf0f5a1a` if confirmed safe

### `3caed525e5` — fix: add missing type field — huangshan_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huangshan_pine.json`
- **Revert command** (review diff first!): `git show 3caed525e5` then `git revert 3caed525e5` if confirmed safe

### `65ab81bf7d` — fix: add missing type field — holly.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/holly.json`
- **Revert command** (review diff first!): `git show 65ab81bf7d` then `git revert 65ab81bf7d` if confirmed safe

### `cb6a5372e6` — fix: add missing type field — ground_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ground_pine.json`
- **Revert command** (review diff first!): `git show cb6a5372e6` then `git revert cb6a5372e6` if confirmed safe

### `c6c2067ea3` — fix: add missing type field — glow_banyan.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/glow_banyan.json`
- **Revert command** (review diff first!): `git show c6c2067ea3` then `git revert c6c2067ea3` if confirmed safe

### `48e2cb5257` — fix: add missing type field — giant_magnolia.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/giant_magnolia.json`
- **Revert command** (review diff first!): `git show 48e2cb5257` then `git revert 48e2cb5257` if confirmed safe

### `d6fd4d2521` — fix: add missing type field — forest_tropical_pine_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_4.json`
- **Revert command** (review diff first!): `git show d6fd4d2521` then `git revert d6fd4d2521` if confirmed safe

### `14fba56a33` — fix: add missing type field — forest_tropical_pine_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_3.json`
- **Revert command** (review diff first!): `git show 14fba56a33` then `git revert 14fba56a33` if confirmed safe

### `db63b20d5b` — fix: add missing type field — forest_tropical_pine_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_2.json`
- **Revert command** (review diff first!): `git show db63b20d5b` then `git revert db63b20d5b` if confirmed safe

### `99786cc451` — fix: add missing type field — forest_tropical_pine_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_1.json`
- **Revert command** (review diff first!): `git show 99786cc451` then `git revert 99786cc451` if confirmed safe

### `35d198d861` — fix: add missing type field — forest_tropical_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine.json`
- **Revert command** (review diff first!): `git show 35d198d861` then `git revert 35d198d861` if confirmed safe

### `b35a7ffadf` — fix: add missing type field — forest_pine_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_4.json`
- **Revert command** (review diff first!): `git show b35a7ffadf` then `git revert b35a7ffadf` if confirmed safe

### `e8b6841cbb` — fix: add missing type field — forest_pine_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_3.json`
- **Revert command** (review diff first!): `git show e8b6841cbb` then `git revert e8b6841cbb` if confirmed safe

### `f779a39495` — fix: add missing type field — forest_pine_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_2.json`
- **Revert command** (review diff first!): `git show f779a39495` then `git revert f779a39495` if confirmed safe

### `905213fc0b` — fix: add missing type field — forest_pine_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_1.json`
- **Revert command** (review diff first!): `git show 905213fc0b` then `git revert 905213fc0b` if confirmed safe

### `7b39e3aa77` — fix: add missing type field — forest_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine.json`
- **Revert command** (review diff first!): `git show 7b39e3aa77` then `git revert 7b39e3aa77` if confirmed safe

### `d1b8500606` — fix: add missing type field — forest_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_oak.json`
- **Revert command** (review diff first!): `git show d1b8500606` then `git revert d1b8500606` if confirmed safe

### `59b4142a02` — fix: add missing type field — forest_eucalyptus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_eucalyptus.json`
- **Revert command** (review diff first!): `git show 59b4142a02` then `git revert 59b4142a02` if confirmed safe

### `254c718306` — fix: add missing type field — forest_eucalypt_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_eucalypt_birch.json`
- **Revert command** (review diff first!): `git show 254c718306` then `git revert 254c718306` if confirmed safe

### `81b3188220` — fix: add missing type field — forest_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_birch.json`
- **Revert command** (review diff first!): `git show 81b3188220` then `git revert 81b3188220` if confirmed safe

### `38ed5aa2e7` — fix: add missing type field — forest_azalea.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_azalea.json`
- **Revert command** (review diff first!): `git show 38ed5aa2e7` then `git revert 38ed5aa2e7` if confirmed safe

### `a77e96379b` — fix: add missing type field — flowering_cassia.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_cassia.json`
- **Revert command** (review diff first!): `git show a77e96379b` then `git revert a77e96379b` if confirmed safe

### `bed900dc5b` — fix: add missing type field — flowering_azalea_bush.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_azalea_bush.json`
- **Revert command** (review diff first!): `git show bed900dc5b` then `git revert bed900dc5b` if confirmed safe

### `98a7d2d8dd` — fix: add missing type field — fir_medium.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fir_medium.json`
- **Revert command** (review diff first!): `git show 98a7d2d8dd` then `git revert 98a7d2d8dd` if confirmed safe

### `34698a0528` — fix: add missing type field — fen_pine.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fen_pine.json`
- **Revert command** (review diff first!): `git show 34698a0528` then `git revert 34698a0528` if confirmed safe

### `9f65523361` — fix: add missing type field — eucalyptus_salubris.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_salubris.json`
- **Revert command** (review diff first!): `git show 9f65523361` then `git revert 9f65523361` if confirmed safe

### `c2e2cc12b1` — fix: add missing type field — eucalyptus_deanei_white.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json`
- **Revert command** (review diff first!): `git show c2e2cc12b1` then `git revert c2e2cc12b1` if confirmed safe

### `7cc20d61d9` — fix: add missing type field — eucalyptus_deanei_gray.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_gray.json`
- **Revert command** (review diff first!): `git show 7cc20d61d9` then `git revert 7cc20d61d9` if confirmed safe

### `07fbc1f1ab` — fix: add missing type field — elephant_bamboo_tropical_gold.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show 07fbc1f1ab` then `git revert 07fbc1f1ab` if confirmed safe

### `0b6d311ab2` — fix: add missing type field — elephant_bamboo_tropical.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 0b6d311ab2` then `git revert 0b6d311ab2` if confirmed safe

### `89de6b2daf` — fix: add missing type field — elephant_bamboo_temperate_gold.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show 89de6b2daf` then `git revert 89de6b2daf` if confirmed safe

### `cda5949d74` — fix: add missing type field — elephant_bamboo_temperate.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show cda5949d74` then `git revert cda5949d74` if confirmed safe

### `201c89c05c` — fix: add missing type field — elephant_bamboo_medium.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_medium.json`
- **Revert command** (review diff first!): `git show 201c89c05c` then `git revert 201c89c05c` if confirmed safe

### `afb92503f0` — fix: add missing type field — elephant_bamboo_dependent.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_dependent.json`
- **Revert command** (review diff first!): `git show afb92503f0` then `git revert afb92503f0` if confirmed safe

### `e37f5a64d6` — fix: add missing type field — elephant_bamboo_dark.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_dark.json`
- **Revert command** (review diff first!): `git show e37f5a64d6` then `git revert e37f5a64d6` if confirmed safe

### `53783a6023` — fix: add missing type field — elephant_bamboo_bright.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_bright.json`
- **Revert command** (review diff first!): `git show 53783a6023` then `git revert 53783a6023` if confirmed safe

### `862a6076df` — fix: add missing type field — ebony.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ebony.json`
- **Revert command** (review diff first!): `git show 862a6076df` then `git revert 862a6076df` if confirmed safe

### `0b414faf50` — fix: add missing type field — desert_fan_palm_tall.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_tall.json`
- **Revert command** (review diff first!): `git show 0b414faf50` then `git revert 0b414faf50` if confirmed safe

### `a5a615ac00` — fix: add missing type field — desert_fan_palm_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_2.json`
- **Revert command** (review diff first!): `git show a5a615ac00` then `git revert a5a615ac00` if confirmed safe

### `cef6916acf` — fix: add missing type field — desert_fan_palm.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm.json`
- **Revert command** (review diff first!): `git show cef6916acf` then `git revert cef6916acf` if confirmed safe

### `0a5ce711fe` — fix: add missing type field — 2_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 0a5ce711fe` then `git revert 0a5ce711fe` if confirmed safe

### `104c00e60f` — fix: add missing type field — 2_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 104c00e60f` then `git revert 104c00e60f` if confirmed safe

### `a5bea24793` — fix: add missing type field — 2_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show a5bea24793` then `git revert a5bea24793` if confirmed safe

### `173d492c89` — fix: add missing type field — 2_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 173d492c89` then `git revert 173d492c89` if confirmed safe

### `8b7bcba563` — fix: add missing type field — 1_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 8b7bcba563` then `git revert 8b7bcba563` if confirmed safe

### `7a1170336b` — fix: add missing type field — 1_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 7a1170336b` then `git revert 7a1170336b` if confirmed safe

### `168c2c6a2e` — fix: add missing type field — 1_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 168c2c6a2e` then `git revert 168c2c6a2e` if confirmed safe

### `1dfe54df6c` — fix: add missing type field — 1_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 1dfe54df6c` then `git revert 1dfe54df6c` if confirmed safe

### `d0b5dc226b` — fix: add missing type field — 5.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/5.json`
- **Revert command** (review diff first!): `git show d0b5dc226b` then `git revert d0b5dc226b` if confirmed safe

### `80fc033e00` — fix: add missing type field — 4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/4.json`
- **Revert command** (review diff first!): `git show 80fc033e00` then `git revert 80fc033e00` if confirmed safe

### `b97dd38c95` — fix: add missing type field — 3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/3.json`
- **Revert command** (review diff first!): `git show b97dd38c95` then `git revert b97dd38c95` if confirmed safe

### `cb62b69366` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/2.json`
- **Revert command** (review diff first!): `git show cb62b69366` then `git revert cb62b69366` if confirmed safe

### `29e7a3ef65` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/1.json`
- **Revert command** (review diff first!): `git show 29e7a3ef65` then `git revert 29e7a3ef65` if confirmed safe

### `d39d6ec4f0` — fix: add missing type field — dark_eucalyptus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dark_eucalyptus.json`
- **Revert command** (review diff first!): `git show d39d6ec4f0` then `git revert d39d6ec4f0` if confirmed safe

### `a2064f7981` — fix: add missing type field — dark_banyan.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dark_banyan.json`
- **Revert command** (review diff first!): `git show a2064f7981` then `git revert a2064f7981` if confirmed safe

### `79be240ae2` — fix: add missing type field — corymbia_aparrerinja.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/corymbia_aparrerinja.json`
- **Revert command** (review diff first!): `git show 79be240ae2` then `git revert 79be240ae2` if confirmed safe

### `ba635a70f4` — fix: add missing type field — complex_oak_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show ba635a70f4` then `git revert ba635a70f4` if confirmed safe

### `4e1d6d7715` — fix: add missing type field — complex_oak_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show 4e1d6d7715` then `git revert 4e1d6d7715` if confirmed safe

### `05e4c197fd` — fix: add missing type field — complex_dark_oak_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show 05e4c197fd` then `git revert 05e4c197fd` if confirmed safe

### `415c9ffc05` — fix: add missing type field — complex_dark_oak_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 415c9ffc05` then `git revert 415c9ffc05` if confirmed safe

### `e4d6ba9710` — fix: add missing type field — cold_pine_medium.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cold_pine_medium.json`
- **Revert command** (review diff first!): `git show e4d6ba9710` then `git revert e4d6ba9710` if confirmed safe

### `58c6d284e7` — fix: add missing type field — coastal_palm_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 58c6d284e7` then `git revert 58c6d284e7` if confirmed safe

### `c12ec96bb8` — fix: add missing type field — coastal_palm_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show c12ec96bb8` then `git revert c12ec96bb8` if confirmed safe

### `9662e461bd` — fix: add missing type field — coastal_palm_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 9662e461bd` then `git revert 9662e461bd` if confirmed safe

### `3feb2a6ea1` — fix: add missing type field — coastal_palm_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 3feb2a6ea1` then `git revert 3feb2a6ea1` if confirmed safe

### `d4dfc4b156` — fix: add missing type field — cloud_forest_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_4.json`
- **Revert command** (review diff first!): `git show d4dfc4b156` then `git revert d4dfc4b156` if confirmed safe

### `aba513a799` — fix: add missing type field — cloud_forest_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_3.json`
- **Revert command** (review diff first!): `git show aba513a799` then `git revert aba513a799` if confirmed safe

### `fdeed88862` — fix: add missing type field — cloud_forest_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_2.json`
- **Revert command** (review diff first!): `git show fdeed88862` then `git revert fdeed88862` if confirmed safe

### `eb8818e9e2` — fix: add missing type field — cloud_forest_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cloud_forest_1.json`
- **Revert command** (review diff first!): `git show eb8818e9e2` then `git revert eb8818e9e2` if confirmed safe

### `74b1a45146` — fix: add missing type field — brazilwood.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json`
- **Revert command** (review diff first!): `git show 74b1a45146` then `git revert 74b1a45146` if confirmed safe

### `3da820bee8` — fix: add missing type field — birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/birch.json`
- **Revert command** (review diff first!): `git show 3da820bee8` then `git revert 3da820bee8` if confirmed safe

### `55ca6b1092` — fix: add missing type field — 3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show 55ca6b1092` then `git revert 55ca6b1092` if confirmed safe

### `ff99a4825f` — fix: add missing type field — 2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show ff99a4825f` then `git revert ff99a4825f` if confirmed safe

### `c6e3832b36` — fix: add missing type field — 1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show c6e3832b36` then `git revert c6e3832b36` if confirmed safe

### `68e6959157` — fix: add missing type field — bent_palm_west.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_west.json`
- **Revert command** (review diff first!): `git show 68e6959157` then `git revert 68e6959157` if confirmed safe

### `251f570aab` — fix: add missing type field — bent_palm_south.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_south.json`
- **Revert command** (review diff first!): `git show 251f570aab` then `git revert 251f570aab` if confirmed safe

### `bf7b880bfa` — fix: add missing type field — bent_palm_north.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_north.json`
- **Revert command** (review diff first!): `git show bf7b880bfa` then `git revert bf7b880bfa` if confirmed safe

### `43333f593d` — fix: add missing type field — bent_palm_east.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_east.json`
- **Revert command** (review diff first!): `git show 43333f593d` then `git revert 43333f593d` if confirmed safe

### `cd6beebb19` — fix: add missing type field — bayou_cypress_surface_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json`
- **Revert command** (review diff first!): `git show cd6beebb19` then `git revert cd6beebb19` if confirmed safe

### `6def838bcb` — fix: add missing type field — bayou_cypress_surface.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json`
- **Revert command** (review diff first!): `git show 6def838bcb` then `git revert 6def838bcb` if confirmed safe

### `23f6104976` — fix: add missing type field — bayou_cypress_shallow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json`
- **Revert command** (review diff first!): `git show 23f6104976` then `git revert 23f6104976` if confirmed safe

### `209651e719` — fix: add missing type field — bayou_cypress_middle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
- **Revert command** (review diff first!): `git show 209651e719` then `git revert 209651e719` if confirmed safe

### `ca56d69920` — fix: add missing type field — bayou_cypress_deep.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
- **Revert command** (review diff first!): `git show ca56d69920` then `git revert ca56d69920` if confirmed safe

### `2e0c3097f5` — fix: add missing type field — bayou_cypress_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_4.json`
- **Revert command** (review diff first!): `git show 2e0c3097f5` then `git revert 2e0c3097f5` if confirmed safe

### `b5d71aad02` — fix: add missing type field — bayou_cypress_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_3.json`
- **Revert command** (review diff first!): `git show b5d71aad02` then `git revert b5d71aad02` if confirmed safe

### `6ef7a7b7c1` — fix: add missing type field — bayou_cypress_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_2.json`
- **Revert command** (review diff first!): `git show 6ef7a7b7c1` then `git revert 6ef7a7b7c1` if confirmed safe

### `6b271305ef` — fix: add missing type field — bayou_cypress_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_1.json`
- **Revert command** (review diff first!): `git show 6b271305ef` then `git revert 6b271305ef` if confirmed safe

### `abbae3813d` — fix: add missing type field — bayou_cypress.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress.json`
- **Revert command** (review diff first!): `git show abbae3813d` then `git revert abbae3813d` if confirmed safe

### `c401c234a2` — fix: add missing type field — baobab_small.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_small.json`
- **Revert command** (review diff first!): `git show c401c234a2` then `git revert c401c234a2` if confirmed safe

### `9500005bcd` — fix: add missing type field — baobab_short.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_short.json`
- **Revert command** (review diff first!): `git show 9500005bcd` then `git revert 9500005bcd` if confirmed safe

### `ce2f628a63` — fix: add missing type field — baobab.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab.json`
- **Revert command** (review diff first!): `git show ce2f628a63` then `git revert ce2f628a63` if confirmed safe

### `3eb41277d5` — fix: add missing type field — banyan.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/banyan.json`
- **Revert command** (review diff first!): `git show 3eb41277d5` then `git revert 3eb41277d5` if confirmed safe

### `b60c338b08` — fix: add missing type field — bamboo_palm.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bamboo_palm.json`
- **Revert command** (review diff first!): `git show b60c338b08` then `git revert b60c338b08` if confirmed safe

### `84585055a6` — fix: add missing type field — azalea_conifer.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_conifer.json`
- **Revert command** (review diff first!): `git show 84585055a6` then `git revert 84585055a6` if confirmed safe

### `213cfa4f02` — fix: add missing type field — azalea_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_birch.json`
- **Revert command** (review diff first!): `git show 213cfa4f02` then `git revert 213cfa4f02` if confirmed safe

### `c487dc5429` — fix: add missing type field — aspen_leaf_litter.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen_leaf_litter.json`
- **Revert command** (review diff first!): `git show c487dc5429` then `git revert c487dc5429` if confirmed safe

### `30bcaeca59` — fix: add missing type field — aspen.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen.json`
- **Revert command** (review diff first!): `git show 30bcaeca59` then `git revert 30bcaeca59` if confirmed safe

### `2a15a81ead` — fix: add missing type field — ancient_swamp_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
- **Revert command** (review diff first!): `git show 2a15a81ead` then `git revert 2a15a81ead` if confirmed safe

### `f2b01b9e38` — fix: add missing type field — ancient_pale_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_pale_oak.json`
- **Revert command** (review diff first!): `git show f2b01b9e38` then `git revert f2b01b9e38` if confirmed safe

### `a0a1bdd2e3` — fix: add missing type field — ancient_oak_old.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_oak_old.json`
- **Revert command** (review diff first!): `git show a0a1bdd2e3` then `git revert a0a1bdd2e3` if confirmed safe

### `15768a47d2` — fix: add missing type field — ancient_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_oak.json`
- **Revert command** (review diff first!): `git show 15768a47d2` then `git revert 15768a47d2` if confirmed safe

### `8a405508a5` — fix: add missing type field — ancient_dead_pale_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dead_pale_oak.json`
- **Revert command** (review diff first!): `git show 8a405508a5` then `git revert 8a405508a5` if confirmed safe

### `d4e942875d` — fix: add missing type field — ancient_dark_oak_old.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak_old.json`
- **Revert command** (review diff first!): `git show d4e942875d` then `git revert d4e942875d` if confirmed safe

### `bc96c11dd4` — fix: add missing type field — ancient_dark_oak.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak.json`
- **Revert command** (review diff first!): `git show bc96c11dd4` then `git revert bc96c11dd4` if confirmed safe

### `46ce5c03d4` — fix: add missing type field — ancient_birch_old.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_birch_old.json`
- **Revert command** (review diff first!): `git show 46ce5c03d4` then `git revert 46ce5c03d4` if confirmed safe

### `f1e564a2e3` — fix: add missing type field — ancient_birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_birch.json`
- **Revert command** (review diff first!): `git show f1e564a2e3` then `git revert f1e564a2e3` if confirmed safe

### `06a200a0a5` — fix: add missing type field — ancient_azalea_old.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_azalea_old.json`
- **Revert command** (review diff first!): `git show 06a200a0a5` then `git revert 06a200a0a5` if confirmed safe

### `4468b14045` — fix: add missing type field — ancient_azalea.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_azalea.json`
- **Revert command** (review diff first!): `git show 4468b14045` then `git revert 4468b14045` if confirmed safe

### `89317aa58e` — fix: add missing type field — acacia_plains.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/acacia_plains.json`
- **Revert command** (review diff first!): `git show 89317aa58e` then `git revert 89317aa58e` if confirmed safe

### `cc4d65f966` — fix: add missing type field — acacia_forest.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/acacia_forest.json`
- **Revert command** (review diff first!): `git show cc4d65f966` then `git revert cc4d65f966` if confirmed safe

### `ca03fca920` — fix: add missing type field — oasis_pool.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/oasis_pool.json`
- **Revert command** (review diff first!): `git show ca03fca920` then `git revert ca03fca920` if confirmed safe

### `06ca6c7df1` — fix: add missing type field — groundsel_leaves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/groundsel_leaves.json`
- **Revert command** (review diff first!): `git show 06ca6c7df1` then `git revert 06ca6c7df1` if confirmed safe

### `508de36997` — fix: add missing type field — patch_enoki.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
- **Revert command** (review diff first!): `git show 508de36997` then `git revert 508de36997` if confirmed safe

### `9d6c7f8409` — fix: add missing type field — medium_muscaria.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/medium_muscaria.json`
- **Revert command** (review diff first!): `git show 9d6c7f8409` then `git revert 9d6c7f8409` if confirmed safe

### `f8cf6dc954` — fix: add missing type field — giant_omphalotus_illudens.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json`
- **Revert command** (review diff first!): `git show f8cf6dc954` then `git revert f8cf6dc954` if confirmed safe

### `a8926632c4` — fix: add missing type field — giant_muscaria.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_muscaria.json`
- **Revert command** (review diff first!): `git show a8926632c4` then `git revert a8926632c4` if confirmed safe

### `523ec3ee3f` — fix: add missing type field — giant_morel.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_morel.json`
- **Revert command** (review diff first!): `git show 523ec3ee3f` then `git revert 523ec3ee3f` if confirmed safe

### `a3b8fcd4e4` — fix: add missing type field — giant_matsutake.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show a3b8fcd4e4` then `git revert a3b8fcd4e4` if confirmed safe

### `2acbf1d151` — fix: add missing type field — giant_enoki.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 2acbf1d151` then `git revert 2acbf1d151` if confirmed safe

### `998448ea3c` — fix: add missing type field — fungal_forest_red.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_red.json`
- **Revert command** (review diff first!): `git show 998448ea3c` then `git revert 998448ea3c` if confirmed safe

### `d475c3d65c` — fix: add missing type field — fungal_forest_orange.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json`
- **Revert command** (review diff first!): `git show d475c3d65c` then `git revert d475c3d65c` if confirmed safe

### `2d9cab4447` — fix: add missing type field — fungal_forest_gray.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_gray.json`
- **Revert command** (review diff first!): `git show 2d9cab4447` then `git revert 2d9cab4447` if confirmed safe

### `2e526e6333` — fix: add missing type field — fungal_forest_brown.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_brown.json`
- **Revert command** (review diff first!): `git show 2e526e6333` then `git revert 2e526e6333` if confirmed safe

### `4a8e75effc` — fix: add missing type field — colossal_mushroom_32.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_32.json`
- **Revert command** (review diff first!): `git show 4a8e75effc` then `git revert 4a8e75effc` if confirmed safe

### `935ea57f2a` — fix: add missing type field — colossal_mushroom_30.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_30.json`
- **Revert command** (review diff first!): `git show 935ea57f2a` then `git revert 935ea57f2a` if confirmed safe

### `79b33f7bf3` — fix: add missing type field — colossal_mushroom_28.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_28.json`
- **Revert command** (review diff first!): `git show 79b33f7bf3` then `git revert 79b33f7bf3` if confirmed safe

### `7ac52538a7` — fix: add missing type field — colossal_mushroom_26.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_26.json`
- **Revert command** (review diff first!): `git show 7ac52538a7` then `git revert 7ac52538a7` if confirmed safe

### `ce52ebc117` — fix: add missing type field — colossal_mushroom_24.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/colossal_mushroom_24.json`
- **Revert command** (review diff first!): `git show ce52ebc117` then `git revert ce52ebc117` if confirmed safe

### `2d7493afa3` — fix: add missing type field — bracket_fungus.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show 2d7493afa3` then `git revert 2d7493afa3` if confirmed safe

### `84444982e8` — fix: add missing type field — pale.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/pale.json`
- **Revert command** (review diff first!): `git show 84444982e8` then `git revert 84444982e8` if confirmed safe

### `d1c33c8205` — fix: add missing type field — jungle.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/jungle.json`
- **Revert command** (review diff first!): `git show d1c33c8205` then `git revert d1c33c8205` if confirmed safe

### `80c9687d08` — fix: add missing type field — desert.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/desert.json`
- **Revert command** (review diff first!): `git show 80c9687d08` then `git revert 80c9687d08` if confirmed safe

### `ed2f9dd68e` — fix: add missing type field — birch.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/birch.json`
- **Revert command** (review diff first!): `git show ed2f9dd68e` then `git revert ed2f9dd68e` if confirmed safe

### `66d52e512b` — fix: add missing type field — acacia.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/acacia.json`
- **Revert command** (review diff first!): `git show 66d52e512b` then `git revert 66d52e512b` if confirmed safe

### `51be395089` — fix: add missing type field — terracotta_mound_yellow.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show 51be395089` then `git revert 51be395089` if confirmed safe

### `9794322752` — fix: add missing type field — terracotta_mound_red.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show 9794322752` then `git revert 9794322752` if confirmed safe

### `d00caddfdb` — fix: add missing type field — terracotta_mound_orange.json

- **Removed debunked keys**: can_grow_through
- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json`
- **Revert command** (review diff first!): `git show d00caddfdb` then `git revert d00caddfdb` if confirmed safe

### `34a6db5253` — fix: add missing type field — warm_island.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/warm_island.json`
- **Revert command** (review diff first!): `git show 34a6db5253` then `git revert 34a6db5253` if confirmed safe

### `17aac76c20` — fix: add missing type field — volcanic_island.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/volcanic_island.json`
- **Revert command** (review diff first!): `git show 17aac76c20` then `git revert 17aac76c20` if confirmed safe

### `5cab0a7871` — fix: add missing type field — volcanic_flooded_cavern_mud.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/volcanic_flooded_cavern_mud.json`
- **Revert command** (review diff first!): `git show 5cab0a7871` then `git revert 5cab0a7871` if confirmed safe

### `7f2a1ad239` — fix: add missing type field — rock_formation_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/rock_formation_1.json`
- **Revert command** (review diff first!): `git show 7f2a1ad239` then `git revert 7f2a1ad239` if confirmed safe

### `ffbf1298a4` — fix: add missing type field — mushroom_spires.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/mushroom_spires.json`
- **Revert command** (review diff first!): `git show ffbf1298a4` then `git revert ffbf1298a4` if confirmed safe

### `eb67b61001` — fix: add missing type field — mushroom_island_table.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/mushroom_island_table.json`
- **Revert command** (review diff first!): `git show eb67b61001` then `git revert eb67b61001` if confirmed safe

### `f77eafcec0` — fix: add missing type field — lukewarm_ocean_caves_sand.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_ocean_caves_sand.json`
- **Revert command** (review diff first!): `git show f77eafcec0` then `git revert f77eafcec0` if confirmed safe

### `bf0b5b7edf` — fix: add missing type field — lukewarm_ocean_caves.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_ocean_caves.json`
- **Revert command** (review diff first!): `git show bf0b5b7edf` then `git revert bf0b5b7edf` if confirmed safe

### `546ec0be01` — fix: add missing type field — lukewarm_island_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_island_2.json`
- **Revert command** (review diff first!): `git show 546ec0be01` then `git revert 546ec0be01` if confirmed safe

### `4fe11a7236` — fix: add missing type field — lukewarm_island.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/lukewarm_island.json`
- **Revert command** (review diff first!): `git show 4fe11a7236` then `git revert 4fe11a7236` if confirmed safe

### `34d3eca1f2` — fix: add missing type field — huangshan_spires.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/huangshan_spires.json`
- **Revert command** (review diff first!): `git show 34d3eca1f2` then `git revert 34d3eca1f2` if confirmed safe

### `14c67d43db` — fix: add missing type field — gravelly_beach_rocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/gravelly_beach_rocks.json`
- **Revert command** (review diff first!): `git show 14c67d43db` then `git revert 14c67d43db` if confirmed safe

### `827fa14a3d` — fix: add missing type field — gravel_in_dead_coral.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/gravel_in_dead_coral.json`
- **Revert command** (review diff first!): `git show 827fa14a3d` then `git revert 827fa14a3d` if confirmed safe

### `56c550538d` — fix: add missing type field — giant_mushrooms.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/giant_mushrooms.json`
- **Revert command** (review diff first!): `git show 56c550538d` then `git revert 56c550538d` if confirmed safe

### `987600f19c` — fix: add missing type field — fan_corals.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/fan_corals.json`
- **Revert command** (review diff first!): `git show 987600f19c` then `git revert 987600f19c` if confirmed safe

### `d88ba4bc47` — fix: add missing type field — dead_coral_stack_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/dead_coral_stack_2.json`
- **Revert command** (review diff first!): `git show d88ba4bc47` then `git revert d88ba4bc47` if confirmed safe

### `352531163d` — fix: add missing type field — dead_coral_stack.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/dead_coral_stack.json`
- **Revert command** (review diff first!): `git show 352531163d` then `git revert 352531163d` if confirmed safe

### `c1db168f40` — fix: add missing type field — coral_air_pockets.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/coral_air_pockets.json`
- **Revert command** (review diff first!): `git show c1db168f40` then `git revert c1db168f40` if confirmed safe

### `0eb79e0498` — fix: add missing type field — cold_island_processor.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/cold_island_processor.json`
- **Revert command** (review diff first!): `git show 0eb79e0498` then `git revert 0eb79e0498` if confirmed safe

### `8f8db5c969` — fix: add missing type field — cold_island.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/cold_island.json`
- **Revert command** (review diff first!): `git show 8f8db5c969` then `git revert 8f8db5c969` if confirmed safe

### `ab574d1f93` — fix: add missing type field — bore_hole_corals.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/bore_hole_corals.json`
- **Revert command** (review diff first!): `git show ab574d1f93` then `git revert ab574d1f93` if confirmed safe

### `df9fca38c0` — fix: add missing type field — bore_hole.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/bore_hole.json`
- **Revert command** (review diff first!): `git show df9fca38c0` then `git revert df9fca38c0` if confirmed safe

### `c03bbbf835` — fix: add missing type field — beach_rocks.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/beach_rocks.json`
- **Revert command** (review diff first!): `git show c03bbbf835` then `git revert c03bbbf835` if confirmed safe

### `d8e5f99d3f` — fix: add missing type field — cliff_dripstone.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/cliff_dripstone.json`
- **Revert command** (review diff first!): `git show d8e5f99d3f` then `git revert d8e5f99d3f` if confirmed safe

### `17560dc631` — fix: add missing type field — tall.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/palm/tall.json`
- **Revert command** (review diff first!): `git show 17560dc631` then `git revert 17560dc631` if confirmed safe

### `09ea124d0b` — fix: add missing type field — tall_top.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/palm/branch/tall_top.json`
- **Revert command** (review diff first!): `git show 09ea124d0b` then `git revert 09ea124d0b` if confirmed safe

### `545cce7bb8` — fix: add missing type field — hydrothermal_vent.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
- **Revert command** (review diff first!): `git show 545cce7bb8` then `git revert 545cce7bb8` if confirmed safe

### `84ef13791e` — fix: add missing type field — giant_tubeworm_4.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
- **Revert command** (review diff first!): `git show 84ef13791e` then `git revert 84ef13791e` if confirmed safe

### `88ffd0572d` — fix: add missing type field — giant_tubeworm_3.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
- **Revert command** (review diff first!): `git show 88ffd0572d` then `git revert 88ffd0572d` if confirmed safe

### `a5545f9257` — fix: add missing type field — giant_tubeworm_2.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
- **Revert command** (review diff first!): `git show a5545f9257` then `git revert a5545f9257` if confirmed safe

### `b22fbb027a` — fix: add missing type field — giant_tubeworm_1.json

- **Likely added an unnecessary `"type"` field** (heuristic match on commit message + diff)
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
- **Revert command** (review diff first!): `git show b22fbb027a` then `git revert b22fbb027a` if confirmed safe

### `cd889b2527` — fix(placed_feature): remove ColumnPlacer keys — white_bracket_fungi.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show cd889b2527` then `git revert cd889b2527` if confirmed safe

### `2218108ac7` — fix(placed_feature): remove ColumnPlacer keys — fungal_savanna_vegetation.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_savanna_vegetation.json`
- **Revert command** (review diff first!): `git show 2218108ac7` then `git revert 2218108ac7` if confirmed safe

### `b0fb41721a` — fix(placed_feature): remove ColumnPlacer keys — fungal_powder_spores.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show b0fb41721a` then `git revert b0fb41721a` if confirmed safe

### `c0ddf78cef` — fix(placed_feature): remove ColumnPlacer keys — fungal_jungle_vegetation.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_vegetation.json`
- **Revert command** (review diff first!): `git show c0ddf78cef` then `git revert c0ddf78cef` if confirmed safe

### `07f2187c9c` — fix(configured_feature): remove ColumnPlacer keys — stony_shore_tuff.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stony_shore_tuff.json`
- **Revert command** (review diff first!): `git show 07f2187c9c` then `git revert 07f2187c9c` if confirmed safe

### `116bfb1617` — fix(configured_feature): remove ColumnPlacer keys — stone_cliffs_surface.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs_surface.json`
- **Revert command** (review diff first!): `git show 116bfb1617` then `git revert 116bfb1617` if confirmed safe

### `79bf399a5c` — fix(configured_feature): remove ColumnPlacer keys — snow_blocks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/snow_blocks.json`
- **Revert command** (review diff first!): `git show 79bf399a5c` then `git revert 79bf399a5c` if confirmed safe

### `8c7d3bbd3f` — fix(configured_feature): remove ColumnPlacer keys — shadow_snow.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/shadow_snow.json`
- **Revert command** (review diff first!): `git show 8c7d3bbd3f` then `git revert 8c7d3bbd3f` if confirmed safe

### `5ede485ab0` — fix(configured_feature): remove ColumnPlacer keys — sandy_floor.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/sandy_floor.json`
- **Revert command** (review diff first!): `git show 5ede485ab0` then `git revert 5ede485ab0` if confirmed safe

### `182a7d8dfe` — fix(configured_feature): remove ColumnPlacer keys — river_grass.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/river_grass.json`
- **Revert command** (review diff first!): `git show 182a7d8dfe` then `git revert 182a7d8dfe` if confirmed safe

### `9c5e0d4d76` — fix(configured_feature): remove ColumnPlacer keys — replace_volcanics_flower_forest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_volcanics_flower_forest.json`
- **Revert command** (review diff first!): `git show 9c5e0d4d76` then `git revert 9c5e0d4d76` if confirmed safe

### `82843af39b` — fix(configured_feature): remove ColumnPlacer keys — replace_coarse_dirt_to_moss.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_coarse_dirt_to_moss.json`
- **Revert command** (review diff first!): `git show 82843af39b` then `git revert 82843af39b` if confirmed safe

### `4a248c0fef` — fix(configured_feature): remove ColumnPlacer keys — pamukkale_diorite.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_diorite.json`
- **Revert command** (review diff first!): `git show 4a248c0fef` then `git revert 4a248c0fef` if confirmed safe

### `af2e200e9c` — fix(configured_feature): remove ColumnPlacer keys — pamukkale_calcite.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_calcite.json`
- **Revert command** (review diff first!): `git show af2e200e9c` then `git revert af2e200e9c` if confirmed safe

### `b56acd69d1` — fix(configured_feature): remove ColumnPlacer keys — ice_spikes_grass.json

- **Removed debunked keys**: heightmap, snowy
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_grass.json`
- **Revert command** (review diff first!): `git show b56acd69d1` then `git revert b56acd69d1` if confirmed safe

### `a90e667cfb` — fix(configured_feature): remove ColumnPlacer keys — ice_spikes_glacial_gravel.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_gravel.json`
- **Revert command** (review diff first!): `git show a90e667cfb` then `git revert a90e667cfb` if confirmed safe

### `c5e45e469c` — fix(configured_feature): remove ColumnPlacer keys — ice_spikes_glacial_grass.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/ice_spikes_glacial_grass.json`
- **Revert command** (review diff first!): `git show c5e45e469c` then `git revert c5e45e469c` if confirmed safe

### `2ac8e3a61f` — fix(configured_feature): remove ColumnPlacer keys — highland_stone_cliffs_surface.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/highland_stone_cliffs_surface.json`
- **Revert command** (review diff first!): `git show 2ac8e3a61f` then `git revert 2ac8e3a61f` if confirmed safe

### `7407363569` — fix(configured_feature): remove ColumnPlacer keys — grove_cliffs.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/grove_cliffs.json`
- **Revert command** (review diff first!): `git show 7407363569` then `git revert 7407363569` if confirmed safe

### `594a1febdc` — fix(configured_feature): remove ColumnPlacer keys — glacial_scree.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacial_scree.json`
- **Revert command** (review diff first!): `git show 594a1febdc` then `git revert 594a1febdc` if confirmed safe

### `cd61f23822` — fix(configured_feature): remove ColumnPlacer keys — glacial_pools.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/glacial_pools.json`
- **Revert command** (review diff first!): `git show cd61f23822` then `git revert cd61f23822` if confirmed safe

### `f528164c7c` — fix(configured_feature): remove ColumnPlacer keys — fungal_sculk_infection.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_sculk_infection.json`
- **Revert command** (review diff first!): `git show f528164c7c` then `git revert f528164c7c` if confirmed safe

### `351c569d99` — fix(configured_feature): remove ColumnPlacer keys — fungal_savanna_floor.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_savanna_floor.json`
- **Revert command** (review diff first!): `git show 351c569d99` then `git revert 351c569d99` if confirmed safe

### `b24faf7930` — fix(configured_feature): remove ColumnPlacer keys — fungal_prismarine_shore.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_prismarine_shore.json`
- **Revert command** (review diff first!): `git show b24faf7930` then `git revert b24faf7930` if confirmed safe

### `e9db4b4293` — fix(configured_feature): remove ColumnPlacer keys — fungal_powder.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_powder.json`
- **Revert command** (review diff first!): `git show e9db4b4293` then `git revert e9db4b4293` if confirmed safe

### `6bb14ba4de` — fix(configured_feature): remove ColumnPlacer keys — fungal_mossy_shore_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_mossy_shore_2.json`
- **Revert command** (review diff first!): `git show 6bb14ba4de` then `git revert 6bb14ba4de` if confirmed safe

### `b15ccdeac7` — fix(configured_feature): remove ColumnPlacer keys — fungal_mossy_shore.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_mossy_shore.json`
- **Revert command** (review diff first!): `git show b15ccdeac7` then `git revert b15ccdeac7` if confirmed safe

### `1cb5d97d65` — fix(configured_feature): remove ColumnPlacer keys — fungal_moss.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_moss.json`
- **Revert command** (review diff first!): `git show 1cb5d97d65` then `git revert 1cb5d97d65` if confirmed safe

### `24bfcc9f3a` — fix(configured_feature): remove ColumnPlacer keys — fungal_fire_coral_shore_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_fire_coral_shore_2.json`
- **Revert command** (review diff first!): `git show 24bfcc9f3a` then `git revert 24bfcc9f3a` if confirmed safe

### `d7310f75fc` — fix(configured_feature): remove ColumnPlacer keys — fungal_fire_coral_shore.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_fire_coral_shore.json`
- **Revert command** (review diff first!): `git show d7310f75fc` then `git revert d7310f75fc` if confirmed safe

### `9e1f209290` — fix(configured_feature): remove ColumnPlacer keys — fungal_coral_mycelium.json

- **Removed debunked keys**: heightmap, snowy
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral_mycelium.json`
- **Revert command** (review diff first!): `git show 9e1f209290` then `git revert 9e1f209290` if confirmed safe

### `182951c232` — fix(configured_feature): remove ColumnPlacer keys — fungal_coral_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral_2.json`
- **Revert command** (review diff first!): `git show 182951c232` then `git revert 182951c232` if confirmed safe

### `b0e83c84e4` — fix(configured_feature): remove ColumnPlacer keys — fungal_coral.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/fungal_coral.json`
- **Revert command** (review diff first!): `git show b0e83c84e4` then `git revert b0e83c84e4` if confirmed safe

### `cd7ac4b762` — fix(configured_feature): remove ColumnPlacer keys — forest_snow_blocks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/forest_snow_blocks.json`
- **Revert command** (review diff first!): `git show cd7ac4b762` then `git revert cd7ac4b762` if confirmed safe

### `a16b5bb4b7` — fix(configured_feature): remove ColumnPlacer keys — de_snowify_stone.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/de_snowify_stone.json`
- **Revert command** (review diff first!): `git show a16b5bb4b7` then `git revert a16b5bb4b7` if confirmed safe

### `0a75b4ef26` — fix(configured_feature): remove ColumnPlacer keys — crimson_patch.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crimson_patch.json`
- **Revert command** (review diff first!): `git show 0a75b4ef26` then `git revert 0a75b4ef26` if confirmed safe

### `21102c6bbb` — fix(configured_feature): remove ColumnPlacer keys — crack_ice.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/crack_ice.json`
- **Revert command** (review diff first!): `git show 21102c6bbb` then `git revert 21102c6bbb` if confirmed safe

### `125fdbbd11` — fix(configured_feature): remove ColumnPlacer keys — cherry_pools_edge.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cherry_pools_edge.json`
- **Revert command** (review diff first!): `git show 125fdbbd11` then `git revert 125fdbbd11` if confirmed safe

### `8c228ddc00` — fix(configured_feature): remove ColumnPlacer keys — cherry_pools.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/cherry_pools.json`
- **Revert command** (review diff first!): `git show 8c228ddc00` then `git revert 8c228ddc00` if confirmed safe

### `1bae94b65d` — fix(configured_feature): remove ColumnPlacer keys — beach_mossy_stone.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/beach_mossy_stone.json`
- **Revert command** (review diff first!): `git show 1bae94b65d` then `git revert 1bae94b65d` if confirmed safe

### `b3ce52a074` — fix(configured_feature): remove ColumnPlacer keys — base_snowy_beach.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_snowy_beach.json`
- **Revert command** (review diff first!): `git show b3ce52a074` then `git revert b3ce52a074` if confirmed safe

### `c62a330922` — fix(configured_feature): remove ColumnPlacer keys — base_mangrove_swamp_bayou_hills.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mangrove_swamp_bayou_hills.json`
- **Revert command** (review diff first!): `git show c62a330922` then `git revert c62a330922` if confirmed safe

### `66b67c2512` — fix(configured_feature): remove ColumnPlacer keys — base_jagged_peaks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_jagged_peaks.json`
- **Revert command** (review diff first!): `git show 66b67c2512` then `git revert 66b67c2512` if confirmed safe

### `842dab7f09` — fix(configured_feature): remove ColumnPlacer keys — base_grove.json

- **Removed debunked keys**: heightmap, snowy
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_grove.json`
- **Revert command** (review diff first!): `git show 842dab7f09` then `git revert 842dab7f09` if confirmed safe

### `d578d06c2d` — fix(configured_feature): remove ColumnPlacer keys — base_dark_forest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_dark_forest.json`
- **Revert command** (review diff first!): `git show d578d06c2d` then `git revert d578d06c2d` if confirmed safe

### `2747f5fb00` — fix(configured_feature): remove ColumnPlacer keys — tepui_terrain.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_terrain.json`
- **Revert command** (review diff first!): `git show 2747f5fb00` then `git revert 2747f5fb00` if confirmed safe

### `0c1cd59e6b` — fix(configured_feature): remove ColumnPlacer keys — tepui_lowland_for_glacier.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_lowland_for_glacier.json`
- **Revert command** (review diff first!): `git show 0c1cd59e6b` then `git revert 0c1cd59e6b` if confirmed safe

### `ee0833ab3d` — fix(configured_feature): remove ColumnPlacer keys — tepui_filler.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_filler.json`
- **Revert command** (review diff first!): `git show ee0833ab3d` then `git revert ee0833ab3d` if confirmed safe

### `b43f1f99c8` — fix(configured_feature): remove ColumnPlacer keys — tepui.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui.json`
- **Revert command** (review diff first!): `git show b43f1f99c8` then `git revert b43f1f99c8` if confirmed safe

### `2849968994` — fix(configured_feature): remove ColumnPlacer keys — windswept_snow.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/windswept_snow.json`
- **Revert command** (review diff first!): `git show 2849968994` then `git revert 2849968994` if confirmed safe

### `6ab33a3da6` — fix(configured_feature): remove ColumnPlacer keys — volcano_snow_blocks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/volcano_snow_blocks.json`
- **Revert command** (review diff first!): `git show 6ab33a3da6` then `git revert 6ab33a3da6` if confirmed safe

### `180c02e33e` — fix(configured_feature): remove ColumnPlacer keys — thermal_savanna_forest_base.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/thermal_savanna_forest_base.json`
- **Revert command** (review diff first!): `git show 180c02e33e` then `git revert 180c02e33e` if confirmed safe

### `585140b578` — fix(configured_feature): remove ColumnPlacer keys — scree.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/scree.json`
- **Revert command** (review diff first!): `git show 585140b578` then `git revert 585140b578` if confirmed safe

### `950548d166` — fix(configured_feature): remove ColumnPlacer keys — replace_mud_to_sand.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_mud_to_sand.json`
- **Revert command** (review diff first!): `git show 950548d166` then `git revert 950548d166` if confirmed safe

### `e95ab9fb60` — fix(configured_feature): remove ColumnPlacer keys — replace_gravel_to_sand.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_gravel_to_sand.json`
- **Revert command** (review diff first!): `git show e95ab9fb60` then `git revert e95ab9fb60` if confirmed safe

### `99bb3478ec` — fix(configured_feature): remove ColumnPlacer keys — replace_gravel_to_mud.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_gravel_to_mud.json`
- **Revert command** (review diff first!): `git show 99bb3478ec` then `git revert 99bb3478ec` if confirmed safe

### `2a25ba1969` — fix(configured_feature): remove ColumnPlacer keys — replace_dirt_to_sand.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_dirt_to_sand.json`
- **Revert command** (review diff first!): `git show 2a25ba1969` then `git revert 2a25ba1969` if confirmed safe

### `cc148d895d` — fix(configured_feature): remove ColumnPlacer keys — onsen_deepslate.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_deepslate.json`
- **Revert command** (review diff first!): `git show cc148d895d` then `git revert cc148d895d` if confirmed safe

### `fb12c79a74` — fix(configured_feature): remove ColumnPlacer keys — onsen_calcite.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_calcite.json`
- **Revert command** (review diff first!): `git show fb12c79a74` then `git revert fb12c79a74` if confirmed safe

### `bd0dad7f0e` — fix(configured_feature): remove ColumnPlacer keys — mudify_rooted_dirt.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/mudify_rooted_dirt.json`
- **Revert command** (review diff first!): `git show bd0dad7f0e` then `git revert bd0dad7f0e` if confirmed safe

### `ce120ee9b7` — fix(configured_feature): remove ColumnPlacer keys — disk_clay_dirt_only.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/disk_clay_dirt_only.json`
- **Revert command** (review diff first!): `git show ce120ee9b7` then `git revert ce120ee9b7` if confirmed safe

### `b1abe30804` — fix(configured_feature): remove ColumnPlacer keys — desert_edge.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/desert_edge.json`
- **Revert command** (review diff first!): `git show b1abe30804` then `git revert b1abe30804` if confirmed safe

### `ef6702629d` — fix(configured_feature): remove ColumnPlacer keys — coral_pools_edge.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coral_pools_edge.json`
- **Revert command** (review diff first!): `git show ef6702629d` then `git revert ef6702629d` if confirmed safe

### `55d133e136` — fix(configured_feature): remove ColumnPlacer keys — coral_pools.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coral_pools.json`
- **Revert command** (review diff first!): `git show 55d133e136` then `git revert 55d133e136` if confirmed safe

### `708d93ecd3` — fix(configured_feature): remove ColumnPlacer keys — coastal_sand.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/coastal_sand.json`
- **Revert command** (review diff first!): `git show 708d93ecd3` then `git revert 708d93ecd3` if confirmed safe

### `ca567cfe77` — fix(configured_feature): remove ColumnPlacer keys — base_taiga.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_taiga.json`
- **Revert command** (review diff first!): `git show ca567cfe77` then `git revert ca567cfe77` if confirmed safe

### `f0944f40c8` — fix(configured_feature): remove ColumnPlacer keys — river.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/carver/river.json`
- **Revert command** (review diff first!): `git show f0944f40c8` then `git revert f0944f40c8` if confirmed safe

### `f5448b9bbf` — fix(configured_feature): remove ColumnPlacer keys — ocean.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/carver/ocean.json`
- **Revert command** (review diff first!): `git show f5448b9bbf` then `git revert f5448b9bbf` if confirmed safe

### `f612dff549` — fix(configured_feature): remove ColumnPlacer keys — rainforest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/rainforest.json`
- **Revert command** (review diff first!): `git show f612dff549` then `git revert f612dff549` if confirmed safe

### `80c76ba2e2` — fix(configured_feature): remove ColumnPlacer keys — jungle.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/jungle.json`
- **Revert command** (review diff first!): `git show 80c76ba2e2` then `git revert 80c76ba2e2` if confirmed safe

### `a0466bae1c` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_4.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_4.json`
- **Revert command** (review diff first!): `git show a0466bae1c` then `git revert a0466bae1c` if confirmed safe

### `e3e79982c1` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_3.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_3.json`
- **Revert command** (review diff first!): `git show e3e79982c1` then `git revert e3e79982c1` if confirmed safe

### `c6c4115c3d` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_2b.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_2b.json`
- **Revert command** (review diff first!): `git show c6c4115c3d` then `git revert c6c4115c3d` if confirmed safe

### `41f6490d9e` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_2.json`
- **Revert command** (review diff first!): `git show 41f6490d9e` then `git revert 41f6490d9e` if confirmed safe

### `f40896bd78` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_1b.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_1b.json`
- **Revert command** (review diff first!): `git show f40896bd78` then `git revert f40896bd78` if confirmed safe

### `a962e80671` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_1.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/harvest_fields_1.json`
- **Revert command** (review diff first!): `git show a962e80671` then `git revert a962e80671` if confirmed safe

### `3df9398506` — fix(configured_feature): remove ColumnPlacer keys — bamboo_jungle_old_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle_old_2.json`
- **Revert command** (review diff first!): `git show 3df9398506` then `git revert 3df9398506` if confirmed safe

### `341788dfad` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_2.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/harvest_fields_2.json`
- **Revert command** (review diff first!): `git show 341788dfad` then `git revert 341788dfad` if confirmed safe

### `79ba3fc7c1` — fix(configured_feature): remove ColumnPlacer keys — harvest_fields_1.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/harvest_fields_1.json`
- **Revert command** (review diff first!): `git show 79ba3fc7c1` then `git revert 79ba3fc7c1` if confirmed safe

### `ff4b20a9f2` — fix(configured_feature): remove ColumnPlacer keys — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show ff4b20a9f2` then `git revert ff4b20a9f2` if confirmed safe

### `5d1e36a9ca` — fix(configured_feature): remove ColumnPlacer keys — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 5d1e36a9ca` then `git revert 5d1e36a9ca` if confirmed safe

### `d222d2721d` — fix(configured_feature): remove ColumnPlacer keys — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show d222d2721d` then `git revert d222d2721d` if confirmed safe

### `5355614b1b` — fix(configured_feature): remove ColumnPlacer keys — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 5355614b1b` then `git revert 5355614b1b` if confirmed safe

### `43a3ae8ff5` — fix(configured_feature): remove ColumnPlacer keys — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 43a3ae8ff5` then `git revert 43a3ae8ff5` if confirmed safe

### `a43098979e` — fix(configured_feature): remove ColumnPlacer keys — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show a43098979e` then `git revert a43098979e` if confirmed safe

### `7ae839c2f9` — fix(configured_feature): remove ColumnPlacer keys — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 7ae839c2f9` then `git revert 7ae839c2f9` if confirmed safe

### `5dbf6ef58d` — fix(configured_feature): remove ColumnPlacer keys — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 5dbf6ef58d` then `git revert 5dbf6ef58d` if confirmed safe

### `1d0670a93e` — fix(configured_feature): remove ColumnPlacer keys — 8.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/8.json`
- **Revert command** (review diff first!): `git show 1d0670a93e` then `git revert 1d0670a93e` if confirmed safe

### `afc4839bd5` — fix(configured_feature): remove ColumnPlacer keys — 7.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/7.json`
- **Revert command** (review diff first!): `git show afc4839bd5` then `git revert afc4839bd5` if confirmed safe

### `c9f49f1389` — fix(configured_feature): remove ColumnPlacer keys — 6.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/6.json`
- **Revert command** (review diff first!): `git show c9f49f1389` then `git revert c9f49f1389` if confirmed safe

### `278d296a65` — fix(configured_feature): remove ColumnPlacer keys — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/5.json`
- **Revert command** (review diff first!): `git show 278d296a65` then `git revert 278d296a65` if confirmed safe

### `3ee318a31e` — fix(configured_feature): remove ColumnPlacer keys — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/4.json`
- **Revert command** (review diff first!): `git show 3ee318a31e` then `git revert 3ee318a31e` if confirmed safe

### `bb61d251d6` — fix(configured_feature): remove ColumnPlacer keys — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/3.json`
- **Revert command** (review diff first!): `git show bb61d251d6` then `git revert bb61d251d6` if confirmed safe

### `b81e782925` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/2.json`
- **Revert command** (review diff first!): `git show b81e782925` then `git revert b81e782925` if confirmed safe

### `6061e3fd64` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/1.json`
- **Revert command** (review diff first!): `git show 6061e3fd64` then `git revert 6061e3fd64` if confirmed safe

### `766dd29f71` — fix(configured_feature): remove ColumnPlacer keys — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show 766dd29f71` then `git revert 766dd29f71` if confirmed safe

### `678e793b2a` — fix(configured_feature): remove ColumnPlacer keys — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show 678e793b2a` then `git revert 678e793b2a` if confirmed safe

### `2655127ae7` — fix(configured_feature): remove ColumnPlacer keys — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show 2655127ae7` then `git revert 2655127ae7` if confirmed safe

### `7078f05a03` — fix(configured_feature): remove ColumnPlacer keys — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show 7078f05a03` then `git revert 7078f05a03` if confirmed safe

### `9dcb2a1768` — fix(configured_feature): remove ColumnPlacer keys — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show 9dcb2a1768` then `git revert 9dcb2a1768` if confirmed safe

### `6b58d32c31` — fix(configured_feature): remove ColumnPlacer keys — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 6b58d32c31` then `git revert 6b58d32c31` if confirmed safe

### `376acd878e` — fix(configured_feature): remove ColumnPlacer keys — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show 376acd878e` then `git revert 376acd878e` if confirmed safe

### `1ae6c73860` — fix(configured_feature): remove ColumnPlacer keys — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show 1ae6c73860` then `git revert 1ae6c73860` if confirmed safe

### `c66256b6c2` — fix(configured_feature): remove ColumnPlacer keys — 8.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/8.json`
- **Revert command** (review diff first!): `git show c66256b6c2` then `git revert c66256b6c2` if confirmed safe

### `018d1da8b6` — fix(configured_feature): remove ColumnPlacer keys — 7.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/7.json`
- **Revert command** (review diff first!): `git show 018d1da8b6` then `git revert 018d1da8b6` if confirmed safe

### `8c6580633a` — fix(configured_feature): remove ColumnPlacer keys — 6.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/6.json`
- **Revert command** (review diff first!): `git show 8c6580633a` then `git revert 8c6580633a` if confirmed safe

### `e764a106fb` — fix(configured_feature): remove ColumnPlacer keys — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/5.json`
- **Revert command** (review diff first!): `git show e764a106fb` then `git revert e764a106fb` if confirmed safe

### `23452214fe` — fix(configured_feature): remove ColumnPlacer keys — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/4.json`
- **Revert command** (review diff first!): `git show 23452214fe` then `git revert 23452214fe` if confirmed safe

### `aaba1eea26` — fix(configured_feature): remove ColumnPlacer keys — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/3.json`
- **Revert command** (review diff first!): `git show aaba1eea26` then `git revert aaba1eea26` if confirmed safe

### `e195865e11` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/2.json`
- **Revert command** (review diff first!): `git show e195865e11` then `git revert e195865e11` if confirmed safe

### `cddfb30022` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/1.json`
- **Revert command** (review diff first!): `git show cddfb30022` then `git revert cddfb30022` if confirmed safe

### `2b3c3ba933` — fix(configured_feature): remove ColumnPlacer keys — leaves_2_z.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show 2b3c3ba933` then `git revert 2b3c3ba933` if confirmed safe

### `e093d91344` — fix(configured_feature): remove ColumnPlacer keys — leaves_2_x.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show e093d91344` then `git revert e093d91344` if confirmed safe

### `f110241039` — fix(configured_feature): remove ColumnPlacer keys — leaves_1_z.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show f110241039` then `git revert f110241039` if confirmed safe

### `8414c379aa` — fix(configured_feature): remove ColumnPlacer keys — leaves_1_x.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 8414c379aa` then `git revert 8414c379aa` if confirmed safe

### `0ae881bfa8` — fix(configured_feature): remove ColumnPlacer keys — leaves_2_z.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show 0ae881bfa8` then `git revert 0ae881bfa8` if confirmed safe

### `f574d50272` — fix(configured_feature): remove ColumnPlacer keys — leaves_2_x.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show f574d50272` then `git revert f574d50272` if confirmed safe

### `8b121a5ea2` — fix(configured_feature): remove ColumnPlacer keys — leaves_1_z.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show 8b121a5ea2` then `git revert 8b121a5ea2` if confirmed safe

### `d5215a4d8a` — fix(configured_feature): remove ColumnPlacer keys — leaves_1_x.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show d5215a4d8a` then `git revert d5215a4d8a` if confirmed safe

### `85ef2ec131` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show 85ef2ec131` then `git revert 85ef2ec131` if confirmed safe

### `0c381ae68a` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show 0c381ae68a` then `git revert 0c381ae68a` if confirmed safe

### `2fbcd73f03` — fix(configured_feature): remove ColumnPlacer keys — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 2fbcd73f03` then `git revert 2fbcd73f03` if confirmed safe

### `82b036f28a` — fix(configured_feature): remove ColumnPlacer keys — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 82b036f28a` then `git revert 82b036f28a` if confirmed safe

### `87d425d94b` — fix(configured_feature): remove ColumnPlacer keys — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show 87d425d94b` then `git revert 87d425d94b` if confirmed safe

### `e7fe03861a` — fix(configured_feature): remove ColumnPlacer keys — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show e7fe03861a` then `git revert e7fe03861a` if confirmed safe

### `18659eca05` — fix(configured_feature): remove ColumnPlacer keys — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 18659eca05` then `git revert 18659eca05` if confirmed safe

### `4707910321` — fix(configured_feature): remove ColumnPlacer keys — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 4707910321` then `git revert 4707910321` if confirmed safe

### `50b1dd3a16` — fix(configured_feature): remove ColumnPlacer keys — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 50b1dd3a16` then `git revert 50b1dd3a16` if confirmed safe

### `84ec7ce985` — fix(configured_feature): remove ColumnPlacer keys — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 84ec7ce985` then `git revert 84ec7ce985` if confirmed safe

### `5de2268492` — fix(configured_feature): remove ColumnPlacer keys — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show 5de2268492` then `git revert 5de2268492` if confirmed safe

### `3ea5914622` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show 3ea5914622` then `git revert 3ea5914622` if confirmed safe

### `a6150eab94` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show a6150eab94` then `git revert a6150eab94` if confirmed safe

### `7a9153fad1` — fix(configured_feature): remove ColumnPlacer keys — willow_large.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow_large.json`
- **Revert command** (review diff first!): `git show 7a9153fad1` then `git revert 7a9153fad1` if confirmed safe

### `f5d5ac2f4c` — fix(configured_feature): remove ColumnPlacer keys — willow.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow.json`
- **Revert command** (review diff first!): `git show f5d5ac2f4c` then `git revert f5d5ac2f4c` if confirmed safe

### `0a0f2ca3d0` — fix(configured_feature): remove ColumnPlacer keys — pink_lapacho.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pink_lapacho.json`
- **Revert command** (review diff first!): `git show 0a0f2ca3d0` then `git revert 0a0f2ca3d0` if confirmed safe

### `bdee3cac98` — fix(configured_feature): remove ColumnPlacer keys — pandanus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show bdee3cac98` then `git revert bdee3cac98` if confirmed safe

### `ac736b0548` — fix(configured_feature): remove ColumnPlacer keys — pale_shroom.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom.json`
- **Revert command** (review diff first!): `git show ac736b0548` then `git revert ac736b0548` if confirmed safe

### `636b8a29f7` — fix(configured_feature): remove ColumnPlacer keys — old_willow.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_willow.json`
- **Revert command** (review diff first!): `git show 636b8a29f7` then `git revert 636b8a29f7` if confirmed safe

### `803365ba0a` — fix(configured_feature): remove ColumnPlacer keys — mega_jungle.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 803365ba0a` then `git revert 803365ba0a` if confirmed safe

### `f5c5fb7480` — fix(configured_feature): remove ColumnPlacer keys — marula.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/marula.json`
- **Revert command** (review diff first!): `git show f5c5fb7480` then `git revert f5c5fb7480` if confirmed safe

### `ee9bd5413e` — fix(configured_feature): remove ColumnPlacer keys — kapok.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show ee9bd5413e` then `git revert ee9bd5413e` if confirmed safe

### `b2b7bc443c` — fix(configured_feature): remove ColumnPlacer keys — jungle_mangrove.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show b2b7bc443c` then `git revert b2b7bc443c` if confirmed safe

### `1478d15569` — fix(configured_feature): remove ColumnPlacer keys — flowering_cassia.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_cassia.json`
- **Revert command** (review diff first!): `git show 1478d15569` then `git revert 1478d15569` if confirmed safe

### `d6397254d1` — fix(configured_feature): remove ColumnPlacer keys — complex_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show d6397254d1` then `git revert d6397254d1` if confirmed safe

### `83f2e03b3d` — fix(configured_feature): remove ColumnPlacer keys — complex_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show 83f2e03b3d` then `git revert 83f2e03b3d` if confirmed safe

### `0f1a6c92b6` — fix(configured_feature): remove ColumnPlacer keys — complex_dark_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show 0f1a6c92b6` then `git revert 0f1a6c92b6` if confirmed safe

### `51a6b66b8d` — fix(configured_feature): remove ColumnPlacer keys — complex_dark_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 51a6b66b8d` then `git revert 51a6b66b8d` if confirmed safe

### `8ba740ee93` — fix(configured_feature): remove ColumnPlacer keys — bayou_cypress_4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_4.json`
- **Revert command** (review diff first!): `git show 8ba740ee93` then `git revert 8ba740ee93` if confirmed safe

### `edddd2980b` — fix(configured_feature): remove ColumnPlacer keys — bayou_cypress_3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_3.json`
- **Revert command** (review diff first!): `git show edddd2980b` then `git revert edddd2980b` if confirmed safe

### `8014432f1f` — fix(configured_feature): remove ColumnPlacer keys — bayou_cypress_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_2.json`
- **Revert command** (review diff first!): `git show 8014432f1f` then `git revert 8014432f1f` if confirmed safe

### `b2661043c4` — fix(configured_feature): remove ColumnPlacer keys — bayou_cypress_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_1.json`
- **Revert command** (review diff first!): `git show b2661043c4` then `git revert b2661043c4` if confirmed safe

### `5eaf44a84b` — fix(configured_feature): remove ColumnPlacer keys — bayou_cypress.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress.json`
- **Revert command** (review diff first!): `git show 5eaf44a84b` then `git revert 5eaf44a84b` if confirmed safe

### `a96f7ffacd` — fix(configured_feature): remove ColumnPlacer keys — patch_enoki.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
- **Revert command** (review diff first!): `git show a96f7ffacd` then `git revert a96f7ffacd` if confirmed safe

### `c09ff038ce` — fix(configured_feature): remove ColumnPlacer keys — medium_muscaria.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/medium_muscaria.json`
- **Revert command** (review diff first!): `git show c09ff038ce` then `git revert c09ff038ce` if confirmed safe

### `fe56fbc6b2` — fix(configured_feature): remove ColumnPlacer keys — giant_omphalotus_illudens.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json`
- **Revert command** (review diff first!): `git show fe56fbc6b2` then `git revert fe56fbc6b2` if confirmed safe

### `5bfabd4d12` — fix(configured_feature): remove ColumnPlacer keys — giant_muscaria.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_muscaria.json`
- **Revert command** (review diff first!): `git show 5bfabd4d12` then `git revert 5bfabd4d12` if confirmed safe

### `466c290cd3` — fix(configured_feature): remove ColumnPlacer keys — giant_morel.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_morel.json`
- **Revert command** (review diff first!): `git show 466c290cd3` then `git revert 466c290cd3` if confirmed safe

### `166ff1b421` — fix(configured_feature): remove ColumnPlacer keys — giant_matsutake.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show 166ff1b421` then `git revert 166ff1b421` if confirmed safe

### `88baedde52` — fix(configured_feature): remove ColumnPlacer keys — giant_enoki.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 88baedde52` then `git revert 88baedde52` if confirmed safe

### `feaa03ca31` — fix(configured_feature): remove ColumnPlacer keys — fungal_forest_red.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_red.json`
- **Revert command** (review diff first!): `git show feaa03ca31` then `git revert feaa03ca31` if confirmed safe

### `58c3c107ed` — fix(configured_feature): remove ColumnPlacer keys — fungal_forest_orange.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json`
- **Revert command** (review diff first!): `git show 58c3c107ed` then `git revert 58c3c107ed` if confirmed safe

### `a138548ea0` — fix(configured_feature): remove ColumnPlacer keys — fungal_forest_brown.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_brown.json`
- **Revert command** (review diff first!): `git show a138548ea0` then `git revert a138548ea0` if confirmed safe

### `de53d79439` — fix(configured_feature): remove ColumnPlacer keys — bracket_fungus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show de53d79439` then `git revert de53d79439` if confirmed safe

### `b573904a7c` — fix(configured_feature): remove ColumnPlacer keys — desert.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/desert.json`
- **Revert command** (review diff first!): `git show b573904a7c` then `git revert b573904a7c` if confirmed safe

### `2daf149672` — fix(configured_feature): remove ColumnPlacer keys — birch.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/birch.json`
- **Revert command** (review diff first!): `git show 2daf149672` then `git revert 2daf149672` if confirmed safe

### `10f8b9acf5` — fix(configured_feature): remove ColumnPlacer keys — riverside_jungle_tree.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/riverside_jungle_tree.json`
- **Revert command** (review diff first!): `git show 10f8b9acf5` then `git revert 10f8b9acf5` if confirmed safe

### `3f41741a5c` — fix(configured_feature): remove ColumnPlacer keys — old_swamp_oak.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json`
- **Revert command** (review diff first!): `git show 3f41741a5c` then `git revert 3f41741a5c` if confirmed safe

### `cd9c980973` — fix(configured_feature): remove ColumnPlacer keys — live_oak_dark_swamp.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json`
- **Revert command** (review diff first!): `git show cd9c980973` then `git revert cd9c980973` if confirmed safe

### `45f2a7ead1` — fix(configured_feature): remove ColumnPlacer keys — live_oak_dark.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark.json`
- **Revert command** (review diff first!): `git show 45f2a7ead1` then `git revert 45f2a7ead1` if confirmed safe

### `1976bc46c2` — fix(configured_feature): remove ColumnPlacer keys — 9.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 1976bc46c2` then `git revert 1976bc46c2` if confirmed safe

### `e660963108` — fix(configured_feature): remove ColumnPlacer keys — 8.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show e660963108` then `git revert e660963108` if confirmed safe

### `ab6406d830` — fix(configured_feature): remove ColumnPlacer keys — 7.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show ab6406d830` then `git revert ab6406d830` if confirmed safe

### `c66a0a393a` — fix(configured_feature): remove ColumnPlacer keys — 6.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show c66a0a393a` then `git revert c66a0a393a` if confirmed safe

### `2cdae9751e` — fix(configured_feature): remove ColumnPlacer keys — 10.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show 2cdae9751e` then `git revert 2cdae9751e` if confirmed safe

### `f3ac84f79d` — fix(configured_feature): remove ColumnPlacer keys — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show f3ac84f79d` then `git revert f3ac84f79d` if confirmed safe

### `cf4f77f9ee` — fix(configured_feature): remove ColumnPlacer keys — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show cf4f77f9ee` then `git revert cf4f77f9ee` if confirmed safe

### `289974da86` — fix(configured_feature): remove ColumnPlacer keys — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show 289974da86` then `git revert 289974da86` if confirmed safe

### `61ad0ffb97` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show 61ad0ffb97` then `git revert 61ad0ffb97` if confirmed safe

### `9335791180` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show 9335791180` then `git revert 9335791180` if confirmed safe

### `adb79780c0` — fix(configured_feature): remove ColumnPlacer keys — branch_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show adb79780c0` then `git revert adb79780c0` if confirmed safe

### `f8958e83f5` — fix(configured_feature): remove ColumnPlacer keys — branch_sw.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_sw.json`
- **Revert command** (review diff first!): `git show f8958e83f5` then `git revert f8958e83f5` if confirmed safe

### `3a324a9e5d` — fix(configured_feature): remove ColumnPlacer keys — branch_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show 3a324a9e5d` then `git revert 3a324a9e5d` if confirmed safe

### `158fa09a46` — fix(configured_feature): remove ColumnPlacer keys — branch_se.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_se.json`
- **Revert command** (review diff first!): `git show 158fa09a46` then `git revert 158fa09a46` if confirmed safe

### `d0c84f9605` — fix(configured_feature): remove ColumnPlacer keys — branch_nw.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_nw.json`
- **Revert command** (review diff first!): `git show d0c84f9605` then `git revert d0c84f9605` if confirmed safe

### `56a2dbac78` — fix(configured_feature): remove ColumnPlacer keys — branch_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 56a2dbac78` then `git revert 56a2dbac78` if confirmed safe

### `04e367e4b1` — fix(configured_feature): remove ColumnPlacer keys — branch_ne.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_ne.json`
- **Revert command** (review diff first!): `git show 04e367e4b1` then `git revert 04e367e4b1` if confirmed safe

### `1bcb0b9c76` — fix(configured_feature): remove ColumnPlacer keys — branch_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show 1bcb0b9c76` then `git revert 1bcb0b9c76` if confirmed safe

### `0cde6decdd` — fix(configured_feature): remove ColumnPlacer keys — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/5.json`
- **Revert command** (review diff first!): `git show 0cde6decdd` then `git revert 0cde6decdd` if confirmed safe

### `d0c8b6bd71` — fix(configured_feature): remove ColumnPlacer keys — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/4.json`
- **Revert command** (review diff first!): `git show d0c8b6bd71` then `git revert d0c8b6bd71` if confirmed safe

### `f97c0b82ca` — fix(configured_feature): remove ColumnPlacer keys — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/3.json`
- **Revert command** (review diff first!): `git show f97c0b82ca` then `git revert f97c0b82ca` if confirmed safe

### `001a71a739` — fix(configured_feature): remove ColumnPlacer keys — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/2.json`
- **Revert command** (review diff first!): `git show 001a71a739` then `git revert 001a71a739` if confirmed safe

### `662afbff29` — fix(configured_feature): remove ColumnPlacer keys — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/1.json`
- **Revert command** (review diff first!): `git show 662afbff29` then `git revert 662afbff29` if confirmed safe

### `a5a2ed3813` — fix(configured_feature): remove ColumnPlacer keys — ancient_swamp_oak.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
- **Revert command** (review diff first!): `git show a5a2ed3813` then `git revert a5a2ed3813` if confirmed safe

### `1caeacfa94` — fix(configured_feature): remove leaf blockstate keys — savanna_mossy.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/savanna_mossy.json`
- **Revert command** (review diff first!): `git show 1caeacfa94` then `git revert 1caeacfa94` if confirmed safe

### `1152a1973d` — fix(configured_feature): remove leaf blockstate keys — oasis_palms.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/oasis_palms.json`
- **Revert command** (review diff first!): `git show 1152a1973d` then `git revert 1152a1973d` if confirmed safe

### `b9e30e2982` — fix(configured_feature): remove leaf blockstate keys — cherry_pools.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_pools.json`
- **Revert command** (review diff first!): `git show b9e30e2982` then `git revert b9e30e2982` if confirmed safe

### `b4b31216c3` — fix(configured_feature): remove leaf blockstate keys — cherry_maple.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_maple.json`
- **Revert command** (review diff first!): `git show b4b31216c3` then `git revert b4b31216c3` if confirmed safe

### `d005f5c567` — fix(configured_feature): remove leaf blockstate keys — cherry_huangshan_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_huangshan_pine.json`
- **Revert command** (review diff first!): `git show d005f5c567` then `git revert d005f5c567` if confirmed safe

### `b0e1ef4585` — fix(configured_feature): remove leaf blockstate keys — white_bracket_fungi.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show b0e1ef4585` then `git revert b0e1ef4585` if confirmed safe

### `9c0c1517fb` — fix(configured_feature): remove leaf blockstate keys — fungal_weeping_growths.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_weeping_growths.json`
- **Revert command** (review diff first!): `git show 9c0c1517fb` then `git revert 9c0c1517fb` if confirmed safe

### `aea54f6bbb` — fix(configured_feature): remove leaf blockstate keys — fungal_savanna_vegetation.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_savanna_vegetation.json`
- **Revert command** (review diff first!): `git show aea54f6bbb` then `git revert aea54f6bbb` if confirmed safe

### `4bb347165a` — fix(configured_feature): remove leaf blockstate keys — fungal_powder_spores.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show 4bb347165a` then `git revert 4bb347165a` if confirmed safe

### `1d04de2ff1` — fix(configured_feature): remove leaf blockstate keys — fungal_moss_sprouts.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_moss_sprouts.json`
- **Revert command** (review diff first!): `git show 1d04de2ff1` then `git revert 1d04de2ff1` if confirmed safe

### `ca8cbf9751` — fix(configured_feature): remove leaf blockstate keys — fungal_jungle_vegetation.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_vegetation.json`
- **Revert command** (review diff first!): `git show ca8cbf9751` then `git revert ca8cbf9751` if confirmed safe

### `a1c12b94df` — fix(configured_feature): remove leaf blockstate keys — fungal_blood_woods.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_blood_woods.json`
- **Revert command** (review diff first!): `git show a1c12b94df` then `git revert a1c12b94df` if confirmed safe

### `46c7b11fa3` — fix(configured_feature): remove leaf blockstate keys — cherry_maple_snowy.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_maple_snowy.json`
- **Revert command** (review diff first!): `git show 46c7b11fa3` then `git revert 46c7b11fa3` if confirmed safe

### `7a226a468d` — fix(configured_feature): remove leaf blockstate keys — cherry_huangshan_pine_snowy.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_huangshan_pine_snowy.json`
- **Revert command** (review diff first!): `git show 7a226a468d` then `git revert 7a226a468d` if confirmed safe

### `e45c534597` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show e45c534597` then `git revert e45c534597` if confirmed safe

### `ca7b97ea10` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show ca7b97ea10` then `git revert ca7b97ea10` if confirmed safe

### `c112b3e370` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show c112b3e370` then `git revert c112b3e370` if confirmed safe

### `76ae7d9a4c` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 76ae7d9a4c` then `git revert 76ae7d9a4c` if confirmed safe

### `0cf242cda9` — fix(configured_feature): remove leaf blockstate keys — young_mega_jungle.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json`
- **Revert command** (review diff first!): `git show 0cf242cda9` then `git revert 0cf242cda9` if confirmed safe

### `8042ec5883` — fix(configured_feature): remove leaf blockstate keys — young_kapok.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json`
- **Revert command** (review diff first!): `git show 8042ec5883` then `git revert 8042ec5883` if confirmed safe

### `ff1041603b` — fix(configured_feature): remove leaf blockstate keys — young_brazilwood.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json`
- **Revert command** (review diff first!): `git show ff1041603b` then `git revert ff1041603b` if confirmed safe

### `be4bc13f4d` — fix(configured_feature): remove leaf blockstate keys — willow_large.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow_large.json`
- **Revert command** (review diff first!): `git show be4bc13f4d` then `git revert be4bc13f4d` if confirmed safe

### `93a4202c08` — fix(configured_feature): remove leaf blockstate keys — willow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/willow.json`
- **Revert command** (review diff first!): `git show 93a4202c08` then `git revert 93a4202c08` if confirmed safe

### `fcd9a686e6` — fix(configured_feature): remove leaf blockstate keys — wierwood.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/wierwood.json`
- **Revert command** (review diff first!): `git show fcd9a686e6` then `git revert fcd9a686e6` if confirmed safe

### `7ea2570e44` — fix(configured_feature): remove leaf blockstate keys — tundra_spruce.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_spruce.json`
- **Revert command** (review diff first!): `git show 7ea2570e44` then `git revert 7ea2570e44` if confirmed safe

### `10de08e8b4` — fix(configured_feature): remove leaf blockstate keys — tundra_bush.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_bush.json`
- **Revert command** (review diff first!): `git show 10de08e8b4` then `git revert 10de08e8b4` if confirmed safe

### `eebcbfe26a` — fix(configured_feature): remove leaf blockstate keys — teak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/teak.json`
- **Revert command** (review diff first!): `git show eebcbfe26a` then `git revert eebcbfe26a` if confirmed safe

### `0ae908e98c` — fix(configured_feature): remove leaf blockstate keys — swamp_gum.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json`
- **Revert command** (review diff first!): `git show 0ae908e98c` then `git revert 0ae908e98c` if confirmed safe

### `de07673945` — fix(configured_feature): remove leaf blockstate keys — swamp_forest_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json`
- **Revert command** (review diff first!): `git show de07673945` then `git revert de07673945` if confirmed safe

### `260e699e26` — fix(configured_feature): remove leaf blockstate keys — swamp_forest_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json`
- **Revert command** (review diff first!): `git show 260e699e26` then `git revert 260e699e26` if confirmed safe

### `85ee41e378` — fix(configured_feature): remove leaf blockstate keys — straight_cocoa_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/straight_cocoa_palm.json`
- **Revert command** (review diff first!): `git show 85ee41e378` then `git revert 85ee41e378` if confirmed safe

### `b44e268d9b` — fix(configured_feature): remove leaf blockstate keys — stick_plant_small.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant_small.json`
- **Revert command** (review diff first!): `git show b44e268d9b` then `git revert b44e268d9b` if confirmed safe

### `6cdf0f80e8` — fix(configured_feature): remove leaf blockstate keys — stick_plant.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant.json`
- **Revert command** (review diff first!): `git show 6cdf0f80e8` then `git revert 6cdf0f80e8` if confirmed safe

### `06611a5024` — fix(configured_feature): remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 06611a5024` then `git revert 06611a5024` if confirmed safe

### `4ebffcd0be` — fix(configured_feature): remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 4ebffcd0be` then `git revert 4ebffcd0be` if confirmed safe

### `a990ecd9b0` — fix(configured_feature): remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show a990ecd9b0` then `git revert a990ecd9b0` if confirmed safe

### `6096b2b283` — fix(configured_feature): remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 6096b2b283` then `git revert 6096b2b283` if confirmed safe

### `c2092ef4f6` — fix(configured_feature): remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show c2092ef4f6` then `git revert c2092ef4f6` if confirmed safe

### `2d6a55505f` — fix(configured_feature): remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 2d6a55505f` then `git revert 2d6a55505f` if confirmed safe

### `0d194dd6bd` — fix(configured_feature): remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 0d194dd6bd` then `git revert 0d194dd6bd` if confirmed safe

### `0243ebb092` — fix(configured_feature): remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 0243ebb092` then `git revert 0243ebb092` if confirmed safe

### `6d02b8aaf4` — fix(configured_feature): remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/8.json`
- **Revert command** (review diff first!): `git show 6d02b8aaf4` then `git revert 6d02b8aaf4` if confirmed safe

### `4395137272` — fix(configured_feature): remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/7.json`
- **Revert command** (review diff first!): `git show 4395137272` then `git revert 4395137272` if confirmed safe

### `997e02b99e` — fix(configured_feature): remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/6.json`
- **Revert command** (review diff first!): `git show 997e02b99e` then `git revert 997e02b99e` if confirmed safe

### `4586d33175` — fix(configured_feature): remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/5.json`
- **Revert command** (review diff first!): `git show 4586d33175` then `git revert 4586d33175` if confirmed safe

### `65185bba56` — fix(configured_feature): remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/4.json`
- **Revert command** (review diff first!): `git show 65185bba56` then `git revert 65185bba56` if confirmed safe

### `ed1577942c` — fix(configured_feature): remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/3.json`
- **Revert command** (review diff first!): `git show ed1577942c` then `git revert ed1577942c` if confirmed safe

### `c919de2ac4` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/2.json`
- **Revert command** (review diff first!): `git show c919de2ac4` then `git revert c919de2ac4` if confirmed safe

### `a8518f85f4` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/1.json`
- **Revert command** (review diff first!): `git show a8518f85f4` then `git revert a8518f85f4` if confirmed safe

### `59e11b9215` — fix(configured_feature): remove leaf blockstate keys — sparse_jungle_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sparse_jungle_palm.json`
- **Revert command** (review diff first!): `git show 59e11b9215` then `git revert 59e11b9215` if confirmed safe

### `0729c0d585` — fix(configured_feature): remove leaf blockstate keys — scrub_spruce.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_spruce.json`
- **Revert command** (review diff first!): `git show 0729c0d585` then `git revert 0729c0d585` if confirmed safe

### `112a16fa32` — fix(configured_feature): remove leaf blockstate keys — scrub_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_oak.json`
- **Revert command** (review diff first!): `git show 112a16fa32` then `git revert 112a16fa32` if confirmed safe

### `83713e3e46` — fix(configured_feature): remove leaf blockstate keys — scrub_jungle.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_jungle.json`
- **Revert command** (review diff first!): `git show 83713e3e46` then `git revert 83713e3e46` if confirmed safe

### `29f1eff240` — fix(configured_feature): remove leaf blockstate keys — scrub_flowering_azalea.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_flowering_azalea.json`
- **Revert command** (review diff first!): `git show 29f1eff240` then `git revert 29f1eff240` if confirmed safe

### `ff6c7b12cf` — fix(configured_feature): remove leaf blockstate keys — scrub_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_dark_oak.json`
- **Revert command** (review diff first!): `git show ff6c7b12cf` then `git revert ff6c7b12cf` if confirmed safe

### `0a1a2ba40c` — fix(configured_feature): remove leaf blockstate keys — scrub_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_birch.json`
- **Revert command** (review diff first!): `git show 0a1a2ba40c` then `git revert 0a1a2ba40c` if confirmed safe

### `4c696960f6` — fix(configured_feature): remove leaf blockstate keys — scrub_azalea.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_azalea.json`
- **Revert command** (review diff first!): `git show 4c696960f6` then `git revert 4c696960f6` if confirmed safe

### `4d67b6bd2d` — fix(configured_feature): remove leaf blockstate keys — scrub_acacia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/scrub_acacia.json`
- **Revert command** (review diff first!): `git show 4d67b6bd2d` then `git revert 4d67b6bd2d` if confirmed safe

### `76bab514ce` — fix(configured_feature): remove leaf blockstate keys — sclerophylous_tall.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous_tall.json`
- **Revert command** (review diff first!): `git show 76bab514ce` then `git revert 76bab514ce` if confirmed safe

### `03ee5435d2` — fix(configured_feature): remove leaf blockstate keys — sclerophylous_birch.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous_birch.json`
- **Revert command** (review diff first!): `git show 03ee5435d2` then `git revert 03ee5435d2` if confirmed safe

### `36aac0d944` — fix(configured_feature): remove leaf blockstate keys — sclerophylous.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous.json`
- **Revert command** (review diff first!): `git show 36aac0d944` then `git revert 36aac0d944` if confirmed safe

### `ed64a31839` — fix(configured_feature): remove leaf blockstate keys — savanna_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/savanna_oak.json`
- **Revert command** (review diff first!): `git show ed64a31839` then `git revert ed64a31839` if confirmed safe

### `2e27488a69` — fix(configured_feature): remove leaf blockstate keys — sandalwood.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sandalwood.json`
- **Revert command** (review diff first!): `git show 2e27488a69` then `git revert 2e27488a69` if confirmed safe

### `3c4dad3ad0` — fix(configured_feature): remove leaf blockstate keys — rosewood.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/rosewood.json`
- **Revert command** (review diff first!): `git show 3c4dad3ad0` then `git revert 3c4dad3ad0` if confirmed safe

### `88dafa532c` — fix(configured_feature): remove leaf blockstate keys — riverside_jungle_tree.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/riverside_jungle_tree.json`
- **Revert command** (review diff first!): `git show 88dafa532c` then `git revert 88dafa532c` if confirmed safe

### `d167782c72` — fix(configured_feature): remove leaf blockstate keys — red_ivorywood.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/red_ivorywood.json`
- **Revert command** (review diff first!): `git show d167782c72` then `git revert d167782c72` if confirmed safe

### `b6044db53e` — fix(configured_feature): remove leaf blockstate keys — ponderosa_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_pine.json`
- **Revert command** (review diff first!): `git show b6044db53e` then `git revert b6044db53e` if confirmed safe

### `0917485150` — fix(configured_feature): remove leaf blockstate keys — ponderosa_blackjack.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_blackjack.json`
- **Revert command** (review diff first!): `git show 0917485150` then `git revert 0917485150` if confirmed safe

### `72c203dee7` — fix(configured_feature): remove leaf blockstate keys — ponderosa_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_2.json`
- **Revert command** (review diff first!): `git show 72c203dee7` then `git revert 72c203dee7` if confirmed safe

### `377af04089` — fix(configured_feature): remove leaf blockstate keys — ponderosa_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_1.json`
- **Revert command** (review diff first!): `git show 377af04089` then `git revert 377af04089` if confirmed safe

### `7e58d08ba5` — fix(configured_feature): remove leaf blockstate keys — pinyon_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pinyon_1.json`
- **Revert command** (review diff first!): `git show 7e58d08ba5` then `git revert 7e58d08ba5` if confirmed safe

### `2d38e7b453` — fix(configured_feature): remove leaf blockstate keys — pink_lapacho.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pink_lapacho.json`
- **Revert command** (review diff first!): `git show 2d38e7b453` then `git revert 2d38e7b453` if confirmed safe

### `6167731c4f` — fix(configured_feature): remove leaf blockstate keys — pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pine.json`
- **Revert command** (review diff first!): `git show 6167731c4f` then `git revert 6167731c4f` if confirmed safe

### `e666953732` — fix(configured_feature): remove leaf blockstate keys — pandanus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show e666953732` then `git revert e666953732` if confirmed safe

### `09e66d4714` — fix(configured_feature): remove leaf blockstate keys — pale_shroom.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom.json`
- **Revert command** (review diff first!): `git show 09e66d4714` then `git revert 09e66d4714` if confirmed safe

### `411370d8c4` — fix(configured_feature): remove leaf blockstate keys — pale_dark_eucalyptus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pale_dark_eucalyptus.json`
- **Revert command** (review diff first!): `git show 411370d8c4` then `git revert 411370d8c4` if confirmed safe

### `e493d75a94` — fix(configured_feature): remove leaf blockstate keys — olive.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/olive.json`
- **Revert command** (review diff first!): `git show e493d75a94` then `git revert e493d75a94` if confirmed safe

### `7910618e6f` — fix(configured_feature): remove leaf blockstate keys — old_willow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_willow.json`
- **Revert command** (review diff first!): `git show 7910618e6f` then `git revert 7910618e6f` if confirmed safe

### `8ee842f2d6` — fix(configured_feature): remove leaf blockstate keys — old_swamp_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json`
- **Revert command** (review diff first!): `git show 8ee842f2d6` then `git revert 8ee842f2d6` if confirmed safe

### `e8c995c3d1` — fix(configured_feature): remove leaf blockstate keys — old_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_oak.json`
- **Revert command** (review diff first!): `git show e8c995c3d1` then `git revert e8c995c3d1` if confirmed safe

### `a026b9f266` — fix(configured_feature): remove leaf blockstate keys — old_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/old_dark_oak.json`
- **Revert command** (review diff first!): `git show a026b9f266` then `git revert a026b9f266` if confirmed safe

### `9603798286` — fix(configured_feature): remove leaf blockstate keys — oak_bush.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/oak_bush.json`
- **Revert command** (review diff first!): `git show 9603798286` then `git revert 9603798286` if confirmed safe

### `6c166fd825` — fix(configured_feature): remove leaf blockstate keys — oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/oak.json`
- **Revert command** (review diff first!): `git show 6c166fd825` then `git revert 6c166fd825` if confirmed safe

### `d47dcfa225` — fix(configured_feature): remove leaf blockstate keys — mpingo.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mpingo.json`
- **Revert command** (review diff first!): `git show d47dcfa225` then `git revert d47dcfa225` if confirmed safe

### `b650e5a7d6` — fix(configured_feature): remove leaf blockstate keys — montane_forest_spruce.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/montane_forest_spruce.json`
- **Revert command** (review diff first!): `git show b650e5a7d6` then `git revert b650e5a7d6` if confirmed safe

### `048e730626` — fix(configured_feature): remove leaf blockstate keys — mega_jungle.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show 048e730626` then `git revert 048e730626` if confirmed safe

### `5c3a85d064` — fix(configured_feature): remove leaf blockstate keys — mediterranean_cypress.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mediterranean_cypress.json`
- **Revert command** (review diff first!): `git show 5c3a85d064` then `git revert 5c3a85d064` if confirmed safe

### `266833eac4` — fix(configured_feature): remove leaf blockstate keys — marula.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/marula.json`
- **Revert command** (review diff first!): `git show 266833eac4` then `git revert 266833eac4` if confirmed safe

### `3d5d8a5031` — fix(configured_feature): remove leaf blockstate keys — maple_tall.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/maple_tall.json`
- **Revert command** (review diff first!): `git show 3d5d8a5031` then `git revert 3d5d8a5031` if confirmed safe

### `551900dff6` — fix(configured_feature): remove leaf blockstate keys — mahogany.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mahogany.json`
- **Revert command** (review diff first!): `git show 551900dff6` then `git revert 551900dff6` if confirmed safe

### `70c01e0720` — fix(configured_feature): remove leaf blockstate keys — live_oak_dark_swamp.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json`
- **Revert command** (review diff first!): `git show 70c01e0720` then `git revert 70c01e0720` if confirmed safe

### `887f04514d` — fix(configured_feature): remove leaf blockstate keys — live_oak_dark.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark.json`
- **Revert command** (review diff first!): `git show 887f04514d` then `git revert 887f04514d` if confirmed safe

### `30c2f80756` — fix(configured_feature): remove leaf blockstate keys — live_oak_bright.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_bright.json`
- **Revert command** (review diff first!): `git show 30c2f80756` then `git revert 30c2f80756` if confirmed safe

### `8f2a842329` — fix(configured_feature): remove leaf blockstate keys — live_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/live_oak.json`
- **Revert command** (review diff first!): `git show 8f2a842329` then `git revert 8f2a842329` if confirmed safe

### `c10c231324` — fix(configured_feature): remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show c10c231324` then `git revert c10c231324` if confirmed safe

### `188ff4dd57` — fix(configured_feature): remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show 188ff4dd57` then `git revert 188ff4dd57` if confirmed safe

### `b652e9e342` — fix(configured_feature): remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show b652e9e342` then `git revert b652e9e342` if confirmed safe

### `783fe8caf5` — fix(configured_feature): remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show 783fe8caf5` then `git revert 783fe8caf5` if confirmed safe

### `80419e545b` — fix(configured_feature): remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show 80419e545b` then `git revert 80419e545b` if confirmed safe

### `6bec3eac13` — fix(configured_feature): remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 6bec3eac13` then `git revert 6bec3eac13` if confirmed safe

### `e7a5235956` — fix(configured_feature): remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show e7a5235956` then `git revert e7a5235956` if confirmed safe

### `d0a919048e` — fix(configured_feature): remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show d0a919048e` then `git revert d0a919048e` if confirmed safe

### `797ee3cdb8` — fix(configured_feature): remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/8.json`
- **Revert command** (review diff first!): `git show 797ee3cdb8` then `git revert 797ee3cdb8` if confirmed safe

### `bfa1716032` — fix(configured_feature): remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/7.json`
- **Revert command** (review diff first!): `git show bfa1716032` then `git revert bfa1716032` if confirmed safe

### `543af15f2b` — fix(configured_feature): remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/6.json`
- **Revert command** (review diff first!): `git show 543af15f2b` then `git revert 543af15f2b` if confirmed safe

### `9d95e9d53c` — fix(configured_feature): remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/5.json`
- **Revert command** (review diff first!): `git show 9d95e9d53c` then `git revert 9d95e9d53c` if confirmed safe

### `b47832e1c2` — fix(configured_feature): remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/4.json`
- **Revert command** (review diff first!): `git show b47832e1c2` then `git revert b47832e1c2` if confirmed safe

### `52b2295a73` — fix(configured_feature): remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/3.json`
- **Revert command** (review diff first!): `git show 52b2295a73` then `git revert 52b2295a73` if confirmed safe

### `00b648e91b` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/2.json`
- **Revert command** (review diff first!): `git show 00b648e91b` then `git revert 00b648e91b` if confirmed safe

### `df481dfe2c` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/1.json`
- **Revert command** (review diff first!): `git show df481dfe2c` then `git revert df481dfe2c` if confirmed safe

### `cfa7c2492a` — fix(configured_feature): remove leaf blockstate keys — kapok.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show cfa7c2492a` then `git revert cfa7c2492a` if confirmed safe

### `a34074cf4b` — fix(configured_feature): remove leaf blockstate keys — jungle_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_pine.json`
- **Revert command** (review diff first!): `git show a34074cf4b` then `git revert a34074cf4b` if confirmed safe

### `b50e71730b` — fix(configured_feature): remove leaf blockstate keys — jungle_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_palm.json`
- **Revert command** (review diff first!): `git show b50e71730b` then `git revert b50e71730b` if confirmed safe

### `f39db3c228` — fix(configured_feature): remove leaf blockstate keys — jungle_mangrove.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show f39db3c228` then `git revert f39db3c228` if confirmed safe

### `0b3977c5e1` — fix(configured_feature): remove leaf blockstate keys — leaves_2_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show 0b3977c5e1` then `git revert 0b3977c5e1` if confirmed safe

### `d855804893` — fix(configured_feature): remove leaf blockstate keys — leaves_2_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show d855804893` then `git revert d855804893` if confirmed safe

### `ada8eee0ad` — fix(configured_feature): remove leaf blockstate keys — leaves_1_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show ada8eee0ad` then `git revert ada8eee0ad` if confirmed safe

### `5c082555ae` — fix(configured_feature): remove leaf blockstate keys — leaves_1_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 5c082555ae` then `git revert 5c082555ae` if confirmed safe

### `0265f28a30` — fix(configured_feature): remove leaf blockstate keys — 9.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 0265f28a30` then `git revert 0265f28a30` if confirmed safe

### `87dcc679c6` — fix(configured_feature): remove leaf blockstate keys — 8.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show 87dcc679c6` then `git revert 87dcc679c6` if confirmed safe

### `2b2994bac8` — fix(configured_feature): remove leaf blockstate keys — 7.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show 2b2994bac8` then `git revert 2b2994bac8` if confirmed safe

### `c198e55db9` — fix(configured_feature): remove leaf blockstate keys — 6.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show c198e55db9` then `git revert c198e55db9` if confirmed safe

### `392160da3e` — fix(configured_feature): remove leaf blockstate keys — 10.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show 392160da3e` then `git revert 392160da3e` if confirmed safe

### `e218b28f52` — fix(configured_feature): remove leaf blockstate keys — leaves_2_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_z.json`
- **Revert command** (review diff first!): `git show e218b28f52` then `git revert e218b28f52` if confirmed safe

### `bc566bffb7` — fix(configured_feature): remove leaf blockstate keys — leaves_2_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_2_x.json`
- **Revert command** (review diff first!): `git show bc566bffb7` then `git revert bc566bffb7` if confirmed safe

### `60beee604e` — fix(configured_feature): remove leaf blockstate keys — leaves_1_z.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_z.json`
- **Revert command** (review diff first!): `git show 60beee604e` then `git revert 60beee604e` if confirmed safe

### `63055a63da` — fix(configured_feature): remove leaf blockstate keys — leaves_1_x.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/leaves_1_x.json`
- **Revert command** (review diff first!): `git show 63055a63da` then `git revert 63055a63da` if confirmed safe

### `46e9a1a5c9` — fix(configured_feature): remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show 46e9a1a5c9` then `git revert 46e9a1a5c9` if confirmed safe

### `1b21444bde` — fix(configured_feature): remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show 1b21444bde` then `git revert 1b21444bde` if confirmed safe

### `e518d929b4` — fix(configured_feature): remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show e518d929b4` then `git revert e518d929b4` if confirmed safe

### `db55567872` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show db55567872` then `git revert db55567872` if confirmed safe

### `aa4a8a0b13` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show aa4a8a0b13` then `git revert aa4a8a0b13` if confirmed safe

### `df87cba6fd` — fix(configured_feature): remove leaf blockstate keys — branch_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show df87cba6fd` then `git revert df87cba6fd` if confirmed safe

### `8223e90151` — fix(configured_feature): remove leaf blockstate keys — branch_sw.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_sw.json`
- **Revert command** (review diff first!): `git show 8223e90151` then `git revert 8223e90151` if confirmed safe

### `7415789beb` — fix(configured_feature): remove leaf blockstate keys — branch_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show 7415789beb` then `git revert 7415789beb` if confirmed safe

### `28aba1ba46` — fix(configured_feature): remove leaf blockstate keys — branch_se.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_se.json`
- **Revert command** (review diff first!): `git show 28aba1ba46` then `git revert 28aba1ba46` if confirmed safe

### `f20efb8f82` — fix(configured_feature): remove leaf blockstate keys — branch_nw.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_nw.json`
- **Revert command** (review diff first!): `git show f20efb8f82` then `git revert f20efb8f82` if confirmed safe

### `29e2c8aaf4` — fix(configured_feature): remove leaf blockstate keys — branch_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 29e2c8aaf4` then `git revert 29e2c8aaf4` if confirmed safe

### `ce2b9a9db0` — fix(configured_feature): remove leaf blockstate keys — branch_ne.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_ne.json`
- **Revert command** (review diff first!): `git show ce2b9a9db0` then `git revert ce2b9a9db0` if confirmed safe

### `2206de71cb` — fix(configured_feature): remove leaf blockstate keys — branch_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show 2206de71cb` then `git revert 2206de71cb` if confirmed safe

### `7d581cfe08` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show 7d581cfe08` then `git revert 7d581cfe08` if confirmed safe

### `53b2c01a27` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show 53b2c01a27` then `git revert 53b2c01a27` if confirmed safe

### `3e16e012e9` — fix(configured_feature): remove leaf blockstate keys — huangshan_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huangshan_pine.json`
- **Revert command** (review diff first!): `git show 3e16e012e9` then `git revert 3e16e012e9` if confirmed safe

### `c429b10f16` — fix(configured_feature): remove leaf blockstate keys — ground_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ground_pine.json`
- **Revert command** (review diff first!): `git show c429b10f16` then `git revert c429b10f16` if confirmed safe

### `e229a170fc` — fix(configured_feature): remove leaf blockstate keys — glow_banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/glow_banyan.json`
- **Revert command** (review diff first!): `git show e229a170fc` then `git revert e229a170fc` if confirmed safe

### `a8ff13601f` — fix(configured_feature): remove leaf blockstate keys — giant_magnolia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/giant_magnolia.json`
- **Revert command** (review diff first!): `git show a8ff13601f` then `git revert a8ff13601f` if confirmed safe

### `2a5c39aea0` — fix(configured_feature): remove leaf blockstate keys — forest_tropical_pine_4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_4.json`
- **Revert command** (review diff first!): `git show 2a5c39aea0` then `git revert 2a5c39aea0` if confirmed safe

### `6628fc6824` — fix(configured_feature): remove leaf blockstate keys — forest_tropical_pine_3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_3.json`
- **Revert command** (review diff first!): `git show 6628fc6824` then `git revert 6628fc6824` if confirmed safe

### `b48d9ee9f6` — fix(configured_feature): remove leaf blockstate keys — forest_tropical_pine_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_2.json`
- **Revert command** (review diff first!): `git show b48d9ee9f6` then `git revert b48d9ee9f6` if confirmed safe

### `edc41b331c` — fix(configured_feature): remove leaf blockstate keys — forest_tropical_pine_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine_1.json`
- **Revert command** (review diff first!): `git show edc41b331c` then `git revert edc41b331c` if confirmed safe

### `56a39817c9` — fix(configured_feature): remove leaf blockstate keys — forest_tropical_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_tropical_pine.json`
- **Revert command** (review diff first!): `git show 56a39817c9` then `git revert 56a39817c9` if confirmed safe

### `d90aab2532` — fix(configured_feature): remove leaf blockstate keys — forest_pine_4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_4.json`
- **Revert command** (review diff first!): `git show d90aab2532` then `git revert d90aab2532` if confirmed safe

### `35e1f6834b` — fix(configured_feature): remove leaf blockstate keys — forest_pine_3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_3.json`
- **Revert command** (review diff first!): `git show 35e1f6834b` then `git revert 35e1f6834b` if confirmed safe

### `52c439b843` — fix(configured_feature): remove leaf blockstate keys — forest_pine_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_2.json`
- **Revert command** (review diff first!): `git show 52c439b843` then `git revert 52c439b843` if confirmed safe

### `9414bed908` — fix(configured_feature): remove leaf blockstate keys — forest_pine_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine_1.json`
- **Revert command** (review diff first!): `git show 9414bed908` then `git revert 9414bed908` if confirmed safe

### `a6cee57e9e` — fix(configured_feature): remove leaf blockstate keys — forest_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_pine.json`
- **Revert command** (review diff first!): `git show a6cee57e9e` then `git revert a6cee57e9e` if confirmed safe

### `b90ada8c06` — fix(configured_feature): remove leaf blockstate keys — forest_eucalyptus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_eucalyptus.json`
- **Revert command** (review diff first!): `git show b90ada8c06` then `git revert b90ada8c06` if confirmed safe

### `f91bc0aa90` — fix(configured_feature): remove leaf blockstate keys — forest_eucalypt_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_eucalypt_birch.json`
- **Revert command** (review diff first!): `git show f91bc0aa90` then `git revert f91bc0aa90` if confirmed safe

### `b1389737b5` — fix(configured_feature): remove leaf blockstate keys — forest_azalea.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/forest_azalea.json`
- **Revert command** (review diff first!): `git show b1389737b5` then `git revert b1389737b5` if confirmed safe

### `3cb4137aac` — fix(configured_feature): remove leaf blockstate keys — flowering_cassia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_cassia.json`
- **Revert command** (review diff first!): `git show 3cb4137aac` then `git revert 3cb4137aac` if confirmed safe

### `ad7c0b9d5a` — fix(configured_feature): remove leaf blockstate keys — flowering_azalea_bush.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/flowering_azalea_bush.json`
- **Revert command** (review diff first!): `git show ad7c0b9d5a` then `git revert ad7c0b9d5a` if confirmed safe

### `152412a82a` — fix(configured_feature): remove leaf blockstate keys — fir_tall.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fir_tall.json`
- **Revert command** (review diff first!): `git show 152412a82a` then `git revert 152412a82a` if confirmed safe

### `24b72e8ab7` — fix(configured_feature): remove leaf blockstate keys — fir_medium.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fir_medium.json`
- **Revert command** (review diff first!): `git show 24b72e8ab7` then `git revert 24b72e8ab7` if confirmed safe

### `042d46a90f` — fix(configured_feature): remove leaf blockstate keys — fen_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fen_pine.json`
- **Revert command** (review diff first!): `git show 042d46a90f` then `git revert 042d46a90f` if confirmed safe

### `80fe9031ce` — fix(configured_feature): remove leaf blockstate keys — eucalyptus_salubris.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_salubris.json`
- **Revert command** (review diff first!): `git show 80fe9031ce` then `git revert 80fe9031ce` if confirmed safe

### `5405c4de16` — fix(configured_feature): remove leaf blockstate keys — eucalyptus_deanei_white.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json`
- **Revert command** (review diff first!): `git show 5405c4de16` then `git revert 5405c4de16` if confirmed safe

### `fb14ca3ed6` — fix(configured_feature): remove leaf blockstate keys — eucalyptus_deanei_gray.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_gray.json`
- **Revert command** (review diff first!): `git show fb14ca3ed6` then `git revert fb14ca3ed6` if confirmed safe

### `320bfd6d03` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_tropical_gold.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show 320bfd6d03` then `git revert 320bfd6d03` if confirmed safe

### `75449de16e` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_tropical.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 75449de16e` then `git revert 75449de16e` if confirmed safe

### `f1610cf5b3` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_temperate_gold.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show f1610cf5b3` then `git revert f1610cf5b3` if confirmed safe

### `0fa1302372` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_temperate.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show 0fa1302372` then `git revert 0fa1302372` if confirmed safe

### `027e3ca812` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_medium.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_medium.json`
- **Revert command** (review diff first!): `git show 027e3ca812` then `git revert 027e3ca812` if confirmed safe

### `71565eb791` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_dependent.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_dependent.json`
- **Revert command** (review diff first!): `git show 71565eb791` then `git revert 71565eb791` if confirmed safe

### `f3fb11de7b` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_dark.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_dark.json`
- **Revert command** (review diff first!): `git show f3fb11de7b` then `git revert f3fb11de7b` if confirmed safe

### `20b37a61b5` — fix(configured_feature): remove leaf blockstate keys — elephant_bamboo_bright.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_bright.json`
- **Revert command** (review diff first!): `git show 20b37a61b5` then `git revert 20b37a61b5` if confirmed safe

### `1b6ca9f7f0` — fix(configured_feature): remove leaf blockstate keys — ebony.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ebony.json`
- **Revert command** (review diff first!): `git show 1b6ca9f7f0` then `git revert 1b6ca9f7f0` if confirmed safe

### `5dd1b53ec4` — fix(configured_feature): remove leaf blockstate keys — desert_fan_palm_tall.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_tall.json`
- **Revert command** (review diff first!): `git show 5dd1b53ec4` then `git revert 5dd1b53ec4` if confirmed safe

### `2ee5054631` — fix(configured_feature): remove leaf blockstate keys — desert_fan_palm_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm_2.json`
- **Revert command** (review diff first!): `git show 2ee5054631` then `git revert 2ee5054631` if confirmed safe

### `7d564af881` — fix(configured_feature): remove leaf blockstate keys — desert_fan_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/desert_fan_palm.json`
- **Revert command** (review diff first!): `git show 7d564af881` then `git revert 7d564af881` if confirmed safe

### `2722ed2b24` — fix(configured_feature): remove leaf blockstate keys — 2_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 2722ed2b24` then `git revert 2722ed2b24` if confirmed safe

### `5ac1f6f4c0` — fix(configured_feature): remove leaf blockstate keys — 2_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 5ac1f6f4c0` then `git revert 5ac1f6f4c0` if confirmed safe

### `a60cc122db` — fix(configured_feature): remove leaf blockstate keys — 2_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show a60cc122db` then `git revert a60cc122db` if confirmed safe

### `369727b68a` — fix(configured_feature): remove leaf blockstate keys — 2_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 369727b68a` then `git revert 369727b68a` if confirmed safe

### `5ff445d221` — fix(configured_feature): remove leaf blockstate keys — 1_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 5ff445d221` then `git revert 5ff445d221` if confirmed safe

### `cb847c51e8` — fix(configured_feature): remove leaf blockstate keys — 1_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show cb847c51e8` then `git revert cb847c51e8` if confirmed safe

### `b64f0cbef1` — fix(configured_feature): remove leaf blockstate keys — 1_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show b64f0cbef1` then `git revert b64f0cbef1` if confirmed safe

### `62eed2b14b` — fix(configured_feature): remove leaf blockstate keys — 1_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 62eed2b14b` then `git revert 62eed2b14b` if confirmed safe

### `5540c9dddc` — fix(configured_feature): remove leaf blockstate keys — 5.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/5.json`
- **Revert command** (review diff first!): `git show 5540c9dddc` then `git revert 5540c9dddc` if confirmed safe

### `e03dce31cc` — fix(configured_feature): remove leaf blockstate keys — 4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/4.json`
- **Revert command** (review diff first!): `git show e03dce31cc` then `git revert e03dce31cc` if confirmed safe

### `50dadf63e6` — fix(configured_feature): remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/3.json`
- **Revert command** (review diff first!): `git show 50dadf63e6` then `git revert 50dadf63e6` if confirmed safe

### `f21fda363c` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/2.json`
- **Revert command** (review diff first!): `git show f21fda363c` then `git revert f21fda363c` if confirmed safe

### `8cb03c3920` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/1.json`
- **Revert command** (review diff first!): `git show 8cb03c3920` then `git revert 8cb03c3920` if confirmed safe

### `d02c5aa68e` — fix(configured_feature): remove leaf blockstate keys — dark_eucalyptus.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dark_eucalyptus.json`
- **Revert command** (review diff first!): `git show d02c5aa68e` then `git revert d02c5aa68e` if confirmed safe

### `6beae55be0` — fix(configured_feature): remove leaf blockstate keys — dark_banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dark_banyan.json`
- **Revert command** (review diff first!): `git show 6beae55be0` then `git revert 6beae55be0` if confirmed safe

### `a345804363` — fix(configured_feature): remove leaf blockstate keys — corymbia_aparrerinja.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/corymbia_aparrerinja.json`
- **Revert command** (review diff first!): `git show a345804363` then `git revert a345804363` if confirmed safe

### `8e920461ee` — fix(configured_feature): remove leaf blockstate keys — complex_oak_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show 8e920461ee` then `git revert 8e920461ee` if confirmed safe

### `fa909a7134` — fix(configured_feature): remove leaf blockstate keys — complex_oak_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show fa909a7134` then `git revert fa909a7134` if confirmed safe

### `51f016fd9c` — fix(configured_feature): remove leaf blockstate keys — complex_dark_oak_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show 51f016fd9c` then `git revert 51f016fd9c` if confirmed safe

### `77d132efca` — fix(configured_feature): remove leaf blockstate keys — complex_dark_oak_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 77d132efca` then `git revert 77d132efca` if confirmed safe

### `14be98a874` — fix(configured_feature): remove leaf blockstate keys — cold_pine_medium.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cold_pine_medium.json`
- **Revert command** (review diff first!): `git show 14be98a874` then `git revert 14be98a874` if confirmed safe

### `25ef67488f` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 25ef67488f` then `git revert 25ef67488f` if confirmed safe

### `1c01cab7db` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show 1c01cab7db` then `git revert 1c01cab7db` if confirmed safe

### `a95cf67ac6` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show a95cf67ac6` then `git revert a95cf67ac6` if confirmed safe

### `71df9de91f` — fix(configured_feature): remove leaf blockstate keys — coastal_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 71df9de91f` then `git revert 71df9de91f` if confirmed safe

### `ed1c52ce5f` — fix(configured_feature): remove leaf blockstate keys — brazilwood.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json`
- **Revert command** (review diff first!): `git show ed1c52ce5f` then `git revert ed1c52ce5f` if confirmed safe

### `fb4c5bcc34` — fix(configured_feature): remove leaf blockstate keys — birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/birch.json`
- **Revert command** (review diff first!): `git show fb4c5bcc34` then `git revert fb4c5bcc34` if confirmed safe

### `06e594da34` — fix(configured_feature): remove leaf blockstate keys — 3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show 06e594da34` then `git revert 06e594da34` if confirmed safe

### `b391939ef9` — fix(configured_feature): remove leaf blockstate keys — 2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show b391939ef9` then `git revert b391939ef9` if confirmed safe

### `0b886d9537` — fix(configured_feature): remove leaf blockstate keys — 1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show 0b886d9537` then `git revert 0b886d9537` if confirmed safe

### `5d5fdac279` — fix(configured_feature): remove leaf blockstate keys — bent_palm_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_west.json`
- **Revert command** (review diff first!): `git show 5d5fdac279` then `git revert 5d5fdac279` if confirmed safe

### `20b4830dcc` — fix(configured_feature): remove leaf blockstate keys — bent_palm_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_south.json`
- **Revert command** (review diff first!): `git show 20b4830dcc` then `git revert 20b4830dcc` if confirmed safe

### `e3d0341840` — fix(configured_feature): remove leaf blockstate keys — bent_palm_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_north.json`
- **Revert command** (review diff first!): `git show e3d0341840` then `git revert e3d0341840` if confirmed safe

### `e4101c7370` — fix(configured_feature): remove leaf blockstate keys — bent_palm_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_east.json`
- **Revert command** (review diff first!): `git show e4101c7370` then `git revert e4101c7370` if confirmed safe

### `0ceee02d0b` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_surface_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json`
- **Revert command** (review diff first!): `git show 0ceee02d0b` then `git revert 0ceee02d0b` if confirmed safe

### `a2ea20e78f` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_surface.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json`
- **Revert command** (review diff first!): `git show a2ea20e78f` then `git revert a2ea20e78f` if confirmed safe

### `39efa2c01b` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_shallow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json`
- **Revert command** (review diff first!): `git show 39efa2c01b` then `git revert 39efa2c01b` if confirmed safe

### `dae69b346b` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_middle.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
- **Revert command** (review diff first!): `git show dae69b346b` then `git revert dae69b346b` if confirmed safe

### `ee1cc4cbaf` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_deep.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
- **Revert command** (review diff first!): `git show ee1cc4cbaf` then `git revert ee1cc4cbaf` if confirmed safe

### `b423499c72` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_4.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_4.json`
- **Revert command** (review diff first!): `git show b423499c72` then `git revert b423499c72` if confirmed safe

### `ca715fd57d` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_3.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_3.json`
- **Revert command** (review diff first!): `git show ca715fd57d` then `git revert ca715fd57d` if confirmed safe

### `18a06dbbe3` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_2.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_2.json`
- **Revert command** (review diff first!): `git show 18a06dbbe3` then `git revert 18a06dbbe3` if confirmed safe

### `c5488e2aa2` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress_1.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_1.json`
- **Revert command** (review diff first!): `git show c5488e2aa2` then `git revert c5488e2aa2` if confirmed safe

### `790592b723` — fix(configured_feature): remove leaf blockstate keys — bayou_cypress.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress.json`
- **Revert command** (review diff first!): `git show 790592b723` then `git revert 790592b723` if confirmed safe

### `eac10baff5` — fix(configured_feature): remove leaf blockstate keys — baobab_small.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_small.json`
- **Revert command** (review diff first!): `git show eac10baff5` then `git revert eac10baff5` if confirmed safe

### `10ddc3c1fb` — fix(configured_feature): remove leaf blockstate keys — baobab_short.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_short.json`
- **Revert command** (review diff first!): `git show 10ddc3c1fb` then `git revert 10ddc3c1fb` if confirmed safe

### `dab7dc561e` — fix(configured_feature): remove leaf blockstate keys — baobab.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab.json`
- **Revert command** (review diff first!): `git show dab7dc561e` then `git revert dab7dc561e` if confirmed safe

### `b288619dc4` — fix(configured_feature): remove leaf blockstate keys — banyan.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/banyan.json`
- **Revert command** (review diff first!): `git show b288619dc4` then `git revert b288619dc4` if confirmed safe

### `448876082b` — fix(configured_feature): remove leaf blockstate keys — bamboo_palm.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bamboo_palm.json`
- **Revert command** (review diff first!): `git show 448876082b` then `git revert 448876082b` if confirmed safe

### `1a8dd0496f` — fix(configured_feature): remove leaf blockstate keys — azalea_conifer.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_conifer.json`
- **Revert command** (review diff first!): `git show 1a8dd0496f` then `git revert 1a8dd0496f` if confirmed safe

### `87b0b6f07c` — fix(configured_feature): remove leaf blockstate keys — azalea_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_birch.json`
- **Revert command** (review diff first!): `git show 87b0b6f07c` then `git revert 87b0b6f07c` if confirmed safe

### `28022a167e` — fix(configured_feature): remove leaf blockstate keys — aspen_leaf_litter.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen_leaf_litter.json`
- **Revert command** (review diff first!): `git show 28022a167e` then `git revert 28022a167e` if confirmed safe

### `2b5af94838` — fix(configured_feature): remove leaf blockstate keys — aspen.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen.json`
- **Revert command** (review diff first!): `git show 2b5af94838` then `git revert 2b5af94838` if confirmed safe

### `14f30fbf28` — fix(configured_feature): remove leaf blockstate keys — ancient_swamp_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json`
- **Revert command** (review diff first!): `git show 14f30fbf28` then `git revert 14f30fbf28` if confirmed safe

### `6e08bbf151` — fix(configured_feature): remove leaf blockstate keys — ancient_pale_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_pale_oak.json`
- **Revert command** (review diff first!): `git show 6e08bbf151` then `git revert 6e08bbf151` if confirmed safe

### `55bdf7cb54` — fix(configured_feature): remove leaf blockstate keys — ancient_oak_old.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_oak_old.json`
- **Revert command** (review diff first!): `git show 55bdf7cb54` then `git revert 55bdf7cb54` if confirmed safe

### `71a7d315a2` — fix(configured_feature): remove leaf blockstate keys — ancient_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_oak.json`
- **Revert command** (review diff first!): `git show 71a7d315a2` then `git revert 71a7d315a2` if confirmed safe

### `687acae765` — fix(configured_feature): remove leaf blockstate keys — ancient_dark_oak_old.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak_old.json`
- **Revert command** (review diff first!): `git show 687acae765` then `git revert 687acae765` if confirmed safe

### `9853c6149f` — fix(configured_feature): remove leaf blockstate keys — ancient_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak.json`
- **Revert command** (review diff first!): `git show 9853c6149f` then `git revert 9853c6149f` if confirmed safe

### `bc7004adec` — fix(configured_feature): remove leaf blockstate keys — ancient_birch_old.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_birch_old.json`
- **Revert command** (review diff first!): `git show bc7004adec` then `git revert bc7004adec` if confirmed safe

### `70c928f42c` — fix(configured_feature): remove leaf blockstate keys — ancient_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_birch.json`
- **Revert command** (review diff first!): `git show 70c928f42c` then `git revert 70c928f42c` if confirmed safe

### `0ebf00e076` — fix(configured_feature): remove leaf blockstate keys — ancient_azalea_old.json

- **Removed debunked keys**: persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_azalea_old.json`
- **Revert command** (review diff first!): `git show 0ebf00e076` then `git revert 0ebf00e076` if confirmed safe

### `736f0e9f54` — fix(configured_feature): remove leaf blockstate keys — ancient_azalea.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_azalea.json`
- **Revert command** (review diff first!): `git show 736f0e9f54` then `git revert 736f0e9f54` if confirmed safe

### `0f34fa955a` — fix(configured_feature): remove leaf blockstate keys — acacia_plains.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/acacia_plains.json`
- **Revert command** (review diff first!): `git show 0f34fa955a` then `git revert 0f34fa955a` if confirmed safe

### `10f7982d96` — fix(configured_feature): remove leaf blockstate keys — acacia_forest.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/acacia_forest.json`
- **Revert command** (review diff first!): `git show 10f7982d96` then `git revert 10f7982d96` if confirmed safe

### `1f12b9dada` — fix(configured_feature): remove leaf blockstate keys — patch_enoki.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json`
- **Revert command** (review diff first!): `git show 1f12b9dada` then `git revert 1f12b9dada` if confirmed safe

### `90f03532ac` — fix(configured_feature): remove leaf blockstate keys — medium_muscaria.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/medium_muscaria.json`
- **Revert command** (review diff first!): `git show 90f03532ac` then `git revert 90f03532ac` if confirmed safe

### `8e3da96c52` — fix(configured_feature): remove leaf blockstate keys — giant_omphalotus_illudens.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json`
- **Revert command** (review diff first!): `git show 8e3da96c52` then `git revert 8e3da96c52` if confirmed safe

### `3fc21640ea` — fix(configured_feature): remove leaf blockstate keys — giant_muscaria.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_muscaria.json`
- **Revert command** (review diff first!): `git show 3fc21640ea` then `git revert 3fc21640ea` if confirmed safe

### `244b954dc5` — fix(configured_feature): remove leaf blockstate keys — giant_morel.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_morel.json`
- **Revert command** (review diff first!): `git show 244b954dc5` then `git revert 244b954dc5` if confirmed safe

### `1d85e7f0c0` — fix(configured_feature): remove leaf blockstate keys — giant_matsutake.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show 1d85e7f0c0` then `git revert 1d85e7f0c0` if confirmed safe

### `5b390b42df` — fix(configured_feature): remove leaf blockstate keys — giant_enoki.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 5b390b42df` then `git revert 5b390b42df` if confirmed safe

### `912709dc1b` — fix(configured_feature): remove leaf blockstate keys — fungal_forest_red.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_red.json`
- **Revert command** (review diff first!): `git show 912709dc1b` then `git revert 912709dc1b` if confirmed safe

### `3709af1c6e` — fix(configured_feature): remove leaf blockstate keys — fungal_forest_orange.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json`
- **Revert command** (review diff first!): `git show 3709af1c6e` then `git revert 3709af1c6e` if confirmed safe

### `74555811a0` — fix(configured_feature): remove leaf blockstate keys — fungal_forest_brown.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_brown.json`
- **Revert command** (review diff first!): `git show 74555811a0` then `git revert 74555811a0` if confirmed safe

### `8b92077e9a` — fix(configured_feature): remove leaf blockstate keys — bracket_fungus.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show 8b92077e9a` then `git revert 8b92077e9a` if confirmed safe

### `497f661425` — fix(configured_feature): remove leaf blockstate keys — pale.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/pale.json`
- **Revert command** (review diff first!): `git show 497f661425` then `git revert 497f661425` if confirmed safe

### `d0832476f1` — fix(configured_feature): remove leaf blockstate keys — jungle.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/jungle.json`
- **Revert command** (review diff first!): `git show d0832476f1` then `git revert d0832476f1` if confirmed safe

### `2f35eca994` — fix(configured_feature): remove leaf blockstate keys — desert.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/desert.json`
- **Revert command** (review diff first!): `git show 2f35eca994` then `git revert 2f35eca994` if confirmed safe

### `bd892904c7` — fix(configured_feature): remove leaf blockstate keys — birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/birch.json`
- **Revert command** (review diff first!): `git show bd892904c7` then `git revert bd892904c7` if confirmed safe

### `94950a4b7f` — fix(configured_feature): remove leaf blockstate keys — acacia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/bush/acacia.json`
- **Revert command** (review diff first!): `git show 94950a4b7f` then `git revert 94950a4b7f` if confirmed safe

### `fc36cb0eb2` — fix(configured_feature): remove leaf blockstate keys — terracotta_mound_yellow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show fc36cb0eb2` then `git revert fc36cb0eb2` if confirmed safe

### `4033f11943` — fix(configured_feature): remove leaf blockstate keys — terracotta_mound_red.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show 4033f11943` then `git revert 4033f11943` if confirmed safe

### `e0ed53692e` — fix(configured_feature): remove leaf blockstate keys — tall_top.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/palm/branch/tall_top.json`
- **Revert command** (review diff first!): `git show e0ed53692e` then `git revert e0ed53692e` if confirmed safe

### `d1f431cdcb` — fix(configured_feature): remove leaf blockstate keys — trees_snowy.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/trees_snowy.json`
- **Revert command** (review diff first!): `git show d1f431cdcb` then `git revert d1f431cdcb` if confirmed safe

### `99adff9d99` — fix(configured_feature): remove leaf blockstate keys — trees_cherry.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/trees_cherry.json`
- **Revert command** (review diff first!): `git show 99adff9d99` then `git revert 99adff9d99` if confirmed safe

### `c315e9232e` — fix(configured_feature): remove leaf blockstate keys — trees_badlands.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/trees_badlands.json`
- **Revert command** (review diff first!): `git show c315e9232e` then `git revert c315e9232e` if confirmed safe

### `a4cd8b9414` — fix(configured_feature): remove leaf blockstate keys — tall_mangrove_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/tall_mangrove_checked.json`
- **Revert command** (review diff first!): `git show a4cd8b9414` then `git revert a4cd8b9414` if confirmed safe

### `e3674edb4a` — fix(configured_feature): remove leaf blockstate keys — spruce_on_snow.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/spruce_on_snow.json`
- **Revert command** (review diff first!): `git show e3674edb4a` then `git revert e3674edb4a` if confirmed safe

### `995b6ef325` — fix(configured_feature): remove leaf blockstate keys — spruce_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/spruce_checked.json`
- **Revert command** (review diff first!): `git show 995b6ef325` then `git revert 995b6ef325` if confirmed safe

### `d00a225125` — fix(configured_feature): remove leaf blockstate keys — spruce.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/spruce.json`
- **Revert command** (review diff first!): `git show d00a225125` then `git revert d00a225125` if confirmed safe

### `ba2614a0ad` — fix(configured_feature): remove leaf blockstate keys — oak_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/oak_checked.json`
- **Revert command** (review diff first!): `git show ba2614a0ad` then `git revert ba2614a0ad` if confirmed safe

### `f20f02bbd9` — fix(configured_feature): remove leaf blockstate keys — oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/oak.json`
- **Revert command** (review diff first!): `git show f20f02bbd9` then `git revert f20f02bbd9` if confirmed safe

### `718ea07613` — fix(configured_feature): remove leaf blockstate keys — mega_spruce_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/mega_spruce_checked.json`
- **Revert command** (review diff first!): `git show 718ea07613` then `git revert 718ea07613` if confirmed safe

### `a5031f8197` — fix(configured_feature): remove leaf blockstate keys — mega_pine_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/mega_pine_checked.json`
- **Revert command** (review diff first!): `git show a5031f8197` then `git revert a5031f8197` if confirmed safe

### `6a4cc7297c` — fix(configured_feature): remove leaf blockstate keys — mega_jungle_tree_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/mega_jungle_tree_checked.json`
- **Revert command** (review diff first!): `git show 6a4cc7297c` then `git revert 6a4cc7297c` if confirmed safe

### `9fd51da46d` — fix(configured_feature): remove leaf blockstate keys — mangrove_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/mangrove_checked.json`
- **Revert command** (review diff first!): `git show 9fd51da46d` then `git revert 9fd51da46d` if confirmed safe

### `dc24d8c686` — fix(configured_feature): remove leaf blockstate keys — fancy_oak_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/fancy_oak_checked.json`
- **Revert command** (review diff first!): `git show dc24d8c686` then `git revert dc24d8c686` if confirmed safe

### `ae0d18af17` — fix(configured_feature): remove leaf blockstate keys — dark_oak_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/dark_oak_checked.json`
- **Revert command** (review diff first!): `git show ae0d18af17` then `git revert ae0d18af17` if confirmed safe

### `5e0dd1900f` — fix(configured_feature): remove leaf blockstate keys — cherry_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/cherry_checked.json`
- **Revert command** (review diff first!): `git show 5e0dd1900f` then `git revert 5e0dd1900f` if confirmed safe

### `ef74f68cd8` — fix(configured_feature): remove leaf blockstate keys — cherry_bees_005.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/cherry_bees_005.json`
- **Revert command** (review diff first!): `git show ef74f68cd8` then `git revert ef74f68cd8` if confirmed safe

### `f7f5f22545` — fix(configured_feature): remove leaf blockstate keys — birch_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/birch_checked.json`
- **Revert command** (review diff first!): `git show f7f5f22545` then `git revert f7f5f22545` if confirmed safe

### `5eddb35569` — fix(configured_feature): remove leaf blockstate keys — acacia_checked.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/acacia_checked.json`
- **Revert command** (review diff first!): `git show 5eddb35569` then `git revert 5eddb35569` if confirmed safe

### `9fe8c24b53` — fix(configured_feature): remove leaf blockstate keys — acacia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/placed_feature/acacia.json`
- **Revert command** (review diff first!): `git show 9fe8c24b53` then `git revert 9fe8c24b53` if confirmed safe

### `a41ebb6ade` — fix(configured_feature): remove leaf blockstate keys — tall_mangrove.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/tall_mangrove.json`
- **Revert command** (review diff first!): `git show a41ebb6ade` then `git revert a41ebb6ade` if confirmed safe

### `619b7fd6bd` — fix(configured_feature): remove leaf blockstate keys — oak_bees_005.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/oak_bees_005.json`
- **Revert command** (review diff first!): `git show 619b7fd6bd` then `git revert 619b7fd6bd` if confirmed safe

### `8711cbe229` — fix(configured_feature): remove leaf blockstate keys — oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/oak.json`
- **Revert command** (review diff first!): `git show 8711cbe229` then `git revert 8711cbe229` if confirmed safe

### `525786fd84` — fix(configured_feature): remove leaf blockstate keys — mangrove.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/mangrove.json`
- **Revert command** (review diff first!): `git show 525786fd84` then `git revert 525786fd84` if confirmed safe

### `f5567db7b6` — fix(configured_feature): remove leaf blockstate keys — fancy_oak_bees_005.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/fancy_oak_bees_005.json`
- **Revert command** (review diff first!): `git show f5567db7b6` then `git revert f5567db7b6` if confirmed safe

### `647fbbd11a` — fix(configured_feature): remove leaf blockstate keys — fancy_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/fancy_oak.json`
- **Revert command** (review diff first!): `git show 647fbbd11a` then `git revert 647fbbd11a` if confirmed safe

### `276afcf6e5` — fix(configured_feature): remove leaf blockstate keys — cherry_bees_005.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/cherry_bees_005.json`
- **Revert command** (review diff first!): `git show 276afcf6e5` then `git revert 276afcf6e5` if confirmed safe

### `db3944dc3f` — fix(configured_feature): remove leaf blockstate keys — cherry.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/cherry.json`
- **Revert command** (review diff first!): `git show db3944dc3f` then `git revert db3944dc3f` if confirmed safe

### `aeb64ba927` — fix(configured_feature): remove leaf blockstate keys — birch_bees_005.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/birch_bees_005.json`
- **Revert command** (review diff first!): `git show aeb64ba927` then `git revert aeb64ba927` if confirmed safe

### `b11e71aafe` — fix(configured_feature): remove leaf blockstate keys — birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/birch.json`
- **Revert command** (review diff first!): `git show b11e71aafe` then `git revert b11e71aafe` if confirmed safe

### `2246e0d132` — fix(configured_feature): remove leaf blockstate keys — azalea_tree.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/azalea_tree.json`
- **Revert command** (review diff first!): `git show 2246e0d132` then `git revert 2246e0d132` if confirmed safe

### `058a42dd15` — fix(configured_feature): remove leaf blockstate keys — acacia.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/minecraft/worldgen/configured_feature/acacia.json`
- **Revert command** (review diff first!): `git show 058a42dd15` then `git revert 058a42dd15` if confirmed safe

### `fddabc0c3b` — fix(configured_feature): remove dirt_provider and force_dirt — savanna_mossy.json

- **Removed debunked keys**: heightmap
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/savanna_mossy.json`
- **Revert command** (review diff first!): `git show fddabc0c3b` then `git revert fddabc0c3b` if confirmed safe

### `fc18a5eea0` — fix(configured_feature): remove dirt_provider and force_dirt — cherry_maple.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_maple.json`
- **Revert command** (review diff first!): `git show fc18a5eea0` then `git revert fc18a5eea0` if confirmed safe

### `b7f3d40e3c` — fix(configured_feature): remove dirt_provider and force_dirt — white_bracket_fungi.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json`
- **Revert command** (review diff first!): `git show b7f3d40e3c` then `git revert b7f3d40e3c` if confirmed safe

### `e9a7ebdfc0` — fix(configured_feature): remove dirt_provider and force_dirt — fungal_weeping_growths.json

- **Removed debunked keys**: heightmap, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_weeping_growths.json`
- **Revert command** (review diff first!): `git show e9a7ebdfc0` then `git revert e9a7ebdfc0` if confirmed safe

### `1c91a1f2bf` — fix(configured_feature): remove dirt_provider and force_dirt — fungal_powder_spores.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json`
- **Revert command** (review diff first!): `git show 1c91a1f2bf` then `git revert 1c91a1f2bf` if confirmed safe

### `451538ca3b` — fix(configured_feature): remove dirt_provider and force_dirt — fungal_moss_sprouts.json

- **Removed debunked keys**: heightmap, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_moss_sprouts.json`
- **Revert command** (review diff first!): `git show 451538ca3b` then `git revert 451538ca3b` if confirmed safe

### `5241ea5368` — fix(configured_feature): remove dirt_provider and force_dirt — fungal_blood_woods.json

- **Removed debunked keys**: snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_blood_woods.json`
- **Revert command** (review diff first!): `git show 5241ea5368` then `git revert 5241ea5368` if confirmed safe

### `db1673218a` — fix(configured_feature): remove dirt_provider and force_dirt — cherry_maple_snowy.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_maple_snowy.json`
- **Revert command** (review diff first!): `git show db1673218a` then `git revert db1673218a` if confirmed safe

### `54e6dcb3e1` — fix(configured_feature): remove dirt_provider and force_dirt — coastal_palm_west.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_west.json`
- **Revert command** (review diff first!): `git show 54e6dcb3e1` then `git revert 54e6dcb3e1` if confirmed safe

### `c8f470718a` — fix(configured_feature): remove dirt_provider and force_dirt — coastal_palm_south.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_south.json`
- **Revert command** (review diff first!): `git show c8f470718a` then `git revert c8f470718a` if confirmed safe

### `5ec7723e85` — fix(configured_feature): remove dirt_provider and force_dirt — coastal_palm_north.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_north.json`
- **Revert command** (review diff first!): `git show 5ec7723e85` then `git revert 5ec7723e85` if confirmed safe

### `66430dbc95` — fix(configured_feature): remove dirt_provider and force_dirt — coastal_palm_east.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/palm/coastal_palm_east.json`
- **Revert command** (review diff first!): `git show 66430dbc95` then `git revert 66430dbc95` if confirmed safe

### `d6986dc0b5` — fix(configured_feature): remove dirt_provider and force_dirt — young_mega_jungle.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json`
- **Revert command** (review diff first!): `git show d6986dc0b5` then `git revert d6986dc0b5` if confirmed safe

### `f30bf27605` — fix(configured_feature): remove dirt_provider and force_dirt — young_kapok.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json`
- **Revert command** (review diff first!): `git show f30bf27605` then `git revert f30bf27605` if confirmed safe

### `b80c3da440` — fix(configured_feature): remove dirt_provider and force_dirt — young_brazilwood.json

- **Removed debunked keys**: can_grow_through, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json`
- **Revert command** (review diff first!): `git show b80c3da440` then `git revert b80c3da440` if confirmed safe

### `0134e6f73a` — fix(configured_feature): remove dirt_provider and force_dirt — tundra_spruce.json

- **Removed debunked keys**: persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_spruce.json`
- **Revert command** (review diff first!): `git show 0134e6f73a` then `git revert 0134e6f73a` if confirmed safe

### `9a5dde7d13` — fix(configured_feature): remove dirt_provider and force_dirt — tundra_bush.json

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/tundra_bush.json`
- **Revert command** (review diff first!): `git show 9a5dde7d13` then `git revert 9a5dde7d13` if confirmed safe

### `d010c122ad` — fix(configured_feature): remove dirt_provider and force_dirt — swamp_gum.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json`
- **Revert command** (review diff first!): `git show d010c122ad` then `git revert d010c122ad` if confirmed safe

### `bf11137444` — fix(configured_feature): remove dirt_provider and force_dirt — swamp_forest_oak.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json`
- **Revert command** (review diff first!): `git show bf11137444` then `git revert bf11137444` if confirmed safe

### `07edbd9593` — fix(configured_feature): remove dirt_provider and force_dirt — swamp_forest_birch.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json`
- **Revert command** (review diff first!): `git show 07edbd9593` then `git revert 07edbd9593` if confirmed safe

### `a9ac886c6e` — fix(configured_feature): remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show a9ac886c6e` then `git revert a9ac886c6e` if confirmed safe

### `4fcfbab258` — fix(configured_feature): remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 4fcfbab258` then `git revert 4fcfbab258` if confirmed safe

### `f580135f21` — fix(configured_feature): remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show f580135f21` then `git revert f580135f21` if confirmed safe

### `7a78612932` — fix(configured_feature): remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 7a78612932` then `git revert 7a78612932` if confirmed safe

### `c80a740667` — fix(configured_feature): remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show c80a740667` then `git revert c80a740667` if confirmed safe

### `ece50a2ec2` — fix(configured_feature): remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show ece50a2ec2` then `git revert ece50a2ec2` if confirmed safe

### `f3f1148d42` — fix(configured_feature): remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show f3f1148d42` then `git revert f3f1148d42` if confirmed safe

### `a0dcb47b55` — fix(configured_feature): remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show a0dcb47b55` then `git revert a0dcb47b55` if confirmed safe

### `93bb916e11` — fix(configured_feature): remove dirt_provider and force_dirt — sclerophylous_tall.json

- **Removed debunked keys**: heightmap, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/sclerophylous_tall.json`
- **Revert command** (review diff first!): `git show 93bb916e11` then `git revert 93bb916e11` if confirmed safe

### `7a2baf7b34` — fix(configured_feature): remove dirt_provider and force_dirt — ponderosa_pine.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_pine.json`
- **Revert command** (review diff first!): `git show 7a2baf7b34` then `git revert 7a2baf7b34` if confirmed safe

### `a9cdec4340` — fix(configured_feature): remove dirt_provider and force_dirt — pine.json

- **Removed debunked keys**: snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pine.json`
- **Revert command** (review diff first!): `git show a9cdec4340` then `git revert a9cdec4340` if confirmed safe

### `e9ae095b04` — fix(configured_feature): remove dirt_provider and force_dirt — pandanus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json`
- **Revert command** (review diff first!): `git show e9ae095b04` then `git revert e9ae095b04` if confirmed safe

### `e65b27a686` — fix(configured_feature): remove dirt_provider and force_dirt — mega_jungle.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json`
- **Revert command** (review diff first!): `git show e65b27a686` then `git revert e65b27a686` if confirmed safe

### `f70ac35335` — fix(configured_feature): remove dirt_provider and force_dirt — maple_tall.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/maple_tall.json`
- **Revert command** (review diff first!): `git show f70ac35335` then `git revert f70ac35335` if confirmed safe

### `a57a195585` — fix(configured_feature): remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_west.json`
- **Revert command** (review diff first!): `git show a57a195585` then `git revert a57a195585` if confirmed safe

### `4bddf3ff56` — fix(configured_feature): remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_south.json`
- **Revert command** (review diff first!): `git show 4bddf3ff56` then `git revert 4bddf3ff56` if confirmed safe

### `e8fd623f4d` — fix(configured_feature): remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_north.json`
- **Revert command** (review diff first!): `git show e8fd623f4d` then `git revert e8fd623f4d` if confirmed safe

### `e6a087e2bf` — fix(configured_feature): remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/2_east.json`
- **Revert command** (review diff first!): `git show e6a087e2bf` then `git revert e6a087e2bf` if confirmed safe

### `a54d78e997` — fix(configured_feature): remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_west.json`
- **Revert command** (review diff first!): `git show a54d78e997` then `git revert a54d78e997` if confirmed safe

### `9dff1e7a7a` — fix(configured_feature): remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_south.json`
- **Revert command** (review diff first!): `git show 9dff1e7a7a` then `git revert 9dff1e7a7a` if confirmed safe

### `ea64f909b7` — fix(configured_feature): remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_north.json`
- **Revert command** (review diff first!): `git show ea64f909b7` then `git revert ea64f909b7` if confirmed safe

### `c9d999300d` — fix(configured_feature): remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/larch/branch/1_east.json`
- **Revert command** (review diff first!): `git show c9d999300d` then `git revert c9d999300d` if confirmed safe

### `5b360db07c` — fix(configured_feature): remove dirt_provider and force_dirt — kapok.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json`
- **Revert command** (review diff first!): `git show 5b360db07c` then `git revert 5b360db07c` if confirmed safe

### `15f40db567` — fix(configured_feature): remove dirt_provider and force_dirt — jungle_mangrove.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json`
- **Revert command** (review diff first!): `git show 15f40db567` then `git revert 15f40db567` if confirmed safe

### `5a3a29a40f` — fix(configured_feature): remove dirt_provider and force_dirt — 9.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json`
- **Revert command** (review diff first!): `git show 5a3a29a40f` then `git revert 5a3a29a40f` if confirmed safe

### `3ee747aa20` — fix(configured_feature): remove dirt_provider and force_dirt — 8.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/8.json`
- **Revert command** (review diff first!): `git show 3ee747aa20` then `git revert 3ee747aa20` if confirmed safe

### `18bb033340` — fix(configured_feature): remove dirt_provider and force_dirt — 7.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/7.json`
- **Revert command** (review diff first!): `git show 18bb033340` then `git revert 18bb033340` if confirmed safe

### `98a45bf499` — fix(configured_feature): remove dirt_provider and force_dirt — 6.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/6.json`
- **Revert command** (review diff first!): `git show 98a45bf499` then `git revert 98a45bf499` if confirmed safe

### `a8eddf9eee` — fix(configured_feature): remove dirt_provider and force_dirt — 10.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/10.json`
- **Revert command** (review diff first!): `git show a8eddf9eee` then `git revert a8eddf9eee` if confirmed safe

### `0b26d1e253` — fix(configured_feature): remove dirt_provider and force_dirt — 5.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/5.json`
- **Revert command** (review diff first!): `git show 0b26d1e253` then `git revert 0b26d1e253` if confirmed safe

### `e935f3dfea` — fix(configured_feature): remove dirt_provider and force_dirt — 4.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/4.json`
- **Revert command** (review diff first!): `git show e935f3dfea` then `git revert e935f3dfea` if confirmed safe

### `ad3166c237` — fix(configured_feature): remove dirt_provider and force_dirt — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/3.json`
- **Revert command** (review diff first!): `git show ad3166c237` then `git revert ad3166c237` if confirmed safe

### `1150aba6df` — fix(configured_feature): remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/2.json`
- **Revert command** (review diff first!): `git show 1150aba6df` then `git revert 1150aba6df` if confirmed safe

### `16b4fab577` — fix(configured_feature): remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/1.json`
- **Revert command** (review diff first!): `git show 16b4fab577` then `git revert 16b4fab577` if confirmed safe

### `3be3936186` — fix(configured_feature): remove dirt_provider and force_dirt — branch_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_west.json`
- **Revert command** (review diff first!): `git show 3be3936186` then `git revert 3be3936186` if confirmed safe

### `d0987f1358` — fix(configured_feature): remove dirt_provider and force_dirt — branch_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_south.json`
- **Revert command** (review diff first!): `git show d0987f1358` then `git revert d0987f1358` if confirmed safe

### `82f5091319` — fix(configured_feature): remove dirt_provider and force_dirt — branch_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_north.json`
- **Revert command** (review diff first!): `git show 82f5091319` then `git revert 82f5091319` if confirmed safe

### `3e8ae4ce5a` — fix(configured_feature): remove dirt_provider and force_dirt — branch_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/branch_east.json`
- **Revert command** (review diff first!): `git show 3e8ae4ce5a` then `git revert 3e8ae4ce5a` if confirmed safe

### `838324ee32` — fix(configured_feature): remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/2.json`
- **Revert command** (review diff first!): `git show 838324ee32` then `git revert 838324ee32` if confirmed safe

### `a1373b6ba6` — fix(configured_feature): remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/1.json`
- **Revert command** (review diff first!): `git show a1373b6ba6` then `git revert a1373b6ba6` if confirmed safe

### `3e9e2f0475` — fix(configured_feature): remove dirt_provider and force_dirt — fir_tall.json

- **Removed debunked keys**: persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fir_tall.json`
- **Revert command** (review diff first!): `git show 3e9e2f0475` then `git revert 3e9e2f0475` if confirmed safe

### `97d2632729` — fix(configured_feature): remove dirt_provider and force_dirt — fir_medium.json

- **Removed debunked keys**: persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/fir_medium.json`
- **Revert command** (review diff first!): `git show 97d2632729` then `git revert 97d2632729` if confirmed safe

### `f3a8d4e6a2` — fix(configured_feature): remove dirt_provider and force_dirt — eucalyptus_deanei_white.json

- **Removed debunked keys**: can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json`
- **Revert command** (review diff first!): `git show f3a8d4e6a2` then `git revert f3a8d4e6a2` if confirmed safe

### `66147fe952` — fix(configured_feature): remove dirt_provider and force_dirt — elephant_bamboo_tropical_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json`
- **Revert command** (review diff first!): `git show 66147fe952` then `git revert 66147fe952` if confirmed safe

### `94ad4a9a4b` — fix(configured_feature): remove dirt_provider and force_dirt — elephant_bamboo_tropical.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json`
- **Revert command** (review diff first!): `git show 94ad4a9a4b` then `git revert 94ad4a9a4b` if confirmed safe

### `92e18ea901` — fix(configured_feature): remove dirt_provider and force_dirt — elephant_bamboo_temperate_gold.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json`
- **Revert command** (review diff first!): `git show 92e18ea901` then `git revert 92e18ea901` if confirmed safe

### `5201cc1506` — fix(configured_feature): remove dirt_provider and force_dirt — elephant_bamboo_temperate.json

- **Removed debunked keys**: extra_branch_steps, extra_branch_length, place_branch_per_log_probability, can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json`
- **Revert command** (review diff first!): `git show 5201cc1506` then `git revert 5201cc1506` if confirmed safe

### `2e7f1c388d` — fix(configured_feature): remove dirt_provider and force_dirt — 2_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_west.json`
- **Revert command** (review diff first!): `git show 2e7f1c388d` then `git revert 2e7f1c388d` if confirmed safe

### `8b5d551cd2` — fix(configured_feature): remove dirt_provider and force_dirt — 2_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_south.json`
- **Revert command** (review diff first!): `git show 8b5d551cd2` then `git revert 8b5d551cd2` if confirmed safe

### `4f4374975b` — fix(configured_feature): remove dirt_provider and force_dirt — 2_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_north.json`
- **Revert command** (review diff first!): `git show 4f4374975b` then `git revert 4f4374975b` if confirmed safe

### `71b36dae46` — fix(configured_feature): remove dirt_provider and force_dirt — 2_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/2_east.json`
- **Revert command** (review diff first!): `git show 71b36dae46` then `git revert 71b36dae46` if confirmed safe

### `6ef771a1a6` — fix(configured_feature): remove dirt_provider and force_dirt — 1_west.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_west.json`
- **Revert command** (review diff first!): `git show 6ef771a1a6` then `git revert 6ef771a1a6` if confirmed safe

### `25dc430902` — fix(configured_feature): remove dirt_provider and force_dirt — 1_south.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_south.json`
- **Revert command** (review diff first!): `git show 25dc430902` then `git revert 25dc430902` if confirmed safe

### `221092e47a` — fix(configured_feature): remove dirt_provider and force_dirt — 1_north.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_north.json`
- **Revert command** (review diff first!): `git show 221092e47a` then `git revert 221092e47a` if confirmed safe

### `9abc69dc7a` — fix(configured_feature): remove dirt_provider and force_dirt — 1_east.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/dead_spruce/branch/1_east.json`
- **Revert command** (review diff first!): `git show 9abc69dc7a` then `git revert 9abc69dc7a` if confirmed safe

### `8399dff553` — fix(configured_feature): remove dirt_provider and force_dirt — complex_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_2.json`
- **Revert command** (review diff first!): `git show 8399dff553` then `git revert 8399dff553` if confirmed safe

### `84f8314440` — fix(configured_feature): remove dirt_provider and force_dirt — complex_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json`
- **Revert command** (review diff first!): `git show 84f8314440` then `git revert 84f8314440` if confirmed safe

### `79a8a4e572` — fix(configured_feature): remove dirt_provider and force_dirt — complex_dark_oak_2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_2.json`
- **Revert command** (review diff first!): `git show 79a8a4e572` then `git revert 79a8a4e572` if confirmed safe

### `1680dfe2de` — fix(configured_feature): remove dirt_provider and force_dirt — complex_dark_oak_1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json`
- **Revert command** (review diff first!): `git show 1680dfe2de` then `git revert 1680dfe2de` if confirmed safe

### `e4c93ac33e` — fix(configured_feature): remove dirt_provider and force_dirt — cold_pine_medium.json

- **Removed debunked keys**: persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/cold_pine_medium.json`
- **Revert command** (review diff first!): `git show e4c93ac33e` then `git revert e4c93ac33e` if confirmed safe

### `20a27488ed` — fix(configured_feature): remove dirt_provider and force_dirt — brazilwood.json

- **Removed debunked keys**: can_grow_through, snowy, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json`
- **Revert command** (review diff first!): `git show 20a27488ed` then `git revert 20a27488ed` if confirmed safe

### `a5e2bc992e` — fix(configured_feature): remove dirt_provider and force_dirt — birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/birch.json`
- **Revert command** (review diff first!): `git show a5e2bc992e` then `git revert a5e2bc992e` if confirmed safe

### `c0a2bb443a` — fix(configured_feature): remove dirt_provider and force_dirt — 3.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/3.json`
- **Revert command** (review diff first!): `git show c0a2bb443a` then `git revert c0a2bb443a` if confirmed safe

### `476cde42fb` — fix(configured_feature): remove dirt_provider and force_dirt — 2.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/2.json`
- **Revert command** (review diff first!): `git show 476cde42fb` then `git revert 476cde42fb` if confirmed safe

### `e613f47e7d` — fix(configured_feature): remove dirt_provider and force_dirt — 1.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/big_spruce/1.json`
- **Revert command** (review diff first!): `git show e613f47e7d` then `git revert e613f47e7d` if confirmed safe

### `efe5d41519` — fix(configured_feature): remove dirt_provider and force_dirt — bayou_cypress_surface_2.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json`
- **Revert command** (review diff first!): `git show efe5d41519` then `git revert efe5d41519` if confirmed safe

### `c756351e52` — fix(configured_feature): remove dirt_provider and force_dirt — bayou_cypress_surface.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json`
- **Revert command** (review diff first!): `git show c756351e52` then `git revert c756351e52` if confirmed safe

### `3e90f5d44d` — fix(configured_feature): remove dirt_provider and force_dirt — bayou_cypress_shallow.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json`
- **Revert command** (review diff first!): `git show 3e90f5d44d` then `git revert 3e90f5d44d` if confirmed safe

### `276cd77e4b` — fix(configured_feature): remove dirt_provider and force_dirt — bayou_cypress_middle.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json`
- **Revert command** (review diff first!): `git show 276cd77e4b` then `git revert 276cd77e4b` if confirmed safe

### `56f03075d7` — fix(configured_feature): remove dirt_provider and force_dirt — bayou_cypress_deep.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json`
- **Revert command** (review diff first!): `git show 56f03075d7` then `git revert 56f03075d7` if confirmed safe

### `882517271e` — fix(configured_feature): remove dirt_provider and force_dirt — baobab_short.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/baobab_short.json`
- **Revert command** (review diff first!): `git show 882517271e` then `git revert 882517271e` if confirmed safe

### `f89f238089` — fix(configured_feature): remove dirt_provider and force_dirt — bamboo_palm.json

- **Removed debunked keys**: snowy
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bamboo_palm.json`
- **Revert command** (review diff first!): `git show f89f238089` then `git revert f89f238089` if confirmed safe

### `1739a05337` — fix(configured_feature): remove dirt_provider and force_dirt — azalea_conifer.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_conifer.json`
- **Revert command** (review diff first!): `git show 1739a05337` then `git revert 1739a05337` if confirmed safe

### `ac3a5d2512` — fix(configured_feature): remove dirt_provider and force_dirt — azalea_birch.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/azalea_birch.json`
- **Revert command** (review diff first!): `git show ac3a5d2512` then `git revert ac3a5d2512` if confirmed safe

### `5df8ee463e` — fix(configured_feature): remove dirt_provider and force_dirt — aspen_leaf_litter.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen_leaf_litter.json`
- **Revert command** (review diff first!): `git show 5df8ee463e` then `git revert 5df8ee463e` if confirmed safe

### `ad5c59b2c1` — fix(configured_feature): remove dirt_provider and force_dirt — aspen.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/aspen.json`
- **Revert command** (review diff first!): `git show ad5c59b2c1` then `git revert ad5c59b2c1` if confirmed safe

### `faf4a5f4bf` — fix(configured_feature): remove dirt_provider and force_dirt — ancient_dark_oak.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dark_oak.json`
- **Revert command** (review diff first!): `git show faf4a5f4bf` then `git revert faf4a5f4bf` if confirmed safe

### `8005ee1fe9` — fix(configured_feature): remove dirt_provider and force_dirt — acacia_plains.json

- **Removed debunked keys**: waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/acacia_plains.json`
- **Revert command** (review diff first!): `git show 8005ee1fe9` then `git revert 8005ee1fe9` if confirmed safe

### `cee76be2c4` — fix(configured_feature): remove dirt_provider and force_dirt — giant_matsutake.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_matsutake.json`
- **Revert command** (review diff first!): `git show cee76be2c4` then `git revert cee76be2c4` if confirmed safe

### `99ce7647de` — fix(configured_feature): remove dirt_provider and force_dirt — giant_enoki.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/giant_enoki.json`
- **Revert command** (review diff first!): `git show 99ce7647de` then `git revert 99ce7647de` if confirmed safe

### `8aa584d830` — fix(configured_feature): remove dirt_provider and force_dirt — bracket_fungus.json

- **Removed debunked keys**: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks, waterlogged
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/bracket_fungus.json`
- **Revert command** (review diff first!): `git show 8aa584d830` then `git revert 8aa584d830` if confirmed safe

### `c3a9fd4c94` — fix(configured_feature): remove dirt_provider and force_dirt — terracotta_mound_yellow.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json`
- **Revert command** (review diff first!): `git show c3a9fd4c94` then `git revert c3a9fd4c94` if confirmed safe

### `25e777f3a0` — fix(configured_feature): remove dirt_provider and force_dirt — terracotta_mound_red.json

- **Removed debunked keys**: can_grow_through, waterlogged, persistent, distance
- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: dirt_provider, force_dirt — review carefully before reverting, this commit may have mixed a real fix with a debunked one
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json`
- **Revert command** (review diff first!): `git show 25e777f3a0` then `git revert 25e777f3a0` if confirmed safe

### `56fc160f94` — Fix 2: Unwrap complex random_patch: desert_bushes.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/desert_bushes.json`
- **Revert command** (review diff first!): `git show 56fc160f94` then `git revert 56fc160f94` if confirmed safe

### `ded29a9508` — Fix 2: Unwrap complex random_patch: bayou_pine_forest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou_pine_forest.json`
- **Revert command** (review diff first!): `git show ded29a9508` then `git revert ded29a9508` if confirmed safe

### `1e1b55e49a` — Fix 2: Unwrap complex random_patch: bayou.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou.json`
- **Revert command** (review diff first!): `git show 1e1b55e49a` then `git revert 1e1b55e49a` if confirmed safe

### `2cf277f541` — Fix 2: Unwrap complex random_patch: red_coral_tall.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/red_coral_tall.json`
- **Revert command** (review diff first!): `git show 2cf277f541` then `git revert 2cf277f541` if confirmed safe

### `a0adb723ba` — Fix 2: Unwrap complex random_patch: mangrove_swamp_dripleaves.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/mangrove_swamp_dripleaves.json`
- **Revert command** (review diff first!): `git show a0adb723ba` then `git revert a0adb723ba` if confirmed safe

### `1938b0b13e` — Fix 2: Unwrap complex random_patch: fungal_twisted_reef_vegetation.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_twisted_reef_vegetation.json`
- **Revert command** (review diff first!): `git show 1938b0b13e` then `git revert 1938b0b13e` if confirmed safe

### `0832a2ef78` — Fix 2: Unwrap complex random_patch: fungal_twisted_kelp.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_twisted_kelp.json`
- **Revert command** (review diff first!): `git show 0832a2ef78` then `git revert 0832a2ef78` if confirmed safe

### `a20874ded7` — Fix 2: Unwrap complex random_patch: fungal_sculk_growths.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_sculk_growths.json`
- **Revert command** (review diff first!): `git show a20874ded7` then `git revert a20874ded7` if confirmed safe

### `0dbeb8bac3` — Fix 2: Unwrap complex random_patch: fungal_jungle_groundcover.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_groundcover.json`
- **Revert command** (review diff first!): `git show 0dbeb8bac3` then `git revert 0dbeb8bac3` if confirmed safe

### `20faa202a8` — Fix 2: Unwrap complex random_patch: mushroom_island_plateau.json

- **Removed debunked keys**: heightmap, snowy
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/mushroom_island_plateau.json`
- **Revert command** (review diff first!): `git show 20faa202a8` then `git revert 20faa202a8` if confirmed safe

### `121aa22b45` — Fix 2: Unwrap complex random_patch: desert.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/desert.json`
- **Revert command** (review diff first!): `git show 121aa22b45` then `git revert 121aa22b45` if confirmed safe

### `a2c3226f39` — Fix 2: Unwrap complex random_patch: badlands.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/badlands.json`
- **Revert command** (review diff first!): `git show a2c3226f39` then `git revert a2c3226f39` if confirmed safe

### `8b61a0c117` — Fix 1: Convert random_offset IntProvider: old_growth_spruce_taiga.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/old_growth_spruce_taiga.json`
- **Revert command** (review diff first!): `git show 8b61a0c117` then `git revert 8b61a0c117` if confirmed safe

### `50df515056` — Fix 1: Convert random_offset IntProvider: baobab_interior.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/baobab_interior.json`
- **Revert command** (review diff first!): `git show 50df515056` then `git revert 50df515056` if confirmed safe

### `8d854ecb87` — Fix 1: Convert random_offset IntProvider: giant_taiga_edge.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/trees/giant_taiga_edge.json`
- **Revert command** (review diff first!): `git show 8d854ecb87` then `git revert 8d854ecb87` if confirmed safe

### `956378769c` — Fix 1: Convert random_offset IntProvider: mushroom_disks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/other/mushroom_disks.json`
- **Revert command** (review diff first!): `git show 956378769c` then `git revert 956378769c` if confirmed safe

### `5eef58e7fb` — Fix 1: Convert random_offset IntProvider: stone_cliffs_sheer.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/stone_cliffs_sheer.json`
- **Revert command** (review diff first!): `git show 5eef58e7fb` then `git revert 5eef58e7fb` if confirmed safe

### `4af16258c3` — Fix 1: Convert random_offset IntProvider: highland_stone_cliffs.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/highland_stone_cliffs.json`
- **Revert command** (review diff first!): `git show 4af16258c3` then `git revert 4af16258c3` if confirmed safe

### `62a73dbde1` — Fix 1: Convert random_offset IntProvider: base_wooded_badlands.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_wooded_badlands.json`
- **Revert command** (review diff first!): `git show 62a73dbde1` then `git revert 62a73dbde1` if confirmed safe

### `027c741ca8` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/base_mangrove_swamp.json`
- **Revert command** (review diff first!): `git show 027c741ca8` then `git revert 027c741ca8` if confirmed safe

### `824936b893` — Fix 1: Convert random_offset IntProvider: tepui_geodes.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_geodes.json`
- **Revert command** (review diff first!): `git show 824936b893` then `git revert 824936b893` if confirmed safe

### `80c1c0033e` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_sudd.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_sudd.json`
- **Revert command** (review diff first!): `git show 80c1c0033e` then `git revert 80c1c0033e` if confirmed safe

### `d55d5a8c6d` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_sparse_jungle.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_sparse_jungle.json`
- **Revert command** (review diff first!): `git show d55d5a8c6d` then `git revert d55d5a8c6d` if confirmed safe

### `99a0f6271b` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_savanna.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_savanna.json`
- **Revert command** (review diff first!): `git show 99a0f6271b` then `git revert 99a0f6271b` if confirmed safe

### `b0f547d33a` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_plains.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_plains.json`
- **Revert command** (review diff first!): `git show b0f547d33a` then `git revert b0f547d33a` if confirmed safe

### `d9a0e70dce` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_jungle.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_jungle.json`
- **Revert command** (review diff first!): `git show d9a0e70dce` then `git revert d9a0e70dce` if confirmed safe

### `ab335fa350` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_forest.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_forest.json`
- **Revert command** (review diff first!): `git show ab335fa350` then `git revert ab335fa350` if confirmed safe

### `b5473181b3` — Fix 1: Convert random_offset IntProvider: base_mangrove_swamp_arid.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_mangrove_swamp_arid.json`
- **Revert command** (review diff first!): `git show b5473181b3` then `git revert b5473181b3` if confirmed safe

### `9244e12d4c` — Fix 1: Convert random_offset IntProvider: base_frozen_peaks_snow.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_frozen_peaks_snow.json`
- **Revert command** (review diff first!): `git show 9244e12d4c` then `git revert 9244e12d4c` if confirmed safe

### `7cba15274a` — Fix 1: Convert random_offset IntProvider: base_frozen_peaks.json

- **Removed debunked keys**: heightmap
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/base_frozen_peaks.json`
- **Revert command** (review diff first!): `git show 7cba15274a` then `git revert 7cba15274a` if confirmed safe

### `ade948ad10` — Convert string_reference random_patch to placed_feature: melon_patch.json

- **Removed debunked keys**: heightmap
- **Files touched**: 2
  - `data/wythers/worldgen/configured_feature/vegetation/melon_patch.json`
  - `data/wythers/worldgen/placed_feature/vegetation/melon_patch.json`
- **Revert command** (review diff first!): `git show ade948ad10` then `git revert ade948ad10` if confirmed safe

### `ea34ce51d5` — Convert string_reference random_patch to placed_feature: patch_morel.json

- **Removed debunked keys**: heightmap
- **Files touched**: 2
  - `data/wythers/worldgen/configured_feature/vegetation/fungus/patch_morel.json`
  - `data/wythers/worldgen/placed_feature/vegetation/fungus/patch_morel.json`
- **Revert command** (review diff first!): `git show ea34ce51d5` then `git revert ea34ce51d5` if confirmed safe

### `59fa003e14` — Remove leaf blockstate inline keys: palm_leaves.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/part/palm_leaves.json`
- **Revert command** (review diff first!): `git show 59fa003e14` then `git revert 59fa003e14` if confirmed safe

### `16995d7807` — Remove leaf blockstate inline keys: mangrove_swamp_mangroves.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/mangrove_swamp_mangroves.json`
- **Revert command** (review diff first!): `git show 16995d7807` then `git revert 16995d7807` if confirmed safe

### `6e68762b65` — Remove leaf blockstate inline keys: mangrove_swamp_bayou_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/mangrove_swamp_bayou_2.json`
- **Revert command** (review diff first!): `git show 6e68762b65` then `git revert 6e68762b65` if confirmed safe

### `c270e09de6` — Remove leaf blockstate inline keys: mangrove_swamp_bayou.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/mangrove_swamp_bayou.json`
- **Revert command** (review diff first!): `git show c270e09de6` then `git revert c270e09de6` if confirmed safe

### `71ce5275d7` — Remove leaf blockstate inline keys: mangrove_swamp.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/mangrove_swamp.json`
- **Revert command** (review diff first!): `git show 71ce5275d7` then `git revert 71ce5275d7` if confirmed safe

### `43980308e7` — Remove leaf blockstate inline keys: jungle_river.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/trees/jungle_river.json`
- **Revert command** (review diff first!): `git show 43980308e7` then `git revert 43980308e7` if confirmed safe

### `50e1759b06` — Remove leaf blockstate inline keys: tube_worms.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/tube_worms.json`
- **Revert command** (review diff first!): `git show 50e1759b06` then `git revert 50e1759b06` if confirmed safe

### `1a5fa87188` — Remove leaf blockstate inline keys: savanna_water_plants.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/savanna_water_plants.json`
- **Revert command** (review diff first!): `git show 1a5fa87188` then `git revert 1a5fa87188` if confirmed safe

### `506bb69f49` — Remove leaf blockstate inline keys: sandy_marsh_dripleaf.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/sandy_marsh_dripleaf.json`
- **Revert command** (review diff first!): `git show 506bb69f49` then `git revert 506bb69f49` if confirmed safe

### `412e8fabc8` — Remove leaf blockstate inline keys: red_coral_tall.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/red_coral_tall.json`
- **Revert command** (review diff first!): `git show 412e8fabc8` then `git revert 412e8fabc8` if confirmed safe

### `d90951c291` — Remove leaf blockstate inline keys: red_coral.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/red_coral.json`
- **Revert command** (review diff first!): `git show d90951c291` then `git revert d90951c291` if confirmed safe

### `385c8e0d75` — Remove leaf blockstate inline keys: oasis_vegetation_moss.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/oasis_vegetation_moss.json`
- **Revert command** (review diff first!): `git show 385c8e0d75` then `git revert 385c8e0d75` if confirmed safe

### `89fd03754f` — Remove leaf blockstate inline keys: flower_cloud_forest.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/flower_cloud_forest.json`
- **Revert command** (review diff first!): `git show 89fd03754f` then `git revert 89fd03754f` if confirmed safe

### `a50edd0c12` — Remove leaf blockstate inline keys: floating_vegetation.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/floating_vegetation.json`
- **Revert command** (review diff first!): `git show a50edd0c12` then `git revert a50edd0c12` if confirmed safe

### `f78ef5a154` — Remove leaf blockstate inline keys: elephant_grass.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/elephant_grass.json`
- **Revert command** (review diff first!): `git show f78ef5a154` then `git revert f78ef5a154` if confirmed safe

### `a5eee10ba1` — Remove leaf blockstate inline keys: elephant_bamboo_cherry.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/elephant_bamboo_cherry.json`
- **Revert command** (review diff first!): `git show a5eee10ba1` then `git revert a5eee10ba1` if confirmed safe

### `3005da207f` — Remove leaf blockstate inline keys: elephant_bamboo_3.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/elephant_bamboo_3.json`
- **Revert command** (review diff first!): `git show 3005da207f` then `git revert 3005da207f` if confirmed safe

### `f49eec9c1e` — Remove leaf blockstate inline keys: elephant_bamboo_2.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/elephant_bamboo_2.json`
- **Revert command** (review diff first!): `git show f49eec9c1e` then `git revert f49eec9c1e` if confirmed safe

### `eabd7b2987` — Remove leaf blockstate inline keys: elephant_bamboo_1.json

- **Removed debunked keys**: heightmap, waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/elephant_bamboo_1.json`
- **Revert command** (review diff first!): `git show eabd7b2987` then `git revert eabd7b2987` if confirmed safe

### `552cecd773` — Remove leaf blockstate inline keys: banyan_vines.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/patch/banyan_vines.json`
- **Revert command** (review diff first!): `git show 552cecd773` then `git revert 552cecd773` if confirmed safe

### `d42e8fb9b3` — Remove leaf blockstate inline keys: fungal_sculk_growths.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_sculk_growths.json`
- **Revert command** (review diff first!): `git show d42e8fb9b3` then `git revert d42e8fb9b3` if confirmed safe

### `a8cb6f209a` — Remove leaf blockstate inline keys: fungal_glow.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_glow.json`
- **Revert command** (review diff first!): `git show a8cb6f209a` then `git revert a8cb6f209a` if confirmed safe

### `7a9268a2e1` — Remove leaf blockstate inline keys: coral_blobs.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/local/other/coral_blobs.json`
- **Revert command** (review diff first!): `git show 7a9268a2e1` then `git revert 7a9268a2e1` if confirmed safe

### `7aeb13b332` — Remove leaf blockstate inline keys: tropical_water_plants.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/patch/tropical_water_plants.json`
- **Revert command** (review diff first!): `git show 7aeb13b332` then `git revert 7aeb13b332` if confirmed safe

### `9c651bb848` — Remove leaf blockstate inline keys: tepui_plants.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/vegetation/extended/patch/tepui_plants.json`
- **Revert command** (review diff first!): `git show 9c651bb848` then `git revert 9c651bb848` if confirmed safe

### `7697c862f6` — Remove leaf blockstate inline keys: tundra_light.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/tundra_light.json`
- **Revert command** (review diff first!): `git show 7697c862f6` then `git revert 7697c862f6` if confirmed safe

### `cab8a123e2` — Remove leaf blockstate inline keys: replace_basalt_to_tuff.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_basalt_to_tuff.json`
- **Revert command** (review diff first!): `git show cab8a123e2` then `git revert cab8a123e2` if confirmed safe

### `72e2915043` — Remove leaf blockstate inline keys: replace_basalt_to_deepslate.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/replace_basalt_to_deepslate.json`
- **Revert command** (review diff first!): `git show 72e2915043` then `git revert 72e2915043` if confirmed safe

### `a97864f83d` — Remove leaf blockstate inline keys: pamukkale_pools.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/pamukkale_pools.json`
- **Revert command** (review diff first!): `git show a97864f83d` then `git revert a97864f83d` if confirmed safe

### `57ef2ae9f0` — Remove leaf blockstate inline keys: deglaciator_01.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/deglaciator_01.json`
- **Revert command** (review diff first!): `git show 57ef2ae9f0` then `git revert 57ef2ae9f0` if confirmed safe

### `1cbbfdc3f7` — Remove leaf blockstate inline keys: danakil_water.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/local/danakil_water.json`
- **Revert command** (review diff first!): `git show 1cbbfdc3f7` then `git revert 1cbbfdc3f7` if confirmed safe

### `ab5a0b2584` — Remove leaf blockstate inline keys: tepui_plants.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_plants.json`
- **Revert command** (review diff first!): `git show ab5a0b2584` then `git revert ab5a0b2584` if confirmed safe

### `2f5ae3835c` — Remove leaf blockstate inline keys: tepui_falls.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_falls.json`
- **Revert command** (review diff first!): `git show 2f5ae3835c` then `git revert 2f5ae3835c` if confirmed safe

### `bc76295b2a` — Remove leaf blockstate inline keys: tepui_crystals.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_crystals.json`
- **Revert command** (review diff first!): `git show bc76295b2a` then `git revert bc76295b2a` if confirmed safe

### `b5c16c11fd` — Remove leaf blockstate inline keys: tepui_chasms.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_chasms.json`
- **Revert command** (review diff first!): `git show b5c16c11fd` then `git revert b5c16c11fd` if confirmed safe

### `4a3f6836c7` — Remove leaf blockstate inline keys: tepui_cavern_lakes.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/feature/tepui_cavern_lakes.json`
- **Revert command** (review diff first!): `git show 4a3f6836c7` then `git revert 4a3f6836c7` if confirmed safe

### `a244ff5e20` — Remove leaf blockstate inline keys: volcanic_extinction.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/volcanic_extinction.json`
- **Revert command** (review diff first!): `git show a244ff5e20` then `git revert a244ff5e20` if confirmed safe

### `77e143d8ac` — Remove leaf blockstate inline keys: replace_basalt_to_deepslate.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/replace_basalt_to_deepslate.json`
- **Revert command** (review diff first!): `git show 77e143d8ac` then `git revert 77e143d8ac` if confirmed safe

### `ec7a024bdc` — Remove leaf blockstate inline keys: onsen_pools.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/terrain/extended/onsen_pools.json`
- **Revert command** (review diff first!): `git show ec7a024bdc` then `git revert ec7a024bdc` if confirmed safe

### `ed7ba1b217` — Remove leaf blockstate inline keys: sunflower_plains.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/sunflower_plains.json`
- **Revert command** (review diff first!): `git show ed7ba1b217` then `git revert ed7ba1b217` if confirmed safe

### `0bd823870a` — Remove leaf blockstate inline keys: cherry_grove.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/cherry_grove.json`
- **Revert command** (review diff first!): `git show 0bd823870a` then `git revert 0bd823870a` if confirmed safe

### `b8f0b89366` — Remove leaf blockstate inline keys: bamboo_jungle.json

- **Removed debunked keys**: heightmap, waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/bamboo_jungle.json`
- **Revert command** (review diff first!): `git show b8f0b89366` then `git revert b8f0b89366` if confirmed safe

### `8fb8f60965` — Remove leaf blockstate inline keys: andesite.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/road/andesite.json`
- **Revert command** (review diff first!): `git show 8fb8f60965` then `git revert 8fb8f60965` if confirmed safe

### `c3e24a5de5` — Remove leaf blockstate inline keys: paddy_leaf.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/farm/paddy_leaf.json`
- **Revert command** (review diff first!): `git show c3e24a5de5` then `git revert c3e24a5de5` if confirmed safe

### `895b2f46c9` — Remove leaf blockstate inline keys: sparse_steam.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/sparse_steam.json`
- **Revert command** (review diff first!): `git show 895b2f46c9` then `git revert 895b2f46c9` if confirmed safe

### `e490c2d4af` — Remove leaf blockstate inline keys: dense_steam.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/placed_feature/decor/dense_steam.json`
- **Revert command** (review diff first!): `git show e490c2d4af` then `git revert e490c2d4af` if confirmed safe

### `8196ab4a86` — Remove leaf blockstate inline keys: 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/5.json`
- **Revert command** (review diff first!): `git show 8196ab4a86` then `git revert 8196ab4a86` if confirmed safe

### `504991b59e` — Remove leaf blockstate inline keys: 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/4.json`
- **Revert command** (review diff first!): `git show 504991b59e` then `git revert 504991b59e` if confirmed safe

### `5040c80cbc` — Remove leaf blockstate inline keys: 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/3.json`
- **Revert command** (review diff first!): `git show 5040c80cbc` then `git revert 5040c80cbc` if confirmed safe

### `1b4fd0e1bb` — Remove leaf blockstate inline keys: 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/2.json`
- **Revert command** (review diff first!): `git show 1b4fd0e1bb` then `git revert 1b4fd0e1bb` if confirmed safe

### `8a456f8aa0` — Remove leaf blockstate inline keys: 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/roots/1.json`
- **Revert command** (review diff first!): `git show 8a456f8aa0` then `git revert 8a456f8aa0` if confirmed safe

### `edafc8bf78` — Remove leaf blockstate inline keys: 4_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_west.json`
- **Revert command** (review diff first!): `git show edafc8bf78` then `git revert edafc8bf78` if confirmed safe

### `1041bf8af3` — Remove leaf blockstate inline keys: 4_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_south.json`
- **Revert command** (review diff first!): `git show 1041bf8af3` then `git revert 1041bf8af3` if confirmed safe

### `4a71c31db7` — Remove leaf blockstate inline keys: 4_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_north.json`
- **Revert command** (review diff first!): `git show 4a71c31db7` then `git revert 4a71c31db7` if confirmed safe

### `cb927a4376` — Remove leaf blockstate inline keys: 4_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/branch/4_east.json`
- **Revert command** (review diff first!): `git show cb927a4376` then `git revert cb927a4376` if confirmed safe

### `7e7b1f0988` — Remove leaf blockstate inline keys: 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/5.json`
- **Revert command** (review diff first!): `git show 7e7b1f0988` then `git revert 7e7b1f0988` if confirmed safe

### `27ba411dcd` — Remove leaf blockstate inline keys: 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/4.json`
- **Revert command** (review diff first!): `git show 27ba411dcd` then `git revert 27ba411dcd` if confirmed safe

### `9f47105b1d` — Remove leaf blockstate inline keys: 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/3.json`
- **Revert command** (review diff first!): `git show 9f47105b1d` then `git revert 9f47105b1d` if confirmed safe

### `a8deb588ae` — Remove leaf blockstate inline keys: 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/2.json`
- **Revert command** (review diff first!): `git show a8deb588ae` then `git revert a8deb588ae` if confirmed safe

### `dff0c125a7` — Remove leaf blockstate inline keys: 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/roots/1.json`
- **Revert command** (review diff first!): `git show dff0c125a7` then `git revert dff0c125a7` if confirmed safe

### `c233ffb0be` — Remove leaf blockstate inline keys: 4_west.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_west.json`
- **Revert command** (review diff first!): `git show c233ffb0be` then `git revert c233ffb0be` if confirmed safe

### `d013852f24` — Remove leaf blockstate inline keys: 4_south.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_south.json`
- **Revert command** (review diff first!): `git show d013852f24` then `git revert d013852f24` if confirmed safe

### `a5df8235e5` — Remove leaf blockstate inline keys: 4_north.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_north.json`
- **Revert command** (review diff first!): `git show a5df8235e5` then `git revert a5df8235e5` if confirmed safe

### `703c332508` — Remove leaf blockstate inline keys: 4_east.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_sequoia/branch/4_east.json`
- **Revert command** (review diff first!): `git show 703c332508` then `git revert 703c332508` if confirmed safe

### `1d25270b8d` — Remove leaf blockstate inline keys: extra_leaf.json

- **Removed debunked keys**: waterlogged, persistent, distance
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle/extra_leaf.json`
- **Revert command** (review diff first!): `git show 1d25270b8d` then `git revert 1d25270b8d` if confirmed safe

### `d43f0fea54` — Remove leaf blockstate inline keys: bayou.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/tree/bayou.json`
- **Revert command** (review diff first!): `git show d43f0fea54` then `git revert d43f0fea54` if confirmed safe

### `d7349c68ce` — Remove leaf blockstate inline keys: patch_dead_corals_on_gravel.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch_dead_corals_on_gravel.json`
- **Revert command** (review diff first!): `git show d7349c68ce` then `git revert d7349c68ce` if confirmed safe

### `b84c1a5ce4` — Remove leaf blockstate inline keys: waterlily_pink.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_pink.json`
- **Revert command** (review diff first!): `git show b84c1a5ce4` then `git revert b84c1a5ce4` if confirmed safe

### `e54f9e73f1` — Remove leaf blockstate inline keys: waterlily_magenta.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_magenta.json`
- **Revert command** (review diff first!): `git show e54f9e73f1` then `git revert e54f9e73f1` if confirmed safe

### `ab6e62c70d` — Remove leaf blockstate inline keys: waterlily_blue.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/waterlily_blue.json`
- **Revert command** (review diff first!): `git show ab6e62c70d` then `git revert ab6e62c70d` if confirmed safe

### `0a074ee79a` — Remove leaf blockstate inline keys: water_grass_with_lily.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_lily.json`
- **Revert command** (review diff first!): `git show 0a074ee79a` then `git revert 0a074ee79a` if confirmed safe

### `94ee6baead` — Remove leaf blockstate inline keys: water_grass_with_blue_orchids.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_blue_orchids.json`
- **Revert command** (review diff first!): `git show 94ee6baead` then `git revert 94ee6baead` if confirmed safe

### `9d47507558` — Remove leaf blockstate inline keys: water_grass_with_azure_bluets.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass_with_azure_bluets.json`
- **Revert command** (review diff first!): `git show 9d47507558` then `git revert 9d47507558` if confirmed safe

### `12b5c424f3` — Remove leaf blockstate inline keys: water_grass.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/water_grass.json`
- **Revert command** (review diff first!): `git show 12b5c424f3` then `git revert 12b5c424f3` if confirmed safe

### `aac65b1f0d` — Remove leaf blockstate inline keys: oasis_pool.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/patch/oasis_pool.json`
- **Revert command** (review diff first!): `git show aac65b1f0d` then `git revert aac65b1f0d` if confirmed safe

### `c8a7a605a1` — Remove leaf blockstate inline keys: agave_spiking_large.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_spiking_large.json`
- **Revert command** (review diff first!): `git show c8a7a605a1` then `git revert c8a7a605a1` if confirmed safe

### `780f0c700d` — Remove leaf blockstate inline keys: agave_spiking.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_spiking.json`
- **Revert command** (review diff first!): `git show 780f0c700d` then `git revert 780f0c700d` if confirmed safe

### `f26c591912` — Remove leaf blockstate inline keys: agave_flowering_large.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_large.json`
- **Revert command** (review diff first!): `git show f26c591912` then `git revert f26c591912` if confirmed safe

### `c96a5a2f88` — Remove leaf blockstate inline keys: agave_flowering_dead.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_dead.json`
- **Revert command** (review diff first!): `git show c96a5a2f88` then `git revert c96a5a2f88` if confirmed safe

### `f0e44f2ebb` — Remove leaf blockstate inline keys: agave_flowering_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering_2.json`
- **Revert command** (review diff first!): `git show f0e44f2ebb` then `git revert f0e44f2ebb` if confirmed safe

### `afb7ada134` — Remove leaf blockstate inline keys: agave_flowering.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave_flowering.json`
- **Revert command** (review diff first!): `git show afb7ada134` then `git revert afb7ada134` if confirmed safe

### `74858c4802` — Remove leaf blockstate inline keys: agave.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/other/agave.json`
- **Revert command** (review diff first!): `git show 74858c4802` then `git revert 74858c4802` if confirmed safe

### `92ebf07375` — Remove leaf blockstate inline keys: groundsel_leaves.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/groundsel_leaves.json`
- **Revert command** (review diff first!): `git show 92ebf07375` then `git revert 92ebf07375` if confirmed safe

### `1011709d41` — Remove leaf blockstate inline keys: twisting_rose.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/twisting_rose.json`
- **Revert command** (review diff first!): `git show 1011709d41` then `git revert 1011709d41` if confirmed safe

### `8fec4c0fce` — Remove leaf blockstate inline keys: spanish_moss.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/spanish_moss.json`
- **Revert command** (review diff first!): `git show 8fec4c0fce` then `git revert 8fec4c0fce` if confirmed safe

### `7ae283b076` — Remove leaf blockstate inline keys: 9.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/9.json`
- **Revert command** (review diff first!): `git show 7ae283b076` then `git revert 7ae283b076` if confirmed safe

### `b87af8498c` — Remove leaf blockstate inline keys: 8.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/8.json`
- **Revert command** (review diff first!): `git show b87af8498c` then `git revert b87af8498c` if confirmed safe

### `a900a0a522` — Remove leaf blockstate inline keys: 7.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/7.json`
- **Revert command** (review diff first!): `git show a900a0a522` then `git revert a900a0a522` if confirmed safe

### `8194ed5a04` — Remove leaf blockstate inline keys: 6.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/6.json`
- **Revert command** (review diff first!): `git show 8194ed5a04` then `git revert 8194ed5a04` if confirmed safe

### `d77b0142f0` — Remove leaf blockstate inline keys: 5.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/5.json`
- **Revert command** (review diff first!): `git show d77b0142f0` then `git revert d77b0142f0` if confirmed safe

### `1647d9ff9b` — Remove leaf blockstate inline keys: 4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/4.json`
- **Revert command** (review diff first!): `git show 1647d9ff9b` then `git revert 1647d9ff9b` if confirmed safe

### `47bd017c25` — Remove leaf blockstate inline keys: 3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/3.json`
- **Revert command** (review diff first!): `git show 47bd017c25` then `git revert 47bd017c25` if confirmed safe

### `2621e0ab94` — Remove leaf blockstate inline keys: 2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/2.json`
- **Revert command** (review diff first!): `git show 2621e0ab94` then `git revert 2621e0ab94` if confirmed safe

### `9205afaeab` — Remove leaf blockstate inline keys: 14.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/14.json`
- **Revert command** (review diff first!): `git show 9205afaeab` then `git revert 9205afaeab` if confirmed safe

### `783b91c8f9` — Remove leaf blockstate inline keys: 13.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/13.json`
- **Revert command** (review diff first!): `git show 783b91c8f9` then `git revert 783b91c8f9` if confirmed safe

### `5ba6cd56fe` — Remove leaf blockstate inline keys: 12.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/12.json`
- **Revert command** (review diff first!): `git show 5ba6cd56fe` then `git revert 5ba6cd56fe` if confirmed safe

### `922d8a6d08` — Remove leaf blockstate inline keys: 11.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/11.json`
- **Revert command** (review diff first!): `git show 922d8a6d08` then `git revert 922d8a6d08` if confirmed safe

### `295bb04cb4` — Remove leaf blockstate inline keys: 10.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/10.json`
- **Revert command** (review diff first!): `git show 295bb04cb4` then `git revert 295bb04cb4` if confirmed safe

### `7dde58e21e` — Remove leaf blockstate inline keys: 1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/saguaro/1.json`
- **Revert command** (review diff first!): `git show 7dde58e21e` then `git revert 7dde58e21e` if confirmed safe

### `53ccc7a4ac` — Remove leaf blockstate inline keys: mini_dripleaf.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/mini_dripleaf.json`
- **Revert command** (review diff first!): `git show 53ccc7a4ac` then `git revert 53ccc7a4ac` if confirmed safe

### `d65783bd65` — Remove leaf blockstate inline keys: floating_vegetation_mat_dripleaf_west.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/floating_vegetation_mat_dripleaf_west.json`
- **Revert command** (review diff first!): `git show d65783bd65` then `git revert d65783bd65` if confirmed safe

### `d8670d9047` — Remove leaf blockstate inline keys: floating_vegetation_mat_dripleaf_south.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/floating_vegetation_mat_dripleaf_south.json`
- **Revert command** (review diff first!): `git show d8670d9047` then `git revert d8670d9047` if confirmed safe

### `169f7f6dfe` — Remove leaf blockstate inline keys: floating_vegetation_mat_dripleaf_north.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/floating_vegetation_mat_dripleaf_north.json`
- **Revert command** (review diff first!): `git show 169f7f6dfe` then `git revert 169f7f6dfe` if confirmed safe

### `552f5a189c` — Remove leaf blockstate inline keys: floating_vegetation_mat_dripleaf_east.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/floating_vegetation_mat_dripleaf_east.json`
- **Revert command** (review diff first!): `git show 552f5a189c` then `git revert 552f5a189c` if confirmed safe

### `84542c2d02` — Remove leaf blockstate inline keys: bamboo_shoot.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/vegetation/column/bamboo_shoot.json`
- **Revert command** (review diff first!): `git show 84542c2d02` then `git revert 84542c2d02` if confirmed safe

### `84c63f6240` — Remove leaf blockstate inline keys: fan_corals.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/fan_corals.json`
- **Revert command** (review diff first!): `git show 84c63f6240` then `git revert 84c63f6240` if confirmed safe

### `7357bed643` — Remove leaf blockstate inline keys: coral_air_pockets.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/local/coral_air_pockets.json`
- **Revert command** (review diff first!): `git show 7357bed643` then `git revert 7357bed643` if confirmed safe

### `3db634b670` — Remove leaf blockstate inline keys: dripstone_spike_3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_3.json`
- **Revert command** (review diff first!): `git show 3db634b670` then `git revert 3db634b670` if confirmed safe

### `e808954462` — Remove leaf blockstate inline keys: dripstone_spike_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_2.json`
- **Revert command** (review diff first!): `git show e808954462` then `git revert e808954462` if confirmed safe

### `44f204e36a` — Remove leaf blockstate inline keys: dripstone_spike_1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/terrain/dripstone_spike_1.json`
- **Revert command** (review diff first!): `git show 44f204e36a` then `git revert 44f204e36a` if confirmed safe

### `1d1c5e9e24` — Remove leaf blockstate inline keys: tubeworm.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/tubeworm.json`
- **Revert command** (review diff first!): `git show 1d1c5e9e24` then `git revert 1d1c5e9e24` if confirmed safe

### `1af9f40d44` — Remove leaf blockstate inline keys: small_tubeworm.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/small_tubeworm.json`
- **Revert command** (review diff first!): `git show 1af9f40d44` then `git revert 1af9f40d44` if confirmed safe

### `dc2d7a1585` — Remove leaf blockstate inline keys: hydrothermal_vent.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/hydrothermal_vent.json`
- **Revert command** (review diff first!): `git show dc2d7a1585` then `git revert dc2d7a1585` if confirmed safe

### `299cb1ce2a` — Remove leaf blockstate inline keys: giant_tubeworm_4.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_4.json`
- **Revert command** (review diff first!): `git show 299cb1ce2a` then `git revert 299cb1ce2a` if confirmed safe

### `85adcb1cce` — Remove leaf blockstate inline keys: giant_tubeworm_3.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_3.json`
- **Revert command** (review diff first!): `git show 85adcb1cce` then `git revert 85adcb1cce` if confirmed safe

### `dee8266176` — Remove leaf blockstate inline keys: giant_tubeworm_2.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_2.json`
- **Revert command** (review diff first!): `git show dee8266176` then `git revert dee8266176` if confirmed safe

### `777de3c895` — Remove leaf blockstate inline keys: giant_tubeworm_1.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/other/giant_tubeworm_1.json`
- **Revert command** (review diff first!): `git show 777de3c895` then `git revert 777de3c895` if confirmed safe

### `a23fa45c12` — Remove leaf blockstate inline keys: scarecrow.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/decor/scarecrow.json`
- **Revert command** (review diff first!): `git show a23fa45c12` then `git revert a23fa45c12` if confirmed safe

### `9e5aa8cab5` — Remove leaf blockstate inline keys: floating_lantern.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/decor/floating_lantern.json`
- **Revert command** (review diff first!): `git show 9e5aa8cab5` then `git revert 9e5aa8cab5` if confirmed safe

### `9b3eb78c45` — Remove leaf blockstate inline keys: campfires.json

- **Removed debunked keys**: waterlogged
- **Files touched**: 1
  - `data/wythers/worldgen/configured_feature/decor/campfires.json`
- **Revert command** (review diff first!): `git show 9b3eb78c45` then `git revert 9b3eb78c45` if confirmed safe

