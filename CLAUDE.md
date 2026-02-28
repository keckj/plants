# Plantes indicatrices - Morilles

Jeu interactif de reconnaissance des plantes indicatrices de sol calcaire associees aux morilles.

**Stack :** Vue.js 3 (Composition API) + Vite
**Langue :** Interface en francais

## Structure

```
plantes_morilles/
  [22 images originales]
  game/                               # Projet Vite
    src/
      main.js
      style.css
      App.vue                         # Navigation par ref('home'|'quiz'|'flashcard')
      data/plants.js                  # Registre des 22 plantes (extensible)
      utils/shuffle.js                # Fisher-Yates shuffle
      composables/
        useScore.js                   # Compteur correct/total/percentage
        useQuiz.js                    # Logique QCM
        useFlashcard.js               # Logique flashcards
      components/
        HomeScreen.vue                # Ecran d'accueil / selection du mode
        QuizGame.vue                  # Mode QCM (4 choix, feedback vert/rouge)
        FlashcardGame.vue             # Mode flashcards (animation flip CSS 3D)
        PlantImage.vue                # Image responsive (object-fit: contain)
        ScoreBoard.vue                # Score inline + ecran de fin
    public/images/                    # 22 images (noms ASCII)
```

## Lancer le jeu

```bash
cd game
npm run dev
```

## Ajouter une plante

1. Deposer l'image dans `game/public/images/` (nom ASCII)
2. Ajouter une entree dans `src/data/plants.js`

## Decisions techniques

- Images dans `public/` (pas `src/assets/`) : servies telles quelles, pas de bundling
- Pas de vue-router : navigation par `ref` + `v-if` dans `App.vue`
- Pas de CSS framework : CSS simple, mobile-first
- Pas de persistence de score (reset au rechargement)
- Noms de fichiers ASCII dans `public/images/`
