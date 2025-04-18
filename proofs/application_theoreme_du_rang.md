---
title: Application du théorème du rang
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060870
tags:
  - algèbre linéaire
---

Soient $E, F$ et $G$ trois $\K$-espaces vectoriels, et $(f,g) \in \L_{\K}(E,F)\times \L_{\K}(F,G)$. On suppose que $E$ est de dimension finie. Alors

$$
    \rg f = \rg g\circ f + \dim_{\K} (\Img f \cap  \Ker g)
$$

---

Appliquons le théorème du rang à $g_{|\Img f}$ (ce qui est autorisé car $g_{| \Img f} \in \L_{\K}(\Img f,G)$ et $E$ est de dimension finie donc $f(E)=\Img f$ l’est également) :

$$
   \underbrace{\dim_{\K} \Img f}_{=\rg f} = \underbrace{\rg g_{|\Img f}}_{\substack{=\dim_{\K} \Img g_{|\Img f}\\=\dim_{\K} \Img  (g\circ f)\\ = \rg g\circ f\;\qquad}} + \dim_{\K} \Ker g_{|\Img f}
$$

Or

$$
\begin{align*}
    \Ker g_{|\Img f} = \{x \in \Img f \mid g_{|\Img f}(x) = 0_{G}\} \\
    &=\{x \in  \Img f \mid g(x) = 0_{G}\} \\
&= \Img f \cap  \Ker g
\end{align*}
$$

donc

$$
    \rg f = \rg g\circ f + \dim_{\K} (\Img f \cap  \Ker g)
$$
