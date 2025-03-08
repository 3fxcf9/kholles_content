---
title: Image de sous-espaces vectoriels en somme directe
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353632
tags:
  - algèbre linéaire
---

Si $f\in\L_{\K}(E, F))$ est injective et $(E_{i})_{i\in\iset{1,p}}$ des sous-espaces vectoriels de $E$ en somme directe,

$$
    f(E_{1} \oplus \cdots \oplus E_{p}) = f(E_{1}) \oplus \cdots \oplus f(E_{p})
$$

---

- _L’image de la somme est la somme des images._

  $$
      \begin{align*}
          f(E_{1} \oplus \cdots \oplus E_{p}) &= f(E_{1} + \cdots + E_{p}) && \\
                                    &= f \left(\Vect \bigcup_{i=1}^{p}E_{i}\right) && \text{(définition somme de sev)}\\
                                    &= \Vect f \left(\bigcup_{i=1}^{p}E_{i}\right) && \text{(lemme du cours)}\\
                                    &= \Vect \left(\bigcup_{i=1}^{p}f(E_{i})\right) && \text{(image d’une union)}\\
                                    &= f(E_{1}) + \cdots + f(E_{p}) && \text{(définition somme de sev)} && \\
                                    &= f(E_{1}) \oplus \cdots \oplus f(E_{p})
      \end{align*}
  $$

- _La somme de droite est directe._ Soient $(y_{1},\dots, y_{p})\in f(E_{1}) \times \cdots \times f(E_{p})$ fixés quelconques tels que

  $$
    y_{1} + \cdots + y_{p} = 0_{F} \quad\text{(*)}
  $$

  Pour tout $i\in\iset{1, p}$, il existe $x_{i}\in E_{i}$ tel que $y_{i}=f(x_{i})$ donc la relation $(*)$ donne

  $$
      f(x_{1}) + \cdots + f(x_{p}) = 0_{F}
  $$

  d’où

  $$
      \begin{align*}
          f(x_{1}+\cdots +x_{p}) = 0_{F} &\quad\text{donc}\quad  x_{1} + \cdots + x_{p} \in \Ker f = \{0_{E}\} \\
                                         &\quad\text{donc}\quad  \underbrace{x_{1}}_{\in E_{1}} + \cdots + \underbrace{x_{p}}_{\in E_{p}} = 0_{E} \\
                                         &\quad\text{donc}\quad  \forall i\in\iset{1, p}, x_{i}=0_{E}    \\
                                         &\quad\text{donc}\quad  \forall i\in\iset{1, p}, y_{i}=f(x_{i})=f(0_{E}) = 0_{F}
      \end{align*}
  $$

  ainsi, $E_{1}, \dots, E_{p}$ sont en somme directe.
