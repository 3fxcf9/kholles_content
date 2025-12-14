---
title: Absolue convergence et convergence
authors:
  - Félix Rondeau
date: 05/18/2025
pid: 1747562588
tags:
  - séries
---

Soit $(u)_{n \geq n_{0}}$ une suite à valeurs dans le corps $\K$.
Si la série de terme général $u$ est absolument convergente, alors elle est convergente.

---

- Supposons que $u$ soit le terme général d’une **série absolument convergente réelle**.
  Posons, pour tout $n \in \ico{n_{0},+\infty}, u_{n}^{+} = \max\{u_{n},0\}$ et $u_{n}^{-} = -\min\{u_{n},0\}$.
  Avec ces notations, pour tout $n \in \ico{n_{0},+\infty}$, $u_{n}^{+}\geq 0$, $u_{n}^{-}\geq 0$, $\abs{u_{n}} = u_{n}^{+} + u_{n}^{-}$ et $u_{n} = u_{n}^{+} - u_{n}^{-}$. En effet,

  - si $u_{n} \geq 0$, alors $u_{n}^{+} = u_{n}$ et $u_{n}^{-} = 0$ donc $u_{n}^{+} + u_{n}^{-} = u_{n} = \abs{u_{n}}$ et $u_{n}^{+} - u_{n}^{-} = u_{n} - 0 = u_{n}$.
  - si $u_{n} \leq 0$, alors $u_{n}^{+} = 0$ et $u_{n}^{-} = -u_{n}$ donc $u_{n}^{+} + u_{n}^{-} = -u_{n} = \abs{u_{n}}$ et $u_{n}^{+} - u_{n}^{-} = 0 - (-u_{n}) = u_{n}$.

  Ainsi, pour tout $n \in \ico{n_{0},+\infty}$,

  - $u_{n}^{+} \geq 0$
  - $\abs{u_{n}} \geq 0$
  - $u_{n}^{+} \leq  \abs{u_{n}}$
  - $\sum_{n \geq n_{0}}\abs{u_{n}}$ converge (hyp.)

  ce qui permet d’appliquer le critère de convergence par comparaison pour obtenir la convergence de la série de terme général $u_{n}^{+}$.

  On montre de même que la série de terme général $u_{n}^{-}$ converge, ce qui permet, du fait de la structure de $\R$-espace vectoriel des suites étant terme général d’une série convergente, d’aboutir à la convergence de la série $\sum_{n \geq n_{0}}u_{n}$.

- Supposons que $u$ soit le terme général d’une **série absolument convergente complexe**.
  Posons pour tout $n \in \ico{n_{0},+\infty}$, $a_{n} = \Re(u_{n})$ et $b_{n} = \Im(u_{n})$.
  Alors, pour tout $n \in \ico{n_{0},+\infty}$,

  - $\abs{a_{n}} = \abs{\Re(u_{n})} \leq \abs{u_{n}}$
  - $\abs{a_{n}} \geq 0$
  - $\abs{u_{n}} \geq 0$

  ce qui permet d’utiliser le critère de convergence par comparaison pour obtenir l’absolue convergence de la série $\sum_{n \geq n_{0}}a_{n}$, et comme son terme général est à valeurs réelles, le premier point en donne la convergence.

  On montre de même la convergence de la série $\sum_{n \geq n_{0}}b_{n}$ ce qui permet de conclure à la convergence de $\sum_{n \geq n_{0}}u_{n}$.
