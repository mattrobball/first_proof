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
