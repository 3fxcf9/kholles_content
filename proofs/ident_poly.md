---
title: Identification polynôme/fonction polynomiale
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933254
tags:
  - polynômes
---

Si $\K$ est un corps de cardinal infini, alors il est possible d’itentifier un polynôme de $\K[X]$ et sa fonction polynomiale (i.e. $\Phi$ est injective).

---

- L’inclusion $\{0_{\K[X]}\} \subset \Ker \Phi$ est immédiate car $\Phi \in \L_{\K}(\K[X], \Func(\K))$
- Soit $P \in \Ker \Phi$. Alors $\Phi(P) = 0_{\Func(\K)}$ donc $\forall x \in \K, \tilde{P}(x) = 0_{\K}$. $\K$ étant de cardinal infini, le polynôme $P$ admet une infinité de racine donc $P = 0_{\K[X]}$.

Ainsi, $\Ker \Phi = \{0_{\K[X]}\}$ donc $\Phi$ est un morphisme de $\K$-algèbres injectif.

</br>

#### Contre-exemple si $\K$ n’est pas de cardinal infini

Dans $\F_{p}[X]$, les fonctions polynomiales associées à $X^{p}-X$ et à $0_{\F_{p}[X]}$ sont les mêmes.

Dans $\Z/3\Z$ par exemple,

$$
\begin{align*}
    X^{3}-X &= X(X^{2}-1) \\
&= X(X-1)(X+1) \\
&= X(X-1)(X-2)
\end{align*}
$$

si bien que les fonctions polynomiales associées à ce polynôme et à $0_{\Z/3\Z}$ sont identiques (fonction identiquement nulle).
