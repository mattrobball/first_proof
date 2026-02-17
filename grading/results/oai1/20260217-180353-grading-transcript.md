# Grading Transcript

- Problem: `1`
- Attempt: `oai1`
- Started (UTC): `2026-02-17T18:03:53.818790+00:00`
- Finished (UTC): `2026-02-17T18:07:05.765338+00:00`
- Grade: **3/4** (Substantial Progress (nearly complete))

## Question

Let $\mathbb{T}^3$ be the three dimensional unit size torus and let $\mu$ be the $\Phi^4_3$ measure on the space of distributions $\mathcal{D}'(\mathbb{T}^3)$. Let $\psi : \mathbb{T}^3 \to \mathbb{R}$ be a smooth function that is not identically zero and let $T_\psi : \mathcal{D}'(\mathbb{T}^3) \to \mathcal{D}'(\mathbb{T}^3)$ be the shift map given by $T_\psi(u) = u + \psi$ (with the usual identification of smooth functions as distributions). Are the measures $\mu$ and $T_\psi^* \mu$ equivalent? Here, equivalence of measures is in the sense of having the same null sets and $T_\psi^*$ denotes the pushforward under $T_\psi$.

## Solution Attempt

## 1 Smooth shifts of the \(\Phi_3^4\) measure on \(\mathbb{T}^3\)

### Problem

Let \(\mathbb{T}^3\) be the three dimensional unit size torus and let \(\mu\) be the \(\Phi_3^4\) measure on the space of distributions \(\mathcal{D}'(\mathbb{T}^3)\). Let \(\psi : \mathbb{T}^3 \to \mathbb{R}\) be a smooth function that is not identically zero and let \(T_\psi : \mathcal{D}'(\mathbb{T}^3) \to \mathcal{D}'(\mathbb{T}^3)\) be the shift map given by \(T_\psi(u) = u + \psi\) (with the usual identification of smooth functions as distributions). Are the measures \(\mu\) and \(T_\psi^*\mu\) equivalent? Here, equivalence of measures is in the sense of having the same null sets and \(T_\psi^*\) denotes the pushforward under \(T_\psi\).

### Solution

We separate the Gaussian case \(\lambda = 0\) from the interacting case \(\lambda \neq 0\). We use the notation \(T_\psi^*\mu\) for the image (push-forward) of a measure by the shift, that is \((T_\psi^*\mu)(A) = \mu(T_\psi^{-1}A)\) for Borel sets \(A \subset \mathcal{D}'(\mathbb{T}^3)\). Throughout, equivalence means having the same null sets and \(\mu \perp \nu\) denotes mutual singularity.

### 1. Gaussian case \(\lambda = 0\)

When \(\lambda = 0\), \(\mu = \mu_0\) is the (massive) Gaussian free field (GFF) on \(\mathbb{T}^3\) with covariance \((m^2 - \Delta)^{-1}\). In the massless case \(m = 0\), one typically works with the pinned/mean-zero GFF on the closed subspace \(\{u : \langle u, 1 \rangle = 0\}\).

By the Cameron--Martin theorem, \(T_\psi^*\mu_0\) is equivalent to \(\mu_0\) if and only if \(\psi\) lies in the Cameron--Martin space: \(\psi \in H^1(\mathbb{T}^3)\) in the massive case, and \(\psi \in H^1(\mathbb{T}^3)\) with \(\int_{\mathbb{T}^3} \psi = 0\) in the pinned massless case. In particular, for \(m > 0\) every \(\psi \in C^\infty(\mathbb{T}^3)\) yields equivalence. If \(\psi\) lies outside the Cameron--Martin space, then \(\mu_0\) and \(T_\psi^*\mu_0\) are mutually singular.

### 2. Interacting case \(\lambda \neq 0\): singularity under every nonzero smooth shift

Assume henceforth \(\lambda \neq 0\) and fix \(\psi \in C^\infty(\mathbb{T}^3)\), \(\psi \not\equiv 0\). We implicitly restrict to the physical/stable range of couplings for which the Euclidean \(\Phi_3^4\) measure is known to exist (with the usual stochastic-quantisation sign convention this is \(\lambda > 0\)); the argument itself only uses the non-vanishing of the logarithmic coefficient \(b_\lambda\).

**Pinned/mean-zero variants.** If one works with a pinned/mean-zero version of \(\mu\) supported on \(\{u : \langle u, 1 \rangle = 0\}\) and \(\int_{\mathbb{T}^3} \psi \neq 0\), then \(\mu\) and \(T_\psi^*\mu\) are supported on disjoint affine subspaces, hence are singular. In the remainder we either work in the massive case, or (in the pinned case) assume \(\int_{\mathbb{T}^3} \psi = 0\).

The key point in \(d = 3\) is that the *logarithmic* ("setting-sun") mass renormalisation produces a large *deterministic* linear term at small scales; this term is what ultimately separates \(\mu\) from its smooth shifts. The argument below uses only mollified fields at *super-exponentially* small scales, together with standard renormalised model convergence results from regularity structures (or paracontrolled calculus) for the dynamical \(\Phi_3^4\) model. Crucially, we do *not* assume that there exists a time-zero "renormalised cube" as a random distribution under \(\mu\) (in fact, this is precisely what fails in \(d = 3\); see [2] for an "infinitesimal" manifestation).

### 2.1. Mollifiers and super-exponential scales

Fix \(\varrho \in C_c^\infty(\mathbb{R}^3)\), \(\varrho \geq 0\), \(\int_{\mathbb{R}^3} \varrho = 1\), and extend it periodically to \(\mathbb{T}^3\). For \(\varepsilon \in (0,1)\) define \(\varrho_\varepsilon(x) := \varepsilon^{-3}\varrho(x/\varepsilon)\) and, for \(w \in \mathcal{D}'(\mathbb{T}^3)\),

\[
w_\varepsilon := w * \varrho_\varepsilon \in C^\infty(\mathbb{T}^3).
\]

Let

\[
\varepsilon_n := \exp(-e^n), \quad n \geq 1, \quad \text{and write} \quad w_n := w_{\varepsilon_n}.
\]

Then \(\varepsilon_n^{-1} = e^{e^n}\) and \(\log(\varepsilon_n^{-1}) = e^n\).

### 2.2. The renormalisation constants \(a\) and \(b_\lambda\)

In dimension 3, renormalisation for the dynamical \(\Phi_3^4\) equation involves two divergent counterterms:

- a *Wick* (tadpole) constant \(C_1(\varepsilon) \sim c_1\,\varepsilon^{-1}\),
- a *logarithmic* (setting-sun) mass constant \(C_2(\varepsilon) \sim c_2\,\log(\varepsilon^{-1})\).

For the usual stochastic-quantisation normalisation at coupling \(\lambda\), the logarithmic counterterm enters the drift with a factor proportional to \(\lambda^2\), hence is nonzero for \(\lambda \neq 0\) (see e.g. [6, \S10] and the BPHZ description [4]).

For our purposes we fix deterministic constants \(a > 0\) and \(b_\lambda \neq 0\) such that, as \(\varepsilon \downarrow 0\),

\[
C_1(\varepsilon) = a\,\varepsilon^{-1} + O(1), \qquad \lambda^2 C_2(\varepsilon) = b_\lambda \log(\varepsilon^{-1}) + O(1),
\]

where \(b_\lambda \neq 0\) for \(\lambda \neq 0\).

### 2.3. A \((\log)^{-\beta}\)-normalised cubic observable

Fix any exponent

\[
\beta \in \left(\frac{1}{2}, 1\right) \qquad (\text{e.g. } \beta = \tfrac{3}{4}).
\]

For \(w \in \mathcal{D}'(\mathbb{T}^3)\) define the real random variables (measurable functions of \(w\))

\[
Y_n(w) := e^{-\beta n}\big\langle w_n^3 - 3a\,e^{e^n}\,w_n\;-\;9b_\lambda\,e^n\,w,\;\psi\big\rangle. \tag{1}
\]

(Here \(\langle\cdot,\cdot\rangle\) denotes the distributional pairing, extending the \(L^2\) inner product.)

The next proposition is the precise substitute for the "renormalised cube exists at time zero" claim: one does *not* get a convergent cubic random distribution, but one does get enough control to deduce that \(Y_n(u) \to 0\) in probability for \(u \sim \mu\) when \(\beta > \frac{1}{2}\).

**Proposition 1.1** (Renormalised cubic at fixed time)**.** *Let \(\mu\) be the \(\Phi_3^4\) measure on \(\mathbb{T}^3\) with \(\lambda \neq 0\), realised as the time-marginal of a stationary solution to the renormalised stochastic quantisation equation (see [6, 7, 5, 1]). Let \(u \sim \mu\) and define \(u_n = u * \varrho_{\varepsilon_n}\) as above. Then there exist random distributions \(\Theta_n \in \mathcal{D}'(\mathbb{T}^3)\) and a random distribution \(R \in \mathcal{D}'(\mathbb{T}^3)\) such that:*

*(i) (Convergent remainder) One has*

\[
u_n^3 - 3a\,e^{e^n}\,u_n\;-\;9b_\lambda\,e^n\,u\;-\;\Theta_n \;\longrightarrow\; R \quad \textit{in probability in } \mathcal{C}^{-3/2-\kappa}(\mathbb{T}^3)
\]

*for every \(\kappa > 0\).*

*(ii) (Variance blowup is only logarithmic) For every \(f \in C^\infty(\mathbb{T}^3)\) there exists \(C_f < \infty\) such that*

\[
\mathbb{E}\Big[\big|\langle\Theta_n, f\rangle\big|^2\Big] \;\leq\; C_f\,e^n \qquad \textit{for all } n \geq 1.
\]

**Proof.** This statement is not a new estimate. It is a convenient repackaging of standard fixed-time estimates for the dynamical \(\Phi_3^4\) model which are scattered in the literature. In order that the present note be usable without guessing which convention for the constants is meant we spell out precisely which results are invoked.

We use the following three inputs.

(a) Let \(X\) denote the stationary solution of the linear equation \((\partial_t + m^2 - \Delta)X = \xi\) on \(\mathbb{R} \times \mathbb{T}^3\). The Wick powers of \(X\) and the additional stochastic diagrams entering the Da Prato--Debussche/regularity-structure expansion of \(\Phi_3^4\) were constructed with sharp moment bounds, for arbitrary mollifiers, in Mourrat--Weber--Xu [8, Sec. 3]. In particular the covariance estimates in that section give the following covariance bound for the only diagram of homogeneity \(-3/2\) (the "setting-sun" diagram). If \(\widetilde{\Theta}_\varepsilon\) denotes this diagram mollified at scale \(\varepsilon\), then for every smooth \(f\)

\[
\mathbb{E}\,\big|\langle\widetilde{\Theta}_\varepsilon, f\rangle\big|^2 \;\leq\; C_f\big(1 + \log\varepsilon^{-1}\big). \tag{2}
\]

For the reader who wants to see the elementary estimate behind (2) we recall it at the end of the proof.

(b) The identification of the nonlinear solution with a finite sum of these stochastic diagrams plus a regular remainder, uniformly for stationary initial data, is proved for the dynamical \(\Phi_3^4\) equation in either of the two equivalent frameworks: see Hairer [6, Sec. 10] and the paracontrolled solution theory / decomposition of the dynamic \(\Phi_3^4\) model (Mourrat--Weber [7, Secs. 2--3]), or, in a form stated directly for the invariant measure, Gubinelli--Hofmanov\'{a} [5, Sec. 4]. With the present normalisation of the coupling these results say the following. There is a random distribution \(\Theta_\varepsilon\) which differs from the diagram \(\widetilde{\Theta}_\varepsilon\) of (a) by a uniformly \(L^2\)-bounded linear combination of more regular diagrams, and there is a random distribution \(R\) such that, for every \(\kappa > 0\),

\[
u_\varepsilon^3 - 3C_1(\varepsilon)u_\varepsilon - 9\lambda^2 C_2(\varepsilon)u_\varepsilon - \Theta_\varepsilon \;\longrightarrow\; R \quad \text{in probability in } \mathcal{C}^{-3/2-\kappa}. \tag{3}
\]

(The factor 9 is the usual combinatorial coefficient of the setting-sun subdiagram for the stochastic-quantisation convention in which the drift is \(\lambda u^3\).)

(c) Finally the invariant measures constructed in Albeverio--Kusuoka [1, Thm. 1.1 and Sec. 4] and in Gubinelli--Hofmanov\'{a} [5, Sec. 4.3] are precisely the laws of the stationary solutions to which (b) applies. In particular all moment estimates in (a)--(b) hold with constants independent of the time at which the solution is observed.

We now explain how (i)--(ii) follow from these references. Put \(\varepsilon = \varepsilon_n\). Since \(C_1(\varepsilon) = a\,\varepsilon^{-1} + O(1)\) and \(\lambda^2 C_2(\varepsilon) = b_\lambda\log\varepsilon^{-1} + O(1)\), and the finite parts hidden in the \(O(1)\) have deterministic limits for a fixed mollifier (as is clear from the explicit integral formulae in the cited references), replacing the counterterms in (3) by the leading terms changes the left-hand side by a deterministic multiple of \(u_{\varepsilon_n}\) plus a remainder tending to \(0\) in \(\mathcal{C}^{-1/2-\kappa}\). Since \(u_{\varepsilon_n} \to u\) in the weaker spaces considered below, this contribution converges in probability to a fixed multiple of \(u\) and can simply be incorporated into the limiting random distribution \(R\) (or, equivalently, into the definition of \(R\) in (i)). The cited expansions are written with the factor \(u_\varepsilon\) in the linear setting-sun term whereas in (1) and in (i) we have put the limiting field \(u\). This replacement is harmless in the topology of \(\mathcal{C}^{-3/2-\kappa}\). Indeed stationary solutions of \(\Phi_3^4\) belong almost surely to \(\mathcal{C}^{-1/2-\eta}\) for every \(\eta > 0\) (one of the basic a priori estimates in the cited works), and the standard smoothing estimate for Besov/H\"{o}lder spaces on the torus gives, for \(0 < \eta < 1/2\),

\[
\|u_\varepsilon - u\|_{\mathcal{C}^{-3/2-\kappa}} \;\leq\; C(u,\eta,\kappa)\,\varepsilon^{1-\eta}.
\]

With our choice \(\varepsilon = \varepsilon_n = \exp(-e^n)\) the factor \(e^n = \log\varepsilon_n^{-1}\) multiplying this difference in the setting-sun term is negligible. (In particular the pairings against smooth test functions also converge, as used later.) After this small correction of the counterterm (3) yields precisely the convergence stated in (i).

It remains only to record the quantitative bound (ii). The covariance estimate (2) for \(\widetilde{\Theta}_\varepsilon\), together with the fact that \(\Theta_\varepsilon - \widetilde{\Theta}_\varepsilon\) is a finite sum of more regular diagrams with uniformly bounded second moments when tested against a smooth function (again part of (a)--(b)), yields

\[
\mathbb{E}\big[|\langle\Theta_n, f\rangle|^2\big] \;\leq\; C_f\,(1 + \log\varepsilon_n^{-1}) \;\leq\; C_f'\,e^n.
\]

For completeness we spell out exactly which estimate from the stochastic diagram literature is used in the preceding line. Uniform covariance estimates for all diagrams of the dynamical \(\Phi_3^4\) model (and for arbitrary smooth mollifiers) are proved in Mourrat--Weber--Xu [8, Sec. 3]. Applying their power-counting result to the diagram of homogeneity \(-3/2\) yields precisely the logarithmic bound (2) when the diagram is tested against a fixed smooth function. We refer to their dyadic summation for the short analytic proof. This completes the proof of (ii) and of the proposition. \(\square\)

**Lemma 1.2** (Convergence of the normalised observable under \(\mu\))**.** *Let \(u \sim \mu\). Then \(Y_n(u) \to 0\) in probability as \(n \to \infty\).*

**Proof.** Write \(f = \psi\) and decompose, using Proposition 1.1,

\[
Y_n(u) = e^{-\beta n}\langle R_n, \psi\rangle \;+\; e^{-\beta n}\langle\Theta_n, \psi\rangle, \qquad R_n := u_n^3 - 3a\,e^{e^n}\,u_n - 9b_\lambda\,e^n\,u - \Theta_n.
\]

By Proposition 1.1(i), \(\langle R_n, \psi\rangle\) converges in probability to \(\langle R, \psi\rangle\), hence is tight; multiplying by \(e^{-\beta n} \to 0\) gives \(e^{-\beta n}\langle R_n, \psi\rangle \to 0\) in probability. By Proposition 1.1(ii) with \(f = \psi\),

\[
\mathbb{E}\big[|e^{-\beta n}\langle\Theta_n, \psi\rangle|^2\big] \;\leq\; C_\psi\,e^{(1-2\beta)n} \;\xrightarrow[n\to\infty]{}\; 0 \qquad \text{since } \beta > \tfrac{1}{2},
\]

hence \(e^{-\beta n}\langle\Theta_n, \psi\rangle \to 0\) in \(L^2\) and therefore in probability. Combining these two terms yields \(Y_n(u) \to 0\) in probability. \(\square\)

### 2.4. An almost sure separating set

From Lemma 1.2, we can extract a deterministic subsequence along which \(Y_n(u) \to 0\) almost surely. Indeed, choose \(n_k \uparrow \infty\) such that

\[
\mathbb{P}_\mu\big(|Y_{n_k}(u)| > 2^{-k}\big) \;\leq\; 2^{-k},
\]

and apply Borel--Cantelli to obtain \(Y_{n_k}(u) \to 0\) \(\mu\)-a.s. Define the measurable set

\[
A := \Big\{w \in \mathcal{D}'(\mathbb{T}^3) : \lim_{k\to\infty} Y_{n_k}(w) = 0\Big\}.
\]

Then \(\mu(A) = 1\).

We shall allow ourselves in the next paragraph to pass, if necessary, to a further subsequence of \((n_k)\) and to redefine \(A\) by the same formula for that refined subsequence (we keep the notation \(n_k\) and \(A\)). This causes no difficulty: every subsequence of a full-measure convergence subsequence still gives a set of \(\mu\)-measure one. The refinement will be chosen so that, in addition to \(Y_{n_k}(u) \to 0\), the auxiliary error terms appearing in (4) below also converge to zero almost surely.

### 2.5. Effect of shifting by \(\psi\)

Let \(v = T_\psi(u) = u + \psi\). Then \(v_n = u_n + \psi_n\) and

\[
v_n^3 - 3a e^{e^n} v_n - 9b_\lambda e^n v = \big(u_n^3 - 3a e^{e^n} u_n - 9b_\lambda e^n u\big) + 3\psi_n\big(u_n^2 - a e^{e^n}\big) + 3\psi_n^2 u_n + \psi_n^3 - 9b_\lambda e^n \psi.
\]

Pair with \(\psi\) and multiply by \(e^{-\beta n}\):

\[
Y_n(v) = Y_n(u) + e^{-\beta n}\big\langle 3\psi_n\big(u_n^2 - ae^{e^n}\big),\psi\big\rangle + e^{-\beta n}\big\langle 3\psi_n^2 u_n + \psi_n^3,\psi\big\rangle - 9b_\lambda e^{(1-\beta)n}\langle\psi,\psi\rangle. \tag{4}
\]

Now:

- Along the subsequence \(n = n_k\) we have \(Y_{n_k}(u) \to 0\) \(\mu\)-a.s. on \(A\) by definition.

- The random distributions \(u_n^2 - ae^{e^n}\) (the renormalised square) are tight when tested against smooth functions (this is a standard output of the \(\Phi_3^4\) construction; see [6, 7, 5, 1]). Since \(\psi_n \to \psi\) in \(C^\infty\), the scalar random variables \(\langle 3\psi_n(u_n^2 - ae^{e^n}),\psi\rangle\) are tight; multiplying by \(e^{-\beta n} \to 0\) forces the second term in (4) to converge to 0 in probability (hence, along a further subsequence if desired, \(\mu\)-a.s.).

- Since \(u_n \to u\) in \(\mathcal{D}'\) and \(\psi_n \to \psi\) in \(C^\infty\), the bracket \(\langle 3\psi_n^2 u_n + \psi_n^3, \psi\rangle\) is tight (indeed convergent in probability), so the third term in (4) also tends to 0 in probability after multiplying by \(e^{-\beta n}\).

- The last term is deterministic and diverges because \(b_\lambda \neq 0\), \(\beta < 1\), and \(\langle\psi,\psi\rangle = \int_{\mathbb{T}^3} \psi(x)^2\,dx > 0\):

\[
-9b_\lambda\,e^{(1-\beta)n}\langle\psi,\psi\rangle \;\longrightarrow\; \pm\infty \qquad (n \to \infty).
\]

We now implement the refinement of the subsequence announced in \S2.4 in a completely explicit way. Since the second and the third terms in (4) converge to 0 in probability, a diagonal selection and another application of the Borel--Cantelli lemma allow us (after passing to a subsequence of the one chosen there and redefining \(A\), without changing the notation) to find a measurable set \(E\) with \(\mu(E) = 1\) such that, for every \(u \in E\), *all three* random terms in (4) other than the deterministic last one tend to 0 along \(n = n_k\). For such a \(u\) the divergent deterministic contribution displayed in the last item forces \(|Y_{n_k}(u+\psi)| \to \infty\) (with a sign depending on \(b_\lambda\)). In particular \(u + \psi \notin A\) because membership in \(A\) is defined by the condition \(Y_{n_k}(w) \to 0\). Thus

\[
(T_\psi^*\mu)(A) = \mu\big(\{u :\; u + \psi \in A\}\big) = 0,
\]

whereas \(\mu(A) = 1\). We conclude that \(\mu \perp T_\psi^*\mu\).

**Theorem 1.3** (Failure of quasi-invariance under smooth shifts)**.** *Let \(\mu\) be a well-defined \(\Phi_3^4\) measure on \(\mathbb{T}^3\) at a non-zero coupling \(\lambda\) (in the usual physical convention, \(\lambda > 0\)). Then for every nonzero \(\psi \in C^\infty(\mathbb{T}^3)\) one has*

\[
\mu \;\perp\; T_\psi^*\mu.
\]

*(In the pinned/mean-zero setup, if \(\int \psi \neq 0\) the measures are trivially singular by disjoint support; if \(\int \psi = 0\) the conclusion still holds.)*

**Proof.** The construction of the separating set in paragraphs 2.4--2.5 gives the claim: the set \(A\) has full \(\mu\)-measure whereas the shifted measure assigns it zero mass, \((T_\psi^*\mu)(A) = 0\). \(\square\)

**Remark 1.4.** For comparison we mention that the mutual singularity of the \(\Phi_3^4\) measure with the (unshifted) Gaussian free field was proved by a different method in Barashkov--Gubinelli [3]. The small-scale observable used above is in the same spirit, but the present proof of non-quasi-invariance under smooth deterministic translations is self-contained once the standard stochastic estimates quoted in Proposition 1.1 are granted.

### References

[1] S. Albeverio and S. Kusuoka, *The invariant measure and the flow associated to the \(\Phi_3^4\)-quantum field model*, Ann. Sc. Norm. Sup. Pisa Cl. Sci. (5) **20** (2020), no. 4, 1359--1427. arXiv:1711.07108.

[2] S. Albeverio, S. Liang, and B. Zegarlinski, *Remark on the integration by parts formula for the \(\varphi_3^4\)-quantum field model*, Infin. Dimens. Anal. Quantum Probab. Relat. Top. **9** (2006), no. 1, 149--154. doi:10.1142/S0219025706002275.

[3] N. Barashkov and M. Gubinelli, *The \(\Phi_3^4\) measure via Girsanov's theorem*, Electron. J. Probab. **26** (2021), paper no. 81, 1--29. doi:10.1214/21-EJP635.

[4] Y. Bruned, M. Hairer, and L. Zambotti, *Algebraic renormalisation of regularity structures*, Invent. Math. **215** (2019), no. 3, 1039--1156. arXiv:1610.08468.

[5] M. Gubinelli and M. Hofmanov\'{a}, *A PDE construction of the Euclidean \(\Phi_3^4\) quantum field theory*, Comm. Math. Phys. **384** (2021), no. 1, 1--75. doi:10.1007/s00220-021-04022-0.

[6] M. Hairer, *A theory of regularity structures*, Invent. Math. **198** (2014), no. 2, 269--504. arXiv:1303.5113.

[7] J.-C. Mourrat and H. Weber, *The dynamic \(\Phi_3^4\) model comes down from infinity*, Comm. Math. Phys. **356** (2017), no. 3, 673--753. arXiv:1601.01234.

[8] J.-C. Mourrat, H. Weber, and W. Xu, *Construction of \(\Phi_3^4\) diagrams for pedestrians*, preprint (2016). arXiv:1610.08897.

## Editor Dispatch

Based on the strengths of the available models and the specific requirements of the mathematical proof regarding the $\Phi_3^4$ measure:

1.  **Correctness & Completeness** is assigned to **claude_code**. The proof involves complex probabilistic arguments (Borel-Cantelli lemmas, convergence types) and specific SPDE estimates (regularity structures). Claude models currently demonstrate state-of-the-art performance in following dense logical chains and identifying subtle reasoning gaps in mathematical texts.
2.  **Clarity & Rigor** is assigned to **codex_cli**. This perspective requires a strict check on notational consistency, variable definitions, and structural precision. As a code-optimized model, Codex is particularly adept at treating the proof as "syntax," ensuring that symbols like $\varepsilon_n$, $C_1(\varepsilon)$, and $\Theta_n$ are defined and used consistently throughout the text.
3.  **Reference Validity** is assigned to **gemini_api**. The proof relies heavily on specific results from the literature (Hairer, Gubinelli, Mourrat-Weber). Gemini's vast training corpus and strong retrieval/knowledge retention capabilities make it the most suitable candidate for verifying that the cited theorems exist and are applied in the correct context.

```json
{
  "assignments": {
    "Correctness & Completeness": "claude_code",
    "Clarity & Rigor": "codex_cli",
    "Reference Validity": "gemini_api"
  },
  "reasoning": "claude_code is assigned to Correctness for its strong logical reasoning capabilities necessary to verify the probabilistic arguments and SPDE estimates. codex_cli is assigned to Clarity & Rigor to leverage its code-based sensitivity to syntax and notational consistency. gemini_api is assigned to Reference Validity due to its extensive knowledge base of academic literature, suitable for checking citations."
}
```

## Reviewer — Correctness & Completeness

# Review: Correctness & Completeness of the $\Phi_3^4$ Smooth Shift Singularity Proof

## Overall Assessment

This is a well-structured proof that the $\Phi_3^4$ measure on $\mathbb{T}^3$ is singular under any nonzero smooth shift. The argument's strategy — constructing a measurable separating set via a renormalized cubic observable whose behavior differs under $\mu$ versus $T_\psi^*\mu$ — is sound in conception. The proof correctly identifies the logarithmic mass renormalization as the mechanism driving singularity. However, there are several issues of varying severity concerning rigor, completeness, and correctness of specific claims.

## Detailed Analysis

### Section 1: Gaussian Case

The Cameron–Martin theorem is correctly invoked. The claim that $C^\infty(\mathbb{T}^3) \subset H^1(\mathbb{T}^3)$ is of course true, so equivalence in the massive Gaussian case is immediate. The pinned/mean-zero variant is correctly noted. This section is clean.

### Section 2.2: Renormalization Constants

The asymptotic forms $C_1(\varepsilon) \sim a\varepsilon^{-1}$ and $\lambda^2 C_2(\varepsilon) \sim b_\lambda \log(\varepsilon^{-1})$ are standard. However, the proof asserts $b_\lambda \neq 0$ for $\lambda \neq 0$ without justification. This is a nontrivial claim — it amounts to saying a specific Feynman diagram integral (the setting-sun diagram) is nonzero. While this is indeed true and well-known, the proof should at least cite the specific computation or give a one-line argument for why the leading coefficient cannot vanish.

### Section 2.3: Proposition 1.1

The proposition is presented as a "repackaging" of known results. The logical structure is:

1. Stochastic diagram estimates from [8] give the variance bound (2).
2. The nonlinear decomposition from [6, 7, 5] gives the convergence (3).
3. Replacing $C_1(\varepsilon), C_2(\varepsilon)$ by their leading terms and $u_\varepsilon$ by $u$ in the linear term introduces errors that are absorbed.

**Issue with the replacement $u_\varepsilon \to u$:** The proof claims replacing $9b_\lambda e^n u_{\varepsilon_n}$ with $9b_\lambda e^n u$ is "harmless in the topology of $\mathcal{C}^{-3/2-\kappa}$." The bound given is $\|u_\varepsilon - u\|_{\mathcal{C}^{-3/2-\kappa}} \leq C \varepsilon^{1-\eta}$, so the error term is $O(e^n \cdot \varepsilon_n^{1-\eta}) = O(e^n \cdot e^{-(1-\eta)e^n})$, which is super-exponentially small. This is correct — the argument works.

**Issue with the definition of $\Theta_n$:** The relationship between $\Theta_n$ (appearing in Proposition 1.1) and $\widetilde{\Theta}_\varepsilon$ (the pure setting-sun diagram from [8]) is stated to differ by "a uniformly $L^2$-bounded linear combination of more regular diagrams." This is plausible but the proof does not specify which diagrams or why they are $L^2$-bounded when tested against smooth functions. This is left entirely to the reader to verify from [6, 7, 5].

### Section 2.4–2.5: The Separating Set Argument

**The core computation in equation (4) is correct.** The binomial expansion of $(u_n + \psi_n)^3$ and the subsequent identification of terms is straightforward algebra that can be verified directly.

**Issue with the subsequence refinement:** The proof claims that one can choose a single subsequence $(n_k)$ along which *all* of the following hold $\mu$-a.s.:
- $Y_{n_k}(u) \to 0$
- $e^{-\beta n_k}\langle 3\psi_{n_k}(u_{n_k}^2 - ae^{e^{n_k}}), \psi\rangle \to 0$
- $e^{-\beta n_k}\langle 3\psi_{n_k}^2 u_{n_k} + \psi_{n_k}^3, \psi\rangle \to 0$

The argument for the second term appeals to "tightness" of $\langle \psi_n(u_n^2 - ae^{e^n}), \psi\rangle$. But tightness alone is not sufficient — one needs that these random variables are $O_P(1)$, i.e., bounded in probability, which tightness does give. Then multiplication by $e^{-\beta n} \to 0$ yields convergence to 0 in probability. The subsequent Borel–Cantelli extraction of an a.s. convergent subsequence requires quantitative probability bounds (e.g., $\mathbb{P}(|\cdot| > M) \leq \delta_n$ summable), which are not provided for this term. The proof only says "tightness" without giving the rate needed for Borel–Cantelli.

**Issue with the tightness claim for renormalized squares:** The proof states that $u_n^2 - ae^{e^n}$ (tested against smooth functions) is tight, citing [6, 7, 5, 1]. This is the Wick square $:u_\varepsilon^2:$ and its tightness when tested against smooth functions is indeed a standard consequence of the stochastic estimates — but the proof conflates $u_n^2 - C_1(\varepsilon_n)$ (the properly Wick-ordered square with the exact counterterm) with $u_n^2 - ae^{e^n}$ (using only the leading-order term). The difference is $O(1) \cdot u_n$, which tested against $\psi_n \psi$ is bounded, so this is not a real problem, but it should be noted.

### Theorem 1.3

The theorem statement is correct given the preceding construction. The proof is a direct corollary of §2.4–2.5.

### Sign of $b_\lambda$

The proof claims the deterministic term $-9b_\lambda e^{(1-\beta)n}\langle\psi,\psi\rangle \to \pm\infty$. Since $\langle\psi,\psi\rangle > 0$ (as $\psi \not\equiv 0$), the sign depends on $b_\lambda$. The argument only needs $|Y_{n_k}(v)| \to \infty$, which follows regardless of the sign of $b_\lambda$ as long as $b_\lambda \neq 0$. This is correctly handled.

### Missing Discussion: Uniqueness of the $\Phi_3^4$ Measure

The proof begins "Let $\mu$ be a well-defined $\Phi_3^4$ measure." The question of uniqueness of the $\Phi_3^4$ measure is delicate and open in full generality. The proof sidesteps this by working with any measure that arises as a time-marginal of the stationary stochastic quantization dynamics. This is logically fine but should be noted: the result applies to *any* $\Phi_3^4$ measure realized as such a marginal, not necessarily to every conceivable construction.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Section 2.2 / throughout",
      "reason": "The claim that b_lambda != 0 for lambda != 0 is asserted without proof or precise citation. This is the linchpin of the entire argument — if b_lambda could vanish, the deterministic divergent term in (4) would vanish and the proof would fail.",
      "required_fix": "Provide an explicit justification: either cite the specific computation of the setting-sun diagram integral showing its leading coefficient is a nonzero numerical constant times lambda^2, or include a brief calculation.",
      "suggestion": "A short remark such as: 'The leading coefficient of C_2(epsilon) equals (const) times the integral of [G_epsilon]^3 over T^3, where G_epsilon is the periodized heat kernel; this integral is strictly positive by positivity of G_epsilon, hence b_lambda = lambda^2 times (positive constant) != 0.' This would close the gap cleanly."
    },
    {
      "severity": "major",
      "location": "Section 2.5, second bullet (tightness of renormalized square term)",
      "reason": "The Borel–Cantelli extraction of an a.s. convergent subsequence for the second and third terms in (4) requires quantitative probability tail bounds (summable), not merely tightness. The proof only asserts 'tightness' and 'convergence to 0 in probability' before claiming a.s. convergence along a subsequence.",
      "required_fix": "Either (a) provide explicit moment bounds (e.g., uniform L^p bounds for some p >= 1) for the renormalized square tested against smooth functions, which would give polynomial tail decay and allow Borel–Cantelli, or (b) note that convergence in probability along any sequence always admits a further subsequence converging a.s. (a basic measure theory fact) and state this explicitly.",
      "suggestion": "The simplest fix is option (b): add a sentence such as 'Since each of the second and third terms converges to 0 in probability, we may (by a standard subsequence extraction) pass to a further subsequence along which they also converge to 0 a.s.' This is a purely measure-theoretic fact (every sequence converging in probability has an a.s. convergent subsequence) and requires no additional estimates."
    },
    {
      "severity": "minor",
      "location": "Section 2.3, Proposition 1.1(i)",
      "reason": "The relationship between Theta_n and the pure setting-sun diagram tilde{Theta}_epsilon is described vaguely as differing by 'a uniformly L^2-bounded linear combination of more regular diagrams.' The specific diagrams are not named, and no explicit regularity exponents are given for them.",
      "required_fix": "Name or characterize the additional diagrams (e.g., 'diagrams of homogeneity strictly greater than -3/2') and note that their contribution when tested against smooth functions is uniformly bounded in L^2 by the estimates in [8].",
      "suggestion": "Add a parenthetical such as: '(specifically, Theta_epsilon = tilde{Theta}_epsilon plus a linear combination of diagrams of homogeneity > -3/2, each of which has uniformly bounded L^2 norm when paired with any fixed smooth test function, by [8, Sec. 3]).' This would make the bound in (ii) fully traceable."
    },
    {
      "severity": "minor",
      "location": "Section 2.3, equation (1)",
      "reason": "In the definition of Y_n(w), the term 9b_lambda e^n w appears with the full distributional field w rather than the mollified field w_n. While the proof later explains this replacement is harmless, presenting it this way in the definition without comment is initially confusing, since the expression '9b_lambda e^n w' paired with psi involves a distributional pairing of w against psi, which is well-defined (psi is smooth) but looks inconsistent with the other terms involving w_n.",
      "required_fix": "Add a brief remark at equation (1) noting that w is paired against psi via the distributional pairing, and that using w rather than w_n is a deliberate choice justified in the proof of Proposition 1.1.",
      "suggestion": "Insert after (1): 'Note that we use the un-mollified field w in the linear term; see the proof of Proposition 1.1 for the justification of this convention.'"
    },
    {
      "severity": "minor",
      "location": "Theorem 1.3 statement",
      "reason": "The theorem states the result for 'a well-defined Phi_3^4 measure' but the proof only applies to measures realized as time-marginals of stationary solutions to stochastic quantization. Since uniqueness of the Phi_3^4 measure is not fully established, this is a (small) over-claim.",
      "required_fix": "Either qualify the theorem to apply to measures arising as invariant measures of the stochastic quantization dynamics, or note that all known constructions produce such measures.",
      "suggestion": "Add a parenthetical to the theorem statement: '...realized as the invariant measure of the dynamical Phi_3^4 stochastic quantization equation (which includes all constructions known to date [1, 3, 5]).' This precisely delineates the scope without weakening the result in practice."
    },
    {
      "severity": "minor",
      "location": "Section 2.5, Wick square versus leading-order subtraction",
      "reason": "The proof uses u_n^2 - a e^{e^n} and appeals to tightness results for the Wick square :u_epsilon^2: = u_epsilon^2 - C_1(epsilon). Since a e^{e^n} = C_1(epsilon_n) - O(1), the difference is O(1) * u_n tested against psi_n * psi, which is bounded. This is correct but unstated.",
      "required_fix": "Note that replacing C_1(epsilon_n) by its leading term a * epsilon_n^{-1} introduces an O(u_n) error that is harmless.",
      "suggestion": "Add one sentence: 'Replacing C_1(epsilon_n) by a epsilon_n^{-1} introduces an error of order O(1) times u_n; testing against psi_n psi and multiplying by e^{-beta n} yields a term tending to 0, so the tightness of the Wick square transfers to u_n^2 - a e^{e^n}.'"
    }
  ],
  "residual_concerns": [
    "The proof's reliance on the full machinery of regularity structures / paracontrolled calculus means that verifying Proposition 1.1 requires expertise in those frameworks. While the proposition is stated as a repackaging of known results, a reader without deep familiarity with [5-8] cannot independently verify the claims. This is inherent to the subject but worth noting.",
    "The choice of super-exponential scales epsilon_n = exp(-e^n) is sufficient but the proof does not discuss whether a weaker rate (e.g., polynomial) would also work. This is not an error but understanding the threshold would strengthen the conceptual picture.",
    "The combinatorial factor 9 in front of b_lambda is stated to be 'the usual combinatorial coefficient' but is not derived. For a self-contained treatment at the graduate level, a one-line derivation or reference to the specific combinatorial identity would be helpful."
  ]
}
```

## Summary

The proof is fundamentally correct in its strategy and core computations. The two major issues are: (1) the non-vanishing of $b_\lambda$ needs explicit justification since it is the engine of the entire argument, and (2) the Borel–Cantelli subsequence extraction in §2.5 needs a clearer appeal to the standard fact that convergence in probability implies a.s. convergence along a subsequence. The minor issues are matters of precision and traceability rather than logical gaps. With the suggested fixes, the proof would be rigorous at the graduate level claimed.

## Reviewer — Clarity & Rigor

No listed skill applies here (`skill-creator`/`skill-installer` are unrelated), so this is a direct clarity-and-rigor review.

The argument has a coherent high-level structure, but at graduate peer-review rigor the core analytic inputs are not pinned down precisely enough to be independently checkable.

```json
{
  "issues": [
    {
      "severity": "critical",
      "location": "Proposition 1.1 (statement and proof)",
      "reason": "This proposition is the linchpin of the singularity argument, but it is presented as a 'repackaging' of broad literature sections without theorem/lemma identifiers that explicitly yield exactly (i) and (ii) with the same objects and topology. The object Theta_n is not defined concretely enough to verify the claim.",
      "required_fix": "Either provide a self-contained proof of Proposition 1.1, or cite exact theorem/proposition numbers (with matching assumptions and normalization) that imply each part of (i) and (ii), including a precise definition of Theta_n.",
      "suggestion": "Add a dedicated 'Imported analytic input' subsection with: exact cited results, one-to-one notation translation, and a short derivation showing how those results imply (i) and (ii) verbatim."
    },
    {
      "severity": "major",
      "location": "Section 2.2 and equations (1), (3), (4)",
      "reason": "Normalization consistency is not fully rigorous: constants a, b_lambda, and the factor 9 are asserted from convention, and non-vanishing of b_lambda is not tied to an explicit formula in the chosen convention. A mismatch here would break the deterministic diverging term used for separation.",
      "required_fix": "Fix one renormalization/sign convention explicitly and derive the exact linear counterterm coefficient in that convention, including why b_lambda != 0 for lambda != 0.",
      "suggestion": "Insert a short computation (or exact formula citation) for the setting-sun coefficient and then restate Y_n with those constants, removing convention ambiguity."
    },
    {
      "severity": "major",
      "location": "Section 2.5, bullets on the 2nd and 3rd terms in (4)",
      "reason": "Key tightness/convergence claims for the cross terms are asserted as 'standard output' without explicit quantitative bounds or precise citations. These are needed to justify the probabilistic limit and the later almost-sure subsequence extraction.",
      "required_fix": "Provide a lemma with explicit bounds/citations for: (a) tightness (or uniform moment bounds) of <psi_n(u_n^2 - a e^{e^n}), psi>, and (b) convergence/tightness of <psi_n^2 u_n + psi_n^3, psi>.",
      "suggestion": "Use a uniform second-moment estimate for the renormalized square tested against smooth functions, then apply c_n X_n -> 0 in probability with c_n = e^{-beta n}."
    },
    {
      "severity": "major",
      "location": "Sections 2.4-2.5 (subsequence refinement, sets A and E)",
      "reason": "The diagonal/Borel-Cantelli refinement is described informally. At this rigor target, the exact construction of one subsequence that handles all required random terms simultaneously should be explicit.",
      "required_fix": "Write an explicit subsequence selection with summable tail probabilities for each required term and define E as an intersection of liminf events.",
      "suggestion": "Define Z_n^(1), Z_n^(2), Z_n^(3) for the three non-deterministic terms in (4), choose n_k with P(|Z_{n_k}^(i)| > 2^{-k}) <= 2^{-k} for each i, then apply Borel-Cantelli and conclude on E = intersection_i E_i."
    },
    {
      "severity": "minor",
      "location": "Gaussian case setup and theorem framing",
      "reason": "The ambient state space switches between full D'(T^3) and pinned mean-zero subspace, but this is not fixed globally at the start. This can obscure which shift maps are admissible in each regime.",
      "required_fix": "State the underlying sample space explicitly for each regime and phrase equivalence/singularity claims on that space.",
      "suggestion": "Add a short 'state-space conventions' paragraph before Section 1 distinguishing massive vs pinned massless settings and admissible shifts."
    }
  ],
  "residual_concerns": [
    "A key bound is traced to a preprint-level source; for peer-review robustness, either provide a published equivalent citation or include more of the estimate directly.",
    "The phrase 'well-defined Phi_3^4 measure at non-zero coupling' should be tied to precise parameter/existence assumptions to avoid overstatement."
  ]
}
```

## Reviewer — Reference Validity

The proof is well-structured and demonstrates a high degree of rigor in its use of external results. The author correctly identifies the necessary machinery from the theory of Regularity Structures and Paracontrolled Calculus to establish the properties of the $\Phi^4_3$ measure. The citations are generally appropriate and support the claims made.

However, there are minor bibliographic issues and opportunities to increase the precision of the citations to aid the reader.

### Issues

```json
{
  "issues": [
    {
      "severity": "minor",
      "location": "References",
      "reason": "Reference [8] is cited as a preprint (2016), but it has since been published.",
      "required_fix": "Update the citation to the published version.",
      "suggestion": "Change [8] to: J.-C. Mourrat, H. Weber, and W. Xu, 'Construction of $\\Phi^3_4$ diagrams for pedestrians', Ann. Inst. Henri Poincaré Probab. Stat. 53 (2017), no. 4, 2229–2266."
    },
    {
      "severity": "minor",
      "location": "Proof of Proposition 1.1, part (a)",
      "reason": "The citation '[8, Sec. 3]' for the covariance bound of the setting-sun diagram is somewhat broad.",
      "required_fix": "Provide a more specific pointer within the reference.",
      "suggestion": "Specify the exact proposition or theorem in Mourrat--Weber--Xu (e.g., Proposition 3.2 or the specific bound on the second Wick power of the stochastic convolution) that establishes the logarithmic divergence."
    }
  ],
  "residual_concerns": [
    "In Section 2.2, the text asserts $b_\\lambda \\neq 0$. While standard, this coefficient depends on the specific choice of mollifier $\\varrho$. It may be worth noting that $b_\\lambda \\neq 0$ holds for the specific class of mollifiers considered (non-negative, integral 1), as this is not automatically true for all kernels."
  ]
}
```

## Grading Decision

## Editorial Synthesis

### Overview

The solution attempts to prove that the $\Phi^4_3$ measure $\mu$ on $\mathbb{T}^3$ is mutually singular with its pushforward under any nonzero smooth shift $T_\psi$. The answer given — mutual singularity in the interacting case ($\lambda \neq 0$), equivalence in the free case ($\lambda = 0$) — is correct and aligns with the expected behavior in constructive QFT. The overall proof strategy is sound and creative: construct a normalised cubic observable $Y_n$ that converges to zero under $\mu$ but diverges under the shifted measure, due to a deterministic logarithmic mass renormalisation term that cannot be cancelled.

### Assessment of Errors

**Incorrect Logic or Reasoning.** The core logical architecture is valid: the Cameron–Martin theorem correctly handles the Gaussian case, and the singularity argument for $\lambda \neq 0$ proceeds by exhibiting a measurable set $A$ with $\mu(A)=1$ and $(T_\psi^*\mu)(A)=0$. However, as reviewers 2 and 10 note, the subsequence extraction and Borel–Cantelli arguments are stated somewhat loosely. The solution asserts tightness and convergence in probability, then claims a.s. convergence along a subsequence — this is correct as a matter of standard measure theory (every sequence converging in probability admits an a.s. convergent subsequence), but the solution does not state this explicitly and the diagonal selection over multiple terms is described informally. This is a presentation/rigor gap rather than a logical error per se. I do not find any genuinely incorrect logical step.

**Hallucinated Results or Literature.** The references are real and correctly attributed. The mathematical content of the cited results (regularity structures, stochastic quantisation estimates, Cameron–Martin theorem) is used appropriately. Reviewer 12 notes that [8] should be updated to its published version — a bibliographic issue, not a hallucination. No hallucinated theorems are detected.

**Calculation Mistakes.** The algebraic expansion in equation (4) — expanding $(u+\psi)_n^3$ and collecting terms — is correct. The identification of the divergent deterministic term $-9b_\lambda e^{(1-\beta)n}\langle\psi,\psi\rangle$ follows from the algebra. No arithmetic or algebraic errors are apparent.

**Conceptual Misunderstanding.** None. The solution demonstrates expert-level understanding of: the renormalisation structure of $\Phi^4_3$, the role of Wick ordering and the setting-sun diagram, the distinction between the $d=2$ case (where the renormalised cube converges) and the $d=3$ case (where it does not, requiring the $(\log)^{-\beta}$ normalisation), and the Cameron–Martin dichotomy for Gaussian measures.

### Assessment of Achievements

**Problem Understanding.** Clearly demonstrated. The solution correctly identifies the two regimes (Gaussian vs. interacting), the relevant mathematical machinery, and the key difficulty in $d=3$.

**Correct End Result.** Yes. The answer is: $\mu$ and $T_\psi^*\mu$ are mutually singular for every nonzero smooth $\psi$ when $\lambda \neq 0$, and equivalent when $\lambda = 0$ (with the appropriate Cameron–Martin condition). This is correct.

**Insight and Creativity.** The construction of the normalised observable $Y_n$ with the super-exponential mollification scale and the $e^{-\beta n}$ damping factor is a genuinely clever device. The idea that the logarithmic mass renormalisation (a peculiarity of $d=3$) creates a deterministic divergence under translation is the key insight, and it is well-executed.

**Practical Usefulness.** An expert working on quasi-invariance questions for singular SPDEs would find this attempt highly informative. The proof strategy is essentially complete and the gaps identified are fillable.

### Mapping Reviewer Findings to the Grade

The reviewers collectively identify:

- **2 critical/major issues of rigor**: (1) the non-vanishing of $b_\lambda$ is not proved (reviews 1, 8), and (2) Proposition 1.1 is a "repackaging" without sufficiently precise citations or a self-contained proof (review 7). These are the most significant gaps.
- **Several major rigor issues**: the subsequence/Borel–Cantelli construction is informal (reviews 2, 10), and cross-term bounds are asserted without explicit estimates (review 9).
- **Multiple minor issues**: notation choices, state-space conventions, bibliographic updates, and small clarifications (reviews 3, 4, 5, 6, 11, 12, 13).

The critical question for grading is: could an expert fill these gaps in a short time? The non-vanishing of $b_\lambda$ is a standard computation (the setting-sun integral is manifestly positive); an expert would supply this in a paragraph. The precise citations for Proposition 1.1 require chasing through the literature but do not involve new mathematics. The subsequence construction is routine. Overall, these gaps are real but routine for an expert in the field — they represent incomplete exposition rather than mathematical obstacles.

### Grade Determination

The solution identifies the correct answer, deploys the right strategy, executes the key steps correctly, and leaves gaps that are fillable by an expert in modest time. This places it squarely at **grade 3** — nearly complete, with gaps that an expert could fill in under an hour. It falls short of grade 4 because Proposition 1.1 is not proved self-containedly nor cited with sufficient precision, and the key constant $b_\lambda \neq 0$ is not justified.

```json
{
  "progress_grade": 3,
  "error_incorrect_logic": "false",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "The solution correctly identifies that the Phi^4_3 measure is mutually singular with its smooth shifts (for nonzero coupling) and equivalent in the free case. The proof strategy — constructing a log-normalised cubic observable that converges to zero under mu but diverges under the shifted measure due to the deterministic logarithmic mass renormalisation — is creative and essentially sound. The main gaps are: (1) the non-vanishing of the setting-sun coefficient b_lambda is asserted without proof or precise citation, (2) Proposition 1.1 is presented as a repackaging of literature results without sufficiently specific references or a self-contained derivation, and (3) the subsequence/Borel-Cantelli diagonal extraction is described informally rather than constructed explicitly. These are genuine rigor deficiencies at the graduate level, but all are fillable by an expert in short order, placing the attempt at nearly complete."
}
```
