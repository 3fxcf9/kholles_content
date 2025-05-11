---
title: Théorème spécial des séries alternées
authors:
  - Félix Rondeau
date: 05/11/2025
pid: 1746969102
tags:
  - intégration
---

Soit $(a_{n})_{n \geq n_{0}}$ une suite réelle. Si

- tous les termes de $(a_{n})$ sont positifs
- $(a_{n})$ est décroissante
- $(a_{n})$ converge vers 0

alors la série

$$
    \sum_{n \geq n_{0}}(-1)^{n}a_{n}
$$

est convergente, et de plus,

- la somme est de signe du premier terme de la somme
- $\forall n \in \iset{n_{0},+\infty}, \abs{R_{n}}\leq a_{n+1}$

---

- **Cas $n_{0}$ pair.** Notons $n_{0}=2p_{0}$.

  - Soit $p \geq p_{0}$.

  $$
  \begin{align*}
      S_{2(p+1)} - S_{2p} &= \sum_{k=2p_{0}}^{(-1)^{k}a_{k}} - \sum_{k=2p}^{2p}(-1)^{k}a_{k} \\
      &= (-1)^{2p+2} a_{2p+2} + (-1)^{2p+1}a_{2p+1} \\
      &= a_{2p+2} - a_{2p+1} \\
      &\leq 0 \quad\text{car } a \text{ est décroissante}
  \end{align*}
  $$

  de même

  $$
      \begin{align*}
          S_{2(p+1)+1} - S_{2p+1} &= (-1)^{2p+3}a_{2p+3} + (-1)^{2p+2}a_{2p+2} \\
          &= -a_{2p+3} + a_{2p+2} \\
          &\geq 0 \quad\text{car } a \text{ est décroissante}
      \end{align*}
  $$

  Ainsi, $(S_{2p+1})$ est croissante et $(S_{2p})$ est décroissante. De plus

  $$
      S_{2p+1}-S_{2p} = (-1)^{2p+1}a_{2p+1} = -a_{2p+1} \arrowlim{p\to +\infty}0
  $$

  si bien que ces deux suites sont adjacentes. Le théorème des suites adjacentes donne alors la convergence de ces suites vers une même limite finie $S_{\infty}$, ce qui permet d’affirmer que la suite $(S_{n})_{n \geq n_{0}}$ converge vers $S_{\infty}$.

  <br/>

  > **Signe de la série**: du fait de l’adjacence des suites $(S_{2p})$ et $(S_{2p+1})$,
  >
  > $$
  >    \forall (m,p)\in \iset{p_{0},+\infty}, S_{2m+1} \leq S_{\infty} \leq S_{2p} \quad (*)
  > $$
  >
  > en particulier pour $n \leftarrow p$, $S_{2p_{0}+1} \leq S_{\infty}$ donc $a_{2p_{0}}-a_{2p_{0}+1} \leq S_{\infty}$, donc $S_{\infty}\geq 0$.

- **Cas $n_{0}$ impair.** On adapte le cas précédent.

- **Contrôle du reste.** Soiit $n \in \iset{n_{0},+\infty}$.

  - si $n$ est pair, notons $n=2p$. Appliquons $(*)$ pour $p \leftarrow p_{n}$ et $m \leftarrow p_{n}$ :

    $$
        S_{2p_{n}+1} \leq S_{\infty} \leq  S_{2p_{n}}
    $$

    En retranchant $S_{2p_{n}}$,

    $$
        -a_{2p_{n}+1} \leq S_{\infty} - S_{2p_{n}} \leq  0
    $$

    donc $-a_{n+1} \leq R_{n} \leq 0$, si bient que $\abs{R_{n}} \leq a_{n+1}$.

  - si $n$ est impair, notons $n = 2p+1$. Appliquons $(*)$ pour $m \leftarrow  p_{n}$ et $p \leftarrow  p_{n}+1$ :

    $$
        S_{2p_{n}+1} \leq S_{\infty} \leq S_{2p_{n}+2}
    $$

    En retranchant $S_{2p_{n}+1}$,

    $$
        0 \leq S_{\infty} - S_{2p_{n}+1} \leq a_{2p_{n}+2}
    $$

    donc $0 \leq R_{n} \leq  a_{n+1}$ si bien que $\abs{R_{n}} \leq  a_{n+1}$.

