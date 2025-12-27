---
title: Norme infinie d’une fonction continue par morceaux
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746296659
tags:
  - intégration
---

Si $f$ est une fonction continue par morceaux sur l’intervalle $\cc{a,b}$, l’ensemble $\left\{\abs{f(t)} \where t \in \cc{a,b}\right\}$ admet une borne supérieurs notée $\infabs{f}{\cc{a,b}}$.

---

Soit $\sigma = (x_{i})_{i \in \iset{0,N-1}} \in S(\cc{a,b})$ une subdivision adaptée à $f$. Soit $i \in\iset{0,N-1}$. Notons $f_{i} = f_{|\oo{x_{i}, x_{i+1}}}$.

$f$ est continue par morceaux sur $\cc{a,b}$ donc elle admet des limites finies à droite en $x_{i}$ (notés $\ell^{+}_{i}$) et à gauche en $x_{i+1}$ (notée $\ell_{i+1}^{+}$), ce qui permet de prolonger $f_{i}$ par continuité en $x_{i}$ et $x_{i+1}$ en

$$
    \tilde{f_{i}} : \applic{\cc{x_{i}, x_{i+1}}}{\R}{x}{\begin{cases}\ell_{i}^{+} \quad\text{si } x = x_{i}\\f(x) \quad\text{si } x \in  \oo{x_{i}, x_{i+1}} \\ \ell_{i+1}^{-} \quad\text{si } x = x_{i+1}\\\end{cases}}
$$

De plus, $f_{i} \in \Cont^{0}(\oo{x_{i}, x_{i+1}},\R)$ donc $\tilde{f_{i}} \in \Cont^{0}(\cc{x_{i}, x_{i+1}}, \R)$. Le théorème de Weierstrass permet alors d’affirmer que

$$
    M_{i} = \sup \left\{\abs{\tilde{f_{i}}(x)} \where x \in \cc{x_{i}, x_i+1}\right\}
$$

est un plus grand élément.

Considérons à présent l’ensemble $\left\{\abs{f(t)} \where t \in \cc{a,b}\right\}$; c’est une partie non vide de $\R$ (contient $\abs{f(a)}$) majorée par

$$
    M = \max \left(\left\{M_{i} \where i \in \iset{0,N-1}\right\} \cup \left\{\abs{f(x_{i})} \where i \in \iset{0,N}\right\}\right)
$$

Soit $t \in  \cc{a,b}$.

- si $\exists i_{0} \in \iset{0,N}: t=x_{i_{0}}$, alors $\abs{f(t)} = \abs{f(x_{i_{0}})} \leq M$
- sinon, $\exists i_{0} \in \iset{0,N-1}: t \in  \oo{x_{i_{0}}, x_{i_{0}+1}}$ donc $\abs{f(t)} \leq \infabs{\tilde{f_{i_{0}}}}{\cc{x_{i_{0}}, x_{i_{0}+1}}} = M_{i_{0}} \leq  M$.

Ainsi, $\left\{\abs{f(t)} \where t \in  \cc{a,b}\right\}$ est majorée donc admet une borne inférieure.

---

Cette borne inférieure n’est pas forcément atteinte, en effet la fonction définie sur $\cc{0,1}$ par

$$
    f(x) = \begin{cases}x \quad\text{si } x \in  \co{0,1} \\ 0 \quad\text{si } x=1\end{cases}
$$

n’atteint pas sa norme infinie 1.
