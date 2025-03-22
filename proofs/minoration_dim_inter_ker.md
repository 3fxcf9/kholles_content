---
title: Minoration de la dimension de l’intersection du noyau d’une forme linéaire avec un sous-espace vectoriel
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662331
tags:
  - algèbre linéaire
---

Soit $\varphi$ une forme linéaire non nulle sur $E$, et $F$ un espace vectoriel de dimension $p \in \N^{*}$. Alors

$$
    \dim_{\K} F \cap \Ker \varphi = \begin{cases}
        p & \text{si } F \subset \Ker \varphi \\
        p-1 & \text{sinon}
    \end{cases}
$$

On a donc toujours

$$
    \dim_{\K} F \cap \Ker \varphi \geq p-1
$$

---

Appliquons le théorème du rang à la restriction $\varphi_{|F}$ de $\varphi$ à $F$ :

$$
    \underbrace{\dim_{\K} F}_{=p} = \rg \varphi_{|F} + \dim_{\K} \underbrace{\Ker  \varphi_{|F}}_{=\Ker \varphi \cap F}
$$

en remarquant que $\rg \varphi_{|F}$ vaut 0 si $F \subset \Ker \varphi$ et 1 sinon, on trouve le résultat attendu.
