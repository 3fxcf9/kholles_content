---
title: Formule de Taylor avec reste intégral
authors:
  - Félix Rondeau
date: 09/05/2025
pid: 1746817606
tags:
  - intégration
---

Soient $f \in \Cont^{n+1}(I,\C)$ et $a \in I$. Alors, pour tout $x \in I$,

$$
    f(x) = \sum_{k=0}^{n}\frac{(x-a)^{k}}{k!}f^{(k)}(a) + \int_{a}^{x}\frac{(x-u)^{n}}{n!}f^{(n+1)}(u)\dd u
$$

---

Considérons la propriété $\P(\cdot)$ définie pour tout $n \in \N$ par

$$
    \P(n): «\; \forall f \in \Cont^{n+1}(I,\C), f(x) = \sum_{k=0}^{n}\frac{(x-a)^{k}}{k!}f^{(k)}(a) + \int_{a}^{x}\frac{(x-u)^{n}}{n!}f^{(n+1)}(u)\dd u \;»
$$

- Pour $n=0$, le théorème fondamental du calcul intégral donne, pour $f \in \Cont^{1}(I,\C)$ et $a \in I$

  $$
      \sum_{k=0}^{0}\frac{f^{(k)}(a)}{k!}(x-a)^{k} + \int_{a}^{x}\frac{(x-t)^{0}}{0!}f'(t)\dd t = f(a) + \underbrace{\int_{a}^{x}f'(t)\dd t}_{f(x)-f(a)} = f(x)
  $$

- Soit $n \in \N$ tel que $\P(n)$ est vraie. Soient $f \in \Cont^{n+2}(I,\C)$ et $(x,a) \in I^{2}$. $f \in \Cont^{n+2}(I,\C)$ donc $f \in \Cont^{n+1}(I,\C)$ ce qui permet d’appliquer $\P(n)$:

  $$
      f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^{k} + \int_{a}^{x}\frac{(x-t)^n}{n!}f^{(n+1)}(t)\dd t
  $$

  Intégrons par partie l’intégrale ci-dessus

  $$
  \begin{align*}
      \int_{a}^{x}\frac{(x-t)}{n!}f^{(n+1)}(t)\dd t &= \left[\frac{-(x-t)^{n+1}}{(n+1)n!}f^{(n+1)}(t)\right]_{a}^{x} - \int_{a}^{x}\frac{-(x-t)^{n+1}}{(n+1)!}\left(f^{(n+1)}\right)'(t)\dd t\\
  &= 0-\frac{-(x-a)^{n+1}}{(n+1)!}f^{(n+1)}(a) + \int_{a}^{x}\frac{(x-t)^{n+1}}{(n+1)!}f^{(n+2)}(t)\dd t
  \end{align*}
  $$

  donc

  $$
      f(x) = \sum_{k=0}^{n+1}\frac{f^{(k)}(a)}{k!}(x-a)^{n} + \int_{a}^{x}\frac{(x-t)^{n+1}}{(n+1)!}f^{(n+2)}(t)\dd t
  $$

  d’où $\P(n+1)$ est vraie.

<br/>

### Application à la minoration de cosinus

Soit $x \in \cc{-\frac{\pi}{2}, \frac{\pi}{2}}$. Appliquons la formule de Taylor avec reste intégral à la fonction cosinus en 0 :

$$
    \cos x - \left(\cos 0 + \frac{\cos '0}{1!}(x-0) + \frac{\cos^{(2)} 0}{2!}(x-0)^{2}\right) = \int_{0}^{x}\frac{(x-t)^{2}}{2!}\underbrace{\cos^{(3)}(t)}_{\sin t}\dd t
$$

donc

$$
    \cos x - \left(1-\frac{x^{2}}{2}\right) = \int_{0}^{x}\frac{(x-t)^{2}}{2}\sin(t)\dd t
$$

- si $x \in \cc{0,\frac{\pi}{2}}$, $t \longmapsto \frac{(x-t)^{2}}{2}\sin t$ est positive donc

  $$
      \int_{0}^{x}\frac{(x-t)^{2}}{2}\sin(t) \dd t \geq 0
  $$

- si $x \in \cc{-\frac{\pi}{2}, 0}$, $t\longmapsto \frac{(x-t)^{2}}{2}\sin t$ est inférieure ou égal à 0 donc

  $$
      \int_{0}^{x}\frac{(x-t)^{2}}{2}\sin(t)\dd t \geq 0
  $$

Ainsi,

$$
    \forall x \in \cc{-\frac{\pi}{2}, \frac{\pi}{2}}, \cos x \geq  1-\frac{x^{2}}{2}
$$
