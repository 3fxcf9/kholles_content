---
title: Caractérisation des polynômes irréductibles dans $\mathbb{K}[X]$
authors:
  - Félix Rondeau
date: 15/04/2025
pid: 1744736762
tags:
  - polynômes
---

Dans $\K[X]$,

1. Les polynômes de degré 1 sont irréductibles
2. Les polynômes irréductibles de degré 2 sont les polynômes de degré 2 sans racine dans $\K$
3. Les polynômes irréductibles de degré 3 sont les polynômes de degré 3 sans racine dans $\K$

---

1. Il n’existe pas de polynôme non constant de degé strictement inférieur à 1 donc la caractérisation de la non irréductibilité permet de conclure que tous les polynômes de degré 1 sont irréductibles.

2. - L’inclusion directe est immédiate car les polynômes irréductibles (de degré supérieur ou égal à 2) n’ont pas de racines dans $\K$.

   - Soit $P \in \K[X]$ de degré 2 sans racine dans $\K$.
     Supposons que $P$ n’est pas irréductible, alors il admet un diviseur de degré compris entre $1$ et $2-1$ (donc égal à 1). Ainsi, il existe $(a,b) \in \K^{*} \times \K$ tels que

     $$
         \exists Q \in \K[X] : P = (aX+b)Q
     $$

     Prenons-en l’image par le morphisme d’évaluation en $-\frac{b}{a}$:

     $$
         P \left(-\frac{b}{a}\right) = \underbrace{\left(a \times \left(-\frac{b}{a}\right) + a)\right)}_{=0} Q \left(-\frac{b}{a}\right) = 0
     $$

     donc $P$ admet au moins une racine dans $\K$ ce qui est une contradiction. Par conséquent, $P$ est irréductible.

3. - L’inclusion directe est immédiate pour les mêmes aguments qu’au point précédent

   - Soit $P \in \K[X]$ de degré 3 sans racine dans $\K$.
     Supposons que $P$ n’est par irréductible, alors il admet un diviseur de degré compris entre $1$ et $3-1$ (donc de degré 1 ou 2). Fixons un tel diviseur $D$.

     - si $D$ est de degré 1, alors $D$ admet une racine et on montre comme ci-dessus que cette racine est aussi racine de $P$ ce qui contredit le choix de $P$
     - donc $D$ est de degré 2. Comme il divise $P$, il existe $C \in \K[X]$ tel que $CD = P$ et et prenant le degré on obtient $\deg C = \deg P - \deg D = 2-1 = 1$. Ainsi, par ln même raisonnement qu’au point précédent, on montre qu’une racine de $C$ est aussi racine de $P$ ce qui contredit le choix de $P$.

     On a ainsi l’inclusion réciproque.
