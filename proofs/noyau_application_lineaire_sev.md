---
title: Le noyau et l'image d'une application linéaire sont des sous-espaces vectoriels
authors:
  - Hugo Vangilluwen
  - George Ober
  - Kylian Boyet
  - Félix Rondeau
date: 24/02/2025
pid: 1740414411
tags:
  - algèbre linéaire
---

Soient $f \in \mathcal{L}_\K(E, F)$, $F'$ un sous-espace vectoriel de $F$ et $E'$ un sous-espace vectoriel de $E$.

Nous démontrerons le résultat plus général suivant :

1. $f(E')$ est un sous-espace vectoriel de $F$.
2. $f^{-1}(F')$ est un sous-espace vectoriel de $E$.

---

1. $0_E \in E'$ et $f(0_E) = 0_F$ donc $0_F \in f(E')$ d'où $f(E') \neq \emptyset$

   Soit $(\alpha, \beta, y, y') \in \K^2 \times f(E')^2$ \fqs.

   Par définition, il existe $(x, x') \in E'^2$ tels que $f(x) = y$ et $f(x') = y$.

   $$
   \begin{aligned}
   \alpha y + \beta y'
   & = \alpha f(x) + \beta f(x') \\
   & = f( \alpha x + \beta x' ) \quad \text{ car } f \in \mathcal{L}\_\K(E, F) \\
   & \in f(E') \quad \text{ car } \alpha x + \beta x' \in E' \text{ puisque } E' \text{ est un sous-espace vectoriel}
   \end{aligned}
   $$

   Donc $f(E')$ est un sous-espace vectoriel.

2. - $f^{-1}(F') \subset E$ et $E$ est un $\K$-espace vectoriel.
   - $f^{-1}(F')\neq \emptyset$ car $f(O_{E})=0_{F}\in F'$ donc $O_{E}\in f^{-1}(F')$
   - Soient $(x_{1}, x_{2})\in f^{-1}(F')^{2}$ et $\lambda\in\K$ fixés quelconques. Calculons

   $$
   f(\lambda x_{1} + x_{2})=\lambda \underbrace{f(x_{1})}_{\in F' \quad\text{car $x_{1}\in f^{-1}(F')$}}+\underbrace{f(x_{2})}_{\in F' \quad\text{car $x_{2}\in f^{-1}(F')$}} \in F'
   $$

   donc $\lambda x_{1}+x_{2} \in f^{-1}(F')$.
