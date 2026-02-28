# Plantes indicatrices - Morilles

Jeu interactif de reconnaissance des plantes indicatrices de sol calcaire associees aux morilles.

100 plantes reparties en 4 niveaux de difficulte :
- **Debutant** (25 plantes) - les classiques du sous-bois calcaire
- **Connaisseur** (50 plantes) - especes moins evidentes
- **Avance** (75 plantes) - arbustes, haies et prairies
- **Expert** (100 plantes) - pelouses seches et orchidees

Deux modes de jeu :
- **QCM** - 4 choix, feedback immediat
- **Flashcards** - memorisation avec animation flip 3D

## Stack

Vue.js 3 (Composition API) + Vite

## Lancer le jeu

```bash
cd game
npm install
npm run dev
```

## Ajouter une plante

1. Deposer l'image dans `game/public/images/` (nom ASCII)
2. Ajouter une entree dans `src/data/plants.js`
