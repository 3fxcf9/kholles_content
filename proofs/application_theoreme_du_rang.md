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
    \rg f = \rg g\circ f + \dim_{\K} (\Imf f \cap  \Ker g)
$$

---

Appliquons le théorème du rang à $g_{|\Imf f}$ (ce qui est autorisé car $g_{| \Imf f} \in \L_{\K}(\Imf f,G)$ et $E$ est de dimension finie donc $f(E)=\Imf f$ l’est également) :

$$
   \underbrace{\dim_{\K} \Imf f}_{=\rg f} = \underbrace{\rg g_{|\Imf f}}_{\substack{=\dim_{\K} \Imf g_{|\Imf f}\\=\dim_{\K} \Imf  (g\circ f)\\ = \rg g\circ f\;\qquad}} + \dim_{\K} \Ker g_{|\Imf f}
$$

Or

$$
\begin{align*}
    \Ker g_{|\Imf f} = \{x \in \Imf f \mid g_{|\Imf f}(x) = 0_{G}\} \\
    &=\{x \in  \Imf f \mid g(x) = 0_{G}\} \\
&= \Imf f \cap  \Ker g
\end{align*}
$$

donc

$$
    \rg f = \rg g\circ f + \dim_{\K} (\Imf f \cap  \Ker g)
$$
