---
title: Critère de convergence des séries de Riemann
authors:
  - Félix Rondeau
date: 05/11/2025
pid: 1746952043
tags:
  - intégration
---

La série

$$
    \sum_{n \geq 1}\frac{1}{n^{\alpha}}
$$

converge si et seulement si $\alpha > 1$.

---

- si $\alpha < 0$, alors $\frac{1}{n^{\alpha}} \arrowlim{n\to + \infty} + \infty$ donc la suite $\left(\frac{1}{n^{\alpha}}\right)$ ne converge pas vers 0; la série est grossièrement divergente.
- si $\alpha=0$, alors $\frac{1}{n^{\alpha}} = 1 \arrowlim{n\to +\infty} 1$ donc la série est aussi grossièrement divergente.
- si $\alpha > 0$, effectuons un calcul préliminaire: cherchons un équivalent de $\frac{1}{(n+1)^{\beta}} - \frac{1}{n^{\beta}}$ en fonction de $\beta \in R$:

  $$
      \begin{align*}
          \frac{1}{(n+1)^{\beta}} - \frac{1}{n^{\beta}} &= \frac{1}{n^{\beta}}\left(1 - \frac{1}{n}\right)^{-\beta} - \frac{1}{n^{\beta}} \\
  &\underset{+ \infty}{=} \frac{1}{n^{\beta}}\left(1-\frac{\beta}{n} + o \left(\frac{1}{n}\right)\right) \\
  &\underset{+ \infty}{=} -\frac{\beta}{n^{\beta+1}} + o \left(\frac{1}{n^{\beta+1}}\right) \\
  &\underset{+ \infty}{\sim} \begin{cases}
      -\frac{\beta}{n^{\beta+1}} & \text{si } \beta \neq 0 \\
  0 & \text{si } \beta=0
  \end{cases} \\
  &&\underset{+ \infty}{\sim} -\frac{\beta}{n^{\beta+1}}
      \end{align*}
  $$

  de plus

  $$
      \left(-\frac{\beta}{n^{\beta+1}}\right)
  $$

  est une suite $\leq 0$ donc de signe constant, ce qui permet d’appliquer le critère d’équivalence pour obtenir

  $$
      \sum_{n \geq 1}\left(\frac{1}{(n+1)^{\beta}} - \frac{1}{n^{\beta}}\right) \quad\text{et}\quad \sum_{n \geq 1}-\frac{\beta}{n^{\beta+1}}
  $$

  ont la même nature. De plus, si $\beta \neq 0$, les séries

  $$
      \sum_{n \geq 1}\frac{-\beta}{n^{\beta+1}} \quad\text{et}\quad \sum_{n \geq 1}\frac{1}{n^{\beta+1}}
  $$

  ont la même nature, donc les séries

  $$
      \sum_{n \geq 1}\frac{1}{n^{\beta+1}} \quad\text{et}\quad \sum_{n \geq 1}\left(\frac{1}{(n+1)^{\beta}} - \frac{1}{n^{\beta}}\right)
  $$

  ont la même nature. Appliquons ce résultat pour $\beta \leftarrow \alpha-1$ avec $\alpha \in \oo{0,\infty}\setminus \{1\}$ (autorisé car $\alpha-a \neq 0$)

  $$
      \sum_{n \geq 1}\frac{1}{n^{\alpha}} \quad\text{et}\quad \sum_{n \geq 1}\left(\frac{1}{(n+1)^{\alpha-1}} - \frac{1}{n^{\alpha-1}}\right)
  $$

  ont la même nature. Cette deuxième série étant téléscopique, elle a la même nature que la suite $\left(\frac{1}{n^{\alpha-1}}\right)_{n \geq  1}$ qui converge si $\alpha>1$ et diverge si $\alpha \in \oo{0,1}$, ainsi, la série

  $$
      \sum_{n \geq 1}\frac{1}{n^{\alpha}}
  $$

  converge si $\alpha>0$ et diverge si $\alpha \in \oo{0,1}$.

- si $\alpha=1$, on peut majorer l’aire sous la courbe de la fonction $x \longmapsto \frac{1}{x}$ par la somme des rectangles dessinés ci-dessous

  ```tikz
    \begin{tikzpicture}

        \draw (1,0) -- (1,-0.05) node[below] {1};
        \draw (2,0) -- (2,-0.05) node[below] {2};
        \draw (3,0) -- (3,-0.05) node[below] {3};
        \draw (6,0) -- (6,-0.05) node[below] {n-1};
        \draw (7,0) -- (7,-0.05) node[below] {n};

        \draw[teal] (1,0) -- (1, 3) -- (2, 3) -- (2,0) -- cycle;
        \draw[teal] (2,0) -- (2,{3/sqrt(2)}) -- (3,{3/sqrt(2)}) -- (3,0) -- cycle;
        \draw[teal] (3,0) -- (3,{3/sqrt(3)}) -- (4,{3/sqrt(3)}) -- (4,0) -- cycle;
        \draw[teal] (6,0) -- (6,{3/sqrt(6)}) -- (7,{3/sqrt(6)}) -- (7,0) -- cycle;

        \node at (1.5,1.6) {\small $1$};
        \node at (2.5,1.2) {\small $\frac{1}{2}$};
        \node at (6.5,0.65) {\small $\frac{1}{n-1}$};

        \draw[domain=0.9:7.2, smooth, variable=\x, purple, thick] plot ({\x}, {3/(\x)^(1/2)});

        \draw[->, thick] (0,0) -- (8,0) node[right] {$x$};
        \draw[->, thick] (0,0) -- (0,4) node[above] {};
    \end{tikzpicture}
  ```

  pour obtenir l’inégalité suivante:

  $$
      \underbrace{\sum_{k=1}^{n-1}\frac{1}{k}}_{\leq \sum_{k=1}^{n}\frac{1}{k}} \geq \underbrace{\int_{1}^{n}\frac{\dd x}{x}}_{=\ln n}
  $$

  et en faisant de même avec les rectangles à gauche, on obtient

  $$
      \sum_{k=1}^{n}\frac{1}{k} \leq 1+\underbrace{\int_{1}^{n}\frac{\dd x}{x}}_{\ln n}
  $$

  Ces deux inégalités permettent de conclure à l’encadrement

  $$
      \forall n \in \N^{*}, \ln n + \frac{1}{n} \leq \sum_{k=1}^{n} \leq 1+\ln n
  $$

  si bien qu’en divisant par $\ln n$, on obtient

  $$
      \forall n \in \N^{*}, \underbrace{1+\frac{1}{n\ln n}}_{\arrowlim{n\to+\infty}1} \leq  \frac{\sum_{k=1}^{n}\frac{1}{k}}{\ln n} \leq \underbrace{\frac{1}{\ln n} + 1}_{\arrowlim{n\to +\infty}1}
  $$

  ce qui permet de conclure, grace au théorème d’existence de limites par encadrement, que

  $$
      \sum_{k=1}^{n}\frac{1}{k} \underset{+\infty}{\sim} \ln n
  $$
