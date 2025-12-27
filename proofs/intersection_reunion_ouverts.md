---
title: Intersection et réunion d’ouverts
authors:
  - Félix Rondeau
date: 06/06/2025
pid: 1749245170
tags:
  - topologie
---

1. Une intersection finie d’ouverts est un ouvert
2. Une réunion quelconque d’ouverts est un ouvert

---

1. Soit $I$ un ensemble et $(G_{i})_{i \in I}$ une famille d’ouverts de $\R^{2}$. Soit $a \in \bigcup_{i \in I}G_{i}$. Alors il existe $i_{0} \in I$ tel que $a \in G_{i_{0}}$, or $G_{i_{0}}$ est un ouvert donc

   $$
       \exists r_{0} \in \R_{+}^{*}: B(a,r_{0}) \subset G_{i_{0}}
   $$

   Par conséquent,

   $$
       B(a,r_{0}) \subset \bigcup_{i \in I}G_{i}
   $$

   et ainsi, $\bigcup_{i \in I}G_{i}$ est un ouvert de $\R^{2}$.

2. Soit $p \in \N^{*}$ et $(G_{i})_{i \in \icc{1,p}}$ une famille de $p$ ouverts de $\R^{2}$. Soit $a \in \bigcap_{i \in \icc{1,p}}G_{i}$. Alors pour tout $i \in \icc{1,p}, a \in G_{i}$ donc

   $$
       \exists r_{i} > 0: B(a,r_{i}) \subset G_{i}
   $$

   Posons $r = \min\{r_{i} \mid i \in \icc{1,p}\}$.

   $$
       \forall i \in \icc{1,p}, B(a,r) \subset B(a, r_{i}) \subset G_{i}
   $$

   donc $B(a,r) \subset \bigcap_{i \in \icc{1,p}}G_{i}$, et par conséquent, $\bigcap_{i=1}^{p}G_{i}$ est un ouvert de $\R^{2}$.
