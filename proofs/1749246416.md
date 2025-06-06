---
title: L’adhérence d’une partie est l’ensemble de ses points adhérents
note: Élèves souhaitant passer en classe étoilée
authors:
  - Félix Rondeau
date: 06/06/2025
pid: 1749246416
tags:
  - topologie
---

L’adhérence d’une partie $A \in \R^{2}$ (le plus petit fermé contenant cette partie) est l’ensemble de ses points adhérents (points pouvant être le centre d’une boule fermée de tout rayon non nul rencontrant $A$).

---

Notons $\tilde{A}$ l’ensemble des points adhérents à $A$.

- **Inclusion directe.** Soit $\omega \in \tilde{A}$. Supposons que $\omega \notin \overline A$. Alors $\omega \in \R^{2} \setminus \overline A$ qui est un ouvert de $\R^{2}$ donc

  $$
      \exists r \in \R_{+}^{*}: B(\omega,r) \subset \R^{2} \setminus \overline A
  $$

  Ainsi, puisque $A \setminus \overline A$, alors $\R^{2} \setminus \overline A \subset \R^{2} \setminus A$ donc $B(\omega, r) \subset \R^{2} \setminus A$ si bien que

  $$
      B(\omega,r) \cap A = \emptyset
  $$

  donc $\omega \notin \tilde{A}$, ce qui contredit l’hypothèse faite sur $\omega$, et par conséquent, $\omega \in \overline A$. Ainsi, $\tilde{A} \subset \overline A$.

- **Inclusion réciproque.**

  > _Sachant que $\overline A$ est, par définition, le plus petit fermé contenant $A$, nous allons montrer que $\tilde{A}$ est une partie fermée contenant $A$._

  - Trivialement, $A \subset \tilde{A}$
  - _Montrons que $\tilde{A}$ est une partie fermée en prouvant que $\R^{2} \setminus \tilde{A}$ est une partie ouverte._
    Soit $b \in \R^{2} \setminus \tilde{A}$. Comme $b$ n’est pas un point adhérent à $A$,

    $$
        \exists r_{b} \in \R_{+}^{*}: B(b,r_{b}) \cap A = \emptyset
    $$

    > _Montrons que $B \left(b, \frac{1}{2}r_{b}\right) \subset \R^{2} \setminus \tilde{A}$._

    Soit $c \in B \left(b, \frac{1}{2}r_{b}\right)$ quelconque. Alors, $B \left(c, \frac{1}{2}r_{b}\right) \subset B(b,r_{b})$ or $B(b,r_{b})\cap A = \emptyset$ donc $B \left(c, \frac{1}{2}r_{b}\right) \cap A = \emptyset$ donc $c \in \R^{2} \setminus \tilde{A}$. Ainsi, $B \left(b, \frac{1}{2}r_{b}\right) \subset \R^{2} \setminus \tilde{A}$ donc $\R^{2} \setminus \tilde{A}$ est un ouvert si bien que $\tilde{A}$ est un fermé de $\R^{2}$.

