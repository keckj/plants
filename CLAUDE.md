# Plantes indicatrices - Morilles / Bolets

Jeu interactif de reconnaissance : plantes indicatrices de sol calcaire associees aux morilles, et bolets (comestibilite, coloration a la coupe, preparation).

**Stack :** Vue.js 3 (Composition API) + Vite
**Langue :** Interface en francais

## Structure

```
plants/
  champi/                             # Corpus bolets source (non versionne)
    bolets.md                         # Copie versionnee dans game/docs/bolets.md
  game/                                # Projet Vite
    docs/bolets.md                    # Source documentaire des 42 bolets (credits images Wikimedia)
    src/
      main.js
      style.css
      App.vue                         # Navigation par ref('home'|'quiz'|'flashcard') + domain + difficulty
      data/
        difficulties.js               # 4 niveaux cumulatifs (beginner/intermediate/advanced/expert) + filterByTier
        domains.js                    # Registre des domaines de jeu (plants, boletes) - aucun import .vue
        plants.js                     # 100 plantes (25 par tier), soilTypes, getPlants(difficulty)
        bolets.js                     # 42 bolets (10/11/11/10 par tier), edibilityTypes, getBoletes(difficulty)
      utils/shuffle.js                # Fisher-Yates shuffle
      composables/                    # Primitives pures, agnostiques du domaine (prennent un tableau d'items)
        useScore.js                   # Compteur correct/total/percentage/failedItems
        useQuiz.js                    # Logique QCM : useQuiz(items)
        useFlashcard.js               # Logique flashcards : useFlashcard(items)
      components/
        HomeScreen.vue                # Accueil : selection domaine + difficulte + mode
        QuizGame.vue                  # Mode QCM (4 choix, feedback vert/rouge, details apres reponse)
        FlashcardGame.vue             # Mode flashcards (flip CSS 3D, verso = nom + trait + details)
        PlantImage.vue                # Image responsive (object-fit: contain)
        TraitBadge.vue                # Pastille generique (types + value), fallback si cle inconnue
        ScoreBoard.vue                # Score inline + ecran de fin (domain-aware)
    public/images/                     # 100 images plantes (noms ASCII) + images/bolets/ (42 images)
```

## Lancer le jeu

```bash
cd game
npm run dev
```

## Systeme de domaines

Le jeu est generique : un "domaine" (`plants` ou `boletes`) fournit ses items, son trait categoriel affiche en pastille, et ses libelles. Les composants de jeu (`QuizGame`, `FlashcardGame`, `ScoreBoard`) ne connaissent que la forme `{id, name, latin, image, tier, [traitKey]}` + des champs de details optionnels.

## Ajouter un item a un domaine existant

1. Deposer l'image dans `game/public/images/` (plantes) ou `game/public/images/bolets/` (bolets), nom ASCII
2. Ajouter une entree dans `src/data/plants.js` ou `src/data/bolets.js`, avec un `tier` valide

## Ajouter un domaine

1. Creer `src/data/<domaine>.js` : items `{id, name, latin, image, tier, [trait], ...details}`, dictionnaire de traits (`{icon, label, color, definition}`), `get<Domaine>(difficulty)` via `filterByTier`
2. Ajouter l'entree au registre `src/data/domains.js` (`traitKey`, `traits`, `getItems`, `details`)
3. Le selecteur de domaine dans `HomeScreen.vue` et les composants de jeu se branchent automatiquement dessus

## Decisions techniques

- Images dans `public/` (pas `src/assets/`) : servies telles quelles, pas de bundling
- Pas de vue-router : navigation par `ref` + `v-if` dans `App.vue`
- Pas de CSS framework : CSS simple, mobile-first
- Pas de persistence de score (reset au rechargement)
- Noms de fichiers ASCII dans `public/images/`
- `data/` n'importe jamais de composant `.vue` : la dependance va des donnees vers l'UI, jamais l'inverse
- Difficulte par tiers cumulatifs (chaque niveau inclut les precedents), commune aux deux domaines
