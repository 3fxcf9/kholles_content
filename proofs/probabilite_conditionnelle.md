---
title: Une probabilité conditionnelle est une probabilité
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749309115
tags:
  - probabilités
---

- Soit $A \in \P(\Omega)$. On a $\emptyset \subset A \cap B \subset B$ donc, par croissance de la probabilité $P$, $0 = P(\emptyset) \leq P(A \cap B) = P(B)$ donc

$$
    0 \leq \frac{P(A \cap B)}{P(B)} \leq 1
$$

si bien que $P_{B}$ est bien définie en tant qu’application de $\P(\Omega)$ dans $\cc{0,1}$.

- $\displaystyle P_{B}(\Omega) = \frac{P(\Omega \cap  B)}{P(B)} = \frac{P(B)}{P(B)} = 1$

- Soient $(A,A') \in \P(\Omega)^{2}$ tels que $A$ et $A'$ sont incompatibles.

$$
    \begin{align*}
        P_{B}(A \cup  A') &= \frac{P(B \cap (A \cup  A'))}{P(B)} \\
&= \frac{P((B \cap  A) \cup (B \cap  A'))}{P(B)} \\
&= \frac{P(B \cap A) + P(B \cap A')}{P(B)} \scriptsize\quad\text{car } B \cap A \text{ et } B \cap A' \text{ sont incompatibles} \\
&= \frac{P(B \cap A)}{P(B)} + \frac{P(B \cap A')}{P(B)} \\
&= P_{B}(A) + P_{B}(A')
    \end{align*}
$$

