---
title: Inverse de la matrice représentative d’une application linéaire
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662335
tags:
  - algèbre linéaire
  - matrices
---

Soient $E$ et $F$ deux $\K$-espaces vectoriels de même dimension $n \in \N^{*}$ et $u \in \L_{\K}(E,F)$.

1. si $u$ est un isomorphisme, alors pour toute bases $\B_{E}$ et $\B_{F}$ de $E$ et $F$, $\mat(u, \B_{E}, \B_{F})$ est inversible et son inverse est $\mat(u^{-1}, \B_{F}, \B_{E})$
2. si il existe deux bases $\B_{E}$ et $\B_{F}$ de $B$ et $F$ telle que $\mat(u, \B_{E},\B_{F})$ est inversible, alors $u$ est un isomorphisme

---

1. Supposons que $u$ est inversible. Soient $\B_{E}$ et $\B_{F}$ deux bases de $E$ et $F$ fixées quelconques. D’une part

   $$
       \underbrace{\mat(u^{-1}\circ u, \B_{E}, \B_{E})}_{=\mat(\Id_{E}, \B_{E})=I_{n}} = \mat(u^{-1}, \B_{F}, \B_{E}) \times \mat(u, \B_{E}, \B_{F})
   $$

   et d’autre part

   $$
       \underbrace{\mat(u\circ u^{-1}, \B_{F}, \B_{F})}_{=\mat(\Id_{F}, \B_{F})=I_{n}} = \mat(u, \B_{E}, \B_{F}) \times \mat(u^{-1}, \B_{F}, \B_{E})
   $$

   si bien que

   $$
       \mat(u^{-1},\B_{F},\B_{E}) \times \mat(u,\B_{E},\B_{F}) = \mat(u,\B_{E},\B_{F})\times \mat(u^{-1},\B_{F},\B_{E}) = I_{n}
   $$

   donc $\mat(u,\B_{E},\B_{F})$ est inversible et son inverse est $\mat(u^{-1},\B_{F},\B_{E})$.

2. Supposons qu’il existe des es $\B_{E}$ et $\B_{F}$ de $E$ et $F$ telles que $\mat(u,\B_{E},\B_{F})$ est inversible. Posons $U=\mat(u,\B_{E},\B_{F})$ et $f=\Phi_{\B_{F}}^{-1}(U^{-1})$ de sorte que $\mat(f,\B_{F},\B_{E})=U^{-1}$.

   $$
       \begin{align*}
           I_{n} &= U^{-1} \times U \\
   &= \mat(f,\B_{F},\B_{E})\times \mat(u,\B_{E},\B_{F}) \\
   &= \mat(f\circ u,\B_{E})
       \end{align*}
   $$

   soit

   $$
       \Phi_{\B_{E}}(\Id_{E}) = I_{n} = \Phi_{\B_{E}}(f\circ u)
   $$

   donc par injectivité de $\Phi_{\B_{F}}$, $f\circ u=\Id_{E}$.
   On a de même $u\circ f=\Id_{E}$, ce qui montre la bijectivité de $u$. De plus, comme $u^{-1}=f$,

   $$
       \mat(u^{-1},\B_{F},\B_{E}) = \mat(f,\B_{F},\B_{E}) = U^{-1} = (\mat(u,\B_{E},\B_{F}))^{-1}
   $$
