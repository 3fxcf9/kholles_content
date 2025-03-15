---
title: Existence d’un supplémentaire pour tout sous-espace d’un espace vectoriel de dimension finie
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060865
tags:
  - algèbre linéaire
---

Soit $F$ un sous-espace vectoriel d’un $\K$-espace vectoriel $E$ de dimension finie. Alors il existe un sous-espace vectoriel $F'$ de $E$ tel que

$$
    F\oplus F'=E
$$

---

- si $F=\{0_{E}\}$, $F'=E$ convient
- sinon, $F$ est un sous-espace vectoriel de dimension finie non réduit au vecteur nul. Le théorème d’existence de la base en dimension finie donne alors l’existence d’une base $B$ de $F$, que le théorème de la base incomplète permet de compléter par la famille de vecteurs $B'$ de $E$ en une base $(B, B')$. Posons $F'=\Vect B'$ et notons $(e_{1}, \dots, e_{p})$ la base $B$, et $(e_{p+1}, \dots, e_{n})$ la famille $B'$.

  - _$F$ et $F'$ sont en somme directe :_ Soit $x\in F\cap F'$ fixé quelconque. $F=\Vect B$ donc

  $$
      \exists (\lambda_{1},\dots, \lambda_{p})\in\K^{p}: x=\sum_{i=1}^{p}\lambda_{i}e_{i}
  $$

  et $F'=\Vect B'$ donc

  $$
      \exists (\lambda_{p+1},\dots,\lambda_{n})\in\K^{p+1}: x=\sum_{i=p+1}^{n}\lambda_{i}e_{i}
  $$

  donc

  $$
      \sum_{i=1}^{p}\lambda_{i}e_{i} - \sum_{i=p+1}^{n}\lambda_{i}e_{i} = 0_{E}
  $$

  or $(e_{1},\dots, e_{p}, e_{p+1}, \dots, e_{n}) = (B,B')$ est libre dans $E$ (c’est est une base), donc

  $$
      \lambda_{1}=\dots =\lambda_{p} = -\lambda_{p+1} = \dots = -\lambda_{n} = 0_{E}
  $$

  d’où

  $$
      x=\sum_{i=1}^{p}\lambda_{i}e_{i} = 0_{E}
  $$

  ce qui montre l’inclusion directe, et donc l’égalité $F\cap F'=\{0_{E}\}$.

  - _$F+F'=E$ :_

    - L’inclusion directe est immédiate.
    - Soit $x\in E$ fixé quelconque. $(e_{1},\dots, e_{p}, e_{p+1}, \dots, e_{n})$ est une base de $E$ donc

      $$
          \exists (\lambda_{i})_{i\in\iset{1,n}}\in\K^{n}: x=\sum_{i=1}^{n}\lambda_{i}e_{i}
      $$

      donc

      $$
          x=\underbrace{\sum_{i=1}^{p}\lambda_{i}e_{i}}_{\in F} + \underbrace{\sum_{i=p+1}^{n}\lambda_{i}e_{i}}_{\in F'} \in F+F'
      $$

      ce qui montre l’inclusion réciproque.
