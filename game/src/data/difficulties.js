export const difficulties = [
  { id: 'beginner', label: 'Débutant', color: '#2d8a4e', tiers: ['beginner'] },
  { id: 'intermediate', label: 'Connaisseur', color: '#f0c800', tiers: ['beginner', 'intermediate'] },
  { id: 'advanced', label: 'Avancé', color: '#ff8c00', tiers: ['beginner', 'intermediate', 'advanced'] },
  { id: 'expert', label: 'Expert', color: '#c0392b', tiers: ['beginner', 'intermediate', 'advanced', 'expert'] },
]

export function filterByTier(items, difficulty) {
  const diff = difficulties.find((d) => d.id === difficulty)
  if (!diff) return items
  return items.filter((i) => diff.tiers.includes(i.tier))
}
