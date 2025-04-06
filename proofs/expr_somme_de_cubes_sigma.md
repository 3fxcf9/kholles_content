---
title: Somme des cubes avec les fonctions symétriques élémentaires
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933256
tags:
  - polynômes
---

Soit $P = (X-x_{1})(X-x_{2})(X-x_{3})$.
Exprimer $S_{3} = x^{1}_{3}+x^{2}_{3}+x_{2}^{3}$ grace aux fonction symétriques élémentaires des racines $x_{1}$, $x_{2}$ et $x_{3}$.

---

On a

$$
    P = X^{3} + \sigma_{1}X_{2} + \sigma_{2}X - \sigma_{3}
$$

Sommons

$$
    \begin{align*}
        0 &= P(x_{1}) &= x_{1}^{3} &- \sigma_{1} x_{1}^{2} &+\; \sigma_{2}x_{1} &- \sigma_{3} \\
        0 &= P(x_{2}) &= x_{2}^{3} &- \sigma_{1} x_{2}^{2} &+\; \sigma_{2}x_{2} &- \sigma_{3} \\
        0 &= P(x_{3}) &= x_{3}^{3} &- \sigma_{1} x_{3}^{2} &+\; \sigma_{2}x_{3} &- \sigma_{3} \\
        \hline
        \phantom 0 &\phantom = 0 &= S_{3} &- \sigma_{1}S_{2} &+\; \sigma_{2}\sigma_{1} &- 3 \sigma_{3}
    \end{align*}
$$

Or

$$
    \begin{align*}
        S_{2} &= \sum_{i=1}^{3}x_{i}^{2} \\
&= \left(\sum_{i=1}^{3}e_{i}\right)^{2} - 2 \sum_{1 \leq  i<j \leq  3} x_{i}x_{j} \\
&= \sigma_{1}^{2} - 2 \sigma_{2}
    \end{align*}
$$

donc

$$
\begin{align*}
    S_{3} &= \sigma_{1}(\sigma_{1}^{2} - 2 \sigma_{2}) - \sigma_{2}\sigma_{1} + 3 \sigma_{3} \\
          &= \sigma_{1}^{3} - 3 \sigma_{1}\sigma_{2} + 3 \sigma_{3}
\end{align*}
$$
