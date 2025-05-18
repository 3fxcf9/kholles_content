---
title: Théorème de convergence des sommes de Riemann
authors:
  - Félix Rondeau
date: 05/09/2025
pid: 1746807940
tags:
  - intégration
---

Soit $f \in \Cont^{0}([a,b],\C)$. Alors, pour tout $\varepsilon \in \R_{+}^{*}$, il existe $\eta \in \R_{+}^{*}$ tel que pour toute subdivision pointée $(\sigma,\pi)$ de $\cc{a,b}$,

$$
    \delta(\sigma) \leq \eta \implies \abs{S(f,\sigma,\pi) - \int_{a}^{b}f(u)\dd u} \leq \varepsilon
$$

---

- Soit $(\sigma,\pi)$ une telle subdivision pointée. Notons $\sigma = (x_{j})_{j \in \iset{0,N}}$ et $\pi = (x'_{j})_{j \in \iset{0,N-1}}$.

$$
\begin{align*}
    \abs{\int_{a}^{b}f(x)\dd x - S(f,\sigma,\pi)} &= \Biggl|\underbrace{\int_{a}^{b}f(x)\dd x}_{=\sum_{i=0}^{N-1}\int_{x_{i+1}}^{x_{i}}f(x)\dd x} - \sum_{i=0}^{N-1}\underbrace{(x_{i+1}-x_{i})f(x'_{i})}_{=\int_{x_{i}}^{x_{i+1}}f(x'_{i})\dd x}\Biggr| \\
&= \abs{\sum_{i=0}^{N-1}\int_{x_{i}}^{x_{i+1}}\left(f(x) - f(x'_{i})\right)\dd x} \\
& \leq \sum_{i=0}^{N-1}\abs{\int_{x_{i}}^{x_{i+1}}\left(f(x) - f(x'_{i})\right)\dd x} \\
& \leq \sum_{i=1}^{N-1}\int_{x_{i}}^{x_{i+1}}\abs{f(x) - f(x'_{i})}\dd x
\end{align*}
$$

- Soit $\varepsilon > 0$. La fonction $f$ est continue sur $\cc{a,b}$ donc uniformément continue sur ce segment (théorème de Heine), donc en appliquant la définition de la continuité uniforme pour $\varepsilon \leftarrow \frac{\varepsilon}{b-a}$,

$$
    \exists \eta \in \R_{+}^{*}: \forall (x,t)\in  \cc{a,b}^{2}, \abs{s-t} \leq  \eta \implies  \abs{f(x)-f(t)}\leq \frac{\varepsilon}{b-a}
$$

Supposons la subdivision pointée $(\sigma, \pi)$ de pas inférieur à $\eta$. La majoration établie précédemment donne

$$
    \begin{align*}
        \abs{\int_{a}^{b}f(x)\dd x - S(f,\sigma,\pi)} & \leq \sum_{i=0}^{N-1}\int_{x_{i}}^{x_{i+1}}\underbrace{\abs{f(x) - f(x'_{i})}}_{\substack{\abs{x-x'_{i}} \leq  \abs{x_{i+1}-x_{i}} \leq  \delta(\sigma) \leq  \eta\\\text{donc }\abs{f(x)-f(x'_{i})}\leq  \frac{\varepsilon}{b-a}}}\dd x \\
& \leq \sum_{i=0}^{N-1}\int_{x_{i}}^{x_{i+1}}\frac{\varepsilon}{b-a}\dd x \\
& \leq \sum_{i=0}^{N-1}\frac{\varepsilon}{b-a}(x_{i+1}-x_{i}) \\
& \leq \frac{\varepsilon}{b-a}(b-a)\leq \varepsilon
    \end{align*}
$$
