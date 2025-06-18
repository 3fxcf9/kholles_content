---
title: Stabilité de la loi binomiale pour la somme
authors:
  - Félix Rondeau
date: 06/18/2025
pid: 1750280187
tags:
  - variables aléatoires
---

Si $X$ et $Y$ sont deux variables aléatoires **indépendantes** définies sur un univers $\Omega$ fini suivant des lois binomiales $\B(n,p)$ et $\B(m,p)$, alors $X+Y$ suit la loi binomiale $\B(n+m,p)$.

---

$(X+Y)(\Omega)=\icc{0,n+m}$ donc pour $k \in \icc{0,n+m}$,

$$
    \begin{align*}
        P(X+Y = k) &= \sum_{i=0}^{k} P(X=i) P(Y=k-i) \\
&= \sum_{i=0}^{k} \binom{n}{i}p^{i}(1-p)^{n-i}\binom{m}{k-i}p^{k-i}(1-p)^{m-(k-i)} \\
&= \left(\sum_{i=0}^{k}\binom{n}{i}\binom{m}{k-i}\right)p^{k}(1-p)^{n+m-k} \\
&=\binom{n+m}{k}p^{k}(1-p)^{n+m-k} \quad\text{(Van der Monde)}
    \end{align*}
$$

donc $X+Y$ suit la loi binomiale $\B(n+m,p)$.

