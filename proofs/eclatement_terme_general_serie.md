---
title: Technique d’éclatement du terme général d’une série
authors:
  - Félix Rondeau
date: 05/18/2025
pid: 1747564039
tags:
  - séries
---

Déterminer la nature de la série

$$
    \sum_{n \geq 2}\frac{(-1)^{n}}{\sqrt{(-1)^{n} + n^{\alpha}}}
$$

---

$$
    \frac{(-1)^{n}}{\sqrt{(-1)^{n} + n^{\alpha}}} \usim{+\infty} \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}}
$$

- Si $\alpha > 2$,

  - $u_{n} \underset{+\infty}{=} \mathcal{O}\left(\frac{1}{n^{\frac{\alpha}{2}}}\right)$
  - $\sum_{n \geq 1} \frac{1}{n^{\frac{\alpha}{2}}}$ est absolument convergente

  donc $\sum_{n \geq 1} u_{n}$ est absolument convergente.

- Sinon,

  $$
      \begin{align*}
          u_{n} &= \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}}\left(1+\frac{(-1)^{n}}{n^{\alpha}}\right)^{-\frac{1}{2}}\\
          &\underset{+\infty}{=} \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}}\left(1 - \frac{(-1)^{n}}{2n^{\alpha}} + \mathcal{O}\left(\frac{1}{n^{2 \alpha}}\right)\right) \\
          &\underset{+\infty}{=} \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}} - \underbrace{\frac{1}{2n^{\frac{3 \alpha}{2}}} + \mathcal{O}\left(\frac{1}{n^{\frac{5 \alpha}{2}}}\right)}_{\overset{\text{def}}{=}v_{n} \usim{+\infty} \frac{1}{2 n^{\frac{3 \alpha}{2}}} \text{ donc } \scriptsize\begin{cases}
              \text{converge } \iff \alpha >\frac{2}{3} \\
              \text{diverge } \iff \alpha \leq \frac{2}{3}
          \end{cases}}
      \end{align*}
  $$

  - si $\alpha > \frac{2}{3}$,

    - $v_{n} \usim{+\infty} \frac{1}{2n^{\frac{3 \alpha}{2}}}$
    - $\sum_{n \geq 1} \frac{1}{2n^{\frac{3 \alpha}{2}}}$ **converge**
    - $\forall n \geq \frac{1}{2^{\frac{3 \alpha}{2}}} \geq 0$

    donc la série $\sum_{n \geq 2}v_{n}$ **converge**, et comme $\sum_{n \geq 1} \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}}$ converge, alors la série $\sum_{n \geq 2}u_{n}$ **converge**.

  - si $\alpha \in \oc{0,\frac{2}{3}}$, alors

    - $v_{n} \usim{+\infty} \frac{1}{2n^{\frac{3 \alpha}{2}}}$
    - $\sum_{n \geq 1} \frac{1}{2n^{\frac{3 \alpha}{2}}}$ **diverge**
    - $\forall n \geq \frac{1}{2^{\frac{3 \alpha}{2}}} \geq 0$

    donc la série $\sum_{n \geq 2}v_{n}$ **diverge**, et comme $\sum_{n \geq 1} \frac{(-1)^{n}}{n^{\frac{\alpha}{2}}}$ converge, alors la série $\sum_{n \geq 2}u_{n}$ **diverge**.
