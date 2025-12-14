---
title: Distance d’un vecteur à un hyperplan affine dans un espace euclidien
authors:
  - Félix Rondeau
date: 06/02/2025
pid: 1748874404
tags:
  - orthogonalité
  - espaces euclidiens
---

Soit $(E,\scalar{\cdot}{\cdot})$ un espace vectoriel euclidien et $\B = (e_{1}, \ldots , e_{n})$ une BON de cet espace.
Soit $u = \sum_{i=1}^{n}u_{i} e_{i}$ un vecteur de $E$ et $(a_{1}, \ldots, a_{n})\in \R^{n} \setminus \{0_{\R^{2}}\}$, $\alpha \in \R$ et $H_{\alpha}$ l’hyperplan affine d’équation

$$
    \sum_{i=1}^{n}a_{i} x_{i} = \alpha
$$

Alors la distance de $u$ à $H_{\alpha}$, définie comme la borne inférieurs de $\{\norm{u-z} \mid z \in H_{\alpha}\}$

- est un plus petit élément
- est atteinte pour un unique vecteur $z$ de $H_{\alpha}$
- vaut

  $$
      d(u,H_{\alpha}) = \frac{\abs{\scalar{u}{a} - \alpha}}{\norm a} = \dfrac{\abs{\displaystyle\sum_{i=1}^{n}a_{i}u_{i} - \alpha}}{\sqrt{\displaystyle\sum_{i=1}^{n}a_{i}^{2}}}
  $$

  où $a$ est le vecteur $\sum_{i=1}^{n}a_{i} e_{i}$.

```tikz
\begin{tikzpicture}[x=1pt,y=1pt,yscale=-1,xscale=1]

\draw    (221.67,86.5) -- (141.67,141.5) -- (380.67,141.5) ;
\draw    (221.67,185.5) -- (141.67,240.5) -- (380.67,240.5) ;
\draw    (236.33,141.73) -- (236.33,219.5) ;
\draw  [dash pattern={on 0.84pt off 2.51pt}]  (236.33,128.43) -- (236.33,141.73) ;
\draw    (236.33,47.97) -- (236.33,125.03) ;
\draw [color=purple  ,draw opacity=1 ]   (236.33,125.03) -- (310.45,91.07) ;
\draw [shift={(312.27,90.23)}, rotate = 155.38] [fill=purple  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
\draw    (294.84,98.43) -- (311.4,64.18) ;
\draw [shift={(312.27,62.38)}, rotate = 115.79] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
\draw    (312.27,141.73) -- (312.27,184.7) ;
\draw  [dash pattern={on 0.84pt off 2.51pt}]  (312.27,90.23) -- (312.27,141.73) ;
\draw    (312.27,90.23) -- (312.27,62.38) ;
\draw [color=purple  ,draw opacity=1 ]   (236.33,219.5) -- (310.45,185.53) ;
\draw [shift={(312.27,184.7)}, rotate = 155.38] [fill=purple  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
\draw    (312.53,171.07) -- (300.53,176.13) -- (300.53,189.73) ;
\draw    (274.17,141.21) -- (236.33,219.5) ;
\draw  [dash pattern={on 0.84pt off 2.51pt}]  (294.84,98.43) -- (274.17,141.21) ;

\draw (141,245.9) node [anchor=north west][inner sep=0.75pt]    {$H_{0}$};
\draw (142,145.9) node [anchor=north west][inner sep=0.75pt]    {$H_{\alpha }$};
\draw (299.5,47.57) node [anchor=north west][inner sep=0.75pt]    {$x$};
\draw (240.5,44.9) node [anchor=north west][inner sep=0.75pt]    {$H_{0}^{\perp }$};
\draw (217.5,215.07) node [anchor=north west][inner sep=0.75pt]    {$ \begin{array}{l}
0_{E}\\
\end{array}$};
\draw (277.5,197.57) node [anchor=north west][inner sep=0.75pt]  [color=purple  ,opacity=1 ]  {$ \begin{array}{l}
p_{H_{0}}^{\perp }( u)\\
\end{array}$};


\end{tikzpicture}
```

---

Posons $a = \sum_{i=1}^{n}a_{i} e_{i}$. $H_{0}$ est un hyperplan vectoriel dont un vecteur normal est $a$ donc $H_{0} = a\ortho$.
Soit $h_{\alpha} \in H_{0}\ortho$ tel que $H_{\alpha} = h_{\alpha} + H_{0}$.

- Graphiquement,

  $$
  \begin{align*}
      d(u,H_{\alpha}) &= \norm{p\ortho_{\Vect\left\{a\right\}}(u) - h_{\alpha}} \\
  &= \norm{\scalar{u}{\frac{a}{\norm a}} \frac{a}{\norm a} - \frac{\alpha}{{\norm a}^{2}}a}\\
  &= \norm{\left(\frac{\scalar{u}{a} - \alpha}{{\norm a}^{2}}\right)a} \\
  &= \frac{\abs{\scalar{u}{a}} - \alpha}{{\norm a}^{2}}\norm a \\
  &= \frac{\abs{\scalar{u}{a} - \alpha}}{\norm a}
  \end{align*}
  $$

  car $h_{\alpha} = \frac{\alpha}{{\norm a}^{2}}a$.

- Sinon, l’égalité $H_{\alpha} = h_{\alpha} + H_{0}$ donne

  $$
  \begin{align*}
      \{\norm{u-z} \mid z \in H_{\alpha}\} &= \{\norm{u - (h_{\alpha} + z')} \mid z' \in H_{0}\} \\
  &= \{\norm{(u-h_{\alpha}) - z'} \mid z' \in H_{0}\}
  \end{align*}
  $$

  or ce dernier ensemble admet une borne inférieure ($d(u-h_{\alpha}, H_{0})$) et cette borne inférieure est un plus petit élément atteint pour $z' = p_{H_{0}}\ortho(u-h_{\alpha}) = p_{H_{0}}\ortho(u)$ ($h_{\alpha}$ est dans le noyau de la projection), donc $d(u,H_{\alpha}) = \inf\{\norm{u-z} \mid z \in H_{\alpha}\}$ est un plus petit élément atteing pour l’unique valeur $z = h_{\alpha} + p_{H_{0}}\ortho(u-h_{\alpha}) = h_{\alpha} + p_{H_{0}}\ortho(u)$ :

  $$
      d(u,H_{\alpha}) = \norm{u-h_{\alpha} - p_{H_{0}}\ortho(u)}
  $$

  or

  $$
    u-p_{H_{0}}\ortho(u) = (\Id_{E} - p_{H_{0}}\ortho)(u) = p_{H_{0}\ortho}\ortho (u) = \scalar{u}{\frac{a}{\norm a}} \frac{a}{\norm a}
  $$

  car $H_{0}\ortho = \Vect\left\{a\right\}$ d’où, sachant que $h_{\alpha} = \frac{\alpha}{{\norm a}^{2}}a$,

  $$
      d(u,H_{\alpha}) = \norm{p_{H_{0}\ortho}\ortho - h_{\alpha}} = \norm{\scalar{u}{\frac{a}{\norm a}}\frac{a}{\norm a} - \frac{\alpha}{{\norm a}^{2}}a} = \frac{\abs{\scalar{u}{a} - \alpha}}{\norm a}
  $$
