---
title: L’ensemble des automorphismes d’un espace vectoriel est un groupe
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353630
tags:
  - algèbre linéaire
---

L’ensemble des automorphismes d’un $\K$-espace vectoriel muni de la loi $\circ$ est un groupe noté $(\GL_{\K}(E), \circ)$ et appelé le groupe linéaire du $\K$-espace vectoriel $E$.

---

Montrons qu’il s’agit d’un sous-groupe du groupe $(\mathcal{S}(E), \circ)$ des permutations de $E$.

- $\GL_{\K}(E)\subseteq \mathcal{S}(E)$
- $\GL_{\K}(E)$ n’est pas vide car contient $\Id_{E}$
- Soient $(f,g)\in\GL_{\K}(E)^{2}$ fixés quelconques. Montrons que $g\circ f^{-1}\in\GL_{\K}(E)$.

  - $g\circ f^{-1}$ est une bijection puisque $(\mathcal{S}(E), \circ)$ est un groupe
  - $f^{-1}$ est linéaire: Soient $(\alpha, \beta, x, y)\in\K^{2}\times E^{2}$ fixés quelconques.

    $$
        \begin{align*}
            f^{-1}(\alpha \cdot x + \beta \cdot  y) &= f^{-1}(\alpha \cdot f(f^{-1}(x))+\beta \cdot f(f^{-1}(y))) \\
            &= f^{-1}\Bigl(f\Bigl(\alpha \cdot \left(f^{-1}(x)\right)+\beta \cdot  \left(f^{-1}(y)\right)\Bigr)\Bigr) \\
            &= \left(f^{-1}\circ f\right)\Bigl(\alpha \cdot f^{-1}(x) + \beta \cdot  f^{-1}(y)\Bigr) \\
            &= \alpha \cdot  f^{-1}(x) + \beta \cdot f^{-1}(y)
        \end{align*}
    $$

  Par conséquent, $g\circ f^{-1}\in\GL_{\K}(E)$.
