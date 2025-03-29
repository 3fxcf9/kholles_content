---
title: Décomposition $PJ_{r}Q$
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272908
tags:
  - algèbre linéaire
  - matrices
---

Soit $A \in \M_{n,p}(\K)$ de rang $r$. Alors il existe $(P,Q) \in \GL_{n}(\K) \times GL_{p}(\K)$ telles que

$$
    A = PJ_{r}(n,p)Q
$$

---

Notons $\hat a$ l’application linéaire de $\K^{p}$ dans $\K^{n}$ canoniquement associée à $A$ de sorte que

$$
    A = \mat(\hat a, \B_{c,\K^{p}}, \B_{c,\K^{n}})
$$

<blockquote>

Si le résultat est vrai, en l’interprétant comme un changement de base, il existe une base $\B_{1}=(f*{1}, \ldots, f*{p})$ de $\K^{p}$ et une base $\B_{2}=(g_{1}, \ldots, g_{n})$ de $\K^{n}$ telles que

$$
    \mat(\hat a, \B_{1}, \B_{2}) = J_{r}(n,p)
$$

donc

$$
    \forall i \in \iset{1,r}, \hat a(f_{i}) = g_{i}
$$

et

$$
    \forall i \in \iset{r+1,p}, \hat a(f_{i}) = 0_{\K^{n}}
$$

Nous allons donc chercher à construire deux bases $\B_{1}$ et $\B_{2}$ de $\K^{p}$ et $\K^{n}$ respectivement qui satisfont ces conditions.

</blockquote>

$A = \mat(\hat a, \B_{c,\K^{p}}, \B_{c,\K^{n}})$ donc $\rg \hat a = \rg A = r$ si bien que le théorème du rang appliqué à $\hat a$ donne

$$
    \dim_{\K} \K^{p} = \rg \hat a + \dim_{\K} \Ker \hat a
$$

soit

$$
    \dim_{\K} \Ker \hat a = p-r
$$

Choisissons $E_{1}$ un sous-espace de $\K^{p}$ supplémentaire de $\Ker \hat a$. On a donc

$$
    \K^{p} = E_{1} \oplus \Ker \hat a
$$

donc $\dim_{\K} E_{1} = \dim_{\K} \K^{p} - \dim_{\K} \Ker \hat a = p-(p-r) = r$.

Choisissons $(f_{1}, \ldots, f_{r})$ une base de $E_{1}$ et $(f_{r+1}, \ldots, f_{p})$ une base de $\Ker \hat a$. Ces deux espaces étant supplémentaires, la concaténation $(f_{1}, \ldots, f_{r}, f_{r+1}, \ldots, f_{p})$ de leur bases forme une base de $E$, notée $\B_{1}$.

L’image d’un endomorphisme étant engendrée par len images des vecteurs d’une base de l’espace de départ,

$$
    \begin{align*}
        \Img \hat a &= \Vect\Bigl\{\hat a(f_{1}), \ldots, \hat a(f_{r}), \underbrace{\hat a(f_{r+1})}_{=0_{\K^{n}}}, \ldots, \underbrace{\hat a(f_{p})}_{=0_{\K^{n}}}\Bigr\}
    \end{align*}
$$

donc $(\hat(f_{1}), \ldots, \hat a(f_{r}))$ est une famille génératrice de cardinal $r$ de $\Img \hat a$ qui est un espace de dimension $r$. C’est donc une base de $\Img \hat a$.

Le théorème de la base incomplète donne l’existence d’une famille $(g_{r+1}, \ldots, g_{n})$ de $\K^{n}$ qui complète $(\hat a(f_{1}), \ldots, \hat a(f_{r}))$ en une base de $\K^{n}$ que l’on note $\B_{2} = (\hat a(f_{1}), \ldots, \hat a(f_{r}), g_{r+1}, \ldots, g_{n})$.

Observons alors que

$$
    \mat(\hat a, \B_{1}, \B_{2}) = \left(\begin{array}{c|c}
        I_r & \mathbf{0}_{r,p-r} \\ \hline
        \mathbf{0}_{n-r,r} & \mathbf{0}_{n-r, p-r}
    \end{array}\right) = J_{r}(n,p)\\
$$

Notons $\widetilde P = \P(\B_{c,\K^{p}} \rightarrow \B_{1}) \in \GL_{p}(\K)$ et $\widetilde Q = \P(\B_{c,\K^{n}} \rightarrow \B_{2}) \in \GL_{n}(\K)$. La formule du changement de base s’écrit alors

$$
    \underbrace{\mat(\hat a,\B_{1},\B_{2})}_{=J_{r}(n,p)} = {\widetilde Q}^{-1} \times \underbrace{\mat(\hat a,\B_{c,\K^{p}}, \B_{c,\K^{n}})}_{=A} \times \widetilde P
$$

donc

$$
    \widetilde Q J_{r}(n,p){\widetilde P}^{-1} = A
$$

d’où le résultat en posant $P=\widetilde Q$ et $Q = {\widetilde P}^{-1}$.
