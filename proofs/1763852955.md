---
title: Montrer que $\mathbb{Q}$ est dense dans $\mathbb{R}$ et $\mathbb{R}\setminus\mathbb{Q}$ sont denses dans $\mathbb{R}$.
authors:
  - Julien Dubousquet
date: 11/23/2025
pid: 1763852955
tags:
  - Réels
---

---

Soit $x \in \mathbb{R}$ fixé.  
Posons 
$$
\forall n \in \mathbb{N}, \quad a_n = \frac{\lfloor 2^n x \rfloor}{2^n}.
$$

Soit $n \in \mathbb{N}$ fixé.  

- $a_n \in \mathbb{Q}$ car $\lfloor 2^n x \rfloor \in \mathbb{Z}$ et $2^n \in \mathbb{N}$.
- De plus, 
$$
a_n = \frac{\lfloor 2^n x \rfloor}{2^n} \implies \frac{2^n x - 1}{2^n} \le a_n \le \frac{2^n x}{2^n} \implies x - \frac{1}{2^n} \le a_n \le x.
$$
Or $\frac{1}{2^n} \to 0$ quand $n \to +\infty$, donc d'après le théorème de limite par encadrement, 
$$
a_n \to x \quad \text{quand } n \to +\infty.
$$

Ainsi, d'après la caractérisation séquentielle de la densité, $\mathbb{Q}$ est dense dans $\mathbb{R}$.

---

Soit $x \in \mathbb{R}$ fixé.  
Alors $x + \sqrt{2} \in \mathbb{R}$.  
D'après la démonstration précédente, il existe $b \in \mathbb{Q}^{\mathbb{N}}$ tel que 
$$
b_n \to x + \sqrt{2} \quad \text{quand } n \to +\infty.
$$
Fixons une telle suite $b$ et considérons $c = b - \sqrt{2}$.  

Soit $n \in \mathbb{N}$ fixé.  

- $c_n \in \mathbb{R} \setminus \mathbb{Q}$ car $b_n \in \mathbb{Q}$ et $\sqrt{2} \in \mathbb{R} \setminus \mathbb{Q}$.
- De plus,
$$
\left\{
\begin{matrix}
b_n \to x + \sqrt{2} \\
c_n = b_n - \sqrt{2}
\end{matrix}
\right.
\implies c_n \to x \quad \text{quand } n \to +\infty.
$$

Donc, d'après la caractérisation séquentielle de la densité, $\mathbb{R} \setminus \mathbb{Q}$ est dense dans $\mathbb{R}$.

