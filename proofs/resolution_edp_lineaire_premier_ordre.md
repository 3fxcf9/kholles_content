---
title: Résolution d’une EDP linéaire du premier ordre
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749306202
tags:
  - EDP
---

Les solution de l’équation d’inconnue $f \in \Cont^{1}(\R^{2},\R)$

$$
    \frac{\partial f}{\partial x} = 0
$$

forment l’espace vectoriel de dimension infinie

$$
    \left\{\applic{\R^{2}}{\R}{(x,y)}{\gamma(y)} \where \gamma \in \Cont^{1}(\R^{2},\R)\right\}
$$

---

Notons $\mathcal{S}$ l’ensemble de solutions cherché.

- Soit $f \in \mathcal S$.

  $$
      \begin{align*}
          f \in \mathcal{S} &\implies \forall (x,y)\in \R^{2}, \frac{\partial f}{\partial x}(x,y) = 0 \\
  &\implies \forall y \in \R, \forall x \in \R, f_{2,y}'(x) = 0\\
  &\implies \forall y \in \R, \exists c_{k} \in \R: \forall x \in \R, f_{2,y}(x) = c_{y} \\
  &\implies \forall y \in \R, \exists c_{y} \in \R: \forall x \in \R, f(x,y) = c_{y}
  \end{align*}
  $$

  Par ailleurs, $f \in \Cont^{1}(\R^{2}, \R)$ donc, pour tout $x \in \R$, $f_{1,x} \in \Cont^{1}(\R)$ si bien que $f_{1,\pi}: \applic{\R}{\R}{y}{c_{y}}$ est une fonction de classe $\Cont^{1}$ doppartien à $\mathcal{S}$.

- Soit $\gamma \in \Cont^{1}(\R)$. Alors l’application

  $$
      \applic{\R^{2}}{\R}{(x,y)}{\gamma(y)}
  $$

  est de classe $\Cont^{1}$ sur $\R^{2}$ et vérifie l’équation à résoudre, si bien que $f \in \mathcal{S}$.

