---
title: Propriété de l’espérance
authors:
  - Félix Rondeau
date: 06/18/2025
pid: 1750272193
tags:
  - variables aléatoires
---

Pour une variable aléatoire $X \geq 0$ presque sûrement,

$$
    E(X) = 0 \iff X = 0 \text{ p.s.}
$$

---

Soit $X$ une variable aléatoire positive presque sûrement.

- Supposons $E(X) = 0$.

  $$
  \begin{align*}
      E(X) &= \sum_{\omega \in \Omega}X(\omega)P(\{\omega\})\\
  &= \sum_{\omega \in (X = 0)}\underbrace{X(\omega)}_{\substack{=0\\\text{car } \omega \in (X =0)}}P(\{\omega\}) + \sum_{\omega \in (X <0)}X(\omega)\underbrace{P(\{\omega\})}_{\substack{=0\\\text{car } (X<0)\text{ est négligeable}}} + \sum_{\omega \in (X>0)}X(\omega)P(\{\omega\})\\
  &= \sum_{\omega \in (X>0)}X(\omega)P(\{\omega\})
  \end{align*}
  $$

  Soit $\omega_{0} \in (X>0)$.

  $$
      0 \leq X(\omega_{0})P(\{\omega_{0}\}) \leq \sum_{\omega \in (X>0)}X(\omega)P(\{\omega\}) = E(X) = 0
  $$

  donc $X(\omega_{0})P(\{\omega_{0}\}) = 0$ or $X(\omega_{0}) > 0$ donc $P(\{\omega_{0}\}) = 0$. Par conséquent

  $$
      P((X>0)) = \sum_{\omega_{0} \in (X>0)}P(\{\omega_{0}\}) = 0
  $$

  donc $(X>0)$ est négligeable, or

  $$
      0 \leq P((X>0) \cup (X<0)) \leq  P(X>0) + P(X<0) = 0
  $$

  donc $(X>0) \cup (X<0)$ est négligeable donc $(X=0)$ est presque certain.

- Supposons $X=0$ presque sûrement.

$$
    \begin{align*}
        E(X) &= \sum_{\omega \in \Omega}X(\omega)P(\{\omega\}) \\
&= \sum_{\omega \in (X=0)}\underbrace{X(\omega)}_{=0}P(\{\omega\}) + \sum_{\phi \in (X\neq 0)}X(\omega)\underbrace{P(\{\omega\})}_{\substack{=0\\\text{car }(X\neq 0)\text{ négligeable}}}\\
&= 0
    \end{align*}
$$

