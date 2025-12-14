---
title: Irréductibilité de $X^3 - X + 1$ dans $\mathbb{Q}[X]$
authors:
  - Félix Rondeau
date: 04/15/2025
pid: 1744738725
tags:
  - polynômes
---

Le polynôme

$$
    P(X) = X^{2} - X + 1
$$

est irréductible dans $\Q[X]$.

---

Supposons par l’absurde que $P$ admette une racine rationnelle $r$. Alors il existe $(p,q) \in \Z \times \N^{*}$ premiers entre eux tels que $r = \frac{p}{q}$. On peut donc écrire

$$
    P(r) = \frac{p^{3}}{q^{3}} - \frac{p}{q} + 1 = 0 \qquad (*)
$$

donc en multipliant par $q^{3}$,

$$
    p^{3} - pq^{2} + q^{3} = 0
$$

soit

$$
    p^{3} = q^{2}(p-q)
$$

On en déduit que $q \mid p^{3}$, et comme $p$ et $q$ sont premiers entre eux et donc que $p^{3}\land q = 1$, le théorème de Gauss permet d’affirmer que $q \mid 1$, donc comme $q \in \N$, $q=1$.

Ainsi, $(*)$ donne

$$
    p^{3} - p + 1 = 0
$$

soit

$$
    p(p^{2} - 1) = -1
$$

d’où $p \mid 1$, i.e. $p=\pm 1$. Or $-1$ et $1$ n’étant pas racine de $P$, le polynôme n’a aucune racine rationnelle et est donc irréductible (théorème de caractérisation de l’irréductibilité pour les polynômes de degré 1,2 et 3).
