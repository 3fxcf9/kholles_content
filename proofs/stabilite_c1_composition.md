---
title: Stabilité du caractère $\mathscr C^1$ par composition
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749289441
tags:
  - fonctions de deux variables
---

Soient $f: \Omega \subset \R^{2} \longrightarrow \R$ de classe $\Cont^{1}$ sur l’ouvert $\Omega$ et $g: U \subset \R^{2}\longrightarrow \Omega$ de classe $\Cont^{1}$ sur l’ouvert $U$.
Alors, la fonction $f \circ g$ est de classe $\Cont^{1}$ sur $U$.

---

- **$f\circ g$ admet des dérivées partielles en tout point $u \in U$ :** Soit $u = (u_{1}, u_{2}) \in U$.

  $$
  \begin{align*}
      (f\circ g)_{2,u_{2}} &= f \longmapsto f(g_{1}(t,u_{2}), g_{2}(t,u_{2})) \\
  &= f\circ \big(t \longmapsto (g_{1}(t, u_{2}), g_{2}(t, u_{2}))\big) \\
  &= \underbrace{f}_{\in \Cont^{1}(\Omega,\R)}\circ \underbrace{\big(t \longmapsto ((g_{1})_{2,u_{2}}(t), (g_{2})_{2,u_{2}}(t))\big)}_{\in \Cont^{1} \text{ au vois. de } u \text{ car } g_{1} \text{ et }g_{2} \text{ de classe } \Cont^{1} \text{ sur } U}
  \end{align*}
  $$

  donc $(f\circ g)_{2,u_{2}}$ est de classe $\Cont^{1}$ donc dérivable en $u_{1}$ et

  $$
  \begin{align*}
      (f\circ g)_{2,u_{2}}'(u_{1}) &= \partial_{1}f \big(\underbrace{(g_{1})_{2,u_{2}}(u_{1}), (g_{2})_{2,u_{2}}(u_{1})}_{=g(u)}\big) \times  \underbrace{(g_{1})_{2,u_{2}}'(u_{1})}_{=\partial_{1}g_{1}(u)} + \partial_{2}f \big(\underbrace{(g_{1})_{2,u_{2}}(u_{1}), (g_{2})_{2,u_{2}}(u_{1})}_{=g(u)}\big)\times \underbrace{(g_{2})_{2,u_{2}}'(u_{1})}_{=\partial_{1}g_{2}(u)}\\
  &= (\partial_{1}f)\circ g(u) \times \partial_{1} g_{1}(u) + (\partial_{2}f)\circ g(u) \times \partial_{1}g_{2}(u)
  \end{align*}
  $$

  ainsi $\partial_{1}(f\circ g)(u)$ existe, et on procède de même pour montrer l’existence de $\partial_{2} (f\circ g)$.

- **Les fonction $\partial_{1}(f\circ g)$ et $\partial_{2}(f\circ g)$ sont continues sur $U$ :**

  $$
      \partial_{1}(f\circ g) = \underbrace{\overbrace{(\partial_{1} f)}^{\in \Cont^{0}(\Omega,\R)}\circ \overbrace{g}^{\in \Cont^{0}(U,\Omega)}}_{\in \Cont^{0}(U,\R)} \times \underbrace{\partial_{1}g_{1}}_{\in \Cont^{0}(U,\R)} + \underbrace{(\partial_{2} f)\circ g\times \partial_{1}g_{2}}_{\in \Cont^{0}(U,\R)} \in \Cont^{0}(U,\R)
  $$

  il en est de même pour $\partial_{2}(f\circ g)$.
