---
title: Interpolation de Lagrange
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933251
tags:
  - polynômes
---

Soient $n \in \N$, $(a_{0}, \ldots, a_{n})\in \K^{n+1}$ deux à deux distincts et $(b_{0}, \ldots, b_{n})\in \K^{n+1}$.

Il existe un unique $P \in \K_{n}[X]$, appelé le **polynôme d’interpolation de Lagrange en $\{(a_{0}, b_{0}), \ldots, (a_{n}, l_{n})\}$** tel que

$$
    \forall i \in \iset{0,n}, P(a_{i}) = b_{i}
$$

---

Considérons l’application

$$
    \Phi : \applic{\K_{n}[X]}{\K^{n+1}}{P}{(P(x_{0}), \ldots, P(a_{n}))}
$$

- _$\Phi$ est bien définie :_ pour tout $P \in \K_{n}[X]$, la liste $(P(a_{0}), \ldots, P(a_{n}))$ est bien définie
- _$\Phi$ est une aplication linéaire de $\K_{n}[X]$ dans $\K^{n+1}$ :_
  Soient $(P_{1}, P*{2})\in \K*{n}[X]^{2}$ et $(\alpha_{1}, \alpha_{2})\in \K^{2}$.

  $$
      \begin{align*}
          \Phi(\alpha_{1}\cdot P_{1} + \alpha_{2}\cdot P_{2}) &= ((\alpha_{1}\cdot P_{1} + \alpha_{2}\cdot P_{2})(a_{0}), \ldots, (\alpha_{1}\cdot P_{1} + \alpha_{2}\cdot P_{2})(a_{n})) \\
          &= (\alpha_{1}\cdot P_{1}(a_{0}) + \alpha_{2}\cdot P_{2}(a_{0}), \ldots, \alpha_{1}\cdot P_{1}(a_{n})+\alpha_{2}\cdot P_{2}(a_{n})) \\
          &= (\alpha_{1}\cdot P_{1}(a_{0}), \ldots, \alpha_{1}\cdot P_{1}(a_{n})) + (\alpha_{2}\cdot P_{2}(a_{0}), \ldots, \alpha_{2}\cdot P_{2}(a_{n})) \\
          &= \alpha_{1}\cdot (P_{1}(a_{0}), \ldots, P_{1}(a_{n})) + \alpha_{2}\cdot (P_{2}(a_{0}), \ldots, P_{2}(a_{n})) \\
          &= \alpha_{1}\cdot \Phi(P_{1}) + \alpha_{2}\cdot \Phi(P_{2})
      \end{align*}
  $$

- _$\Phi$ est injective :_ Soit $P \in \K_{n}[X]$ fixée quelconque telle que $(P(a_{0}), \ldots, P(a_{n}))=0_{\K^{n+1}}$. Si $P \neq 0_{\K_{n}[X]}$, alors son degré étant majoré par $n$, $P$ possède, dans $\K$, au plus $n$ racines deux à deux distinctes, or $\Phi(P)=0_{\K^{n+1}}$ permet d’affirmer que $P$ possède au moins $n+1$ racines deux à deux distinctes (les $(a_{i})_{i \in \iset{0,n}}$ sont deux à deux distincts) d’où une contradiction et $\Ker \Phi = \{0_{\K_{n}[X]}\}$.

Ainsi, $\Phi$ est une application linéaire injective de $\K_{n}[X]$ dans $\K^{n+1}$, or $\dim_{\K} \K_{n}[X] = n+1 = \dim_{\K} \K^{n+1}$, donc $\Phi$ est un isomorphisme. Par conséquent, il existe un unique $P \in \K_{n}[X]$ tel que

$$
    \forall i \in \iset{0,n}, P(a_{i}) = b_{i}
$$
