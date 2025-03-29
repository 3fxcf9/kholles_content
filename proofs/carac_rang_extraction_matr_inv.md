---
title: Caractérisation du rang par extraction de matrice inversible
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272910
tags:
  - algèbre linéaire
  - matrices
---

Le rang d’une matrice $A \in \M_{n,p}(\K)$ est la taille de la plus grande matrice carrée inversible extraite de A, i.e.

$$
    \rg A = \max\{d\in\iset{1,\min\{n,p\}} \mid \exists A'\in\mathcal E(A): A'\in\GL_n(\K)\}
$$

avec la convention que le plus grand élément d’un ensemble vide est nul.

---

Posons $r = \rg A$.

- Si $r=0$, alors $A = 0_{n,p}$ et toute matrice extraite de $A$ est une matrice nulle doonc l’ensemble défini ci dessus est vide, si bien que la convention adoptée permet de conclure à l’égalité annoncée.
- Supposons désormais $r \geq 1$. Notons $(C_{1}, \ldots,C_{p}) \in \M_{n,1}(\K)^{p}$ les colonnes de $A$.

  - Le rang d’une matrice étant égal à la dimension du sous-espace vectoriel engendré par ses colonnes, $\Vect\left\{C_{1}, \ldots, C_{p}\right\}$ est de dimension $r$, on peut donc extraire de cette famille génératrice une base de $\Vect\left\{C_{1}, \ldots, C_{p}\right\}$ : il existe $(j_{1}, \ldots, j_{r}) \in \iset{1,p}^{r}$ tels que $j_{1} < \cdots < j_{r}$ et tels que la famille $(C_{j_{1}}, \ldots, C_{j_{r}})$ est une base de $\Vect\left\{C_{1}, \ldots, C_{p}\right\}$.

    Par conséquent,

    $$
        E = \left(\begin{array}{c|c|c}
          C_{j_{1}} & \cdots & C_{j_{r}}
      \end{array}\right) \in M_{n,r}(\K)
    $$

    est une matrice de rang $r$ extraite de $A$. Notons $(L_{1}, \ldots, L_{n}) \in M_{1,r}(\K)^{n}$ les lignes de $E$ :

    $$
          E = \left(\begin{array}{c}
          L_{1} \\ \hline
          \vdots \\ \hline
          L_{n}
      \end{array}\right)
    $$

    Or le rang d’une matrice est égal à celui de sa transposée donc

    $$
        r = \rg E = \rg E\transp = \underbrace{\left(\begin{array}{c|c|c}
                L_{1}\transp & \cdots & L_{n}\transp
            \end{array}\right)}_{\in \M_{r,n}(\K)}
    $$

    Par conséquent, les $n$ colonnes $(L_{1}\transp, \ldots, L_{n}\transp)$ de $E\transp$ engendrent dans $\M_{r,1}(\K)$ un espace vectoriel de dimension $r$ donc il existe $(i_{1}, \ldots, i_{r}) \in \iset{1,n}^{r}$ tels que $i_{1} < \cdots < i_{r}$ et tels que $(L_{i_{1}}\transp, \ldots, L_{i_{r}}\transp)$ est une base de $\Vect\left\{L_{1}\transp, \ldots, L_{n}\transp\right\}$, de sorte que

    $$
        \rg \left(\begin{array}{c|c|c}
                L_{i_{1}}\transp & \cdots & L_{i_{n}}\transp
            \end{array}\right) = r
    $$

    Par conséquent,

    $$
        A' = \left(\begin{array}{c|c|c}
                L_{i_{1}}\transp & \cdots & L_{i_{n}}\transp
            \end{array}\right) = \left(\begin{array}{c}
          L_{i_{1}} \\ \hline
          \vdots \\ \hline
          L_{i_{n}}
      \end{array}\right) \in \M_{r}(\K)
    $$

    est une matrice de rang $r$ extraite de $A$. Le rang de $A'$ est égal à sa dimension donc $A' \in \GL_{r}(\K)$.

    On en déduit que

    $$
        \max\{d \in \iset{1,\min\{n,p\}} \mid \exists A' \in  \mathcal{E}(A): A' \in \GL_{d}(\K)\} \geq r
    $$

  - Soit $d \in \iset{1,\min\{n,p\}}$ tel qu’il existe $A' \in \GL_{d}(\K)$ une matrice extraite de $A$.
    Alors $\rg A' \leq \rg A = r$ donc, puisque $A'$ est inversible, $d \leq r$. Par conséquent,

    $$
        \max\{d \in \iset{1,\min\{n,p\}} \mid \exists A' \in  \mathcal{E}(A): A' \in \GL_{d}(\K)\} \leq  r
    $$
