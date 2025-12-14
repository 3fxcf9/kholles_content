---
title: Calcul de somme d’une série numérique
authors:
  - Félix Rondeau
date: 05/09/2025
pid: 1746820424
tags:
  - intégration
  - séries
---

$$
    \forall x \in  \cc{0,1}, \lim_{n\to+ \infty}\sum_{k=1}^{n}(-1)^{k-1}\frac{x^{k}}{k} = \ln(1+x)
$$

---

Soit $x \in \cc{0,1}$. $t \longmapsto \ln(1+t)\in \Cont^{\infty}(\cc{0,1}\R)$ donc on peut appliquer la formule de Taylor avec reste intégral à cette fonction en 0 :

$$
    \ln(1+x) - \sum_{k=0}^{n}\frac{\left[\ln(1+x)\right]_{x=0}^{(k)}}{k!}(x-0)^{k} = \int_{0}^{x}\frac{(x-t)^{n} \left[\ln(1+u)\right]_{u=t}^{(n+1)}}{n!}\dd t
$$

donc

$$
    \ln(1+x) - \left(\ln(1+0) + \sum_{k=1}^{n}\frac{(-1)^{k+1}(k-1)!}{k!}x^{k}\right) = \int_{0}^{x}\frac{(x-t)^{n}}{n!}\frac{(-1)^{n+2}n!}{(1+t)^{n+1}}\dd t
$$

donc

$$
    \ln(1+x) - \sum_{k=1}^{n}(-1)^{k+1}\frac{x^{k}}{k} = (-1)^{n} \int_{0}^{x}\frac{(x-t)^{n}}{(1+t)^{n+1}}\dd t
$$

or

$$
\begin{align*}
    \abs{(-1)^{n}\int_{0}^{x}\frac{(x-t)^{n}}{(1+t)^{n+1}}\dd t} &\leq \underbrace{\Biggl\Vert\underbrace{s \longmapsto \frac{1}{(1+s)^{n+1}}}_{\text{decr. et } \geq 0 \text{ sur } \cc{0,x}}\Biggr\Vert_{\infty,\cc{0,x}}}_{=1} \times \underbrace{\int_{0}^{x}\abs{(x-t)^{n}}\dd t}_{=\int_{0}^{x}(x-t)^{n}\dd t = \left[\frac{-(x-t)^{n+1}}{n+1}\right]_{0}^{x}}\\
& \leq \frac{x^{n+1}}{n+1} \leq \frac{1}{n+1} \arrowlim{n\to +\infty} 0
\end{align*}
$$

donc le reste intégral converge vers 0, donc $\left(\sum_{k=1}^{n}\frac{(-1)^{k+1}x^{k}}{k}\right)_{n \in \N^{*}}$ converge vers $\ln(1+x)$.
