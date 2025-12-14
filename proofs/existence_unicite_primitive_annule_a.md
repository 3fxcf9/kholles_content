---
title: Existence et unicité d’une primitive qui s’annule en $a$
authors:
  - Félix Rondeau
date: 09/05/2025
pid: 1746814608
tags:
  - intégration
---

Soit $f$ une fonction continue sur un intervalle $I$ et $a \in I$. Il existe une unique primitive de $f$ définie sur $I$ qui s’annule en $a$, qui est

$$
    F_{a}: \applic{I}{\C}{x}{\int_{a}^{x}f(u)\dd u}
$$

---

- **Bonne définition de $F_{a}$.** Pour tout $x \in I$, le segment d’extrémités $a$ et $x$ est inclus dans l’intervalle $I$ (convexité d’un intervalle) donc $f$ étant continue par morceaux sur $I$, l’intégrale $\int_{a}^{x}f(t)\dd t$ est bien définie.

- **Dérivabilité de $F_{a}$.** Soit $x_{0} \in I$.

  $$
  \begin{align*}
      \forall x \in I \setminus \{x_{0}\}, \frac{F_{a}(x) - F_{a}(x_{0})}{x-x_{0}} - f(x_{0}) &= \frac{1}{x-x_{0}}\Biggl(\underbrace{\int_{a}^{x}f(t)\dd t - \int_{a}^{x_{0}}f(t)\dd t}_{=\int_{x_{0}}^{x}f(t)\dd t}-\underbrace{(x-x_{0})f(x_{0})}_{=\int_{x_{0}}^{x}f(x_{0})\dd t}\Biggr)\\
  &= \frac{1}{x-x_{0}}\int_{x}^{x_{0}}(f(t)-f(x_{0}))\dd t
  \end{align*}
  $$

  d’où

  $$
  \begin{align*}
      \forall x \in I \setminus \{x_{0}\}, \abs{\frac{F_{a}(x) - F_{a}(x_{0})}{x-x_{0}} - f(x_{0})} &\leq \frac{1}{\abs{x-x_{0}}}\abs{x-x_{0}}\cdot \infabs{f-\tilde{f(x_{0})}}{\cc{x,x_{0}} \cup \cc{x_{0}, x}} \\
  & \leq \infabs{f-\tilde{f(x_{0})}}{\cc{x,x_{0}} \cap \cc{x_{0}, x}}
  \end{align*}
  $$

  Soit $\varepsilon>0$. Appliquons la définition de la continuité de $f$ en $x_{0}$ :

  $$
      \exists \eta>0: \forall x \in I, \abs{x-x_{0}} \leq  \eta \implies \abs{f(x)-f(x_{0})} \leq \varepsilon
  $$

  Fixons un tel $\eta$. Soit $x \in I \setminus \{x_{0}\}$ tel que $\abs{x-x_{0}} \leq  \eta$. Alors

  $$
      \forall t \in \cc{x,x_{0}}\cap \cc{x_{0}, x}, \abs{t-x_{0}} \leq  \abs{x-x_{0}} \leq  \eta
  $$

  donc $\abs{f(t)-f(x_{0})} \leq  \varepsilon$, donc $\infabs{f-\tilde{f(x_{0})}}{\cc{x,x_{0}}\cap \cc{x_{0}, x}} \leq  \varepsilon$, d’où

  $$
      \abs{\frac{F_{a}(x) - F_{a}(x_{0})}{x-x_{0}} - f(x_{0})} \leq \varepsilon
  $$

  Ainsi,

  $$
      \lim_{x\to x_{0}}\frac{F_{a}(x) - F_{a}(x_{0})}{x-x_{0}} = f(x_{0})
  $$

  donc $F_{a}$ est dérivable en $x$ et $F_{a}'(x_{0}) = f(x_{0})$.

- **Unicité.** $F_{a}$ est une primitive de $f$ qui s’annule en $a$. Soit $G: I \longrightarrow \C$ une primitive de $f$ qui s’annule en $a$. Alors,

  $$
      (F_{a}-G)' = F_{a}' - G' = f - f = \tilde{0} \quad\text{sur } I
  $$

  or $I$ est un intervalle donc $F_{a}-G$ est constante sur $I$, or $(F_{a} - G)(a) = 0$ donc $F_{a} = G$ sur $I$.
