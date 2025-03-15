---
title: Caractérisation de l’injectivité et de la surjectivité d’une application linéaire par son rang
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060868
tags:
  - algèbre linéaire
---

Soient $E$ et $F$ deux $\K$-espaces vectoriels et $f$ une application linéaire de $E$ dans $F$.

1. Si $E$ est de dimension finie, alors $f$ est de rang fini et

   $$
       f \text{ est injective} \iff \rg f=\dim_{\K}E
   $$

2. Si $E$ est de dimension finie, alors $f$ est de rang fini et

   $$
       f \text{ est surjective} \iff \rg f=\dim_{\K}F
   $$

3. Si $E$ et $F$ sont de même dimension finie, alors $f$ est de rang fini et

   $$
       f \text{ est surjective} \iff f \text{ est surjective}
   $$

---

Notons $n$ la dimension de $E$ et fixons $(e_{1}, \ldots \epsilon_{n})$ une base de $E$.

1. - Supposons que $f$ est inective. Alprs, $(f(e_{1}), \ldots f(e_{n}))$ est une famille libre de $F$, or nous savons qu’elle engendre $\Imf f$(car $(e_{1}, \ldots, e{n})$ engendre $E$) donc $(f(e_{1}), \ldots , f(e_{n}))$ est une base de $\Imf f$ donc $\rg f=f=\dim E$.

   - Supposons que $\rg f=\dim E$.
     $(f(e_{1}), \ldots , f(e_{n}))$ engendre $\Imf f$ (car $(e_{1}, \ldots , e_{n})$ engendre $E$) or $\Imf f$ est de dimension $n$ donc $(f(e_{1}), \ldots , f(e_{n}))$ est une famille génératrice de cardinal minimal donc c’est une base de $\Imf f$. Ainsi, l’image par $f$ de la base $(e_{1}, \ldots , e_{n})$ de $E$ est une famille libre de $F$, donc $f$ est injective.

2. $$
   \begin{align*}
       f \text{ est surjective} &\iff \Imf f = F \\
       &\iff \rg f=\dim F \quad\text{car } \Imf f \subset F
   \end{align*}
   $$

3. $$
       \begin{align*}
           f \text{ est injective} &\iff \rg f=\dim E \quad\text{par } (i)\\
           &\iff \rg f = \dim F \quad\text{car } \dim E=\dim F \\
           &\iff f \text{ est surjective} \quad\text{en appliquant } (ii)
       \end{align*}
   $$
