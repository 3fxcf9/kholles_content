---
title: Relation coefficients racines pour un polynôme scindé
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743933255
tags:
  - polynômes
---

Soit $P(X) = \sum_{k=0}^{n}a_{k}X^{k}$ un polynôme scindé dans $\K$, de degré $n \in \N^{*}$, dont les racines, répétées avec multiplisité sont $x_{1}, \ldots, x_{n}$.

Alors $P(X) = a_{n} \prod_{i=1}^{n}(X-x_{i})$ si bien que

$$
    \forall i \in \iset{1,n}, \sigma_{i} = (-1)^{i} \frac{a_{n-i}}{a_{n}}
$$

---

L’égalité entre la forme de $P$ faisant apparaître ses coefficient et celle obtenue en développant sa forme factorisée $P = a_{n} \prod_{i=1}^{n}(X-x_{i})$, i.e.

$$
    \sum_{k=0}^{n}a_{k}X^{k} = a_{n} \left(X^{n} + \sum_{k=0}^{n-1}(-1)^{n-k}\sigma_{n-k}X^{k}\right)
$$

permet d’obtenir les relations coefficients racines par unicité des coefficients d’un polynôme :

$$
    \forall k \in \iset{0,n-1}, a_{k} = a_{n}(-1)^{n-k}\sigma_{n-k}
$$

d’où en posant $i=n-k$,

$$
    \forall i \in \iset{1,n}, a_{n-i} = a_{n}(-1)^{i}\sigma_{i} \implies \sigma_{i} = (-1)^{i} \frac{a_{n-i}}{a_{n}}
$$

> **Explication du développement de $(X-x_{1})\times (X-x_{2}) \times \cdots \times (X-x_{n})$ :**
> On l’obtient en choisissant dans chacun des $n$ facteurs soit « $X$ » soit « $-x_{i}$ ».
>
> - le degré maximal d’un terme issue du développement est obtenu en choisissant « $X$ » dans chacun des facteurs, ce qui donne le terme $X^{n}$
> - le terme de degré $n-1$ est obtenue en choisissant « $X$ » dans tous les facteurs sauf un, d’où le terme de degré $n-1$ :
>   $$
>     -x_{1}X^{n-1} - x_{2}X^{n-1} - \cdots - x_{n}X^{n-1} = -\sigma_{1}X^{n-1}
>   $$
> - ...
> - le terme de degré 1 est obtenu en choisissant « $-x_{i}$ » dans chaque facteur sauf un, ce qui donne
>   $$
>      (-x_{2})(-x_{3}) \cdots (-x_{n-1})(-x_{n})X + (-x_{1})(-x_{3})\cdots (-x_{n})X + \cdots + (-x_{1})(-x_{2})\cdots(-x_{n-1})X = (-1)^{n-1}\sigma^{n-1}X
>   $$
> - le terme constant est obtenu en ne choisissant que « $x_{i}$ » :
>   $$
>      (-x_{1})(-x_{2})\cdots(-x_{n})X^{0} = (-1)^{n}\sigma_{n}X^{0}
>   $$
