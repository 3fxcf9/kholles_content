---
title: Produit d’une matrice carrée avec la transposée de sa comatrice
authors:
  - Félix Rondeau
date: 18/05/2025
pid: 1747578250
tags:
  - déterminant
  - matrices
---

Si $A$ est une matrice carrée de taille $n$,

$$
    A \times (\com A)\transp = \det (A)I_{n}
$$

---

Soient $(i,j)\in \icc{1,n}^{2}$.

$$
    \begin{align*}
        \left[A \times (\com A)\transp\right]_{i,j} &= \sum_{k=1}^{n}A_{i,k} \times \left[(\com A)\transp\right]_{k,j} \\
                                                    &= \sum_{k=1}^{n} A_{i,k} \times \left[\com A\right]_{j,k} \\
                                                    &= \sum_{k=1}^{n}A_{i,k} \times (-1)^{k+j}\Delta_{j,k}
    \end{align*}
$$

- Supposons que $i=j$. Alors

  $$
      \left[A \times (\com A)\transp\right]_{i,i} = \sum_{k=1}^{n}A_{i,k}\times (-1)^{k+i}\Delta_{i,k} = \det A
  $$

  d’après la formule du développement du déterminant de $A$ selon la $i$-ième ligne.

- Supposons que $i\neq j$. Alors la formule peut être interprétée comme le développement selon la $j$-ième ligne du déterminant de la matrice obtenue à partir de $A$ en remplaçant sa $j$-ième ligne par sa $i$-ième ligne :

  $$
      \begin{align*}
          \left[A \times (\com A)\transp\right]_{i,j} &= \sum_{k=1}^{n}A_{i,k} \times (-1)^{k+j} \Delta_{j,k} \\
  &= \begin{vmatrix}
      L_{1} \\\hline
      \vdots \\\hline
      \qquad L_{i-1} \qquad \\\hline
      L_{i} \\\hline
      L_{i+1} \\\hline
      \vdots \\\hline
      L_{j-1} \\\hline
      L_{j} \\\hline
      L_{j+1} \\\hline
      \vdots \\\hline
      L_{n}
  \end{vmatrix} \\
  &= 0 \quad\text{(lignes } i \text{ et } j \text{ identiques)}
      \end{align*}
  $$

  Ainsi, pour tous $(i,j) \in \icc{1,n}^{2}, \left[A \times (\com A)\transp\right]_{i,j} = \delta_{i,j}\det A$ donc $A \times (\com A)\transp = (\det A)\cdot I_{n}$.

