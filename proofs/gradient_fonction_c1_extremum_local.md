---
title: Gradient d’une fonction $\mathscr C^1$ en un extremum local
authors:
  - Félix Rondeau
date: 06/07/2025
pid: 1749287756
tags:
  - fonctions de deux variables
---

Si une fonction $f \in \Cont^{1}(\Omega \subset \R^{2},\R)$ admet un extremum local en un point $\omega \in \Omega$, alors son gradient est nul en $\omega$ ($\omega$ est un point critique de $f$).

---

Supposons que $f$ admet un maximum local en $\omega = (\omega_{1}, \omega_{2}) \in \Omega$, i.e.

$$
    \exists r_{1} \in \R_{+}^{*}: \forall a \in \Omega \cap B(\omega, r_{1}), f(a) \leq f(\omega)
$$

De plus, $\Omega$ est ouvert donc

$$
    \exists r_{2} \in \R_{+}^{*}: B(\omega, r_{2})\subset \Omega
$$

Posons $r = \min\{r_{1}, r_{2}\}$. Alors $f_{2,\omega_{2}}$ est définie sur $\oo{\omega_{1} - r, \omega_{1} + r}$ et $f_{1,\omega_{1}}$ sur $\oo{\omega_{1} - r, \omega_{1} + r}$) et ces deux applications vérifient respectivement

$$
    \forall x \in \oo{\omega_{1} - r, \omega_{1} + r}, f_{2,\omega_{2}}(x) = f(x,\omega_{2}) \leq  f(\omega) = f_{2,\omega_{2}}(\omega_{1})
$$

et

$$
    \forall y \in \oo{\omega_{2} - r, \omega_{2} + r} , f_{1, \omega_{1}}(y) = f(\omega_{1}, y) \leq f(\omega) = f_{1,\omega_{1}}(\omega_{2})
$$

Ainsi, $f_{2, \omega_{2}}$ edmet un maximum local en $\omega_{1}$ et $f_{1,\omega_{1}}$ admet un maximum local en $\omega_{2}$, or $f \in \Cont^{1}(\Omega,\R)$ donc

$$
    f_{2,\omega_{2}} \in \Cont^{1}(\oo{\omega_{1} - r, \omega_{1} + r},\R) \subset \Diff^{1}(\oo{\omega_{1} - r, \omega_{1}+r},\R)
$$

et

$$
    f_{1,\omega_{1}} \in \Cont^{1}(\oo{\omega_{2} - r, \omega_{2} + r},\R) \subset \Diff^{1}(\oo{\omega_{2} - r, \omega_{2}+r},\R)
$$

Par conséquent,

$$
    f_{2,\omega_{2}}'(\omega_{1}) = 0 \quad\text{et}\quad f_{1,\omega_{1}}'(\omega_{2}) = 0
$$

soit

$$
    \partial_{1}f(\omega) = 0 \quad\text{et}\quad \partial_{2}f(\omega) = 0
$$

