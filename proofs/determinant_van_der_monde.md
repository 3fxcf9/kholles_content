---
title: Déterminant de Van der Monde
authors:
  - Félix Rondeau
date: 18/05/2025
pid: 1747580788
tags:
  - matrices
  - déterminant
---

Soient $(a_0, a_1, \ldots, a_n) \in \mathbb{K}^{n+1}$ fixés quelconques.

$$
\begin{vmatrix}
1 & 1 & \cdots & 1 \\
a_0 & a_1 & \cdots & a_n \\
a_0^2 & a_1^2 & \cdots & a_n^2 \\
\vdots & \vdots & & \vdots \\
a_0^n & a_1^n & \cdots & a_n^n
\end{vmatrix}
= \prod_{0 \leq i < j \leq n} (a_j - a_i)
$$

---

Considérons la propriété $\mathcal{P}(n)$ définie pour tout $n \geq 1$ par

$$
\mathcal{P}(n) : \left( \forall (a_0, a_1, \ldots, a_n) \in \mathbb{K}^{n+1}, \quad
\begin{vmatrix}
1 & 1 & \cdots & 1 \\
a_0 & a_1 & \cdots & a_n \\
a_0^2 & a_1^2 & \cdots & a_n^2 \\
\vdots & \vdots & & \vdots \\
a_0^n & a_1^n & \cdots & a_n^n
\end{vmatrix}
= \prod_{0 \leq i < j \leq n} (a_j - a_i) \right)
$$

- Soient $(a_0, a_1) \in \mathbb{K}^2$ fixés quelconques.

  $$
  \begin{vmatrix}
  1 & 1 \\
  a_0 & a_1
  \end{vmatrix}
  = a_1 - a_0 = \prod_{0 \leq i < j \leq 1} (a_j - a_i)
  $$

  Ainsi, $\mathcal{P}(1)$ est vraie.

  - Soit $n \in \mathbb{N}^*$ fixé quelconque tel que $\mathcal{P}(n)$ est vraie.

  Soient $(a_0, a_1, \ldots, a_{n+1}) \in \mathbb{K}^{n+2}$ fixés quelconques.

  - **Supposons que les éléments de $\{a_0, \ldots, a_{n+1}\}$ ne sont pas tous deux à deux distincts.**  
    Alors le déterminant à calculer possède deux colonnes identiques donc il est nul et la formule avec laquelle il doit coïncider s’annule également, donc $\mathcal{P}(n+1)$ est vraie dans ce cas.

  - **Supposons que les éléments de $\{a_0, \ldots, a_{n+1}\}$ sont tous deux à deux distincts.**
    Notons

    $$
    Q(X) =
          \begin{vmatrix}
          1 & 1 & \cdots & 1 & 1 \\
          a_0 & a_1 & \cdots & a_n & X \\
          a_0^2 & a_1^2 & \cdots & a_n^2 & X^2 \\
          \vdots & \vdots & & \vdots & \vdots \\
          a_0^{n+1} & a_1^{n+1} & \cdots & a_n^{n+1} & X^{n+1}
          \end{vmatrix}
    $$

    L’objectif, pour prouver $\mathcal{P}(n+1)$ est de montrer que $Q(a_{n+1}) = \prod_{0 \leq i < j \leq n+1} (a_j - a_i)$.

    Sachant que le déterminant d’une matrice est une somme de produits de coefficients de la matrice, puisque tous les coefficients du déterminant définissant $Q(X)$ sont des polynômes en $X$, $Q(X) \in \mathbb{K}[X]$ (car $\mathbb{K}[X]$ est un anneau dont stable par somme et produit).

    De plus, en développant le déterminant $Q(X)$ selon sa dernière colonne, on observe d’une part que $\deg Q \leq n+1$ (car il s’agit du degré du coefficient de $X^{n+1}$ et le cofacteur de $X^{n+1}$, qui en utilisant la propriété $\mathcal{P}(n)$, vaut $\prod_{0 \leq i < j \leq n} (a_j - a_i)$. Or, par hypothèse, les éléments de $\{a_0, \ldots, a_n\}$ sont tous deux à deux distincts donc $\prod_{0 \leq i < j \leq n} (a_j - a_i) \ne 0$.

    Donc $Q$ est un polynôme de degré $n+1$.

    Enfin, $Q(a_0) = 0$, $Q(a_1) = 0$, …, $Q(a_n) = 0$ car le déterminant présente dans chacun de ces calculs deux colonnes égales. Nous en déduisons que $Q$ admet au moins $(n+1)$ racines deux à deux distinctes, or son degré est exactement $n+1$ donc

    - il n’y a aucune autre racine,
    - toutes les racines sont simples.

    La forme factorisée de $Q(X)$ est donc

    $$
    Q(X) = \underbrace{\left( \prod_{0 \leq i < j \leq n} (a_j - a_i) \right)}_{\text{coefficient dominant}} \times \underbrace{\prod_{k=0}^{n} (X - a_k)^1}_{(n+1) \text{ racines simples}}
    $$

    Si bien que :

    $$
        \begin{align*}
            Q(a_{n+1}) &= \left( \prod_{0 \leq i < j \leq n} (a_j - a_i) \right) \times \prod_{k=0}^{n} (a_{n+1} - a_k) \\
            &= \left( \prod_{0 \leq i < j \leq n} (a_j - a_i) \right) \times \prod_{\substack{0 \leq i < j \leq n+1 \\ j = n+1}} (a_j - a_i)\\
            &= \prod_{0 \leq i < j \leq n+1} (a_j - a_i)
        \end{align*}
    $$

    Ainsi, $\mathcal{P}(n+1)$ est vraie.

