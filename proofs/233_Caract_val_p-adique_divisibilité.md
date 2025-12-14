---
title: Caractérisation de $a \mid b$ par les valuations p-adiques (preuve de la propriété de morphisme des valuations p-adiques utilisée).
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765733436
tags:
  - Valuation p-adique.
---

Soit $p \in \mathcal{P}$

Montrons que $\nu_p$ est un morphisme de $(\Z,\times)$ dans $(\N,+)$, c'est-à-dire :

$$
\forall (a,b) \in \Z ^2,\ \nu_p(ab) = \nu_p(a) + \nu_p(b)
$$

- Utilisons la caractérisation de la valuation p-adique.

$$
\exists (m_a,m_b) \in \Z^2 : 
\begin{cases}
a=p^{\nu_p(a)}m_a\\
b=p^{\nu_p(b)}m_b\\
m_a \wedge p = 1\\
m_b \wedge p = 1
\end{cases}.
$$

Donc $ab = p^{\nu_p(a)+\nu_p(b)}m_am_b$ et $m_am_b \wedge p = 1$ car p est premier aves les deux.

Donc (caractérisation de la valuation p-adique) : $\nu_p(ab) = \nu_p(a) + \nu_p(b)$


---

Soit $(a,b) \in \Z^2$.

Montrons que 

$$
a \mid b \iff \forall p \in \mathcal{P},\ \nu_p(a) \leq \nu_p(b).
$$

($\implies$)
Supposons que $a \mid b$.

$\exists k \in \Z : ak = b$.

Soit $p \in \mathcal{P}$.

$\nu_p(b) = \nu_p(ak) = \nu_p(a) + \nu_p(k) \geq \nu_p(a)$.

donc $\nu_p(a) \leq \nu_p(b)$.

($\impliedby$) 
Supposons que $\forall p \in \mathcal{P},\ \nu_p(a) \leq \nu_p(b)$.

$$
b = \varepsilon \prod_{p \in \mathcal{P}}p^{\nu_p(b)}=\varepsilon \prod_{\stackrel{p \in \mathcal{P}}{\nu_p(b) \not = 0}} p^{\nu_p(b)} = \prod_{\stackrel{p \in \mathcal{P}}{\nu_p(b) \not = 0}}p^{\nu_p(a)} \times \varepsilon \prod_{\stackrel{p \in \mathcal{P}}{\nu_p(b) \not = 0}}p^{\nu_p(b)-\nu_p(a)}
$$

Or $\forall p \in \mathcal{P}, \nu_p(a) \leq \nu_p(b)$ donne :

$$
\{p \in \mathcal{P} \mid \nu_p(a) \not = 0\} \subset \{p \in \mathcal{P} \mid \nu_p(b) \not = 0\}
$$

Donc
$$
|a| = \prod_{p \in \mathcal{P}}p^{\nu_p(a)} = \prod_{\stackrel{p \in \mathcal{P}}{\nu_p(a) \not = 0}}p^{\nu_p(a)}=\prod_{\stackrel{p \in \mathcal{P}}{\nu_p(b) \not = 0}}p^{\nu_p(a)}
$$

On a donc :

$$
b=|a| \times \varepsilon \prod_{\stackrel{p \in \mathcal{P}}{\nu_p(b) \not = 0}}p^{\nu_p(b)-\nu_p(a)}
$$

Donc $a \mid b$.