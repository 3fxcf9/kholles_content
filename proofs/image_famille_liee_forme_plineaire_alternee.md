---
title: Image d’une famille liée par une forme $p$-linéaire alternée
authors:
  - Félix Rondeau
date: 18/05/2025
pid: 1747567052
tags:
  - déterminant
---

Si $\varphi$ est une forme $p$-linéaire alternée sur le $\K$-espace vectoriel $E$, et $(u_{1}, \ldots, u_{p})$ une famille liée de $E$, alors

$$
    \varphi(u_{1}, \ldots, u_{p}) = 0_{\K}
$$

---

Soit $(u_{1}, \ldots, u_{p})$ une famille liée de $E$. Alors un de ses vecteurs s’exprime comme une combinaison linéaire d’autres vecteurs de la famille, i.e.

$$
    \exists i_{0} \in \icc{1,p}: \exists (\lambda_{j})_{j \in \icc{1,p} \setminus \{i_{0}\}} \in \K^{p-1}: u_{i_{0}} = \sum_{\substack{j=1\\j\neq i_{0}}}^{p}\lambda_{j}\cdot u_{j}
$$

Ainsi,

$$
    \begin{align*}
         \varphi(u_{1}, \ldots , u_{p}) &= \varphi \left(u_{1}, \ldots, \sum_{\substack{j=1\\j\neq i_{0}}}^{p}\lambda_{j} \cdot u_{j}, \ldots, u_{p}\right) \\
&= \sum_{\substack{j=1\\j\neq i_{0}}}^{p}\lambda_{j}\underbrace{\varphi \left(u_{1}, \ldots, \underbrace{u_{j}}_{i_{0}\mathrm{^e}\text{ pos.}}, \ldots, u_{p}\right)}_{\substack{=0 \text{ car les vect en } i\mathrm{^e} \text{ et } j \mathrm{^e}\\\text{ pos. } (i\neq j) \text{ sont égaux}}}\\
&=0_\K
    \end{align*}
$$
