---
title: Endomorphismes induits sur deux sous-espaces vectoriels
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353633
tags:
  - algèbre linéaire
---

Soient $E_{1}$ et $E_{2}$ deux sous-espaces vectoriels supplémentaires du $\K$-espace vectoriel $E$. Soient $u_{1}$ et $u_{2}$ deux endomorphismes respectifs de $E_{1}$ et $E_{2}$. Il existe un unique endomorphisme $u$ de $E$ qui stabilise $E_{1}$ et $E_{2}$ et qui induit respectivement sur ces sous-espaces les endomorphismes $u_{1}$ et $u_{2}$, i.e. tel que

- $u(E_{1})\subset E_{1}$ et $u(E_{2})\subset E_{2}$
- $u_{|E_{1}}^{|E_{1}}=u_{1}$ et $u_{|E_{2}}^{|E_{2}}=u_{2}$

---

- _Analyse :_ Supposons qu’il existe $u\in\L_{\K}(E)$ tel que

  $$
      u(E_{1})\subset E_{1}, u(E_{2})\subset E_{2}, u_{|E_{1}}^{|E_{1}}=u_{1} \quad\text{et}\quad u_{|E_{2}}^{|E_{2}} =u_{2}
  $$

  Soit $x\in E$ fixé quelconque. $E=E_{1}\oplus E_{2}$ donc $\exists (x_{1}, x_{2})\in E_{1} \times E_{2}:\; x=x_{1}+x_{2}$ si bien que

  $$
  \begin{align*}
      u(x)=u(x_{1}+x_{2}) &\underbrace{=}_{u\in\L_{\K}(E)} u(x_{1})+u(x_{2}) \\
                          &\underbrace{=}_{\substack{u_{|E_{1}}^{|E_{1}}=u_{1} \\ u_{|E_{2}}^{|E_{2}}=u_{2}}} u_{2}(x_{1})+u_{2}(x_{2})
  \end{align*}
  $$

  donc $u(x)$ est parfaitement déterminé ce qui prouve l’unicité de $u$ sous réserve d’existence.

- _Synthèse :_ Posons l’application

  $$
  u : \begin{array}{rcccl}
      E &=& E_{1} \oplus E_{2} & \longrightarrow & E \\
      x &=& x_{1} + x_{2} & \longmapsto & u_{1}(x_{1}) + u_{2}(x_{2})
  \end{array}
  $$

  - $u$ est bien définie car tout élément de $E$ se décompose de manière unique comme somme d’un vecteur de $E_{1}$ et d’un vecteur de $E_{2}$.
  - $u\in\L_{\K}(E)$
  - $u(E_{1})\subset E_{1}$ et $u_{|E_{1}}^{|E_{1}}=u_{1}$
  - $u(E_{2})\subset E_{2}$ et $u_{|E_{2}}^{|E_{2}}=u_{2}$
