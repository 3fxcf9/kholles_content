---
title: Équivalence $\mathcal{F}$ base, tout vecteur se décompose de manière unique dans $\mathcal{F}$, $\mathcal{F}$ générarice minimale et $\mathcal{F}$ libre maximale.
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1740414410
tags:
  - algèbre linéaire
---

Si $E$ est un $\K$-espace vectoriel et $\mathcal{F}$ une famille de vecteurs de $E$, les propositions suivantes sont équivalentes&nbsp;:

1. $\mathcal{F}$ est une base de $E$
2. Tout vecteur de $E$ s’écrit d’une manière unique comme une combinaison linéaire des vecteurs de $\mathcal F$
3. $\mathcal{F}$ est une famille génératrice minimale (au sens de l’inclusion)
4. $\mathcal{F}$ est une famille libre maximale (au sens de l’inclusion)

---

Notons $(a_{i})_{i\in I}$ la famille $\mathcal{F}$.

- $\bigl((i) \implies (ii)\bigr)$ Supposons que $\mathcal{F}$ est une base de $E$. Soit $x\in E$ fixé quelconque.

  - $\mathcal{F}$ est une base donc $\mathcal{F}$ est génératrice donc $x$ s’écrit comme une combinaison linéaire de vecteurs de $\mathcal{F}$
  - $\mathcal{F}$ est une base donc $\mathcal{F}$ est libre donc $x$ s’écrit de manière unique comme combinaison linéaire de vecteurs de $\mathcal{F}$

- $\bigl((ii) \implies (iii)\bigr)$ Supposons que tout vecteur de $E$ s’écrit d’une manière unique comme une combinaison linéaire des vecteurs de $\mathcal{F}$. Alors $E\subset \Vect \mathcal{F}$ or $\Vect \mathcal{F}\subset E$ donc $\Vect \mathcal{F} = E$ donc $\mathcal F$ est génératrice.

  > _Rappel&nbsp;:_ $\mathcal{F}$ est génératrice minimale signifie qu’aucune sous-famille stricte de $\mathcal{F}$ n’est génératrice. Il suffit donc de montrer qu’une sous-famille $\mathcal{F}'$ de $\mathcal{F}$ quelconque n’est pas génératrice.

  Soit $\mathcal{F'}$ une sous-famille stricte de $\mathcal{F}$; supposons-la génératrice. Par définition, il existe un élément $a$ de $\mathcal{F}$ n’appartenant pas à $\mathcal{F'}$. De plus, $\mathcal{F'}$ étant génératrice, cet élément s’écrit comme combinaison linéaire de vecteurs de $\mathcal{F'}$ (combinaison linéaire des vecteurs de $\mathcal{F}$ avec le coefficient devant $a$ nul). Or $a=1 \cdot a$ ce qui contredit l’unicité de lécriture de $a$ comme combinaison linéaire de vecteurs de $\mathcal{F}$. Ainsi, $\mathcal{F}$ est génératrice minimale.

- $\bigl((iii) \implies (iv)\bigr)$ Supposons que $\mathcal{F}$ est une famille génératrice minimale. Représentons $\mathcal{F}$ par $(x_{i})_{i\in I}$.

  - Supposons $\mathcal{F}$ liée. Alors un des vecteur doté $x_{i_{0}}$ s’écrit comme combinaison linéaire des autres vecteurs de la famille : $x_{i_{0}} \in \left\{x_{i} \mid i\in I\setminus \{i_{0}\}\right\}$. Or $\mathcal{F}$ est génératrice donc $(x_{i})_{i\in I\setminus \{i_{0}\}}$ l’est également. Ainsi $(x_{i})_{i\in ei\setminus \{i_{0}\}}$ est une sous-famille stricte de $\mathcal{F}$ qui est génératrice, ce qui contredit le caractère générateur minimal de $\mathcal{F}$, donc $\mathcal{F}$ est libre.

  - > _Rappel&nbsp;:_ $\mathcal{F}$ est libre maximale signifie que toute famille ayant $\mathcal{F}$ comme sous-famille stricte est liée, ou encore qu’il n’existe pas de famille libre contenant strictement $\mathcal{F}$

    Soit $\mathcal{F'}$ une famille libre admettant $\mathcal{F}$ comme sous-famille stricte. Notons $a$ un élément de $\mathcal{F}$ n’appartenant pas à $\mathcal{F'}$.

    $\mathcal{F}$ est génératrice donc $a\in\Vect\mathcal{F}$ donc $a$ s’écrit comme combinaison linéaire des autres vecteurs de $\mathcal{F'}$. Or $a\in \mathcal{F'}$ donc $\mathcal{F'}$ est liée d’où une contradiction. Ainsi $\mathcal{F}$ n’admet aucune famille libre la contenant strictement, donc $\mathcal{F}$ est libre maximale.

- $\bigl((iv) \implies (i)\bigr)$ Supposons que $\mathcal{F}$ est une famille libre maximale.
  - $\mathcal{F}$ est libre
  - Supposons que $\mathcal{F}$ n’est pas génératrice. Alors $\Vect\mathcal{F} \varsubsetneq E$ donc $\exists a\in E: a\notin \Vect \mathcal{F}$, or $\mathcal{F}$ est libre donc $(\mathcal{F}, a)$ (adjonction du vecteur $a$ à la famille $\mathcal{F}$) est libre, ce qui contredit le fait que $\mathcal{F}$ est libre maximale (car $(\mathcal{F}, a)$ est libre et admet $\mathcal{F}$ comme sous-famille stricte). Par conséquent, $\mathcal{F}$ est génératrice, et ainsi, $\mathcal{F}$ est une base de $E$.
