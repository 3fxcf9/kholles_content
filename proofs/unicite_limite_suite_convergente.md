---
title: Preuve de l'unicité de la limite d'une suite convergente
authors:
  - Julien Dubousquet
date: 11/28/2025
pid: 1764362602
tags:
  - Limites
---
**Soit $u \in \K^\N$, $(\ell_1,\ell_2) \in \K^2$.  
Si $u$ converge vers $\ell_1$ et $\ell_2$, alors $\ell_1 = \ell_2$.**

Par l'absurde, supposons que $u$ converge vers $\ell_1$ et $\ell_2$, et que $\ell_1 \neq \ell_2$.  
On prendra $\varepsilon_0 = \varepsilon_1 = \varepsilon_2$ assez petit pour que les tubes soient disjoints.  
Posons donc
$$
\varepsilon_0 = \frac{|\ell_1 - \ell_2|}{3}.
$$

- Appliquons la définition de la convergence de $u$ vers $\ell_1$ pour $\varepsilon \leftarrow \varepsilon_0$, ce qui est autorisé car $\varepsilon_0 \in \R_+^*$ :
  $$
  \exists N_1 \in \N : \forall n \geq N_1,\ |u_n - \ell_1| \leq \varepsilon_0
  \tag{1}
  $$
  $$
  \exists N_2 \in \N : \forall n \geq N_2,\ |u_n - \ell_2| \leq \varepsilon_0
  \tag{2}
  $$
  Fixons de tels $N_1$ et $N_2$.

- Posons $n_0 = N_1 + N_2$ :
  - $n_0 \geq N_1$, donc (1) s'applique : $|u_{n_0} - \ell_1| \leq \varepsilon_0$
  - $n_0 \geq N_2$, donc (2) s'applique : $|u_{n_0} - \ell_2| \leq \varepsilon_0$

- Alors :
  $$
  \begin{aligned}
  |\ell_1 - \ell_2|
    &= |\ell_1 - u_{n_0} + u_{n_0} - \ell_2| \\
    &\leq |\,\ell_1 - u_{n_0}\,| + |\,u_{n_0} - \ell_2\,| \\
    &\leq 2 \cdot \frac{|\ell_1 - \ell_2|}{3} \\
  \implies 1 &\leq \frac{2}{3}
  \end{aligned}
  $$
  Contradiction.

Donc $\ell_1 = \ell_2$.
