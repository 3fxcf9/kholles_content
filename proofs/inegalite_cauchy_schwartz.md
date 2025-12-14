---
title: Inégalité de Cauchy-Schwartz
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746307240
tags:
  - intégration
---

Soient $(f,g)\in \CM(\cc{a,b},\R)^{2}$. Alors

$$
    \abs{\int_{a}^{b}f(u)g(u)\dd u} \leq \sqrt{\int_{a}^{b}f^{2}(u)\dd u}\sqrt{\int_{a}^{b}g^{2}(u)\dd u}
$$

avec égalité pour deux fonctions continues sur $\cc{a,b}$ si et seulement si $(f,g)$ est liée dans $\Cont^{0}(\cc{a,b},\R)$.

---

- **Preuve de l’inégalité.**
  Considérons la fonction $P$ définie pour tout $t \in \R$ par

  $$
      P(t) = \int_{a}^{b}(f+tg)^{2}(x)\dd x = \int_{a}^{b}f^{2}(x)\dd x + 2t \int_{a}^{b}f(x)g(x)\dd x + t^{2}\int_{a}^{b}g^{2}(x)\dd x
  $$

  C’est une fonction polynomiale de degré $\leq 2$ positive ou nulle sur $\R$ (par positivité de l’intégrale).

  - si $P$ est un trinôme du second degré, $P$ étant de signe constant sur $\R$, son discriminant est $\leq 0$ soit

    $$
        \left(2\int_{a}^{b}f(x)g(x)\dd x\right)^{2} - 4 \int_{a}^{b}f^{2}(x)\dd x \int_{a}^{b}g^{2}(x)\dd x \leq 0
    $$

    donc

    $$
        \underbrace{\sqrt{\left(\int_{a}^{b}f(x)g(x)\dd x\right)^{2}}}_{=\abs{\int_{a}^{b}f(x)g(x)\dd x}} \leq \sqrt{\int_{a}^{b}f^{2}(x)\dd x}\sqrt{\int_{a}^{b}g^{2}(x)\dd x}
    $$

  - sinon, $\int_{a}^{b}g^{2}(x)\dd x = 0$ donc $P$ est une fonction affine de signe constant sur $\R$, donc elle est constante (sinon elle a des limites en $\pm \infty$ de signes opposés), donc sa pente est nulle d’où

    $$
        \int_{a}^{b}f(x)g(x)\dd x = 0
    $$

    ce qui montre l’inégalité.

- **Caractérisation du cas d’égalité pour deux fonctions $f$ et $g$ continues.**

  - Supposons que $f$ et $g$ réalisant un cas d’égalité de l’inégalité de Cauchy-Schwarz. Reprenons

    $$
        P(t) = \int_{a}^{b}f^{2}(x)\dd x + 2t \int_{a}^{b}f(x)g(x)\dd x + t^{2}\int_{a}^{b}g^{2}(x)\dd x
    $$

    - si $P$ est un trinôme du second degré, son déterminant

      $$
          4 \left(\int_{a}^{b}f(x)g(x)\dd x\right) - 4 \int_{a}^{b}f^{2}(x)\dd x \int_{a}^{b}g^{2}(x)\dd x
      $$

      est nul, donc $P$ admet une racine réelle notée $t_{0}$, donc

      $$
          \int_{a}^{b}(f+t_{0}g)^{2}(x)\dd x = 0
      $$

      donc $(f+t_{0}g)^{2}$ est identiquement nulle sur $\cc{a,b}$ donc la famille $(f,g)$ est liée et une relation de liaison est $f+t_{0}g = 0$.

    - sinon, $P$ est affine et $\int_{a}^{b}g^{2}(x)\dd x = 0$, donc $g^{2} = \tilde{0}$ sur $\cc{a,b}$, donc $g=\tilde{0}$ donc la famille $(f,g)$ est liée.

  - Supposons la famille $(f,g)$ liée.

    - si $f=\tilde{0}$, il y a égalité
    - sinon, $f\neq \tilde{0}$ donc il existe $\lambda \in \R$ tel que $g = \lambda f$, et ainsi

      $$
          \abs{\int_{a}^{b}f(x)g(x)\dd x} = \abs{\int_{a}^{b}\lambda f^{2}(x)\dd x} = \abs{\lambda}\abs{\int_{a}^{b}f^{2}(x)\dd x}
      $$

      et

      $$
          \sqrt{\int_{a}^{b}g^{2}(x)\dd x}\sqrt{\int_{a}^{b}f^{2}(x)\dd x} = \sqrt{\lambda^{2}\int_{a}^{b}f^{2}(x)\dd x}\sqrt{\int_{a}^{b}f^{2}(x)\dd x} = \abs{\lambda}\int_{a}^{b}f^{2}(x)\dd x
      $$

      il y a donc égalité.

