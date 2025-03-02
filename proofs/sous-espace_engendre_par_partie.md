---
title: Définition et existence du sous-espace engendré par une partie d’un espace vectoriel.
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1740414407
tags:
  - algèbre linéaire
---

Soient $(E,+, \cdot)$ un $\K$-espace vectoriel et $A$ une partie de $E$. Notons $\mathcal{F}$ l’ensemble des sous-espaces vectoriels de $E$ contenant $A$. En ordonnant (partiellement) $\mathcal{P}(E)$ par l’inclusion, l’ensemble $\mathcal{F}$ admet un plus petit élément, noté $\Vect_{E}(A)$, et appelé **le sous-espace vectoriel engendré par $A$ dans $E$**.

---

Posons $\mathcal{F}=\{$F$ \text{ sous-espace vectoriel de } E \mid A\subset F\}$ et $\displaystyle V=\bigcap_{F\in \mathcal{F}}F$ (qui est bien défini car $\mathcal{F}\neq \emptyset$ puisque $E\in\mathcal F$). Montrons que $V=\min \mathcal{F}$ pour l’inclusion.

- $V\in \mathcal{F}$ car $V$ est une intersection de sous-espaces vectoriels de $E$ donc est un sous-espace vectoriel de $E$, et
  $$
      \forall F\in \mathcal{F}, A\subset F \implies  A\subset \bigcap_{F\in \mathcal{F}}F \implies A\subset V
  $$
- Soit $F_{0}\in \mathcal{F}$ fixé quelconque.
  $$
      V=\bigcap_{F\in \mathcal{F}} F = F_0 \cap \left(\bigcap_{F\in \mathcal{F}\setminus F_{0}}F\right)\subset F_{0}
  $$
  donc $v$ est plus petit que tous les autres éléments de $\mathcal{f}$ pour l’inclusion.
