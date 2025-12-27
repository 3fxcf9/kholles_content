---
title: Conséquence de la continuité radiale sur la continuité
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749285710
tags:
  - fonctions de deux variables
---

La fonction

$$
    f: \applic{\Omega \subset \R^{2}}{\R}{(x,y)}{\begin{cases}
        0 & \text{si } x=0 \\
        \frac{y^{2}}{x} & \text{si } x\neq 0
    \end{cases}}
$$

est continue radialement dans toutes les directios autour de $(0,0)$ mais non continue en $(0,0)$.

---

- Soit $u = (u_{1}, u_{2}) \in \R^{2}$ un vecteur unitaire. Pour $t>0$,

  $$
      f((0,0) + t u) = f(tu_{1}, tu_{2}) = \begin{cases}
          0 & \arrowlim{t\to 0} 0 = f((0,0)) & \text{si } u_{1}=0 \\
          \frac{t^{2}u_{2}}{tu_{1}} & \arrowlim{t\to 0} 0 = f((0,0)) & \text{si }u_{1} \neq 0
      \end{cases}
  $$

  donc $f$ est continue radialement dans toutes les direction en $(0,0)$.

- La suite $\left(a_{n} = \left(\frac{1}{(n+1)^{2}}, \frac{1}{n+1}\right)\right)_{n \in \N}$ converge vers $(0,0)$ mais son image par $f$ est la suite constante de valeur 1, donc ne converge pas vers $f((0,0)) = 0$. Par conséquent, $f$ n’est pas continue en $(0,0)$.

