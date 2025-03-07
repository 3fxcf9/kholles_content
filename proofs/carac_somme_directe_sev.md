---
title: Caractérisation de la somme directe de sous-espaces vectoriels
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353631
tags:
  - algèbre linéaire
---

Soient $E$ un $\K$-espace vectoriel, $p\in\N^{*}$, $(E_{i})_{i\in\iset{1,p}}$ $p$ sous-espaces vectoriels de $E$.
Les $p$ sous-espaces vectoriels $E_{1}, \dots, E_{p}$ d’un $\K$-espace vectoriel $E$ sont en somme directe si et seulement si

$$
    \forall (x_{1},\dots, x_{p})\in E_{1} \times \cdots \times E_{p}, (x_{1}+ \cdots  + x_{p} = 0_{E} \implies  \forall i\in\iset{1,p}, x_{i}=0_{E})
$$

---

- $(\implies)$ Supposons que $E_{1}, \dots, E_{p}$ sont en somme directe. Soient $(x_{1}, \dots, x_{p})\in E_{1} \times  \cdots  \times E_{p}$ fixés quelconques tels que

  $$
      x_{1} + \cdots + x_{p} = 0_{E}
  $$

  Or $0_{E} = \underbrace{0_{E}}_{\in E_{1}}+\underbrace{0_{E}}_{\in E_{2}}+\cdots +\underbrace{0_{E}}_{\in E_{p}}$ si bien que l’unicité de l’écriture de $0_{E}$ comme somme de vecteurs de $E_{1},\dots,E_{p}$ permet d’affirmer que

  $$
      \forall i\in\iset{1,p}, x_{i}=0_{E}
  $$

- $(\impliedby)$ Supposons que $\forall (x_{1},\dots,x_{p})\in E_{1} \times \cdots \times E_{p}, (x_{1}+\cdots +x_{p}=0_{E} \implies \forall i\in\iset{1,p}, x_{i}=0_{E})$. Soit $x\in E_{1}+\cdots +E_{p}$ tel que

  $$
      \exists (x'_{1}, \dots, x'_{p})\in E_{1}\times \cdots \times E_{p} : x = x'_{1} + \cdots + x'_{p}
  $$

  et

  $$
      \exists (x''_{1}, \dots, x''_{p})\in E_{1}\times \cdots \times E_{p} : x = x''_{1} + \cdots + x''_{p}
  $$

  Alors

  $$
      x'_{1} +\cdots +x'_{p} = x''_{1} + \cdots + x''_{p} \iff \underbrace{(x'_{1}-x''_{1})}_{\in E_{1}} + \cdots + \underbrace{(x'_{p}-x''_{p})}_{\in E_{p}} = 0_{E}
  $$

  si bien que l’hypothèse faite ci-dessus pour prouver le sens réciproque appliqué pour $x_{1} = x'_{1}-x''_{1}\in E_{1}, \dots, x_{p} = x'_{p}-x''_{p}\in E_{p}$ permet d’affirmer que

  $$
    \forall i\in\iset{1, p}, x'_{i}-x''_{i} = 0_{E}
  $$

  c’est à dire

  $$
      \forall i\in\iset{1, p}, x'_{i} = x''_{i}
  $$

  Ainsi, tout vecteur de $E_{1} + \cdots + E_{p}$ s’écrit de manière unique comme somme d’un vecteur de $E_{1}$, d’un vecteur de $E_{2}$, ..., d’un vecteur de $E_{p}$, donc cette somme est directe.
