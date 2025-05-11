---
title: Convergence d’une suite
authors:
  - Félix Rondeau
date: 05/11/2025
pid: 1746968437
tags:
  - intégration
---

Soit $n_{0} \in \N$ et $f$ une fonction définie sur $\co{n_{0},+\infty}$ continue, décroissante et minorée par $m \in \R$. Alors la série de terme général

$$
    \left(f(n) - \int_{n}^{n+1}f(u)\dd u\right)_{n \geq n_{0}}
$$

est à termes positifs ou nuls et converge.

---

Posons pour $n \in \iset{n_{0},+\infty}$, $u_{n} = f(n) - \int_{n}^{n+1}f(t)\dd t$. Par décroissance de $f$,

$$
\begin{align*}
    \forall n \geq n_{0}, f(n+1) \leq \int_{n}^{n+1}f(t)\dd t \leq  f(n) &\implies f(n+1) - f(n) \leq -u_{n} \leq 0 \\
&\implies 0 \leq u_{n} \leq f(n) - f(n+1)
\end{align*}
$$

Ainsi,

- $\sum_{n \geq n_{0}}u_{n}$ est à termes positifs
- On a

  $$
      \begin{align*}
          \forall n \in \N,n \geq n_{0}, \sum_{k=n_{0}}^{n}u_{k} &\leq \sum_{k=n_{0}}^{n}\left(f(k)-f(k+1)\right) \\
  &\leq f(kn_{0}) - f(n+1) \\
  &\leq f(n_{0}) - m
      \end{align*}
  $$

  donc la suite des sommes partielles est majorée, donc $\sum_{n \geq n_{0}}u_{n}$ converge.

La figure suivante illustre la convergence de la série :

```tikz
\begin{tikzpicture}
  \draw[->] (-0.5,0) -- (8.5,0) node[right] {$x$}; % x-axis
  \draw[->] (0,-0.5) -- (0,5.5); % y-axis

  \draw[domain=1:8,samples=100,smooth,thick,teal] plot (\x, {1/\x*4 + 1}) node[right] {};

  \foreach \n in {1,2,...,7} {

      \draw[dashed] (\n, 0) -- (\n, {4/\n + 1});
      \filldraw (\n, {4/\n + 1}) circle (2pt) node[above right] {$f(\n)$};


      \draw[purple, thick] (\n, {4/\n + 1}) -- (\n+1, {4/\n + 1}) -- (\n+1, {1 + 4/(\n + 1)});

      \fill[gray, opacity=0.3]
          plot[domain=\n:\n+1, samples=50] (\x, {1 + 4/\x}) --
          (\n+1, {1 + 4/\n}) -- (\n, {1 + 4/\n}) -- cycle;

      \fill[gray, opacity=0.3]
          plot[domain=\n:\n+1, samples=50] (\x - \n + 9, {1+ 4/\x}) --
          (10, {1 + 4/\n}) -- (9, {1+ 4/\n}) -- cycle;

      \draw[teal] plot[domain = \n:\n+1, samples = 50] (\x - \n + 9, {1 + 4/\x});
      \draw[purple] (9, {1 + 4/\n}) -- (10, {1 + 4/\n}) -- (10, {1 + 4/(\n+1)});
  }

  \draw[dashed] (9, 5) -- (9, 1) -- (10, 1) -- (10, 2);
  \draw[dotted] (0, 1) node[left] {$m = 1$} -- (9, 1);

  \draw[<->] (10.2, 1) -- (10.2, 5) node[pos=0.5, right] {$f(1) - 1$};
\end{tikzpicture}
```

