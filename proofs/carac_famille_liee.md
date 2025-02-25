---
title: Caractérisation d’une famille liée
authors:
  - Hugo Vangilluwen
  - George Ober
  - Kylian Boyet
  - Félix Rondeau
date: 24/02/2025
pid: 1740414406
tags:
  - algèbre linéaire
---

Une famille est liée si et seulement si l'un de ses vecteurs est une combinaison linéaires d'autres vecteurs de la famille.

$$
    (x_i)_{i \in I} \text{ est liée} \iff \exists i_0 \in I : \exists (\lambda_i)_{i \in I\setminus\{i_0\}} \in \K^{\left( I \setminus \{i_0\} \right)} : x_{i_0} = \sum_{\substack{i \in I \\ i \neq i_0}} \lambda_i \ldotp x_i
$$

---

Supposons que $(x_i)_{i \in I}$ est liée.  
Par définition,

$$
\displaystyle \exists (\mu_i) \K^{(I)} :
\begin{cases}
\sum_{i\in I}\mu_{i} x_{i} & =0_{E} \\
(\mu_{i})_{i\in I}         & \neq (0_{\K})_{i\in I}
\end{cases}
$$

Donc $\exists i_0 \in I : \mu_{i_0} \neq 0_\K$. Fixons un tel $i_0$.

$$
\mu_{i_0} x_{i_0} + \sum_{i \in I \setminus \{i_0\}} \mu_i x_i = 0_E
$$

Or $\mu_{i_0} \neq 0$, donc

$$
\displaystyle x_{i_0} = \sum_{i \in I \setminus \{i_0\}} \left( \mu_{i_0}^{-1} \times (-\mu_i) \right) \ldotp x_i
$$

En posant $\lambda_i = \mu_{i_0}^{-1} \times (-\mu_i)$, on obtient

$$
x_{i_0} = \displaystyle \sum_{i \in I \setminus \{i_0\}} \lambda_i \ldotp x_i
$$

Supposons maintenant qu’il existe $i_0 \in I$ et $(\lambda_i)_{i \in I\setminus\{i_0\}} \in \K^{\left( I \setminus \{i_0\} \right)}$ tels que

$$
x_{i_0} = \sum_{\substack{i \in I \\ i \neq i_0}} \lambda_i \ldotp x_i
$$

Alors $-x_{i_0} + \sum_{\substack{i \in I \\ i \neq i_0}} \lambda_i \ldotp x_i = 0_E$.  
Posons $\mu_{i_0} = - 1_\K$ et, pour tout $i \in I \setminus \{i_0\}$, $\mu_i = \lambda_i$.  
Ainsi, $(\mu_i)_{i \in I} \in \K^{(I)}$ et $\sum_{i \in I} \mu_i \ldotp x_i = 0_E$. Or $\mu_{i_0} \neq 0_\K$, donc $(\mu_i)_{i \in I} \neq (0_\K)_{i \in I}$.  
Ainsi, $(\mu_i)_{i \in I}$ est liée.
