---
title: Propriété de morphisme du déterminant, caractérisation des automorphismes
authors:
  - Félix Rondeau
date: 18/05/2025
pid: 1747577215
tags:
  - déterminant
---

- $\det$ est un morphisme de $(\L_{\K}(E), \circ)$ dans $(\K, \times)$.

- Pour tout $f \in \L_{\K}(E)$,

  $$
      f \in \GL_{\K}(E) \iff \det f \neq 0
  $$

---

- Soient $(f,g) \in \L_{\K}(E)^{2}$.

  $$
      \begin{align*}
          \det(f\circ g) &= \det_{\B} ((f\circ g)(e_{1}), \ldots, (f\circ g)(e_{n}))  \\
  &= \det_{\B} ((f(g(e_{1})), \ldots, f(g(e_{n}))) \\
  &= \det f \times \det_{\B} (g(e_{1}), \ldots, g(e_{n})) \\
  &= \det f \times  \det g
      \end{align*}
  $$

- Soit $f \in \L_{\K}(E)$.

  - Supposons que $f \in \GL_{\K}(E)$. Appliquons la relation établie au point précédent pour $g \leftarrow f^{-1}$ :

    $$
        \det \underbrace{(f\circ f^{-1})}_{\det_{\Id_{E}}} = (\det f)\times (\det f^{-1})
    $$

    or $\det(\Id_{E}) = \det_{\B} (e_{1}, \ldots, e_{n}) = 1$ si bien que $(\det f)\times (\det f^{-1}) = 1$. On en déduit d’une part que $\det f \neq 0$ et d’autre part que $\det (f^{-1}) = \frac{1}{\det f}$.

  - Supposons que $\det f \neq 0$. Par définition du déterminant d’un endomorphisme,

    $$
        \det_{\B} (f(e_{1}), \ldots, f(e_{n})) = \det f \underbrace{\det_{\B}(e_{1}, \ldots, e_{n})}_{d=1} = \det f
    $$

    donc $\det_{\B} (f(e_{1}), \ldots, f(e_{n}))\neq 0$ si bien que la caractérisation des bases par le déterminant permet d’affirmer que $(f(e_{1}), \ldots, f(e_{n}))$ est une base de $E$. Par conséquent, $f$ est un endomorphisme de $E$ qui envoie la base $\B$ de $E$ sur une base de $E$ donc $f$ est un automorphisme de $E$.

