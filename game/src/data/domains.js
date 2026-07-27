import { getPlants, soilTypes } from './plants.js'
import { getBoletes, edibilityTypes } from './bolets.js'

export const domains = [
  {
    id: 'plants',
    label: 'Plantes',
    icon: '🌿',
    title: 'Plantes indicatrices',
    subtitle: 'Apprenez à reconnaître les plantes indicatrices de morilles',
    countLabel: (n) => `${n} plante${n > 1 ? 's' : ''} à découvrir`,
    question: 'Quelle est cette plante ?',
    reviewTitle: 'Plantes à revoir',
    perfectMessage: 'Parfait ! Vous connaissez toutes les plantes.',
    traitKey: 'soil',
    traits: soilTypes,
    getItems: getPlants,
    details: [],
  },
  {
    id: 'boletes',
    label: 'Bolets',
    icon: '🍄',
    title: 'Bolets',
    subtitle: 'Apprenez à reconnaître les bolets et leur comestibilité',
    countLabel: (n) => `${n} bolet${n > 1 ? 's' : ''} à découvrir`,
    question: 'Quel est ce bolet ?',
    reviewTitle: 'Bolets à revoir',
    perfectMessage: 'Parfait ! Vous connaissez tous les bolets.',
    traitKey: 'edibility',
    traits: edibilityTypes,
    getItems: getBoletes,
    details: ['biotope', 'flesh', 'prep', 'note'],
  },
]

export function getDomain(id) {
  return domains.find((d) => d.id === id) ?? domains[0]
}

export const detailLabels = {
  biotope: 'Biotope',
  flesh: 'Coloration à la coupe',
  prep: 'Préparation',
  note: 'Note',
}

export function itemDetails(domain, item) {
  if (!item) return []
  return domain.details
    .filter((key) => item[key])
    .map((key) => ({ key, label: detailLabels[key], value: item[key] }))
}
