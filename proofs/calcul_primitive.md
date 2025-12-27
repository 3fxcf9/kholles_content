---
title: Calcul d’une primitive
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746268034
tags:
  - DES
---

Les primitives à valeurs complexes de la fonction

$$
    x \longmapsto \frac{1}{x-z_{0}}
$$

sont, dans le cas $z_{0}\in \R$, définies sur $\oo{-\infty,x_{0}}$ par

$$
    \left\{\applic{\oo{-\infty,x_{0}}}{\C}{x}{\ln(\abs{x-x_{0}}) + \lambda} \where \lambda \in \C\right\}
$$

et sur $\oo{x_{0},+\infty}$ par

$$
    \left\{\applic{\oo{x_{0},+\infty}}{\C}{x}{\ln(x-x_{0})} \where \lambda \in \C\right\}
$$

et dans le cas $x_{0} \in \C \setminus \R$, par

$$
    \left\{\applic{\R}{\C}{x}{\frac{1}{2}\ln((x-a)^{2} + b^{2}) + i\arctan \left(\frac{x-a}{b}\right) + \lambda} \where \lambda \in \C\right\}
$$

---

Traitons le cas $z_{0} \in \C \setminus \R$. Posons $a=\Re(z_{0})$ et $b = \Im(z_{0})$.

$$
    \begin{align*}
        \frac{1}{x-z_{0}} &= \frac{1}{x-a-ib} \\
&= \frac{(x-a) + ib}{(x-a)^{2} + b^{2}} \\
&= \frac{(x-a)}{(x-a)^{2} + b^{2}} + i \frac{b}{(x-a)^{2} + b^{2}} \\
&= \frac{1}{2}\frac{2(x-a)}{(x-a)^{2} + b^{2}} + \frac{i}{b^{2}} \frac{b}{1 + \left(\frac{x-a}{b}\right)^{2}} \\
&= \frac{1}{2}\frac{\bigl((x-a)^{2} + b^{2}\bigr)'}{(x-a)^{2} + b^{2}} + i \frac{\frac{1}{b}}{1 + \left(\frac{x-a}{b}\right)^{2}} \\
&= \frac{1}{2} \frac{\bigl((x-a)^{2} + b^{2}\bigr)'}{(x-a)^{2} + b^{2}} + i \frac{\left(\frac{x-a}{b}\right)'}{1+\left(\frac{x-a}{b}\right)^{2}}
    \end{align*}
$$

d’où le résultat.
