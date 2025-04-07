---
title: Caractérisation de la multiplicité
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933253
tags:
  - polynômes
---

Soient $\K$ un corps de caractéristique nulle, et $P \in \K[X]$, $P$ non nul.

1. $\alpha$ est racine de $P$ dans $\K$ de multiplicité **au moins** $m \in \N^{*}$ si et seulement si

   $$
       \forall k \in \iset{0,m-1}, \tilde{P}^{(k)}(\alpha) = 0_{\K}
   $$

2. $\alpha$ est racine de $P$ dans $\K$ de multiplicité **exactement** $m \in \N^{*}$ si et seulement si

   $$
       \forall k \in \iset{0,m-1}, \tilde{P}^{(k)}(\alpha) = 0_{\K}
   $$

   et

   $$
       \tilde{P}^{(m)}(\alpha) \neq 0_{\K}
   $$

---

1. - Supposons que $\alpha$ est une racine de multiplicité au moins $m \in \N^{*}$ de $P$. Alors,

   $$
       \exists R \in \K[X]: P(X) = (X-\alpha)^{m}R(X)
   $$

   Soit $k \in \iset{0,m-1}$.

   $$
   \begin{align*}
       P^{(k)} &= \sum_{i=0}^{k}\binom{i}{k}[(X-\alpha)^{m}]^{(i)}R^{(k-i)} \\
   &= \sum_{i=0}^{k}\binom{i}{k}\frac{m}{(m-i)!}(X-\alpha)^{m-i}R^{(k-i)}
   \end{align*}
   $$

   donc

   $$
       \tilde{P}^{(k)}(\alpha) = \sum_{i=0}^{k}\binom{i}{k}\frac{m}{(m-i)!}\underbrace{(\alpha-\alpha)^{m-i}}_{=0 \text{ car } m-i>0}\tilde{R}^{(k-i)}(\alpha) = 0
   $$

   - Supposons que $\forall k \in \iset{0,n}, \tilde{P}^{(k)} = 0$. Appliquons la formule de Taylor en $\alpha$ :

     $$
         \begin{align*}
             P &= \sum_{k=0}^{+\infty} \frac{\tilde{P}^{(k)}(\alpha)}{k!}(X-\alpha)^{k} \\
     &= \sum_{k=m}^{+\infty} \frac{\tilde{P}^{(k)}(\alpha)}{k!}(X-\alpha)^{k} \\
     &= (X-\alpha)^{m}\underbrace{\sum_{k=m}^{+\infty} \underbrace{\frac{\tilde{P}^{(k)}(\alpha)}{k!}(X-\alpha)^{k-m}}_{\in \K[X] \text{car } k-m > 0}}_{\in \K[X]}
         \end{align*}
     $$

2. - Supposons que $\alpha$ est racine de $P$ de multiplicité au moins $m$. D’après le sens direct de $(i)$,

     $$
         \forall k \in \iset{0,m-1}, \tilde{P}^{(k)}(\alpha) = 0
     $$

     Si $\tilde{P}^{(m)}(\alpha) = 0$, alors d’après le sens réciproque de la première équivalence, $\alpha$ est racine de multiplicité au moins $m+1$ de $P$ ce qui contredit le fait que la multiplicité de $\alpha$ est exactement $m$.

     Par conséquent, $\tilde{P}^{(m)}(\alpha) = 0$.

   - Supposons que $\forall k \in \iset{0,m-1}, \tilde{P}^{(k)}(\alpha) = 0$ et que $\tilde{P}^{(m)}(\alpha) \neq 0$. D’après le sens réciproque de la première équivalence, $\alpha$ est une racine de multiplicité au moins $m \in \N^{*}$.

     Supposons que $\alpha$ est une racine de multiplicité au moins $m+1$. D’après le sens direct de la première équivalence,

     $$
         \forall k \in \iset{0,m}, \tilde{P}^{(k)}(\alpha) = 0
     $$

     donc $\tilde{P}^{(m)}(\alpha) = 0$ ce qui est une contradiction.

     Ainsi, $\alpha$ est une racine de multiplicité au moins $m$ mais pas de multiplicité au moins $m+1$ donc $\alpha$ est de multiplicité exactement $m$, ce qui est une contradiction.

     Ainsi, $\alpha$ est une racine de multiplicité au moins $m$ mais pas de multiplicité au moins $m+1$ donc $\alpha$ est de multiplicité mexactement $m$.
