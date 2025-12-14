---
title: Densité des matrices inversibles dans les matrices carrées
authors:
  - Félix Rondeau
date: 05/24/2025
pid: 1748100909
tags: []
---

Les matrices inversibles sont denses les matrices carrées pour toute norme.

---

Soit $N$ une norme sur $\M_{n}(\C)$, $X \in \M_{n}(\C)$ et $\varepsilon \in \R_{+}^{*}$. Posons pour tout $t \in \R$, $M_{t} = X + tI_{n}$.

$$
    N(M_{t} - X) = N(X + t I_{n} - X) = N(tI_{n}) = \abs{t}N(I_{n})
$$

Considérons l’application

$$
    f: \applic{\R}{\C}{t}{\det_{\C} M_{t}}
$$

qui est une fonction polynomiale (polynomialité du déterminant) de degré $n$. Notons $(z_{1}, \ldots, z_{n})\in C^{n}$ ses racines répétées avec multiplicité. Posons

$$
    m = \min\{\abs{z_{i}} \mid i \in \icc{1,n}, z_{i} \neq 0\} \cup \{232\}
$$

qui est bien défini comme minimum d’une partie fini non vide d’un ensemble totalement ordonné. De plus, $m>0$ et

$$
    \forall t \in \oo{0,m}, f(t)\neq 0
$$

donc $M_{t} \in \GLM_{n}(\C)$. Posons à présent

$$
    t_{0} = \min \left\{\frac{m}{2}, \frac{\varepsilon}{N(I_{n})}\right\}
$$

alors, $t_{0} \in \oo{0,m}$ donc $M_{t_{0}} \in \GLM_{n}(\C)$, et de plus

$$
    0 < t_{0} \leq \frac{\varepsilon}{N(I_{n})}
$$

donc

$$
    N(M_{t_{0}} - X) = \abs{t_{0}}N(I_{n})\leq \varepsilon
$$
