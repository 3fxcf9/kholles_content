---
title: Inégalité de Markov et de Bienaymé-Tchébychev
authors:
  - Félix Rondeau
date: 18/06/2025
pid: 1750275295
tags:
  - variables aléatoires
---

### Inégalité de Markov

Pour une variable aléatoire réelle positive ou nulle presque sûrement sur un univers fini,

$$
    \forall a>0, P(X \geq a) \leq \frac{E(X)}{a}
$$

### Inégalité de Bienaymé-Tchébychev

Pour une variable aléatoire réelle définie sur un univers fini,

$$
    \forall \varepsilon>0, P(\abs{X-E(X)} \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^{2}}
$$

---

### Preuve de l’inégalité de Markov

> Montrons que $a \mathbb{1}_{(X \geq  a)} \leq X$ presque sûrement.

Soit $\omega \in (X \geq  0)$. Alors

- si $X(\omega) \geq  a$ alors $X(\omega) \geq a\mathbb{1}_{(X \geq  a)}(\omega) = a$
- sinon, $X(\omega) \in \oc{0,a}$ donc $X(\omega) \geq a \mathbb{1}_{(X \geq  a)}(\omega) = 0$

or $(X < 0)$ est négligeable et

$$
    \forall \omega \in \overline{(X<0)}, a \mathbb{1}_{(X \geq a)}(\omega) \leq X(\omega)
$$

donc $a \mathbb{1}_{(X \geq a)} \leq X \mathrm{ p.s.}$ si bien que par monotonie de l’espérance,

$$
    \underbrace{E(a \mathbb{1}_{(X \geq a)})}_{=aE(X \geq a)} \leq  E(X)
$$

<br/>

### Preuve de l’inégalité de Bienaymé-Tchébychev

Soit $\varepsilon \in \R_{+}^{*}$. Observons que

$$
    (\abs{X-E(X)} \geq \varepsilon) = \big((X - E(X))^{2} \geq \varepsilon^{2}\big)
$$

car pour tout $\omega \in \Omega$,

$$
\begin{align*}
     \omega \in (\abs{X-E(X)} \geq \varepsilon) &\iff \abs{X(\omega) - E(X)} \geq \varepsilon
\\
&\iff \big(X(\omega) - E(X)\big)^{2} \geq \varepsilon^{2} \\
&\iff \omega \in \big((X-E(X))^{2} \geq \varepsilon^{2}\big)
\end{align*}
$$

si bien que

$$
    \begin{align*}
        P(\abs{X-E(X)} \geq \varepsilon) &= P\big((X-E(X))^{2}\geq \varepsilon\big) \\
&\leq \frac{E \big((X-E(X))^{2}\big)}{\varepsilon^{2}}\\
&\leq \frac{V(X)}{\varepsilon^{2}}
    \end{align*}
$$

