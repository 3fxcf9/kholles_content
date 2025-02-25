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

Soit $f \in \mathcal{L}_\K(E, F)$.

$$
    \begin{aligned}
        \ker f & = \left\{ x \in E \;|\; f(x) = 0_F \right\} = f^{-1} (\{0_F\}) \\
        \Im f  & = \left\{ y \in F \;|\; \exists x \in E : f(x) = y \right\}
    \end{aligned}
$$

Nous démontrerons le résultat plus général suivant~:

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

2. $0_F \in F'$ et $f(0_E) = 0_F$ donc $0_E \in f^{-1}(F')$ d'où $f(F') \neq \emptyset$

   Soit $(\alpha, \beta, x, x') \in \K^2 \times f^{-1}(F')^2$ fixés quelconques.

   Par définition, il existe $(y, y') \in F'^2$ tels que $f(x) = y$ et $f(x') = y$.

   Or $F'$ est sous-espace vectoriel donc $\alpha y + \beta y' \in F'$. $f \in \mathcal{L}_\K(E, F)$ d'où $f(\alpha x + \beta x') = \alpha y + \beta y'$. Donc $\alpha x + \beta x' \in f^{-1}(F')$.

   Ainsi, $f^{-1}(F')$ est un sous-espace vectoriel.

   En appliquant ce résultat pour $E' = E$ et $F' = \{0_F\}$, nous obtenons que $\ker f$ et $\Im f$ sont des sous-espaces vectoriels.
