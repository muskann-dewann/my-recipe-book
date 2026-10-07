# Muskan's CookBook

A personal recipe website, hosted on GitHub Pages at https://muskann-dewann.github.io/my-recipe-book/.

## Files
- `index.html`: the whole site (styles, layout, features). iOS-style design, light and dark mode.
- `recipes.js`: all recipe data (`RECIPES`) and Hindi ingredient names (`HINDI`). Add new recipes here.
- `photos/`: dish photos, 960x1200 JPG, cropped and colour-corrected. `photos/og/`: 1200x630 link-preview crops.
- `r/<id>/index.html`: share pages for WhatsApp previews. Rebuild with `python3 tools/build_share_pages.py` after adding or renaming a recipe.
- `sw.js`, `manifest.webmanifest`, `icons/`: installable, offline-capable app. Add new photo paths to `CORE` in `sw.js` and bump `CACHE`.

## Rules for adding or editing a recipe (the owner's standing instructions)
- Ingredients first (all together, one list), then the step-by-step method.
- Every step lists the ingredients it uses with quantities (`use`), then how to do it (`x`).
- Write the owner's own changes directly into the recipe. Never add side notes such as "doubled" or "no onions in the marinade".
- Follow the owner's words and screenshots exactly. Do not add techniques, times or details she did not state. If something is unclear (an amount, a conflict between a screenshot's list and its method), ask her with tap-to-answer questions.
- When she cooks a different quantity from a screenshot, scale every amount to what she cooked; set `base` to the chicken weight in grams.
- Fill `rating` (stars out of 5), `cooked` (YYYY-MM-DD), `veg`, `tags` (cuisine, e.g. North Indian, Home style), `quick` (e.g. Air fryer, One pot), `tone` (amber, tomato or green), and `notes` (only what she asks to note).
- Do not credit the original creators (her choice).
- Keep text in simple, plain, formal English. Keep each step short enough to fit on one phone screen.
- Process each new photo the same way (crop black bars, 4:5, 960x1200, light colour correction).
