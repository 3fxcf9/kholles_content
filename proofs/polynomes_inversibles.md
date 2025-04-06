---
title: Inversibles de l’anneau $\K[X]$
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933250
tags:
  - polynômes
---

Les éléments inversibles de l’anneau $(\K[X], +, \times)$ sont les polynômes constants non nuls.

---

- Soit $A \in \K^{\times}$ fixé quelconque. Il existe $B \in \K[X]$ tel que $AB=X^{0}$. En prenant le degré,

  $$
      \underbrace{\deg A}_{\in \N \cup \{-\infty\}} + \underbrace{\deg B}_{\in \N \cup \{-\infty\}} = 0
  $$

  donc $\deg A=0$ donc $A$ est un polynôme constant non nul.

- Soit $A$ un polynôme constant non nul. Alors il existe $\lambda \in \K^{*}$ tel que $A=\lambda \cdot X^{0}$. Posons $B=\lambda^{-1}\cdot X^{0}$ ce qui a un sens car $\lambda$ est non nul.

  $$
  \begin{align*}
      A \times B &= (\lambda \cdot X^{0}) \times (\lambda^{-1}\cdot X^{0}) \\
                 &= (\lambda \times  \lambda^{-1})\cdot X^{0} \\
                 &= X^{0}
  \end{align*}
  $$

  donc par commutativité de la loi $\times_{\K[X]}$, $A$ est inversible.
