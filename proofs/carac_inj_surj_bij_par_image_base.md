---
title: Caractérisation de l’injectivité / surjectivité / bijectivité d’une application linéaire par l’image d’une base de l’espace de départ.
authors:
  - Félix Rondeau
date: 07/03/2025
pid: 1741353629
tags:
  - algèbre linéaire
---

Soient $f\in \L_{\K}(E, F)$ et $(e_{i})_{i\in I}$ une base de $E$.

1. $f$ est injective si et seulement si $(f(e_{i}))_{i\in I}$ est libre
2. $f$ est surjective si et seulement si $(f(e_{i}))_{i\in I}$ est génératrice dans $F$
3. $f$ est un isomorphisme si et seulement si $(f(e_{i}))_{i\in I}$ est une base de $F$

---

1. - Supposons $f$ injective. Soit $(\lambda_{i})_{i\in I}$ une famille de scalaires presque nulle delle que

     $$
         \sum_{i\in I}\lambda_{i} f(e_{i}) = 0_{F} \quad (*)
     $$

     Par linéarité de $f$, $(*)$ donne

     $$
     \begin{align*}
         f \left(\sum_{i\in I}\lambda_{i} e_{i}\right) = 0_{F} &\quad\text{donc}\quad \sum_{i\in I}\lambda_{i} e_{i} \in \Ker f \\
     &\quad\text{donc}\quad \sum_{i\in I}\lambda_{i} e_{i} = 0_{E} \quad\text{car $f$ est injective} \\
     &\quad\text{donc}\quad  \forall i\in I, \lambda_{i} = 0_\K \quad\text{car $(e_{i})_{i\in I}$ est une base donc est libre}
     \end{align*}
     $$

     Ainsi, $(f(e_{i}))_{i\in I}$ est libre.

   - Supposons que $(f(e_{i}))_{i\in I}$ est libre.

     - $\{0_{E}\}\subset \Ker f$ car $f(0_{E})=0_{F}$
     - Soit $x\in \Ker f$ fixé quelconque. On décompose $x$ dans la base $(e_{i})_{i\in I}$ :

       $$
           \exists (x_{i})_{i\in I}\in \K^{(I)}: x=\sum_{i\in I}x_{i} e_{i}
       $$

       Alors $x\in \Ker f$ donc $f(x)=0_{F}$ donc $\displaystyle \sum_{i\in I}x_{i}f(e_{i}) = 0_{F}$ or la famille $(f(e_{i}))_{i\in I}$ est libre donc $\forall i\in I, x_{i} = 0_{\K}$ donc $x=0_{E}$. On a donc l’inclusion réciproque.

2. - Supposons $f$ surjective. $(e_{i})_{i\in I}$ est une base de $E$ donc est génératrice dans $E$ donc $(f(e_{i}))_{i\in I}$ est génératrice dans $\Imf f$, donc par surjectivité de $f$, $(f(e_{i}))_{i\in I}$ est génératrice dans $F$.
   - Supposons que $(f(e_{i})_{i\in I})$ engendre $F$. On sait que $\Imf f = \Vect f(\text{toute famille génératrice de }E)$. Donc en prenant $(e_{i})_{i\in I}$ comme famille génératrice, on a $\Imf f = \Vect (f(e_{i}))_{i\in I}=F$ donc $f$ est surjective.

3. Elle se déduit des deux précédentes équivalences.
