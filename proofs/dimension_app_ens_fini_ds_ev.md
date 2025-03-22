---
title: Dimension des applications d’un ensemble fini dans un espace vectoriel
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662332
tags:
  - algèbre linéaire
---

Soient $X$ un ensemble fini et $E$ un $\K$-espace vectoriel de dimension finie.
Alors $E^{X}$ est un $\K$-espace vectoriel fini et

$$
    \dim_{\K} E^{X}=\dim_{\K} E \times |X|
$$

---

Notons $p=|X|$ et listons les éléments de $X$ :

$$
    X = \{x_{1}, \ldots, x_{p}\}
$$

Fixons une base $(e_{1}, \ldots, e_{n})$ de $E$ (avec $n=\dim_{\K} E$). Pour tous $(i,k)\in \iset{1,p}\times \iset{1,n}$, notons $f_{i,k}$ l’application définie par

$$
    \forall j \in \iset{1,p}, \; f_{i,k}(x_{j}) = \delta_{i,j}\cdot e_{k}
$$

- _Analyse :_ Soient $(\lambda_{i,k})_{\substack{1 \leq i \leq p \\ 1 \leq k \leq n}} \in \K^{np}$ tels que

  $$
      f=\sum_{\substack{1 \leq i \leq p\\ 1 \leq k \leq n}} \lambda_{i,k}f_{i,k} \qquad (*)
  $$

  Soit $i_{0} \in \iset{1,p}$ fixé quelconque. Évaluons $(*)$ en $i_{0}$ :

  $$
      \begin{align*}
          f(x_{i_{0}}) &= \sum_{k=1}^{n}\underbrace{\sum_{i=1}^{p}\lambda_{i,k}\underbrace{f_{i,k}(x_{i_{0}})}_{=\delta_{i, i_{0}}\cdot e_{k}}}_{\lambda_{i_{0}, k}\cdot e_{k}} \\
  &= \sum_{k=1}^{n}\lambda_{i_{0}, k}\cdot e_{k}
      \end{align*}
  $$

  donc pour tout $k \in \iset{1,n}, \; \lambda_{i_{0}, k} = e_{k}^{*}(f(x_{i_{0}}))$ (c’est la coordonnée de $f(x_{i_{0}})$ selon $e_{k}$). On a ainsi l’unicité des coefficients $\lambda_{i,k}$ sous réserve de leur existence.

- _Synthèse :_ Soit $f \in E_{X}$. Posons

  $$
      g = \sum_{k=1}^{n}\sum_{i=1}^{p}e_{k}^{*}(f(x_{i}))\cdot f_{i,k}
  $$

  Par définition, $g \in E^{X}$. Soit $x \in X$ fixé quelconque. Il existe $i_{0} \in \iset{1,p}$ tel que $x=x_{i}$. Calculons

  $$
  \begin{align*}
      g(x) &= \sum_{k=1}^{n}\underbrace{\sum_{i=1}^{p}e_{k}^{*}(f(x_{i}))\cdot \underbrace{f_{i,k}(x)}_{=f_{i,k(x_{i_{0}})}=\delta_{i, i_{0}}\cdot e_{k}}}_{=e_{k}^{*}(f(x_{i_{0}}))\cdot e_{k}} \\
  &= \sum_{k=1}^{n}e_{k}^{*}(f(x_{i_{0}}))\cdot e_{k} \\
  &= f(x_{i_{0}}) \\
  &= f(x)
  \end{align*}
  $$

  Ainsi toute $f \in E^{X}$ s’écrit comme combinaison linéaire de $(f_{i,k})_{\substack{1 \leq i \leq p\\1 \leq k \leq n}}$ donc $(f_{i,k})_{\substack{1 \leq i \leq p\\1 \leq k \leq n}}$ engendre $E^{X}$. C’est donc une base de $E^{X}$. Par conséquent,

  $$
      \dim_{\K} E^{X} = np = \dim_{\K} E \times |X|
  $$
