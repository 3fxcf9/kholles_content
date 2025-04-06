---
title: Expressions de sommes avec les fonctions symétriques élémentaires
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933257
tags:
  - polynômes
---

Exprimer avec les fonctions symétriques élémentaires les sommes

1. $S_{2} = \sum_{i=1}^{n}x_{i}$
2. $S_{-1} = \sum_{i=1}^{n}\frac{1}{x_{i}}$
3. $S_{-2} = \sum_{i=1}^{n}\frac{1}{x_{i}^{2}}$

---

2.  </br>

    $$
        \begin{align*}
            S_{2} &= \sum_{i=1}^{n}x_{i}^{2} \\
    &= \left(\sum_{i=1}^{n}e_{i}\right)^{2} - 2 \sum_{1 \leq  i<j \leq  n} x_{i}x_{j} \\
    &= \sigma_{1}^{2} - 2 \sigma_{2}
        \end{align*}
    $$

3.  </br>

    $$
        \begin{align*}
            S_{-1} &= \sum_{i=1}^{n}\frac{1}{x_{i}}\\
    &= \sum_{i=1}^{n}\frac{\prod_{\substack{j=1\\j\neq i}}^{n}x_{j}}{\prod_{j=1}^{n}x_{j}}\\
    &= \frac{1}{\prod_{j=1}^{n}x_{j}}\left(\sum_{i=1}^{n}\prod_{\substack{j=1\\j\neq i}}^{n}x_{j}\right) \\
    &= \frac{\sigma_{n-1}}{\sigma_{n}}
        \end{align*}
    $$

4.  </br>

    $$
        \begin{align*}
            S_{3} &= \sum_{i=1}^{n}\frac{1}{x_{i}^{2}} \\
    &= \left(\sum_{i=1}^{n}\frac{1}{x_{i}}\right)^{2} - 2\sum_{1 \leq i<j \leq n}\underbrace{\frac{1}{x_{i}x_{j}}}_{=\frac{\prod_{\substack{\tiny k= 1\phantom{,2}\\\tiny k\neq i,j}}^{n}x_{k}}{\prod_{k=1}^{n}x_{k}}}\\
    &= \left(\frac{\sigma_{n-1}}{\sigma_{n}}\right)^{2} - 2\frac{\sigma_{n-2}}{\sigma_{n}}
        \end{align*}
    $$
