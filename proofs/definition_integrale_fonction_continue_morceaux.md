---
title: Définition de l’intégrale d’une fonction continue par morceaux
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746304594
tags:
  - intégration
---

Soit $f \in \CM(\cc{a,b}, \R)$. Posons

$$
    \E^{-}(f) = \left\{\varphi \in \E(\cc{a,b},\R) \where \varphi \leq f\right\}
$$

et

$$
    \E^{+}(f) = \left\{\psi \in \E(\cc{a,b},\R) \where \psi \geq f\right\}
$$

et définissons

$$
    I^{-}(f) = \left\{\int_{a}^{b}\varphi(u)\dd u \where \varphi \in \E^{-}(f)\right\}
$$

et

$$
    I^{+}(f) = \left\{\int_{a}^{b}\psi(u)\dd u \where \psi \in \E^{+}(f)\right\}
$$

Alors $I^{-}(f)$ (resp. $I^{+}(f)$) admet une borne supérieurs (resp. inférieure) et

$$
    \sup I^{-}(f) = \inf I^{+}(f)
$$

On définit alors l’intégrale de $f$ sur le segment $\cc{a,b}$ par

$$
    \int_{a}^{b}f(u)\dd u = \sup I^{-}(f) = \inf I^{+}(f)
$$

---

- **Existence des bornes supérieures / inférieures.**

  - $I^{+}(f)$ est une partie de $\R$, non vide car $\tilde{\infabs{f}{\cc{a,b}}} \in \E^{+}(f)$ donc

    $$
        \int_{a}^{b}\tilde{\infabs{f}{\cc{a,b}}} (x)\dd x = (b-a)\infabs{f}{\cc{a,b}} \in I^{+}(f)
    $$

    De plus, cette partie est minorée car pour toute $\varphi \in \E^{+}(f)$,

    $$
       \forall x \in \cc{a,b}, \varphi(x) \geq f(x) \geq - \infabs{f}{\cc{a,b}}
    $$

    donc

    $$
        \int_{a}^{b}\varphi(x)\dd x \geq \int_{a}^{b}-\tilde{\infabs{f}{\cc{a,v}}}(x)\dd x = (b-a)\underbrace{\left(-\infabs{f}{\cc{a,b}}\right)}_{\text{ne dep. pas de } \varphi}
    $$

  - On procède de même pour montrer l’existence de la borne supérieure de $I^{-}(f)$.

- **Preuve de l’inégalité $\sup I^{-}(f) \leq \inf I^{+}(f)$.**

  Soient $(\varphi, \psi) \in \E^{+}(f)\times \E^{-}(f)$. On a $\forall x \in \cc{a,b}, \varphi(x) \geq f(x) \geq \psi(x)$ donc

  $$
      \int_{a}^{b}\varphi(x) \dd x \geq \int_{a}^{b}\psi(x)\dd x
  $$

  par monotonie de l’intégrale sur les fonctions en escalier.

  Relâchons le caractère fixé de $\varphi$ :

  $$
      \forall \varphi \in \E^{+}(f), \int_{a}^{b}\varphi(x)\dd x \geq \int_{a}^{b}\psi(x)\dd x
  $$

  donc $\int_{a}^{b}\psi(x)\dd x$ minore $I^{+}(f)$, or la borne inférieure est le plus grand des minorants donc $\int_{a}^{b}\psi(x)\dd x \leq  \inf I^{+}(f)$.

  Relâchons le caractère fixé de $\psi$ : l’inégalité ci-dessus exprime que $\inf I^{+}(f)$ est un majorant de $I^{-}(f)$ or la borne supérieure est le plus petit des majorants donc $\sup I^{-}(f) \leq \inf I^{+}(f)$.

- **Preuve de l’inégalité réciproque.**

  Soit $\varepsilon \in \R_{+}^{*}$. Selon le lemme d’approximation des fonctions continues par morceaux,

  $$
      \exists (\varphi,\psi) \in \E^{+}(f) \times \E^{-}(f): \begin{cases}
          \psi \leq f \leq \varphi\\
  \infabs{\varphi-\psi}{\cc{a,b}}\leq \varepsilon
      \end{cases}
  $$

  Observons que $\varphi-\tilde{\varepsilon}\leq f$. En effet,

  $$
      \forall x \in \cc{a,b}, -\varepsilon \leq \varphi(x) - \psi(x) \leq \varepsilon
  $$

  donc $\varphi - \tilde{\varepsilon} \leq f$ sur $\cc{a,b}$. Or $\E(\cc{a,b}, \R)$ étant un espace-vectoriel, $\varphi-\tilde{\varepsilon} \in \E(\cc{a,b}, \R)$ donc $\varphi-\tilde{\varepsilon} \in \E^{-}(f)$, donc

  $$
      \underbrace{\int_{a}^{b}(\varphi-\tilde{\varepsilon})(x)\dd x}_{=\int_{a}^{b}\varphi(x)\dd x - \int_{a}^{b}\varepsilon \dd x = \int_{a}^{b}\varphi(x)\dd x - \varepsilon(b-a)} \leq \sup I^{-}(f)
  $$

  donc $\inf I^{+}(f) \underset{\varphi \in \E^{+}(f)}{\leq} \int_{a}^{b}\varphi(x)\dd x \leq \sup I^{-}(f) + \varepsilon(b-a)$, d’où le résultat par passage à la limite en 0 pour $\varepsilon$.

