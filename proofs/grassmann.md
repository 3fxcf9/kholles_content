---
title: Théorème de Grassmann
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060867
tags:
  - algèbre linéaire
---

Soient $E_{1}$ et $E_{2}$ deux sous-espaces vectoriels d’un $\K$-espace vectoriel $E$ de dimension finie. Alors

$$
    \dim_{\K}(E_{1}+E_{2}) = \dim_{\K}E_{1} + \dim_{\K}E_{2} - \dim_{\K}E_{1}\cap E_{2}
$$

---

$E_{1}\cap E_{2}$ est un sous-espace vectoriel de $E_{1}$ qui est un espace de dimension finie donc $E_{1}\cap E_{2}$ est de dimension finie. Notons

- $n_{1,2}$ la dimension de $E_{1}\cap E_{2}$
- $n_{1}$ la dimension de $E_{1}$
- $n_{2}$ la dimension de $E_{2}$

Le théorème d’existence d’une base en dimension finie permet de choisir $\mathcal{B}_{1,2}=(e_{1}, \ldots e_{n_{1,2}})$ une base de $E_{1}\cap E_{2}$, que l’on peut compléter en une base de $E_{1}$ (resp. de $E_{2}$) en lui adjoignant les vecteurs $(e'_{1}, \ldots \epsilon'_{p_{1}})$ (resp. $(e''_{1}, \ldots e''_{p_{2}})$). On a donc la relations $p_{1}=n_{1}-n_{1,2}$ (resp. $p_{1}=n_{1}-n_{1,2}$).

Montrons que $\mathcal{B}=(\underbrace{e'_{1}, \ldots , e'_{p_{1}}, \underbrace{e_{1}, \ldots , e_{n_{1,2}}}_{E_{1}\cap E_{2}}}_{E_{1}}, e''_{1}, \ldots \epsilon''_{p_{2}})$ est une base de $E_{1}+E_{2}$.

- Soit $x \in E_{1}+E_{2}$ fixé quelconque. Il existe $(x_{1}, x_{2}) \in E_{1} \times E_{2}$ tels que $x=x_{1}+x_{2}$. Il existe donc $(\lambda'_{1}, \ldots , \lambda'_{p_{1}}, \lambda_{1}, \ldots , \lambda_{n_{1,2}})\in \K^{p_{1}+n_{1,2}}$ tels que

  $$
      x_{1}=\sum_{i=1}^{p_{1}}\lambda'_{i}e'_{i} + \sum_{i=1}^{n_{1,2}}\lambda_{i}e_{i}
  $$

  et $(\mu''_{1}, \ldots , \mu''_{p_{2}}, \mu_{1}, \ldots , \mu_{n_{1,2}})\in \K^{p_{2}+n_{1,2}}$ tels que

  $$
      x_{2}=\sum_{i=1}^{n_{1,2}}\mu_{i}e_{i} + \sum_{i=1}^{p_{2}}\mu''_{i}e''_{i}
  $$

  Par conséquent,

  $$
      x=x_{1}+x_{2}=\sum_{i=1}^{p_{1}}\lambda'_{i}e'_{i} + \sum_{i=1}^{n_{1,2}}(\lambda_{i}+\mu_{i})e_{i} + \sum_{i=1}^{n_{1,2}}\mu_{i}e''_{i} \in \Vect \mathcal{B}
  $$

  donc $E_{1}+E_{2} \subset \Vect \mathcal{B}$. Par ailleurs, $\mathcal{B}\subset E_{1} \cup E_{2}$ donc $E_{1}+E_{2} =\Vect \mathcal{B}$ si bien que $\mathcal{B}$ engendre $E_{1}+E_{2}$.

- Soient $(\lambda'_{i}, \ldots , \lambda'_{p_{1}}, \lambda_{i}, \ldots , \lambda_{n_{1,2}}, \lambda''_{1}, \ldots , \lambda''_{p_{2}}) \in \K^{p_{1}+n_{1,2} + p_{2}}$ fixés quelconques tels que

  $$
      \underbrace{\sum_{i=1}^{p_{1}}\lambda'_{i}e'_{i}}_{y_{1}} + \underbrace{\sum_{i=1}^{n_{1,2}}\lambda_{i}e_{i}}_{y_{1,2}} + \underbrace{\sum_{i=1}^{p_{2}}\lambda''_{i}e''_{i}}_{y_{2}} = 0_{E}
  $$

  on obtient $\underbrace{y_{1}+y_{1,2}}_{\in E_{1}} = \underbrace{-y_{2}}_{\in E_{2}}$. Donc $y_{2} \in E_{1} \cap E_{2}$, or $y_{2} \in E'_{2}$ et $(E_{1} \cap E_{2})\cap E^{2}=\{0_{E}\}$ donc $y_{2} = 0_{E}$. La liberté de la famille $(e''_{1}, \ldots , e''_{p_{2}})$ permet de conclure que $\lambda''_{1}= \cdots = \lambda''_{p_{2}}=0_{\K}$.
  On obtient également que $y_{1}+y_{1,2}=0_{E}$, or $(e'_{1}, \ldots , e'_{p_{1}}, e_{1}, \ldots , e_{n_{1,2}})$ est libre (base de $E_{1}$) donc $\lambda'_{1}=\cdots =\lambda'_{p_{1}}=\lambda_{1}=\cdots =\lambda_{n_{1,2}}=0_{\K}$. Par conséquent, la famille $\mathcal{B}$ est libre, et est ainsi une base de $E_{1}+E_{2}$, donc

  $$
  \begin{align*}
      \dim_{\K}(E_{1}+E_{2}) &= p_{1}+n_{1,2}+p_{2} \\
                             &= (n_{1}-n_{1,2})+n_{1,2} + (n_{2}-n_{1,2}) \\
                             &= n_{1}+n_{2}-n_{1,2}
  \end{align*}
  $$
