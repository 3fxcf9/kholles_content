---
title: Stabilité de la liberté d’une famille par adjonction d’un vecteur n’appartenant pas au sous-espace qu’elle engendre.
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1740414409
tags:
  - algèbre linéaire
---

Si $\mathcal{F}$ est une famille libre de vecteurs de $E$ et $x\in E\setminus \Vect \mathcal{F}$, alors la famille $\mathcal{F}\cup\{x\}$ est libre.

---

Soit $x_{\triangle} \in E \setminus \Vect\{x_i \mid i \in I\}$ fixé quelconque.  
Soit $(\lambda_i)_{i \in I \cup \{\triangle\}} \in \K^{(I \cup \{\triangle\})}$ fixée quelconque telle que

$$
    \sum_{i \in I \cup \{\triangle\}} \lambda_i x_i = 0_E \qquad (*)
$$

Supposons $\lambda_{\triangle} \neq 0_{\K}$. Alors, $(*)$ donne

$$
\lambda_{\triangle} x_{\triangle} = \sum_{i \in I} -\lambda_i x_i \implies x_{\triangle} = \sum_{i \in I} -\frac{\lambda_i}{\lambda_{\triangle}} x_i
$$

donc $x_{\triangle} \in \Vect\{x_i \mid i \in I\}$, ce qui contredit le choix de $x_{\triangle}$.

Par conséquent, $\lambda_{\triangle} = 0_{\K} \quad (1)$, donc $(*)$ devient

$$
\sum_{i \in I} \lambda_i x_i = 0_E
$$

Or, $(x_i)_{i \in I}$ est libre, donc

$$
    \quad \forall i \in I, \lambda_i = 0_{\K} \qquad (2)
$$

Les relations $(1)$ et $(2)$ donnent $\forall i \in I \cup \{\triangle\}, \lambda_i = 0_{\K}$,  
donc la famille $(x_i)_{i \in I \cup \{\triangle\}}$ est libre.
