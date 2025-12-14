---
title: Espérance et variance d’une variable aléatoire suivant une loi binomiale
authors:
  - Félix Rondeau
date: 06/18/2025
pid: 1750279142
tags:
  - variables aléatoires
---

Si la variable aléatoire $X$ suit une loi binomiale de paramètres $n$ et $p$,

$$
    E(X) = np \quad\text{et}\quad V(X) = np(1-p)
$$

---

$X(\Omega) = \icc{0,n}$ donc

$$
    \begin{align*}
        E(X) &= \sum_{k=0}^{n}k P(X=k) \\
&= \sum_{k=1}^{n}k \binom{k}{n}p^{k}(1-p)^{n-k} \\
&= \sum_{k=1}^{n}n \binom{n-1}{k-1}p^{k}(1-p)^{n-k} \\
&= n \sum_{i=0}^{n-1}\binom{n-1}{i}p^{i+1}(1-p)^{(n-1)-i}\\
&= np \sum_{i=0}^{n-1} \binom{n-1}{i}p^{i}(1-p)^{(n-1)-i} \\
&= np(p+(1-p))^{n-1}\\
&= np
    \end{align*}
$$

On a aussi

$$
    \begin{align*}
        E(X^{2}) &= \sum_{k=0}^{n}k^{2}P(X=k) \\
&= \sum_{k=1}^{n}k k \binom{n}{k} p^{k}(1-p)^{n-k} \\
&= \sum_{k=1}^{n}k n \binom{n-1}{k-1}p^{k}(1-p)^{n-k} \\
&= n \sum_{k=1}^{n}(k-1)\binom{n-1}{k-1}p^{k}(1-p)^{n-k} + n \sum_{k=1}^{n}\binom{n-1}{k-1}p^{k}(1-p)^{n-k}\\
&= n(n-1)\sum_{i=0}^{n-2}\binom{n-2}{i}p^{i+2}(1-p)^{(n-2)-i} + \sum_{i=0}^{n-1}\binom{n-1}{i}p^{i+1}(1-p)^{(n-1)-i} \\
&= n(n-1)p^{2}(p+(1-p))^{n-1} + np(p+(1-p))^{n-1} \\
&= n(n-1)p^{2} + np \\
&= np((n-1)p + 1)
    \end{align*}
$$

d’où

$$
    \begin{align*}
        V(X) &= E(X^{2}) - (X(X))^{2}\\
&= np((n-1)p + 1) - n^{2}p^{2} \\
&= np((n-1)p + 1-np)\\
&= np(1-p)
    \end{align*}
$$

