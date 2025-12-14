---
title: Primitives des éléments simples de première et seconde espèce
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746294155
tags:
  - DES
  - intégration
---

- Primitives d’un élément simple de première espèce de la forme

  $$
      x \longmapsto \frac{1}{(x-z_{0})^{p}}
  $$

  - si $p \geq 2$, elles sont de la forme

    $$
        x \longmapsto \frac{-\frac{1}{p-1}}{(x-z_{0})^{p-1}}
    $$

    et définies sur $\oo{-\infty,x_{0}}$ ou $\oo{x_{0}, +\infty}$ si $x_{0}$ est réel et sur $\R$ sinon.

  - si $p=1$, elles ont été calculées dans <a href="#1746268034">cette question</a>.

- Primitives d’un élément simple de seconde espèce de la forme

  $$
      x \longmapsto \frac{ax+b}{(x^{2}+\alpha x + \beta)^{p}}
  $$

  avec $a,b, \alpha$ et $\beta$ des réels tels que $\alpha^{2} - 4 \beta < 0$ et $p \in \N^{*}$.

  - si $p=1$, on les obtient en intégrant la totalité du terme de degré 1 du numérateur en logarithme et en intégrant la fraction constituée de la constante et du dénominateur en arctangente en mettant le trinôme sous forme canonique.
  - si $p \geq 2$, on les obtient en intégrant la totalité du terme de degré 1 du numérateur dans une composée du type $\frac{f'}{f^{p}}$ puis en se concentrant sur fraction constituée de la constante et du dénominateur. Il faut ensuite mettre le trinôme sous forme canonique avant de se ramener, par changement de variable et mise sous la forme canonique, à chercher une pmimitive de $x \longmapsto \frac{1}{(1+x^{2})^{p}}$.

