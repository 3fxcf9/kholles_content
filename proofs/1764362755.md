---
title: Toute suite convergente est bornée
authors:
  - Julien Dubousquet
date: 11/28/2025
pid: 1764362755
tags:
  - Limites
---

Soit $u \in \mathbb{K}^{\mathbb{N}}$ convergente.  
Posons $\ell = \lim u$.

Appliquons la définition de la convergence pour $\varepsilon \leftarrow 1$ :

$$
\exists N_{1}\in \mathbb{N} : \forall n \in \mathbb{N},\ n \geqslant N_{1} \implies |u_n - \ell| \leqslant 1
$$

Fixons un tel $N_{1}$.  
Posons alors  
$$
M = \max\{ |u_0|, |u_1|, |u_2|, \dots, |u_{N_1}|, |\ell| + 1 \},
$$  
qui est bien défini, car toute partie finie et non vide d’un ensemble totalement ordonné (ici $(\mathbb{R}, \leqslant)$) admet un plus grand élément.

Soit $n \in \mathbb{N}$ quelconque.

- Si $n \in \llbracket 0, N_{1} \rrbracket$, alors $|u_n| \in \{ |u_0|, |u_1|, \dots, |u_{N_1}|, |\ell|+1 \}$ donc $|u_n| \leqslant M$.
- Sinon :

$$
\begin{aligned}
n > N_1 &\implies |u_n - \ell| \leqslant 1 \\
        &\implies |u_n| - |\ell| \leqslant 1 \\
        &\implies |u_n| \leqslant 1 + |\ell| \leqslant M
\end{aligned}
$$

Ainsi, $\forall n \in \mathbb{N},\ |u_n| \leqslant M$.
