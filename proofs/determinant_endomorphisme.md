---
title: Déterminant d’un endomorphisme
authors:
  - Félix Rondeau
date: 18/05/2025
pid: 1747568547
tags:
  - déterminant
---

On définit le déterminant d’un endomorphisme $f \in \L_{\K}(E)$ comme l’unique scalaire $\lambda$ vérifiant, pour toute base $\B$ de $E$ et toute famille $(u_{1}, \ldots, u_{n})\in E_{n}$,

$$
    \det_{\B}(f(u_{1}), \ldots, f(u_{n})) = \lambda \times \det_{\B}(u_{1}, \ldots, u_{n})
$$

---

- **Existence :** Soit $\B_{0} = (e_{1}, \ldots, e_{n})$ une base de $E$. L’application

  $$
      \varphi: \applic{E^{n}}{\K}{(u_{1}, \ldots, u_{n})}{\det_{\B_{0}}(f(u_{1}), \ldots, f(u_{n}))}
  $$

  est

  - une **forme $n$-linéaire**: soient $(u_{1}, \ldots, u_{n})$ des vecteurs de $E$ et $(v,w,\lambda) \in E^{2} \times \K$.

    $$
        \begin{align*}
            \varphi(v + \lambda \cdot w, u_{2}, \ldots, u_{n}) &= \det_{\B_{0}} (f(v + \lambda \cdot w), f(u_{2}), \ldots, f(u_{n})) \\
    &= \det_{\B_{0}} (f(v) + \lambda \cdot f(w), f(u_{2}), \ldots, f(u_{n})) \\
    &= \det_{\B_{0}}  (f(v), f(u_{2}), \ldots, f(u_{n})) + \lambda \cdot \det_{\B_{0}} (f(w), f(u_{2}), \ldots, f(u_{n}))\\
    &= \varphi(v, u_{2}, \ldots, u_{n}) + \lambda \cdot \varphi(w, u_{2}, \ldots, u_{n})
        \end{align*}
    $$

    On prouve de même la linéarité en sS $n-1$ autres arguments.

  - **alternée**: soient $(u_{1}, \ldots, u_{n}) \in E^{n}$ tel qu’il existe $(i,j) \in \icc{n,n}^{2}$ vérifiant $i\neq j$ et $u_{i} = u_{j}$. Alors la famille $(f(u_{1}), \ldots, f(u_{n}))$ comporte deux éléments identiques, donc

    $$
        \det_{\B_{0}} (f(u_{1}), \ldots, f(u_{n})) = 0
    $$

    si bien que $\varphi(u_{1}, \ldots, u_{n}) = 0$.

  Par conséquent, $\varphi \in \land^{n}(E,\K) = \Vect\left\{\det_{\B_{0}} \right\}$ donc

  $$
      \exists \lambda_{\B_{0}}\in \K : \varphi = \lambda_{\B_{0}}\cdot \det_{\B_{0}}
  $$

  d’où

  $$
      \forall (u_{1}, \ldots, u_{n}) \in E^{n}, \det_{\B_{0}} (f(u_{1}), \ldots, f(u_{n})) = \lambda_{\B_{0}}\times \det_{\B_{0}} (u_{1}, \ldots, u_{n}) \quad (*)
  $$

  Soit $\B$ une base de $E$. Nous savons que

  $$
      \det_{\B}  = (\det_{\B} \B_{0})\cdot \det_{\B_{0}}
  $$

  donc en multipliant la relation $(*)$ par $\det_{\B} \B_{0}$, on obtient

  $$
      \forall (u_{1}, \ldots, u_{n}) \in E^{n}, \underbrace{\det_{\B} \B_{0}\det_{\B_{0}} (f(u_{1}), \ldots, f(u_{n}))}_{=\det_{\B} (f(u_{1}), \ldots, f(u_{n}))} = \lambda_{\B_{0}}\times \underbrace{\det_{\B} \B_{0} \times \det_{\B_{0}} (u_{1}, \ldots, u_{n})}_{=\det_{\B} (u_{1}, \ldots, u_{n})}
  $$

  d’où

  $$
      \forall (u_{1}, \ldots, u_{n})\in E^{n}, \det_{\B} (f(u_{1}), \ldots, f(u_{n})) = \lambda_{\B_{0}}\times \det_{\B} (u_{1}, \ldots, u_{n})
  $$

  Par conséquent, $\lambda_{\B_{0}}$ convient pour toute base $\B$.

- **Unicité :** Soit $\lambda \in \K$ tel que pour toute base $\B$ de $E$,

  $$
      \forall (u_{1}, \ldots, u_{n})\in E^{n}, \det_{\B} (f(u_{1}), \ldots, f(u_{n})) = \lambda \times \det_{\B} (u_{1}, \ldots, u_{n})
  $$

  Particularisons pour la base $\B \leftarrow \B_{0}$ et $(u_{1}, \ldots, u_{n}) \leftarrow \B_{0}$ :

  $$
      \det_{\B_{0}} (f(e_{1}), \ldots, f(e_{n})) = \lambda \times \underbrace{\det_{\B_{0}} \B_{0}}_{=1}
  $$

  Or en particularisant la relation définissant $\lambda_{\B_{0}}$ pour $(u_{1}, \ldots, u_{n})\leftarrow \B_{0}$,

  $$
      \lambda_{\B_{0}} = \det_{\B_{0}} (f(e_{1}), \ldots, f(e_{n}))
  $$

  donc $\lambda = \lambda_{\B_{0}}$.
