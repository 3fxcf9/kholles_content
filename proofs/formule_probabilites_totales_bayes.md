---
title: Formule des probabilités totales et formule de Bayes
authors:
  - Félix Rondeau
date: 06/07/2025
pid: 1749314282
tags:
  - probabilités
---

### Formule des probabilités totales

Si $(A_{i})_{i \in \icc{1,p}}$ est un système complet d’événements, pour tout événement $B$,

$$
    P(B) = \sum_{i=1}^{p}P(A_{i} \cap B)
$$

### Formule de Bayes

Pour deux événements $A$ et $B$ de probabilités non nulles,

$$
    P_{B}(A) = \frac{P_{A}(B)P(A)}{P(B)}
$$

---

### Preuve de la formule des probabilités totales

$(A_{i})_{i \in \icc{1,p}}$ est un système complet d’événements donc

$$
    B = B \cap \Omega = B \cap \left(\bigsqcup_{i=1}^{p}A_{i}\right) = \bigsqcup_{i=1}^{p}(B \cap A_{i})
$$

si bien qu’en prenant l’image de cette réunion d’événements incompatibles par la probabilité $P$ :

$$
    P(B) = \sum_{i=1}^{p}P(B \cap A_{i})
$$

### Preuve de la formule de Bayes

Par définition des probabilités conditionnelles (qui existent car $P(A)>0$ et $P(B)>0$),

$$
    P_{B}(A) \frac{P(A \cap B)}{P(B)} \iff P(A \cap B) = P(B)P_{B}(A)
$$

et

$$
    P_{A}(B) = \frac{P(A \cap B)}{P(A)} \iff P(A \cap B) = P(A)P_{A}(B)
$$

donc en égalant les deux expressions de $P(A \cap B)$,

$$
    P(B)P_{B}(A) = P(A)P_{A}(B)
$$

d’où

$$
    P_{B}(A) = P_{A}(B)\frac{P(A)}{P(B)}
$$

