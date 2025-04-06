---
title: Formule de Taylor
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933252
tags:
  - polynômes
---

Soient $\K$ un corps de caractéristique nulle, et $P \in \K[X]$.

$$
\begin{align*}
    P(X) &= \sum_{k \in \N}\frac{\Phi(D^{k}(P))(a)}{k!}(X-a)^{k} \\
&= \sum_{k \in \N}\frac{\tilde{P}^{(k)}(a)}{k!}(X-a)^{k}
\end{align*}
$$

(on peut aussi sommer jusqu’à un majorant du degré de $P$).

---

$P \in \K[X]$ donc $P$ se décompose dans la base de Taylor en $a$ de $\K_{n}(X)$ : il existe $(\lambda{0}, \ldots, \lambda_{n})\in \K^{n+1}$ tels que

$$
    P=\sum_{k=0}^{n}\lambda_{k}T_{k} = \sum_{k=0}^{n} \frac{\lambda_{k}}{k!}(X-a)^{k}
$$

Pour calculer les coefficients, évaluons en $a$ l’identité polynomiale obtenue en prepant l’image des deux membres par $D^{i}$ pour $i \in \iset{0,n}$. Soient $(i,k)\in \iset{0,n}^{2}$.

$$
    D^{i}(T_{k}) = D^{i}\left(\frac{(X-a)^{k}}{k!}\right) =
\begin{cases}
    0 & \text{si }i>k\\
 \frac{k(k-1)\cdots (k-i+1)}{k!}(X-a)^{k-1} = \frac{1}{(k-i)!}(X-a)^{k-1} =  & \text{si }i \leq k
\end{cases}
$$

Soit $i \in \iset{0,n}$.

$$
    P^{i}(P) = \sum_{k=0}^{n}\lambda_{k}D^{i}(T_{k}) = \sum_{k=1}^{n}\frac{\lambda_{k}}{(k-i)!}(X-a)^{k-i}
$$

Evaluons en $a$ (image par $\phi_{a}$) :

$$
    (D^{i}(P)) = \sum_{k=1}^{n}\frac{\lambda_{k}}{(k-i)!}\times \underbrace{\phi_{a}((X-a)^{k-1})}_{=\begin{cases}1 & \text{si }k=i \\ 0 & \text{si } k \geq i\end{cases}} = \frac{\lambda_{i}}{(i-i)!} = \lambda_{i}
$$
