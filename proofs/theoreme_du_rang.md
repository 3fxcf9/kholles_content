---
title: Théorème du rang
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060869
tags:
  - algèbre linéaire
---

Soit $E$ un $\K$-espace vectoriel de dimension finie et $F$ un $\K$-espace vectoriel quelconque. Soit $f$ une application linéaire de $E$ dans $F$. Alors

$$
    \dim_{\K}E = \rg f + \dim_{\K}\Ker f
$$

---

### Lemme préliminaire

Soit $f$ une application linéaire entre deux $\K$-espaces vectoriels $E$ et $F$ quelconques. Soit $E_{0}$ un supplémentaire de $\Ker f$ dans $E$. Alors, $f$ induit (i.e. se restreint en) un isomorphisme de $E_{0}$ sur $\Img f$.

<br>

#### _Démonstration :_

$E_{0}$ est un sous-espace vectoriel de $E$ donc $f_{|E_{0}} \in \L_{\K}(E_{0},F)$. De plus, $\Img f$ est un sous-espace vectoriel de $F$ et $\forall x \in E_{0}, f_{|E_{0}}(x)=f(x) \in \Img f$ donc $f^{|\Img f}_{|E_{0}} \in \L_{\K}(E_{0}, \Img f)$. On notera $g=f^{|\Img f}_{|E_{0}}$ dans la suite.

- _Injectivité de $g$ :_

  $$
  \begin{align*}
      \Ker g &= \{x \in E_{0} \mid g(x)=0_{F}\} \\
  &= \{x \in E \mid f(x) = 0_{F}\} \\
  &= E_{0} \cap \Ker f = \{0_{E}\}
  \end{align*}
  $$

- _Surjectivité de $g$ :_ Soit $y \in \Img f$ fixé quelconque. Il existe $x \in E$ tel que $y=f(x)$, or $E = E_{0}\oplus \Ker f$ donc

  $$
      \exists (x_{0}, x_{K}) \in E_{0} \times \Ker f : x=x_{0} + x_{K}
  $$

  Observons que $f(x) = f(x_{0}) + \underbrace{f(x_{K})}_{=0_{E}} = f(x_{0})$. Ainsi, $x_{0} \in E_{0}$ et $g(x_{0}) = f(x_{0}) = f(x) = y$.

---

$\Ker f$ est un sous-espace vectoriel de $E$, un $\K$-espace vectoriel de dimension finie, donc d’après le théorème d’existence d’un supplémentaire en dimension finie, il existe un sous-espace vecioriel $E_{0}$ de $E$ supplémentaire de $\Ker f$. Le lemme démontré précedemment s’applique et établit que $E_{0}$ et $\Img f$ sont isomorphes. $E_{0}$ étant de dimension finie comme sous-espace vectoriel de $E$,

$$
    \rg f = \dim_{\K} \Img f = \dim_{\K} E_{0} = \dim_{\K} E - \dim_{\K} \Ker f
$$

Ainsi,

$$
    \dim_{\K} E = \dim_{\K} \Ker f+\rg f
$$
