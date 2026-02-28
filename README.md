# Plantes indicatrices - Morilles

Jeu interactif de reconnaissance des plantes indicatrices de sol calcaire associées aux morilles.

100 plantes réparties en 4 niveaux de difficulté :
- **Débutant** (25 plantes) - les classiques du sous-bois calcaire
- **Connaisseur** (50 plantes) - espèces moins évidentes
- **Avancé** (75 plantes) - arbustes, haies et prairies
- **Expert** (100 plantes) - pelouses sèches et orchidées

Deux modes de jeu :
- **QCM** - 4 choix, feedback immédiat
- **Flashcards** - mémorisation avec animation flip 3D

## Stack

Vue.js 3 (Composition API) + Vite

## Lancer le jeu

```bash
cd game
npm install
npm run dev
```

## Ajouter une plante

1. Déposer l'image dans `game/public/images/` (nom ASCII)
2. Ajouter une entrée dans `src/data/plants.js`
