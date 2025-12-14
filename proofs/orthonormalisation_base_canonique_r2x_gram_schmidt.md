---
title: Orthonormalisation de la base canonique de $\mathbb R_2[X]$ avec la méthode de Gram-Schmidt
authors:
  - Félix Rondeau
date: 05/25/2025
pid: 1748173460
tags:
  - orthogonalité
---

Orthonormaliser la base canonique de $\R_{2}[X]$ pour le produit scalaire

$$
    \scalar P Q = \int_{0}^{1}P(u)Q(u)\dd u
$$

---

- $E_{0} = \frac{1}{\norm{1}} = 1$ car $\norm 1 = \int_{0}^{1}\dd u = 1$

- On a

  $$
    U_{1} = X - p\ortho_{\Vect\left\{E_{0}\right\}}(X) = X-\scalar{X}{E_{0}}E_{0} = X-\frac{1}{2}
  $$

  et

  $$
      \norm{U_{1}}^{2} = \int_{0}^{1}\left(u-\frac{1}{2}\right)^{2}\dd u = \left[\frac{1}{3}\left(u-\frac{1}{2}\right)^{3}\right]^{0}_{1} = \frac{1}{12}
  $$

  donc

  $$
      E_{1} = \frac{U_{1}}{\norm{U_{1}}} = 2 \sqrt{3} \left(X-\frac{1}{2}\right) = 2 \sqrt{3}X - \sqrt{3}
  $$

- On a

  $$
  \begin{align*}
      U_{2} &= X^{2} - p\ortho_{\Vect\left\{E_{0}, E_{1}\right\}}\\
  &= X^{2} - \left(\scalar{X^{2}}{E_{0}}E_{0} + \smash{\underbrace{\scalar{X^{2}}{E_{1}}}_{(2 \sqrt{3})^{2} \left(\int_{0}^{1}u^{2} \left(u-\frac{1}{2}\right)\dd u\right)\left(X-\frac{1}{2}\right) = 12 \Bigl(\smash{\underbrace{\left[\frac{1}{4}u^{4} - \frac{1}{6}u^{3}\right]_{0}^{1}}_{ = \frac{1}{4} - \frac{1}{6} = \frac{1}{12}}}\Bigr)\left(X-\frac{1}{2}\right)}}E_{1}\right)\\
  \\\\\\
  &= X^{2}-\frac{1}{3} - \left(X-\frac{1}{2}\right) = X^{2} - X + \frac{1}{6}
  \end{align*}
  $$

  et

  $$
      \begin{align*}
          \norm{U_{2}}^{2} &= \int_{0}^{1}\left(u^{2} - u + \frac{1}{6}\right)^{2}\dd u \\
  &= \int_{0}^{1}\left(u^{4} + u^{2} + \frac{1}{36} - 2u^{3} + \frac{1}{3}u^{2} - \frac{1}{3}u\right)\dd u \\
  &= \left[\frac{u^{5}}{5} + \frac{4}{9}u^{3} + \frac{u}{36} - \frac{2}{4}u^{4} - \frac{1}{6}u^{2}\right]_{0}^{1} \\
  &= \frac{1}{5} + \frac{4}{9} + \frac{1}{36} - \frac{1}{2} - \frac{1}{6} \\
  &= \frac{1}{5} + \frac{16 + 1 - 24}{36} \\
  &= \frac{36-7 \times 5}{5 \times 36} \\
  &= \frac{1}{5 \times 36} = \frac{1}{(6\sqrt{5})^{2}}
      \end{align*}
  $$

  si bien que

  $$
      E_{2} = \frac{U_{2}}{\norm {U_{2}}} = 6 \sqrt{5}\left(X^{2} - X + \frac{1}{6}\right) = 6 \sqrt{5}X^{2} - 6\sqrt{5}X - \sqrt{5}
  $$

