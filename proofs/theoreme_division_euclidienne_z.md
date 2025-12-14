---
title: Théoréme de la division Euclidienne dans $\mathbb{Z}$.
authors:
  - Julien Dubousquet
date: 22/11/2025
pid: 1763850975
tags:
  - Arithmétique
---

---

$$
\forall (a,b)\in \mathbb{Z}^2,\ 
\exists ! (q,r)\in \mathbb{Z}\times \mathbb{N}:\ 
\begin{cases}
a = bq + r,\\
r \in [\![0\,;\,|b|-1]\!].
\end{cases}
$$

---

### **Unicité**

Soient $(a,b)\in \mathbb{Z}^2$ et deux couples $((q,r),(q',r'))\in (\mathbb{Z}\times \mathbb{N})^2$ tels que :

$$
\begin{cases}
a = bq + r,\\
0 \le r \le |b|-1,
\end{cases}
\qquad
\begin{cases}
a = bq' + r',\\
0 \le r' \le |b|-1.
\end{cases}
$$

Alors :

$$
b(q - q') = r' - r.
$$

Comme $-(|b|-1) \le r' - r \le |b|-1$, on obtient en divisant par $|b|$ :

$$
-1 < q - q' < 1.
$$

Mais $q-q' \in \mathbb{Z}$, donc :

$$
q - q' = 0 \quad \Rightarrow \quad q = q',\quad r = r'.
$$

On a donc bien l’unicité.

---

### **Existence**

Supposons $b \ge 1$.  
Posons :

$$
\Omega = \{ k \in \mathbb{Z} \mid kb \le a \}.
$$

- $\Omega \subset \mathbb{Z}$.
- $\Omega$ est non vide : par exemple $-|a| \in \Omega$.
- $\Omega$ est majorée par $|a|$.  
  En effet, si $k > |a|$, alors :

  $$
  kb > |a|b > a,
  $$

  ce qui contredit la définition de $\Omega$.

Donc $\Omega$ admet un plus grand élément, noté $q$.

Posons :

$$
r = a - bq.
$$

Alors $a = bq + r$ et, comme $q = \max \Omega$, $q\in \mathbb{Z}$ et donc $r\in \mathbb{Z}$.

De plus :

- Comme $q\in \Omega$, on a $bq \le a$ donc :

  $$
  0 \le r.
  $$

- Comme $q$ est le plus grand élément de $\Omega$, on a $b(q+1) > a$, d’où :

  $$
  b > r \quad \Longleftrightarrow \quad r \in [\![0\,;\,|b|-1]\!].
  $$

Si $b < 1$, il suffit d’appliquer la preuve précédente à $-b$ et remplacer $q$ par $-q$.

Ainsi, l’existence de la décomposition euclidienne est démontrée.
