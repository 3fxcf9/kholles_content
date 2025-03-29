---
title: Trace et rang d’un projecteur
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272907
tags:
  - algèbre linéaire
  - matrices
---

La trace d’un projecteur est égale à son rang

---

Soit $p$ un projecteur d’un $\K$-espace vectoriel $E$ de dimension finie $n$.

Par propriété d’un projecteur,

$$
    \Img p \oplus \Ker p
$$

Notons $r = \rg u$ et choisissons une base $(e_{1}, \ldots,e_{r}, e_{r+1}, \ldots,e_{n})$ de $E$ adaptée à cette décomposition, et telle que

- $(e_{1}, \ldots, e_{r})$ est une base de $\Img u$
- $(e_{r+1}, \ldots, e_{n})$ est une base de $\Ker u$ ($\dim_{\K} \Ker u = \dim_{\K} E -\rg u = n-r$)

Alors

$$
    \forall i \in \iset{1,r}, u(e_{i}) = e_{i}
$$

et

$$
    \forall i \in \iset{r+1,n}, u(e_{i}) = 0
$$

donc

$$
\begin{align*}
    \mat(u,(e_{1}, \ldots, e_{n})) &= \mtx{1 & \cdots & 0 & 0 & \cdots & 0 \\
                                          0 & \ddots & \vdots & \vdots & & \vdots \\
                                          \vdots & & 1 & \vdots & & \vdots \\
                                          \vdots & & \vdots & 0 & & \vdots \\
                                          \vdots & & \vdots & \vdots & \ddots & \vdots \\
                                          0 & \cdots & 0 & 0 & \cdots & 0} \\
&=\left(\begin{array}{c|c}
        I_r & \mathbf{0} \\ \hline
        \mathbf{0} & \mathbf{0}
    \end{array}\right)\\
&= J_{r}(n,n)
\end{align*}
$$

Ainsi,

$$
    \tr u = \tr J_{r}(n,n) = r = \rg u
$$
