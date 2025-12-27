---
title: Inégalité triangulaire continue
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746308557
tags:
  - intégration
---

Soit $f \in \CM(\cc{a,b},\R)$. Alors

$$
    \abs{\int_{a}^{b}f(u)\dd u} \leq \int_{a}^{b}\abs{f(u)}\dd u
$$

---

Soit $f \in \CM(\cc{a,b},\R)$.

$$
    \exists (\chi_{k})_{k \in \N} \in \E(\cc{a,b},\R)^{\N}: \begin{cases}
        \forall k \in \N, \infabs{\chi_{k} - f}{\cc{a,b}} \leq \frac{1}{2^{k}}b \\
        \int_{a}^{b}\chi_{k}(x)\dd x \arrowlim{k\to +\infty} \int_{a}^{b}f(x)\dd x
    \end{cases}
$$

Montrons que $(\chi_{k})$ converge uniformément vers $\abs{f}$ sur $\cc{a,b}$ : soit $k \in \N$.

$$
    \forall x \in \cc{a,b}, \abs{\abs{\chi_{k}(x)}-\abs{f(x)}} \leq  \abs{\chi_{k}(x)-f(x)} \leq  \infabs{\chi_{k}-f}{\cc{a,b}} \leq \frac{1}{2^{k}}
$$

donc $\infabs{\abs{\chi_{k}}-\abs{f}}{\cc{a,b}} \arrowlim{k\to+\infty}0$ et par conséquent,

$$
    \int_{a}^{b}\abs{\chi_{k}}(x)\dd x \arrowlim{k\to+\infty} \int_{a}^{b}\abs{f}(x)\dd x
$$

Par inégalité triangulaire continue sur $\E(\cc{a,b},\R)$,

$$
    \forall k \in \N, \underbrace{\abs{\int_{a}^{b}\chi_{k}(x)\dd x}}_{\arrowlim{k\to+\infty}\abs{\int_{a}^{b}\chi_{k}(x)\dd x}} \leq \underbrace{\int_{a}^{b}\abs{\chi_{k}}(x)\dd x}_{\arrowlim{k\to+\infty}\int_{a}^{b}\abs{f}(x)\dd x}
$$

si bien que par passage à la limite,

$$
    \abs{\int_{a}^{b}f(x)\dd x} \leq \int_{a}^{b}\abs{f}(x)\dd x
$$

