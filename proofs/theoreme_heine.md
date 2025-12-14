---
title: Théorème de Heine
authors:
  - Félix Rondeau
date: 05/03/2025
pid: 1746295014
tags:
  - intégration
---

Une fonction continue sur un segment est uniformément continue sur ce segment.

---

Soit $f$ définie et continue sur un segment $\cc{a,b} \subset \R$. Par l’absurde, supposons $f$ non continue, i.e.

$$
    \exists \varepsilon_{0} \in \R_{+}^{*}, \forall \eta \in \R^{*}_{+}, \exists (x,y) \in \cc{a,b}^{2}: \abs{x-y} \leq \eta \text{ et } \abs{f(x) - f(y)} > \varepsilon_{0}
$$

Pour tout $n \in \N^{*}$, appliquons cette définition pour $\eta \leftarrow \frac{1}{n}$ :

$$
    \exists (x_{n},y_{n}) \in  \cc{a,b}^{2}: \underbrace{\abs{x_{n}-y_{n}}\leq  \frac{1}{n}}_{(1)} \text{ et } \underbrace{\abs{f(x_{n}) - f(y_{n})} > \varepsilon_{0}}_{(2)}
$$

La suite $(x_{n})_{n \in \N}$ est à valeurs dans $\cc{a,b}$ donc est bornée, selon le théorème de Bolsano-Weierstrass, il existe une fonction $\varphi$ de $\N^{*}$ dans $\N^{*}$ strictement croissante telle que la sous-suite $\left(x_{\varphi(n)}\right)$ converge vers une limite finie $\ell \in \R$.

De plus, en passant à la limite, comme $\forall n \in \N^{*}, a \leq  x_{\varphi(n)} \leq  b$, alors $\ell \in  \cc{a,b}$.

$$
\begin{align*}
    \forall n \in \N^{*}, \abs{y_{\varphi(n)} - \ell} - \abs{y_{\varphi(n)} - x_{\varphi(n)} + x_{\varphi(n)} - \ell} &\leq  \abs{y_{\varphi(n)} - x_{\varphi(n)}} + \abs{x_{\varphi(n)} - \ell} \\
& \leq \frac{1}{\varphi(n)} + \abs{x_{\varphi(n)} - \ell} \arrowlim{x\to +\infty} 0
\end{align*}
$$

donc le théorème sans nom permet d’affirmer que $(y_{\varphi(n)})$ converge vers $\ell$.

Appliquons $(2)$ pour $n \leftarrow \varphi(n)$ :

$$
    \forall n \in \N^{*}, \underbrace{\abs{f(x_{\varphi(n)}) - f(y_{\varphi(n)})}}_{\longrightarrow f(l) - f(l)} > \varepsilon_{0}
$$

si bien qu’en passant à la limite, on obtient la contradiction $0 \geq \varepsilon_{0}$.
