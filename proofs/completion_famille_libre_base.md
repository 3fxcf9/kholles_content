---
title: Complétion d’une famille libre en une base
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060864
tags:
  - algèbre linéaire
---

Toute famille libre $\mathcal{L}$ finie d’un $\K$-espace vectoriel $E$ de dimension finie peut être complétée en une base de $E$ en lui adjoignant des éléments d’une famille génératrice finie $\mathcal{G}$ de $E$.

---

Posons $\mathcal{E}=\left\{|(\mathcal{L}, \mathcal{G}') \;\middle|\; \mathcal{G}' \text{ sous-famille de } \mathcal{G}, (\mathcal{L}, \mathcal{G}') \text{ libre dans } E\right\}$. Alors

- C’est une partie de $\N$ par construction
- Elle n’est pas vide car contient $|\mathcal{L}|$
- Elle est majorée : pour tout $\mathcal{G}'\in \mathcal{P}(G)$ tel que $(\mathcal{L}, \mathcal{G}')$ est libre dans $E$,
  $$
      |(\mathcal{L}, \mathcal{G}')| \leq |\mathcal{L}|+|\mathcal{G}'| \leq |\mathcal{L}| + |\mathcal{G}|
  $$

donc $\mathcal{E}$ admet un plus grand élément. Par définition d’un plus grand élément

$$
    \exists \mathcal{G}_{0}\in \mathcal{P}(\mathcal{G}): (\mathcal{L}, \mathcal{G}_{0}) \text{ est libre dans $E$}, |(\mathcal{L}, \mathcal{G}_{0})| = \max \mathcal{E}
$$

Montrons que $(\mathcal{L}, \mathcal{G}_{0})$ est une base de $E$.

- Par construction, $(\mathcal{L}, \mathcal{G}_{0})$ est libre
- Supposons que $(\mathcal{L}, \mathcal{G}_{0})$ n’engendre pas $E$. Puisque $\mathcal{G}$ est génératrice dans $E$, si $\mathcal{G}\subseteq\Vect(\mathcal{L}, \mathcal{G}_{0})$, alors $(\mathcal{L}, \mathcal{G}_{0})$ engendre $E$ donc

  $$
      \exists g_{0}\in \mathcal{G}: g_{0} \notin \Vect(\mathcal{L}, \mathcal{G}_{0})
  $$

  Par conséquent, la famille $(\mathcal{L}, \mathcal{G}_{0}, g_{0})$ est libre dans $E$, or $(\mathcal{G}_{0}, g_{0})$ est une sous-famille de $\mathcal{G}$ donc $|(\mathcal{L}, \mathcal{G}_{0}, g_{0}) \in \mathcal{E}$, d’où

  $$
      |(\mathcal{L}, \mathcal{G}_{0}, g_{0})| \leq \max \mathcal{E}=|(\mathcal{L}, \mathcal{G}_{0})|
  $$

  soit

  $$
      |(\mathcal{G}, \mathcal{G}_{0})| + 1 \leq |(\mathcal{L}, \mathcal{G}_{0})|
  $$

  ce qui est une contradiction. Par conséquent, $(\mathcal{L}, \mathcal{G}_{0})$ engendre $E$.

Ainsi, $(\mathcal{L}, \mathcal{G}_{0})$ est une base de $E$.

On peut déduire de ce résultat l’existence d’une base pour espace vectoriel non réduit au vecteur nul et de dimension finie. En effet, un tel espace vectoriel admet une famille génératrice, et un vecteur quelconque forme à lui seul une famille libre. Une application du résultat précédent à ces objets donne alors l’existence d’une base.
