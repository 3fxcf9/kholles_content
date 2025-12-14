---
title: L'ensemble des nombres premiers est infini.
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765721603
tags:
  - Nombres premiers
---

Montrer que l'ensemble $\mathcal{P}$ des nombres premiers est infini.

---

Par l'absurde, supposons que $\mathcal{P}$ est fini.

$$
2 \in \mathcal{P} \implies \mathcal{P} \ne \emptyset
$$

Posons 
$$
N=|\mathcal{P}| \in \N^*
$$

$\N$ est totalement ordonné donc les $N$ nombres premiers peuvent être numérotés dans l'ordre croissant.

$$
p_1 < p_2< \dots < p_N
$$

Considérons 
$$
m=1+ \prod_{i=1}^N p_i
$$

Alors :

$$
\begin{rcases}
m>p_N & \implies & m \not \in \mathcal{P} \\
m>p_1 & \implies & m \geq 2
\end{rcases}
\implies \text{m admet un diviseur premier}
$$

$$
\exists i_0 \in \left[\!\left[ 1,N \right]\!\right] : p_{i_0} \mid 1 + \prod_{i = 1}^N p_i
$$

or 

$$
p_{i_0} \mid \prod_{i=1}^N p_i \implies p_{i_0}\mid 1 + \prod_{i = 1}^N p_i - \prod_{i=1}^N p_i
$$

donc $p_{i_0} \mid 1$,

donc $p_{i_0} \in \{-1,1\}$,

ce qui est faux car $p_{i_0} \in \mathcal{P}$.

Donc $\mathcal{P}$ est infini.

