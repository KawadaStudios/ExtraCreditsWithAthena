Chapter 2 Art Drop Folder

Purpose
- Keep all Chapter 2 art isolated from demo/chapter 1 assets.
- Artists can replace files in this folder without searching other directories.

Naming Rules
- Backgrounds: ch2_bg_<scene_name>.png
- CGs: ch2_cg_<scene_name>.png
- Sprites: ch2_sprite_<character>_<outfit>_<emotion>.png

Current Files In Use
- backgrounds/ch2_bg_athena_room.png
- cgs/ch2_cg_athena_calendar.png
- sprites/athena/ch2_sprite_athena_robes_lust.png

Code Registry
- Declarations live in: game/src/chapter_2/images.rpy
- Chapter 2 script references should use only ch2_ image names.

Workflow
1. Replace placeholder images in this folder.
2. Keep filename exactly the same to avoid script changes.
3. Add new Chapter 2 image declarations only in game/src/chapter_2/images.rpy.
