---
title: Caractérisation de l’indépendance de deux variables aléatoires
authors:
  - Félix Rondeau
date: 18/06/2025
pid: 1750280809
tags:
  - variables aléatoires
---

Deux variables aléatoires $X$ et $Y$ définies sur $\Omega$ à valeurs dans $E_{X}$ et $X_{Y}$ sont indépendantes si et seulement si pour tous $(x,y) \in X(\Omega) \times Y(\Omega)$, les événements $(X=x)$ et $(Y=y)$ sont indépendants.

---

- Supposons $X$ et $Y$ indépendantes. Soient $(x,y) \in X(\Omega) \times Y(\Omega)$. La définition de l’indépendance des variables aléatoires $X$ et $Y$ pour les parties $\{x\}$ et $\{y\}$ donne l’indépendance des événements $(X \in \{x\})=(X=x)$ et $(Y \in \{y\}) = (Y=y)$.

- Supposons que pour tous $(x,y) \in X(\Omega) \times Y(\Omega)$, les événements $(X=x)$ et $(Y=y)$ sont indépendants. Soient $A$ une partie de $X(\Omega)$ et $B$ une partie de $Y(\Omega)$. Dans le système complet associé au couple $(X,Y)$,

$$
    \begin{align*}
        P\bigl((X \in A) \cap (Y \cap B)\bigr) &= \sum_{\substack{x \in X(\Omega)\\y \in Y(\Omega)}}\underbrace{P \big((X \in A) \cap (Y \in B) \cap (X=x \text{ et } Y=y)\big)}_{=P(\emptyset)=0 \text{ si } x \notin A \text{ ou } y \notin B \text{ car } (*)} \\
&= \sum_{\substack{x \in A\\y \in B}}P \big((X \in A) \cap  (X \in B) \cap  (X=x \text{ et } Y=y)\big) \\
&= \sum_{\substack{x \in A\\y \in B}} P(X=x)P(Y=y)\\
&= \sum_{x \in A}\left(P(X=x) \underbrace{\sum_{y \in B}P(Y=y)}_{=P(Y \in B)}\right)\\
&= P(Y \in B)\underbrace{\left(\sum_{x \in A}P(X = x)\right)}_{=P(X \in A)}\\
&=P(X \in A)P(Y \in B)
    \end{align*}
$$

Justifions $(*)$ :

- si $x \notin A$, supposons $(X \in A) \cap (Y \in B)\cap (X=x \text{ et } Y=y)\neq\emptyset$. Alors il existe $\omega$ dans cet ensemble, et

  $$
      x = X(\omega) \in A
  $$

  ce qui est une contradiction

- de même, si $y\notin B$, l’événement ci-dessus est vide.

