---
title: (facultative) Théorème de Bolzano-Weierstrass.
authors:
  - Julien Dubousquet
date: 07/12/2025
pid: 1765121573
tags:
  - Limites de suites
---

**Énoncé.**
Toute suite réelle bornée admet une sous-suite convergente.
L’ensemble des valeurs d’adhérence d’une suite réelle bornée est donc non vide.

---

Soit $u \in \R^\N$ une suite bornée.
Alors il existe $M \in \R_+$ tel que
$$
\forall n \in \N,\quad |u_n| \le M.
$$

Nous construisons une suite de segments emboîtés dans $[-M, M]$ par dichotomie.
Posons $a_0 = -M$, $b_0 = M$ et définissons, pour tout $n \in \N$ :

* $c_n = \frac{a_n + b_n}{2}$
* $I_n = [a_n, b_n]$

---

## Construction des segments

Soit $n \in \N$.
Supposons $a_n$ et $b_n$ construits et que l’ensemble
$$
{ k \in \N \mid u_k \in I_n }
$$
soit infini.

Posons :

* $I_n^- = { k \in \N \mid u_k \in [a_n, c_n] }$
* $I_n^+ = { k \in \N \mid u_k \in [c_n, b_n] }$

Comme
$$
I_n^- \cup I_n^+ = { k \in \N \mid u_k \in I_n },
$$
au moins un des deux est infini.

* Si $I_n^-$ est infini, on pose :
  $$
  a_{n+1} = a_n, \qquad b_{n+1} = c_n.
  $$
* Si $I_n^+$ est infini, on pose :
  $$
  a_{n+1} = c_n, \qquad b_{n+1} = b_n.
  $$

Dans les deux cas,
$$
{ k \in \N \mid u_k \in I_{n+1} }
$$
est infini.

---

## Propriétés des segments $I_n$

* On a toujours $a_n \le b_n$, donc $I_n \neq \varnothing$.
* Par construction, $I_{n+1} \subset I_n$.
* La longueur vérifie
  $$
  |I_{n+1}| = \frac12 |I_n|,
  $$
  donc $|I_n| \to 0$.

D’après le théorème des segments emboîtés, il existe un **unique** réel $\ell$ tel que
$$
\bigcap_{n \in \N} I_n = {\ell}.
$$

---

## Construction d’une extractrice

On construit par récurrence une application strictement croissante $\varphi : \N \to \N$.

On pose $\varphi(0) = 0$.

Puis, ayant construit $\varphi(n)$, on définit :
$$
\varphi(n+1)
= \min { k \in \N \mid u_k \in I_{n+1} \ \text{et}\ k > \varphi(n) }.
$$
Cet ensemble est non borné car infini, donc le minimum existe.

Ainsi $(u_{\varphi(n)})$ est une sous-suite de $u$, et on a :
$$
a_n \le u_{\varphi(n)} \le b_n.
$$

Comme $a_n \to \ell$ et $b_n \to \ell$, le théorème de l’encadrement donne :
$$
u_{\varphi(n)} \longrightarrow \ell.
$$

Ainsi $\ell$ est une valeur d’adhérence de $u$.
