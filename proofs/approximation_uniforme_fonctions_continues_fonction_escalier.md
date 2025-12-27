---
title: Approximation uniforme des fonctions continues par une fonction en escalier
authors:
  - Félix Rondeau
date: 03/05/2025
pid: 1746302222
tags:
  - intégration
---

Soit $f$ une fonction continue sur l’intervalle $\cc{a,b}$.

1. Pour tout $\varepsilon \in \R_{+}^{*}$, il existe $\chi \in \E(\cc{a,b},\R)$ telle que $\infabs{f-\chi}{\cc{a,b}} \leq \varepsilon$
2. Pour tout $\varepsilon \in \R_{+}^{*}$, il existe $(\varphi, \psi) \in \E(\cc{a,b},\R)^{2}$ telles que $\varphi \leq  f \leq  \psi$ et $\infabs{\psi-\varphi}{\cc{a,b}} \leq \varepsilon$

---

1. Soit $\varepsilon \in \R^{*}_{+}$ quelconque. $f$ est continue sur le segment $\cc{a,b}$ donc (théorème de Heine) elle est uniformément continue. Appliquons la définition de la continuité uniforme pour le « $\varepsilon$ » fixé ci-dessus :

   $$
       \exists \eta \in \R_{+}^{*}: \forall (x,y) \in \cc{a,b}^{2}, \abs{x-y} \leq \eta \implies \abs{f(x) - f(y)}\leq \varepsilon
   $$

   Fixons un tel $\eta$ et choisissons $N \in \N^{*}$ tel que $\frac{b-a}{N} \leq \eta \iff N \geq \frac{b-a}{\eta}$ par exemple $N = \lfloor \frac{b-a}{\eta}\rfloor+1$. Considérons $\sigma_{N} = \left(a+i \frac{b-a}{N} = x_{i}\right)_{i \in \iset{0,N}}$ la subdivision uniforme de $\cc{a,b}$ par $\frac{b-a}{N}$. Posons l’application

   $$
       \varphi: \applic{\cc{a,b}}{\R}{x}{\begin{cases}
           f(x_{i}) \quad\text{si } s \in \co{x_{i}, x_{i+1}}\\
   f(b) \quad\text{si } x=b
       \end{cases}}
   $$

   qui est constante sur $\oo{x_{i}, x_{i+1}}$ pour tout $i \in \iset{0,N}$, et qui est donc une fonction en escalier sur $\cc{a,b}$.

   Soit $x \in \cc{a,b}$ quelconque.

   - si il existe $i_{0} \in \iset{0,N}$ tel que $x = x_{i_{0}}$, alors

     $$
         \abs{f(x) - \varphi(x)} = \abs{f(x_{i_{0}}) - f(x_{i_{0}})} = 0 \leq \varepsilon
     $$

   - sinon, il existe $i_{0} \in \iset{0,N-1}$ tel que $x \in \oo{x_{i_{0}}, x_{i_{0}+1}}$ donc

     $$
         \abs{f(x) - \varphi(x)} = \abs{f(x) - f(x_{i_{0}})} \leq \varepsilon
     $$

     car $\abs{x-x_{i_{0}}} \leq  \abs{x_{i_{0}+1} - x_{i_{0}}} \leq  \frac{b-a}{N} \leq \eta$

2. Soit $\varepsilon \in \R_{+}^{*}$. Appliquons le point précédent pour $\varepsilon \leftarrow \frac{\varepsilon}{2}$ :

   $$
       \exists \gamma \in \E(\cc{a,b},\R): \infabs{\gamma-f}{\cc{a,b}} \leq \frac{\varepsilon}{2}
   $$

   Posons $\varphi = \gamma + \tilde{\frac{\varepsilon}{2}} \in \E(\cc{a,b}, \R)$ et $\psi = \gamma - \tilde{\frac{\varepsilon}{2}} \in \E(\cc{a,b}, \R)$.
   Alors,

   $$
       \forall x \in \cc{a,b}, \abs{f(x) - \gamma(x)} \leq \infabs{\gamma-f}{\cc{a,b}} \leq \frac{\varepsilon}{2}
   $$

   donc

   $$
       \forall x \in \cc{a,b}, -\frac{\varepsilon}{2} \leq f(x) - \gamma(x) \leq \frac{\varepsilon}{2}
   $$

   donc

   $$
       \forall x \in \cc{a,b}, \underbrace{\gamma(x) - \frac{\varepsilon}{2}}_{=\psi(x)} \leq f(x) \leq \underbrace{\gamma(x) + \frac{\varepsilon}{2}}_{=\varphi(x)}
   $$

   donc $\psi \leq f \leq \phi$. De plus,

   $$
       \forall x \in \cc{a,b}, \abs{\phi(x) - \psi(x)} = \abs{\gamma(x) + \frac{\varepsilon}{2} - \left(\gamma(x) - \frac{\varepsilon}{2}\right)} = \varepsilon
   $$

   donc on a bien $\infabs{\phi - \psi}{\cc{a,b}} \leq \varepsilon$.
