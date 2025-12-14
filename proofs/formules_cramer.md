---
title: Formules de Cramer
authors:
  - Félix Rondeau
date: 05/18/2025
pid: 1747579312
tags:
  - déterminant
  - matrices
---

La solution du systeme linéaire

$$
    AX = B
$$

d’inconnue $X \in \M_{n,1}(\K)$ vaut, dans le cas où elle existe et est unique (donc si $A$ est inversible)

$$
    \left(
\frac{\abs{\begin{array}{c|c|c|c}\\
        B & C_{2} & \cdots & C_{n}\\\\
    \end{array}}}{\det A},
\ldots,
\frac{\abs{\begin{array}{c|c|c|c}\\
        C_{1} & \cdots & C_{i-1} & B & C_{i+1} & \cdots & C_{n}\\\\
    \end{array}}}{\det A}
,
\ldots,
\frac{\abs{\begin{array}{c|c|c|c}\\
        C_{1} & \cdots & C_{n-1} & B\\\\
    \end{array}}}{\det A}
\right)
$$

---

Comme $A$ est inversible, ses colonnes $(C_{1}, \ldots, C_{n})$ forment une base de $\M_{n,1}(\K)$, donc il existe des scalaires $b_{1}, \ldots, b_{n}$ tels que

$$
    B = \sum_{k=1}^{n}b_{k}C_{k}
$$

Alors, pour tout $i \in \icc{1,n}$,

$$
\begin{align*}
    \det \left(\begin{array}{c|c|c|c|c} \\
        C_{1} & \cdots & \smash{\underbrace{B}_{i\mathrm{^e} \text{ col.}}} & \cdots & C_{n} \\\\
    \end{array}\right) &= \det \left(\begin{array}{c|c|c|c|c} \\
        C_{1} & \cdots & \smash{\underbrace{\sum_{k=1}^{n}b_{k}C_{k}}_{i\mathrm{^e} \text{ col.}}} & \cdots & C_{n} \\\\
    \end{array}\right) \\\\
&=\sum_{k=1}^{n}b_{k} \det \underbrace{\left(\begin{array}{c|c|c|c|c}
    C_{1} & \cdots & C_{k} & \cdots & C_{n}
\end{array}\right)}_{=\begin{cases}
    0 & \text{si }k\neq i \\
\det A & \text{si }k=i
\end{cases}}
\end{align*}
$$

donc pour tout $i \in \icc{1,n}$,

$$
    b_{i} = \frac{\det \left(\begin{array}{c|c|c|c|c}
        C_{1} & \cdots & B & \cdots & C_{n}
    \end{array}\right)}{\det A}
$$

Par ailleurs,

$$
    \begin{align*}
        B &= b_{1}C_{1} + \cdots + b_{n}C_{n} \\
&= b_{1}AE^{11} + \cdots + b_{n}AE^{n,1} \\
&= A \left(b_{1} E^{1,1} + \cdots + b_{n}E^{n,1}\right) \\
&= A \mtx{b_{1} \\ \vdots \\ b_{n}}
    \end{align*}
$$

Ainsi,

$$
    \mtx{b_{1} \\ \vdots \\ b_{n}}
$$

est la solution du système linéaire.

