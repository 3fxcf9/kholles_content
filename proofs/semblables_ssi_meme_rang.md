---
title: Caractérisation de deux matrices équivalentes
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272909
tags:
  - algèbre linéaire
  - matrices
---

Deux matrices sont équivalentes si et seulement si elles ont le même rang.

La relation binaire « être équivalente » partitionne $\M_{n,p}(\K)$ en exactement $\min\{n,p\}+1$ classes d’équivalences caractérisées par le rang de leur éléments.

Un système de représentant des classes d’équivalence est $(J_{r}(n,p))_{0 \leq r \leq \min\{n,p\}}$.

---

- Si deux matrices sont semblables, alors la multiplication à droite et à gauche par des matrices inversibles préservant le rang, on a l’égalité de leur rang.
- Si deux matrices ont le même rang, alors elles sont toutes deux équivalentes à la matrice $J_{r}(n,p)$ (théorème de décomposition $PJ_{r}Q$) donc par transitivité de la relation « être équivalente », elles sont équivalentes.
