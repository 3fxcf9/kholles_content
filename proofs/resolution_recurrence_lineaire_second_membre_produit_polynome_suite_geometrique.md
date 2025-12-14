---
title: Résolution explicite (sur un exemple) d'une relation de récurrence linéaire d'ordre 1 ou 2 à coefficients constants avec un second membre produit d'un polynôme et d'une suite géométrique.
authors:
  - Julien Dubousquet
date: 07/12/2025
pid: 1765122409
tags:
  - Relation de récurrence
  
---

### **1. Récurrence linéaire d’ordre 1**

Considérons une relation :

$$
\forall n \in \N,\quad u_{n+1} - a u_n = v_n.
$$

L’ensemble des solutions est une droite affine : une solution particulière + la droite vectorielle des solutions de l’équation homogène associée.

* **Si $a = 0$**, alors les solutions de l’homogène sont :

$$
{\lambda \cdot \gamma^0 \mid \lambda \in \K}.
$$

* **Si $a \neq 0$**, alors les solutions de l’homogène sont :

$$
{(\lambda a^n)_{n\in\N} \mid \lambda \in \K}.
$$

---

Si le second membre est de la forme :

$$
v_n = P(n) c^n
$$

où $P$ est un polynôme, on cherche une solution particulière sous la forme :

$$
u_n^{(p)} = Q(n) c^n,
$$

avec :

* **si $c \neq a$**, alors $\deg Q = \deg P$ ;
* **si $c = a$**, alors $\deg Q = \deg P + 1$.

---

### **2. Récurrence linéaire d’ordre 2**

Considérons :

$$
\forall n \in \N,\quad u_{n+2} + a_1 u_{n+1} + a_0 u_n = v_n
$$

où $(a_0,a_1) \in \K^2$.

L’ensemble des solutions est un plan affine :
*une solution particulière* + *le plan vectoriel des solutions de l’homogène*.

---

#### **Cas où $\K = \C$**

On distingue selon le discriminant $\Delta$ de l’équation caractéristique.

##### **1) $\Delta = 0$**

L’équation caractéristique a une **racine double** $r_0 \in \C$.

* Si $(a_0,a_1)$ ne sont pas tous deux nuls, alors les solutions homogènes sont :

$$
{((\lambda + \mu n) r_0^n)_{n\in\N} \mid (\lambda,\mu)\in\C^2}.
$$

* Sinon :

$$
{\lambda \gamma^0 + \mu \gamma^1 \mid (\lambda,\mu)\in\C^2 }.
$$

##### **2) $\Delta \neq 0$**

L’équation caractéristique admet deux racines distinctes $r_1, r_2$ et :

$$
{(\lambda r_1^n + \mu r_2^n)_{n\in\N} \mid (\lambda,\mu)\in\C^2}.
$$

---

#### **Cas où $\K = \R$**

On distingue trois cas :

##### **1) $\Delta = 0$**

Les solutions homogènes sont identiques au cas $\C$.

##### **2) $\Delta > 0$**

Même structure que le cas $\Delta \neq 0$ sur $\C$.

##### **3) $\Delta < 0$**

On obtient :

$$
{\bigl( \rho^n (\lambda \cos(n\theta) + \mu \sin(n\theta)) \bigr)_{n\in\N} \mid (\lambda,\mu)\in\R^2}
$$

---

### **Recherche d’une solution particulière**

On cherche une solution particulière sous la forme :

$$
u_n^{(p)} = Q(n) a^n,
$$

où :

* si $a$ n’est **pas** racine de l’équation caractéristique,
  alors $\deg Q = \deg P$ ;
* si $a$ est racine **simple**, on ajoute un degré ;
* si $a$ est racine **double**, on ajoute deux degrés ;
  en général : *on ajoute la multiplicité de $a$*.
