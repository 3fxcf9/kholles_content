---
title: Formule des probabilités composées
authors:
  - Félix Rondeau
date: 06/07/2025
pid: 1749313035
tags:
  - probabilités
---

Si $(A_{i})_{i \in \cc{1,n}}$ est une famille d’événements tels que $P(A_{1} \cap \cdots \cap A_{n-1}) \neq 0$, alors

$$
    P \left(\bigcap_{i=1}^nA_{i}\right) = P(A_{1})P_{A_{1}}(A_{2})P_{A_{1} \cap A_{2}}(A_{3}) \cdots P_{A_{1} \cap  \cdots \cap A_{n-1}}(A_{n})
$$

---

Fixons $(A_{i})_{i \in \cc{1}n}$ de tels événements. Considérons la propriété $\P(\cdot )$ définie pour tout $k \in \icc{2,n}$ par

$$
    \P(k): «\:P \left(\bigcap_{i=1}^{k}A_{i}\right) = P(A_{1})\prod_{i=1}^{k}P_{A_{1} \cap \cdots \cap A_{i-1}}(A_{i})\:»
$$

- $A_{1} \cap \cdots \cap A_{n-1} \subset A_{1}$ donc par croissance de la probabilité $P$,

  $$
      P(A_{1}) \geq P(A_{1} \cap \cdots \cap A_{n-1}) > 0
  $$

  ce qui permet d’utiliser la probabilité conditionnelle $P_{A_{1}}$ :

  $$
      P_{A_{1}}(A_{2}) = \frac{P(A_{1} \cap A_{2})}{P(A_{1})}
  $$

  donc

  $$
      P(A_{1} \cap  A_{2}) = P(A_{1})P_{A_{1}}(A_{2})
  $$

  donc $\P(2)$ est vraie.

- Soit $k \in \icc{2,n-1}$ tel que $\P(k)$ est vraie.

  $A_{1} \cap \cdots \cap A_{n-1} \subset A_{1} \cap \cdots \cap A_{k-1} \cap A_{k}$ donc, par croissance de la probabilté $P$,

  $$
     P(A_{1} \cap \cdots \cap A_{k-1} \cap  A_{k}) \geq P(A_{1} \cap \cdots \cap A_{n-1}) >0
  $$

  ce qui permet d’utiliser la probabilité conditionnelle $P_{A_{1} \cap  \cdots \cap A_{k-1} \cap A_{k}}$ :

  $$
      P_{A_{1} \cap \cdots \cap A_{k-1} \cap A_{k}}(A_{k+1}) = \frac{P(A_{1} \cap \cdots \cap  A_{k} \cap A_{k+1})}{P(A_{1} \cap  \cdots \cap A_{k})}
  $$

  donc

  $$
      P \left(\bigcap_{i=1}^{k+1}A_{i}\right) = P(A_{1} \cap \cdots \cap A_{k-1} \cap A_{k})P_{A_{1} \cap \cdots \cap A_{k-1} \cap A_{k}}(A_{k+1})
  $$

  Or la véracité de $\P(k)$ donne $P \left(\bigcap_{i=1}^{k}A_{i}\right) = P(A_{1})\prod_{i=1}^{k}P_{A_{1} \cap \cdots \cap A_{i-1}}(A_{i})$ donc

  $$
      \begin{align*}
          P \left(\bigcap_{i=1}^{k+1}A_{i}\right) &= P(A_{1} \cap \cdots \cap A_{k-1}\cap A_{k})P_{A_{1} \cap \cdots \cap  A_{k-1} \cap A_{k}}(A_{k+1}) \\
  &= P_{A_{1} \cap \cdots \cap A_{k-1}\cap A_{k}}(A_{k+1}) \times P(A_{1})\prod_{i=1}^{k}P_{A_{1} \cap \cdots \cap A_{i-1}}(A_{i}) \\
  &= P(A_{1})\prod_{i=1}^{k+1}P_{A_{1} \cap  \cdots \cap A_{i-1}}(A_{i})
      \end{align*}
  $$

  d’où la véracité de $\P(k+1)$.

Ainsi, $\P(n)$ est vraie ce qui constitue l’énoncé attendu.
