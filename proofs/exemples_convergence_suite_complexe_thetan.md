---
title: Illustrer par des exemples que la convergence de la suite complexe $(u_{n})=(e^{i \theta_{n}})$ n'implique pas la convergence de $(\theta{n})$ même si on impose à $(\theta{n})$ d'être dans l'intervalle $[0,2 \pi[$ pour la rendre unique et bornée.
authors:
  - Julien Dubousquet
date: 07/12/2025
pid: 1765122210
tags:
  - Suites complexes
---

### **Premier exemple**

Considérons la suite définie par :

$$
\theta_n = \frac{\pi}{2} + 2\pi n.
$$

Alors :

$$
u_n = e^{i\theta_n} = i \quad \text{pour tout } n.
$$

La suite $(u_n)$ est donc constante, donc convergente.
Mais :

$$
\theta_n \longrightarrow +\infty,
$$

donc $(\theta_n)$ diverge.

---

### **Second exemple**

Définissons maintenant :

$$
\theta_n =
\begin{cases}
0 & \text{si } n \equiv 0 \pmod{2},[4pt]
2\pi - \frac{1}{n} & \text{si } n \equiv 1 \pmod{2}.
\end{cases}
$$

Ainsi, $(\theta_n)$ est bien à valeurs dans $[0,2\pi[$.

Alors :

$$
u_n = e^{i\theta_n} \longrightarrow 1.
$$

En revanche, $(\theta_n)$ **ne converge pas**, car :

* les termes pairs valent $0$ ;
* les termes impairs tendent vers $2\pi$.

Ainsi, $(\theta_n)$ possède **deux valeurs d’adhérence** : $0$ et $2\pi$, et ne converge donc pas.
