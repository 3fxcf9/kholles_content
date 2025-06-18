---
title: Loi d’une fonction d’une variable aléatoire
authors:
  - Félix Rondeau
date: 06/18/2025
pid: 1750270681
tags:
  - variables aléatoires
---

Si $X$ est une variable aléatoire définie sur $\Omega$ et $g$ une fonction définie sur $X(\Omega)$, alors pour tout $y \in Y(\Omega)$,

$$
    P(g(X) = y) = \sum_{g \in g^{-1}(\{y\})}P(X = x)
$$

---

Soit $y \in g(X)(\Omega)$. Dans le système complet $(X=x)_{x \in X(\Omega)}$,

$$
\begin{align*}
    P(g(X)=y) &= \sum_{x \in X(\Omega)}P((g(X) = y) \cap (X=x)) \\
&= \sum_{\substack{x \in X(\Omega)\\g(X) = y}}\underbrace{P((g(X) = y)\cap  (X = x))}_{=P(X=x)} + \sum_{\substack{x \in X(\Omega)\\g(x) \neq y}}\underbrace{P((g(X) = y) \cap (X = x))}_{=0}\\
&= \sum_{\substack{x \in X(\Omega)\\g(x) = y}}P(X=x) = \sum_{x \in g^{-1}(\{y\})}P(X = x)
\end{align*}
$$

En effet,

- si $g(x) = y$,

  $$
     \omega \in (X = x) \implies  X(\omega) = x \implies g(X(\omega)) = g(x) = y \implies \omega \in (g(X) = y)
  $$

  donc $(X = x) \subset (g(X) = y)$ donc $(g(X) = y) \cap (X=x) = (X=x)$.

- si $g(x) \neq y$,

  $$
      \omega \in (X = x) \implies X(\omega) = x \implies g(X(\omega)) = g(x) \neq y \implies  \omega \notin (g(X) = y)
  $$

  donc les événements $(X=x)$ et $(g(X) = y)$ sont incompatibles.
