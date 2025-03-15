---
title: Formes linéaires non nulles de même noyau
authors:
  - Misutera
date: 15/03/2025
pid: 1742060872
tags:
  - algèbre linéaire
---

Deux formes linéaires du $\K$-espace vectoriel $E$ ont le même noyau si et seulement si elles sont liées.

---

Soient $(\varphi_{1}, \varphi_{2}) \in (E^{*} \setminus \{ 0_{E^{*}} \})^{2}$ fixées quelconques telles que $\{ \varphi_{1}, \varphi_{2} \}$ est liée.  
Alors :

$$
\forall (\alpha, \beta) \in \mathbb{K}^{2} \setminus \{ (0 ,0) \}, \alpha \times \varphi_{1} + \beta \times \varphi_{2} = 0_{E^{*}}
$$

De plus, sachant que $\varphi_{1} \ne 0_{E^{*}}$ et $\varphi_{2} \ne 0_{E \cdot}$, $\alpha \ne 0_{\mathbb{K}}$ et $\beta \ne 0_{\mathbb{K}}$, si bien que $\displaystyle \varphi_{1} = \frac{\beta}{\alpha} \times \varphi_{2}$ et $\displaystyle \varphi_{2} = \frac{\alpha}{\beta} \times \varphi_{1}$.  
Montrons que $\ker \varphi_{1} = \ker \varphi_{2}$.

- Soit $x \in \ker \varphi_{1}$ fixé quelconque.  
  Alors, $\displaystyle \varphi_{2}(x) = \frac{\alpha}{\beta} \times \underbrace{ \varphi_{1}(x) }_{\displaystyle = 0_{\mathbb{K}} } = 0_{\mathbb{K}}$, donc $x \in \ker \varphi_{2}$, d’où $\ker \varphi_{1} \subset \ker \varphi_{2}$.
- Soit $x \in \ker \varphi_{2}$ fixé quelconque.  
  Alors, $\displaystyle \varphi_{1}(x) = \frac{\beta}{\alpha} \times \underbrace{ \varphi_{2}(x) }_{\displaystyle = 0_{\mathbb{K}} } = 0_{\mathbb{K}}$, donc $x \in \ker \varphi_{1}$, d’où $\ker \varphi_{2} \subset \ker \varphi_{1}$.

Ainsi, $\varphi_{1}$ et $\varphi_{2}$ ont le même noyau.

Soient $(\varphi_{1}, \varphi_{2}) \in (E^{*} \setminus \{ 0_{E \cdot} \})^{2}$ fixées quelconques telles que $\ker \varphi_{1} = \ker \varphi_{2}$.  
$\varphi_{1} \ne 0_{E \cdot}$, donc :

$$
\exists a \in E \setminus \ker \varphi_{1}
$$

On a donc $a \ne 0_{E}$ car $0_{E} \in \ker \varphi_{1}$.  
Montrons que $\ker \varphi_{1} \oplus \mathrm{vect}\{ a \} = E$.

- $\dim \ker \varphi_{1} + \dim \ker \mathrm{vect}\{ a \} = n - 1 + 1 = n$.
- Soit $x \in \ker \varphi_{1} \cap \mathrm{vect}\{ a \}$ fixé quelconque.  
  Alors : $$\exists \lambda \in \mathbb{K}, x = \lambda \times a$$
  Et $\varphi(x) = 0_{\mathbb{K}}$, donc $\lambda \times \varphi_{1}(a) = 0_{\mathbb{K}}$.  
  Or $\varphi_{1}(a) \ne 0_{\mathbb{K}}$ car $a \not\in \ker \varphi_{1}$ et un corps est intègre donc $\lambda = 0_{\mathbb{K}}$ si bien que $x = 0_{E}$.  
  Par conséquent, $\ker \varphi_{1} \cap \mathrm{vect}\{ a \} \subset \{ 0_{E} \}$ d’où l’égalité car $0_{E}$ appartient à tout sous-espace vectoriel.

Par conséquent, $\ker \varphi_{1}$ et $\mathrm{vect}\{ a \}$ sont supplémentaires dans $E$.  
Explicitons $\varphi_{1}$ :

$$
\varphi_{1} : \begin{array}{}
E & = & \ker \varphi_{1} \oplus \mathrm{vect}\{ a \} & \to & \mathbb{K} \\
x & = & x_{\mathbb{K}} + \lambda_{x} \times a & \mapsto & \lambda_{x} \times_{\mathbb{K}} \varphi_{1}(a)
\end{array}
$$

Sachant que $\ker \varphi_{1} = \ker \varphi_{2}$, explicitons également $\varphi_{2}$ :

$$
\varphi_{2} : \begin{array}{}
E & = & \ker \varphi_{2} \oplus \mathrm{vect}\{ a \} & \to & \mathbb{K} \\
x & = & x_{\mathbb{K}} + \lambda_{x} \times a & \mapsto & \lambda_{x} \times_{\mathbb{K}} \varphi_{2}(a)
\end{array}
$$

Il apparaît alors, puisque $\varphi_{1}(a) \ne 0_{\mathbb{K}}$ (donc $\varphi_{1}(a)$ est symétrisable pour la loi de composition interne $\times_{\mathbb{K}}$), que $\displaystyle \varphi_{2} = \frac{\varphi_{2}(a)}{\varphi_{1}(a)} \times \varphi_{1}$.  
Ainsi, deux formes linéaires **non nulles** ont le même noyau si et seulement si elles sont liées.
