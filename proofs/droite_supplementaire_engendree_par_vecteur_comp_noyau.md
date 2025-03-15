---
title: Droite supplémentaire du noyau engendré par un vecteur du complémentaire du noyau
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060871
tags:
  - algèbre linéaire
---

Si $E$ est un $\K$-espace vectoriel et $\varphi \in E^{*}$ non nulle, alors pour tout $a \in E \setminus \Ker \varphi$,

$$
    E=\Ker \varphi \oplus \Vect\{a\}
$$

---

Soit $a \in E \setminus \Vect\left\{a\right\}$ fixé quelconque.

- _Analyse :_ Soit $x \in E$ fixé quelconque. Supposons qu’il existe $x_{K}\in \Ker \varphi$ et $x_{a}\in \Vect\left\{a\right\}$ tels que $x=x_{K}+x_{a}$. Par définition de $\Vect\left\{a\right\}$, il existe $\lambda \in \K$ tel que $x_{a}=\lambda \cdot a$, d’où $x=x_{K} + \lambda \cdot a$.

  $$
      \varphi(x) = \underbrace{\varphi(x_{K})}_{=0_{\K}} + \lambda \cdot \varphi(a) = \lambda \times_{\K}\varphi(a)
  $$

  or $a\notin \Ker \varphi$ donc $\varphi(a)\neq 0_{\K}$ donc $\varphi(a)$ est inversible dans $\K$. Ainsi, $\lambda=\frac{\varphi(x)}{\varphi(a)}$ donc $x_{a}=\frac{\varphi(x)}{\varphi(a)}\cdot a$ et $x_{K} = x-x_{a}$ sont parfaitement définis, donc uniques sous réserves d’existence.

- _Synthèse :_ Soit $x \in E$ fixé quelconque. Posons $x_{a}=\frac{\varphi(x)}{\varphi(a)}\cdot a$ et $x_{K} = x-x_{a}$. Alors,
  - $x_{a} \in \Vect\left\{a\right\}$
  - $\varphi(x_{K}) = \varphi(x) - \frac{\varphi(x)}{\varphi(a)}\cdot \varphi(a) = \varphi(x) - \frac{\varphi(x)}{\varphi(a)} \times \varphi(a) = 0_{\K}$
  - $x_{K} + x_{a} = x$

Ainsi, $\Ker \varphi \oplus \Vect\left\{a\right\} = E$.
