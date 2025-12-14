---
title: Gradient en coordonnées polaires
authors:
  - Félix Rondeau
date: 07/06/2025
pid: 1749307294
tags:
  - fonctions de deux variables
---

Si $\hat f(r,\theta) = f(x,y)$, alors

$$
    \overrightarrow{\nabla(r,\theta)\hat f} = \frac{\partial \hat f}{\partial r}(r,\theta)\vec{u_{r}}(\theta) + \frac{1}{r}\frac{\partial \hat f}{\partial \theta}(r,\theta)\vec{u_{\theta}}(\theta)
$$

---

En utilisant le théorème de dérivation composée,

$$
    \begin{align*}
        \frac{\partial \hat f}{\partial \theta}(r,\theta) &= \frac{\partial }{\partial \theta}(f\circ \left[(r,\theta)\longmapsto (r \cos \theta, r \sin \theta)\right]) \\
        &= \frac{\partial f}{\partial x}(r \cos \theta, r\sin \theta) \times \frac{\partial}{\partial \theta}\left[(r,\theta)\longmapsto r \cos \theta\right] + \frac{\partial f}{\partial y}(r \cos \theta, r \sin \theta) \times \frac{\partial}{\partial \theta}\left[(r,\theta)\longmapsto r \sin \theta\right] \\
&= -r \sin \theta \frac{\partial f}{\partial x} (r \cos \theta, r \sin \theta) + r\cos \theta \frac{\partial f}{\partial y}(r \cos \theta, r \sin \theta) \qquad (1)
    \end{align*}
$$

De même,

$$
    \begin{align*}
        \frac{\partial \hat f}{\partial r}(r,\theta) &= \frac{\partial}{\partial r}(f\circ \left[(r,\theta)\longmapsto (r \cos \theta, r\sin \theta)\right]) \\
&= \frac{\partial f}{\partial x} (r \cos \theta, r\sin \theta) \times \frac{\partial}{\partial r}\left[(r,\theta)\longmapsto r \cos \theta\right] + \frac{\partial f}{\partial y}(r \cos \theta, r\sin \theta) \times  \frac{\partial}{\partial r}\left[(r,\theta)\longmapsto r\sin \theta\right]\\
&= \cos \theta \frac{\partial f}{\partial x}(r \cos \theta, r\sin \theta) + \sin \theta \frac{\partial f}{\partial y}(r \cos \theta,r\sin \theta) \qquad (2)
    \end{align*}
$$

Ainsi, en ajoutant $(1) \times - \frac{\sin \theta}{r}$ et $(2) \times  \cos \theta$, on obtient

$$
    \frac{\partial f}{\partial x}(r \cos \theta, r\sin \theta) = \cos \theta \frac{\partial \hat f}{\partial r}(r, \theta) - \frac{\sin \theta}{r}\frac{\partial \hat f}{\partial \theta}(r, \theta)
$$

et en ajoutant $(1) \times \frac{\cos \theta}{r}$ et $(2) \times \sin \theta$, on obtient

$$
    \frac{\partial f}{\partial y}(r \cos \theta, r\sin \theta) = \sin \theta \frac{\partial \hat f}{\partial r}(r, \theta) + \frac{\cos \theta}{r}\frac{\partial \hat f}{\partial \theta}(r, \theta)
$$

Ainsi,

$$
    \begin{align*}
        \overrightarrow{\nabla(r,\theta)\hat f} &= \left(\cos \theta \frac{\partial \hat f}{\partial r}(r,\theta) - \frac{\sin \theta}{r}\frac{\partial \hat f}{\partial \theta}(r,\theta)\right)\cdot \vec{\imath} + \left(\sin \theta \frac{\partial \hat f}{\partial r}(r, \theta) + \frac{\cos \theta}{r}\frac{\partial \hat f}{\partial \theta}(r, \theta)\right)\cdot \vec{\jmath} \\
&= \frac{\partial \hat f}{\partial r}(r, \theta)(\cos \theta \cdot \vec{\imath} + \sin \theta \cdot \vec{\jmath}) + \frac{1}{r}\frac{\partial \hat f}{\partial \theta}(r, \theta)(-\sin \theta \cdot \vec{\imath} + \cos \theta \cdot \vec{\jmath}) \\
&= \frac{\partial \hat f}{\partial r}(r, \theta)\cdot \vec{u_{r}}(\theta) + \frac{1}{r}\frac{\partial \hat f}{\partial \theta}(r, \theta)\vec{u_{\theta}}(\theta)
    \end{align*}
$$
