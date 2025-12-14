---
title: Caractérisation de la valuation p-adique.
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765727535
tags:
  - Valuation p-adique
---

Soit p $\in \mathcal{P}$ et $(\alpha_0,n) \in \N \times \Z^*$

$$
\alpha_0=\nu_p(n) \iff \exists m \in \Z : 
\begin{cases}
n = p^{\alpha_0}m\\
m \wedge p = 1
\end{cases}
$$

---

( $\implies$ )

Supposons que $\alpha_0 =\nu_p(n)$.

Par définition,
$$\alpha_0=max\{\alpha \in \N \mid p^\alpha \mid n\}
$$
donc $p^{\alpha_0} \mid$ n.

Donc 
$$
\exists m \in \Z : p^{\alpha_0}m = n
$$

Par l'absurde, si $m \wedge p \not = 1$, puisque p est premier, il est premier avec tout entier qu'il ne divise pas, 

donc $p \mid m$, 

donc $\exists m' \in \Z : pm'=m$

donc $p^{\alpha_0 + 1}m'=n$

donc $\alpha_0 + 1 \in \{\alpha \in \N \mid p^{\alpha} \mid n\}$

donc $\alpha_0+1<\alpha_0$ : contradiction.

Ainsi, $m \wedge p = 1$.

($\impliedby$)

Supposons que $\exists m \in \Z : \begin{cases}
n=p^{\alpha_0}n\\
m \wedge p=1
\end{cases}$

- $n=p^{\alpha_0}m$ donc $\alpha_0 \in \{\alpha \in \N \mid \alpha \mid n\}$

- Soit $\beta \in\{\alpha \in \N \mid \alpha \mid n\}$

Par l'absurde, supposons $\beta > \alpha_0$.

Donc $p^{\beta} \mid n \implies p^{\beta} \mid p^{\alpha_0}m \implies p^{\beta - \alpha_0} \mid m \implies p \mid m$ car $p \in \mathcal{P}$

Ce qui contredit $p \wedge m = 1$.


