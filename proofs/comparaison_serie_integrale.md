---
title: Comparaison série / intégrale
authors:
  - Félix Rondeau
date: 11/05/2025
pid: 1746966999
tags:
  - intégrale
---

Soit $n_{0} \in \N$ et $f$ une fonction définie sur $\co{n_{0},+\infty}$, continue et décroissante. Alors

$$
    \forall k \in \iset{n_{0},+\infty}, \int_{n_{0}}^{n+1}f(u)\dd u \leq \sum_{k=n_{0}}^{n}f(u) \leq f(n_{0}) + \int_{n_{0}}^{n}f(u)\dd u
$$

---

Soit $k \in \iset{n_{0},+\infty}$. Par décroissance de $f$ sur le segment $\cc{k,k+1}$,

$$
    \forall t \in \cc{k,k+1}, f(k+1) \leq  f(t) \leq f(k)
$$

En intégrant ces inégalités entre $k$ et $k+1$,

$$
    \underbrace{\int_{k}^{k+1}f(k+1)\dd t}_{=f(k+1)} \underset{(1)}{\leq} \int_{k}^{k+1}f(t)\dd t \underset{(2)}{\leq} \underbrace{\int_{k}^{k+1}f(k)\dd t}_{=f(k)}
$$

Soit $n \geq n_{0}$. Sommons la première majoration ci-dessus pour $k \in \iset{n_{0}, n-1}$ :

$$
    \sum_{i=n_{0}+1}^{n}f(i) = \sum_{k=n_{0}}^{n-1}f(k+1) \leq \sum_{k=n_{0}}^{n-1}\int_{k}^{k+1}f(t)\dd t = \int_{n_{0}}^{n}f(t)\dd t
$$

d’où, en ajoutant $f(n_{0})$ aux deux membres,

$$
    \sum_{i=n_{0}}^{n}f(i) \leq f(n_{0}) + \int_{n_{0}}^{n}f(t)\dd t
$$

À présent, sommons $(2)$ pour $k \in \iset{n_{0}\nu}$ :

$$
  \int_{n_{0}}^{n+1} = \sum_{k=n_{0}}^{n} \int_{k}^{k+1}f(t)\dd t \leq \sum_{k=n_{0}}^{n}f(k)
$$

d’où le résultat.
