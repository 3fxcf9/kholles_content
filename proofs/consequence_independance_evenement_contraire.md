---
title: Conséquence de l’indépendance sur l’événement contraire
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749310044
tags:
  - probabilités
---

Si $A$ et $B$ sont deux événements indépendants, alors les événements $A$ et $\overline B$ sont indépendants.

<br/>

On en déduit une généralisation: Si $A_{1}, \ldots, a_{n}$ sont des événements mutuellement indépendants, alors en choisissant, pour tout $i \in \icc{1,n}, B_{i} \in \{A_{i}, \overline{A_{i}}\}$, les événements $B_{1}, \ldots, B_{n}$ sont mutellement indépendants.

---

Soit $A$ et $B$ deux événements indépendants.

$$
    A = A \cap \Omega = A \cap  \left(\overline B \sqcup B\right) = (a \cap \overline B)\sqcup (A \cap  B)
$$

donc

$$
    \begin{align*}
        P(A) &= P(A \cap  \overline B) + P(A \cap  B) \\
&= P(A \cap  \overline B) + P(A)P(B) \scriptsize\quad\text{car } A \text{ et } B \text{ sont indépendants}
    \end{align*}
$$

donc

$$
    P(A \cap \overline B) = P(A) - P(A)P(B) = P(A)\underbrace{(1-P(B))}_{=P(\overline B)} = P(A)P(\overline B)
$$

Par conséquent, $A$ et $\overline B$ sont indépendants.

