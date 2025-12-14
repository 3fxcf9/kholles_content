---
title: Théorème de Gauss
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765725568
tags:
  - Arithmétique
---

**Énoncé.**  
Soient $(a,b,c)\in\Z^{3}$ tels que

$$
\left.
\begin{array}{l}
a \mid bc \\
a \land b = 1
\end{array}
\right\}
\ \Longrightarrow\ a \mid c.
$$

---

**Preuve.**  

Soient $(a,b,c)\in\Z^{3}$ fixés quelconques.  
$a$ divise $bc$, donc

$$
\exists k \in \Z \text{ tel que } ka = bc.
$$

$a$ et $b$ sont premiers entre eux, donc

$$
\exists (u,v)\in\Z^{2} \text{ tel que } au + bv = 1.
$$

En multipliant cette relation par $c$, on obtient

$$
auc + bvc = c.
$$

En utilisant la relation $bc = ka$, il vient

$$
auc + akv = c,
$$

c’est-à-dire

$$
a(uc + kv) = c,
$$

avec $uc + kv \in \Z$.  

Ainsi, $a \mid c$.
