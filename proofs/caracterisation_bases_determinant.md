---
title: Caractérisation des bases par le déterminant
authors:
  - Félix Rondeau
date: 05/18/2025
pid: 1747567945
tags:
  - déterminant
---

1. Si la famille $(u_{1}, \ldots, u_{n})$ de $E$ est une base de $E$, alors pour toute base $\B$ de $E$,

   $$
       \det_{\B}(u_{1}, \ldots, u_{n}) \neq 0
   $$

2. Si il existe une base $\B$ de $E$ telle que $\det_{\B}(u_{1}, \ldots, u_{n})\neq 0$, alors $(u_{1}, \ldots, u_{p})$ est une base de $E$.

---

1. Supposons que la famille $(u_{1}, \ldots, u_{n})$ est une base de $E$. Soit $\B$ une base de $E$. On a $\det_{\B} = \det_{\B}(u_{1}, \ldots , u_{p}) \cdot \det_{(u_{1}, \ldots , u_{p})}$ qui, évalué en $\B$ donne

   $$
       1 = \det_{\B}(u_{1}, \ldots , u_{p}) \cdot \det_{(u_{1}, \ldots , u_{p})}\B
   $$

   Ainsi, $\det_{\B}(u_{1}, \ldots , u_{p}) \neq 0$.

2. Supposons qu’il existe une base $\B$ de $E$ telle que $\det_{\B}(u_{1}, \ldots, u_{n})\neq 0$. Par l’absurde, supposons la famille $(u_{1}, \ldots, u_{n})$ liée. $\det_{\B}$ étant une forme $n$-linéaire alternée doonc $\det_{\B}(u_{1}, \ldots, u_{n}) = 0$, ce qui est faux. Par conséquent, $(u_{1}, \ldots, u_{n})$ est une famille libre contenant $n$ vecteurs; c’est donc une base de $E$.
