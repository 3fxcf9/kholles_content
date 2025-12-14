---
title: Pour p premier, $\forall (a,b) \in \Z^2, \ (a + b)^n \equiv a^p + b^p [p]$. Application au petit théorème de Fermat (2 versions que l'entier est quelconque ou qu'il n'est pas un multiple de p).
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765741716
tags: []
---

Soit $p \in \mathcal{P}$

$$
\forall (a,b) \in \Z^2, \ (a + b)^p \equiv a^p + b^p [p]
$$

**Preuve**

$$
\begin{align}
(a + b)^p-a^p-b^p &= \sum_{k=0}^p \binom{p}{k}a^kb^{p-k}-a^p-b^p\\
&=\sum_{k=1}^{p-1} \binom{p}{k}a^kb^{p-k}+a^p+b^p-a^p-b^p\\
&=\sum_{k=1}^{p-1} \binom{p}{k}a^kb^{p-k}
\end{align}
$$

Or $\forall k \in \left[\!\left[1,p-1\right]\!\right], \ p \mid \binom{p}{k}$

donc 
$$
p \mid \sum_{k=1}^{p-1} \binom{p}{k}a^kb^{p-k}
$$

donc 

$$
(a+b)^p-a^p-b^p \equiv 0 [p].
$$

---

Soit $p \in \mathcal{P}$

$$ (i) \  \forall a \in \Z, \ a^p \equiv a [p].$$

$$ (ii) \ \forall a \in \Z, \ a \not \equiv 0[p] \implies a^{p-1} \equiv 1[p].$$

**Preuve**

(i):

*Cas $a \in \N$*.

Considérons $\forall a \in \N, \mathcal{P}(a): "a^p \equiv a[p]"$

- Pour a=0 : $a^p = 0$ donc $a^p \equiv a[p]$

- Soit $a \in \N$ tel que $\mathcal{P}(a)$ est vraie.

Appliquons le théorème démontré ci-dessus pour $a \leftarrow a$ et $b \leftarrow 1$, avec $a^p \equiv a[p]$ : 

$$
\begin{align}
(a+1)^p &\equiv a^p + 1[p]\\
&\equiv a+1[p]\\
\end{align}
$$

donc $\mathcal{P}(a+1)$ est vraie.

*Cas $a \in \Z \setminus \N$*.

Alors $-a \in \N$, ce qui permet d'appliquer le résultat précédent à $-a$.

$$
(-a)^p \equiv -a [p] \implies (-1)^pa^p \equiv -a[p]
\implies (-1)^{p+1}a^p \equiv a[p]
$$

* Si $p \geq 3$, p est premier 

donc $(-1)^p+1=1$, 

donc $a^p \equiv a[p]$

* Sinon $p=2$, 

donc $(-1)a^2 \equiv a[2]$

donc $2a^2-a^2 \equiv a+0[p]$

par conséquent, $a^2 \equiv a[p]$.

(ii):

Soit $a \in \Z$ tel que $a \not \equiv 0[p]$

D'après (i): $a^p \equiv a[p]$ 

On a donc 

$$
p \mid a^p -a
$$

donc

$$
p \mid a(a^{p-1}-1)
$$

Or $a \not \equiv 0[p]$

Donc 
$$
p \not | \ a
$$ 

Or p est premier, donc 

$$
p \land a =1
$$

Donc d'après le théorème de Gauss : 

$$
p \mid a^{p-1}-1
$$

Ce qui établit :

$$
a^{p-1} \equiv 1[p]
$$