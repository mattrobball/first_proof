## 6 Large \(\varepsilon\)-light vertex subsets

### Problem

For a graph \(G = (V, E)\), let \(G_S = (V, E(S, S))\) denote the graph with the same vertex set, but only the edges between vertices in \(S\). Let \(L\) be the Laplacian matrix of \(G\) and let \(L_S\) be the Laplacian of \(G_S\). I say that a set of vertices \(S\) is \(\epsilon\)-light if the matrix \(\epsilon L - L_S\) is positive semidefinite. Does there exist a constant \(c > 0\) so that for every graph \(G\) and every \(\epsilon\) between 0 and 1, \(V\) contains an \(\epsilon\)-light subset \(S\) of size at least \(c\epsilon|V|\)?

### Solution

We prove the claim with an explicit constant \(c = 1/256\).

Throughout we write \(n = |V|\). Some degenerate cases are immediate and will be set aside. If \(n = 0\) the assertion is vacuous. If \(\varepsilon = 0\) the empty set is 0-light and has the required size. If the graph has no edges (so that its Laplacian is the zero matrix), then \(L_S = 0\) for every \(S\) and we may simply take all vertices. Thus in the main part of the proof we assume \(n \geq 1\), \(\varepsilon \in (0, 1]\), and that the Laplacian has positive rank. All Loewner inequalities and traces below are taken on the subspace \(\operatorname{range}(L) = (\ker L)^\perp\), and \(I\) denotes the identity on that space. The exceptional cases are revisited in Step 6.

**Step 1: Normalization on the Laplacian range.** Let \(\ker L\) be the space of vectors that are constant on each connected component of \(G\). Let \(L^\dagger\) be the Moore--Penrose pseudoinverse, and define

\[
L^{-1/2} := (L^\dagger)^{1/2}.
\]

Then \(L^{-1/2}\) acts as the inverse square root on \(\operatorname{range}(L) = (\ker L)^\perp\) and as 0 on \(\ker L\).

For an edge \(e = \{u, v\}\) define the rank-one edge Laplacian

\[
L_e := (e_u - e_v)(e_u - e_v)^\top,
\]

so that \(L = \sum_{e \in E} L_e\). All sums over edges below are taken with multiplicity if the graph has parallel edges. Define

\[
A_e := L^{-1/2} L_e L^{-1/2}.
\]

Each \(A_e\) is positive semidefinite on \(\operatorname{range}(L)\), whose dimension is \(d := \operatorname{rank}(L) \leq n\). Moreover, on \(\operatorname{range}(L)\) we have

\[
\sum_{e \in E} A_e = L^{-1/2} \Big( \sum_{e \in E} L_e \Big) L^{-1/2} = L^{-1/2} L L^{-1/2} = I. \tag{31}
\]

Also, for any \(S \subseteq V\),

\[
L^{-1/2} L_S L^{-1/2} = \sum_{e \in E(S,S)} A_e \quad \text{on } \operatorname{range}(L). \tag{32}
\]

Therefore, it suffices to find \(S\) such that on \(\operatorname{range}(L)\),

\[
\sum_{e \in E(S,S)} A_e \preceq \varepsilon I, \tag{33}
\]

because then (32) implies \(L^{-1/2} L_S L^{-1/2} \preceq \varepsilon I\), i.e.

\[
x^\top L_S x \leq \varepsilon \, x^\top L x \quad \text{for all } x \perp \ker L.
\]

If \(P = L^{-1/2} L^{1/2} = L^{1/2} L^{-1/2}\) denotes the orthogonal projection onto \(\operatorname{range}(L)\), the displayed Loewner inequality is equivalent to \(x^T L_S x \leq \varepsilon x^T L x\) for every \(x \in \operatorname{range}(L)\) by taking \(z = L^{1/2} x\) (where \(L^{1/2}\) denotes the positive square root of \(L\), acting as zero on \(\ker L\)) in the quadratic form. Vectors in \(\ker L\) are constant on each connected component and are therefore also annihilated by \(L_S\); by symmetry no mixed terms occur between \(\operatorname{range}(L)\) and \(\ker L\). Hence the inequality holds for all \(x \in \mathbb{R}^V\), which is exactly \(\varepsilon L - L_S \succeq 0\).

**Step 2: A one-sided BSS barrier lemma.** The following lemma is a one-sided variant of the barrier method introduced by Batson, Spielman and Srivastava [1]; we give a complete proof for the reader's convenience. For a PSD matrix \(M \succeq 0\) on a \(d\)-dimensional space and a scalar \(u > \lambda_{\max}(M)\), define the potential

\[
\Phi_u(M) := \operatorname{tr}(uI - M)^{-1}.
\]

**Lemma 6.1** (One-sided barrier). *Assume \(M \prec uI\), let \(u' > u\), and put \(U := (u'I - M)^{-1}\). If \(B \succeq 0\) satisfies*

\[
\operatorname{tr}(BU) + \frac{\operatorname{tr}(BU^2)}{\Phi_u(M) - \Phi_{u'}(M)} \leq 1, \tag{34}
\]

*then \(M + B \prec u'I\) and \(\Phi_{u'}(M + B) \leq \Phi_u(M)\).*

*Proof.* Let \(K := B^{1/2} U B^{1/2} \succeq 0\). The hypothesis (34) implies \(\operatorname{tr}(K) < 1\): the second summand there is non-negative, and if it were zero then the positive semidefinite matrix \(B^{1/2} U^2 B^{1/2}\) would have trace zero and hence vanish; since \(U\) is invertible on our space this forces \(B = 0\). Consequently every eigenvalue of \(K\) is \(< 1\), so in particular \(\|K\| < 1\) and \((I - K)\) is invertible. By the Sherman--Morrison--Woodbury identity (which can be verified by multiplying the two sides),

\[
(u'I - M - B)^{-1} = U + U B^{1/2}(I - K)^{-1} B^{1/2} U,
\]

so \(u'I - M - B \succ 0\), i.e. \(M + B \prec u'I\).

Taking traces, using cyclicity of the trace and the elementary fact that \(\operatorname{tr}(XC) \leq \operatorname{tr}(YC)\) whenever \(0 \preceq X \preceq Y\) and \(C \succeq 0\), together with \((I - K)^{-1} \preceq (1 - \operatorname{tr} K)^{-1} I\) (valid for PSD \(K\) with \(\operatorname{tr} K < 1\)), we obtain

\[
\Phi_{u'}(M + B) \leq \Phi_{u'}(M) + \frac{\operatorname{tr}(BU^2)}{1 - \operatorname{tr}(BU)}.
\]

A short rearrangement shows that (34) is equivalent to the bound that the right-hand side is at most \(\Phi_u(M)\). This yields \(\Phi_{u'}(M + B) \leq \Phi_u(M)\). \(\square\)

We will also use the following inequality: if \(u' = u + \delta\), then

\[
\Phi_u(M) - \Phi_{u'}(M) \geq \delta \operatorname{tr} (u'I - M)^{-2} = \delta \operatorname{tr}(U^2). \tag{35}
\]

Indeed, diagonalizing \(M\) with eigenvalues \(\lambda_j\) gives

\[
\Phi_u(M) - \Phi_{u'}(M) = \sum_j \frac{\delta}{(u - \lambda_j)(u' - \lambda_j)} \geq \sum_j \frac{\delta}{(u' - \lambda_j)^2}.
\]

**Step 3: A partial coloring process.** Fix \(\varepsilon \in (0, 1]\) and set

\[
r := \left\lceil \frac{16}{\varepsilon} \right\rceil, \quad u_0 := \frac{\varepsilon}{2}, \quad \delta := \frac{\varepsilon}{n}, \quad k := \left\lfloor \frac{n}{4} \right\rfloor. \tag{36}
\]

We will color \(k\) vertices, one at a time, using \(r\) colors.

At time \(t\) (\(0 \leq t \leq k\)), let \(T \subseteq V\) be the set of colored vertices, \(|T| = t\), and \(\operatorname{col} : T \to \{1, \ldots, r\}\) the coloring. Define the PSD matrix (on \(\operatorname{range}(L)\))

\[
M_t := \sum_{\substack{uv \in E \\ u, v \in T \\ \operatorname{col}(u) = \operatorname{col}(v)}} A_{uv}. \tag{37}
\]

Thus \(M_t\) contains the contributions from edges whose endpoints are already colored and share the same color.

Let \(R := V \setminus T\) be the uncolored vertices, \(m := |R| = n - t\). For \(v \in R\) and \(\gamma \in \{1, \ldots, r\}\) define the prospective increment obtained by coloring \(v\) with \(\gamma\):

\[
B_v^\gamma := \sum_{\substack{u \in T \\ \operatorname{col}(u) = \gamma \\ uv \in E}} A_{uv}. \tag{38}
\]

Then if we color \(v\) with color \(\gamma\), we have \(M_{t+1} = M_t + B_v^\gamma\).

**Step 4: Inductive barrier invariant.** Let \(u_t := u_0 + t\delta\). We maintain the invariant

\[
M_t \prec u_t I \quad \text{and} \quad \Phi_{u_t}(M_t) \leq \Phi_{u_0}(0) = \frac{d}{u_0}. \tag{39}
\]

This holds at \(t = 0\) since \(M_0 = 0\).

Assume it holds for some \(t < k\). Set \(u = u_t\), \(u' = u_{t+1} = u_t + \delta\), and

\[
U := (u'I - M_t)^{-1}.
\]

We claim there exists a choice of \((v, \gamma) \in R \times \{1, \ldots, r\}\) for which the barrier condition (34) holds with \(M = M_t\) and \(B = B_v^\gamma\).

Consider the average over a uniformly random pair \((v, \gamma)\):

\[
\frac{1}{mr} \sum_{v \in R} \sum_{\gamma=1}^{r} \left[ \operatorname{tr}(B_v^\gamma U) + \frac{\operatorname{tr}(B_v^\gamma U^2)}{\Phi_u(M_t) - \Phi_{u'}(M_t)} \right]. \tag{40}
\]

Observe that

\[
\sum_{v \in R} \sum_{\gamma=1}^{r} B_v^\gamma = \sum_{\substack{uv \in E \\ u \in T,\, v \in R}} A_{uv} \preceq \sum_{e \in E} A_e = I \quad \text{on } \operatorname{range}(L),
\]

because the left-hand side is a sub-sum of the PSD matrices \(\{A_e\}\) in (31). If \(X \preceq Y\) and \(C \succeq 0\), then \(\operatorname{tr}(XC) \leq \operatorname{tr}(YC)\) because \(\operatorname{tr}(C^{1/2}(Y - X)C^{1/2}) \geq 0\). Applying this observation with \(C = U\) and with \(C = U^2\) (both positive semidefinite) we get

\[
\sum_{v, \gamma} \operatorname{tr}(B_v^\gamma U) \leq \operatorname{tr}(U), \quad \sum_{v, \gamma} \operatorname{tr}(B_v^\gamma U^2) \leq \operatorname{tr}(U^2).
\]

Therefore (40) is at most

\[
\frac{\operatorname{tr}(U)}{mr} + \frac{\operatorname{tr}(U^2)}{mr\bigl(\Phi_u(M_t) - \Phi_{u'}(M_t)\bigr)}. \tag{41}
\]

By the inductive hypothesis, \(\operatorname{tr}(U) = \Phi_{u'}(M_t) \leq \Phi_u(M_t) \leq d/u_0\); the middle inequality uses that, for fixed \(M_t\), the function \(s \mapsto \Phi_s(M_t)\) decreases as the barrier level \(s\) increases. By (35),

\[
\Phi_u(M_t) - \Phi_{u'}(M_t) \geq \delta \operatorname{tr}(U^2),
\]

so (in the non-trivial case \(d > 0\), where \(\operatorname{tr}(U^2) > 0\)) the second term in (41) is at most \(1/(\delta mr)\). Hence the average (40) is at most

\[
\frac{d/u_0}{mr} + \frac{1}{\delta mr}. \tag{42}
\]

As long as \(t < k = \lfloor n/4 \rfloor\), we have \(m = n - t \geq 3n/4\) and \(d \leq n\). Using the choices (36), we bound

\[
\frac{d/u_0}{mr} \leq \frac{n/(\varepsilon/2)}{(3n/4) \cdot (16/\varepsilon)} = \frac{1}{6}, \quad \frac{1}{\delta mr} \leq \frac{1}{(\varepsilon/n) \cdot (3n/4) \cdot (16/\varepsilon)} = \frac{1}{12},
\]

so the average (42) is \(< 1\). Therefore there exists at least one pair \((v, \gamma)\) for which (34) holds. Applying Lemma 6.1 yields

\[
M_{t+1} \prec u_{t+1} I \quad \text{and} \quad \Phi_{u_{t+1}}(M_{t+1}) \leq \Phi_{u_t}(M_t) \leq \frac{d}{u_0}.
\]

Thus the invariant (39) propagates to \(t + 1\), completing the induction for \(t = 0, 1, \ldots, k\).

**Step 5: Extracting a large \(\varepsilon\)-light set.** After \(k\) steps, the colored set \(T\) (with \(|T| = k\)) is partitioned into \(r\) color classes \(S_1, \ldots, S_r\). By definition of \(M_k\),

\[
M_k = \sum_{a=1}^{r} \sum_{uv \in E(S_a, S_a)} A_{uv} = \sum_{a=1}^{r} L^{-1/2} L_{S_a} L^{-1/2} \quad \text{on } \operatorname{range}(L).
\]

From the invariant, \(M_k \preceq u_k I\) with \(u_k = u_0 + k\delta \leq \varepsilon/2 + \varepsilon/4 = 3\varepsilon/4\). Since each summand is PSD, each is dominated by the sum. Let \(S\) be the largest color class. Then

\[
L^{-1/2} L_S L^{-1/2} \preceq M_k \preceq \frac{3\varepsilon}{4}\, I \preceq \varepsilon I \quad \text{on } \operatorname{range}(L).
\]

As explained in Step 1, this implies \(L_S \preceq \varepsilon L\), i.e. \(\varepsilon L - L_S \succeq 0\), so \(S\) is \(\varepsilon\)-light.

**Step 6: Size lower bound.** Among the \(k\) colored vertices, the largest color class has size at least \(k/r\). If \(n \geq 4\), then \(k = \lfloor n/4 \rfloor \geq n/8\). Also,

\[
r = \left\lceil \frac{16}{\varepsilon} \right\rceil \leq \frac{16}{\varepsilon} + 1 \leq \frac{32}{\varepsilon}.
\]

Hence

\[
|S| \geq \frac{k}{r} \geq \frac{n/8}{32/\varepsilon} = \frac{\varepsilon n}{256}.
\]

The construction above was used only under the standing assumptions made at the beginning (in particular that the graph has at least one edge). If the graph is edgeless, taking \(S = V\) is trivially \(\varepsilon\)-light. It remains to look at small values of \(n\): for \(1 \leq n \leq 3\) any single vertex set \(S = \{v\}\) has \(L_S = 0\) and hence is \(\varepsilon\)-light, and it satisfies \(|S| = 1 \geq \varepsilon n/256\) because \(\varepsilon \leq 1\). The cases \(n = 0\) or \(\varepsilon = 0\) were disposed of at the start. Thus in all cases there exists an \(\varepsilon\)-light set \(S\) with

\[
|S| \geq \frac{\varepsilon}{256}\,|V|.
\]

This proves the statement with the universal constant \(c = 1/256\).

### References

[1] J. Batson, D. A. Spielman and N. Srivastava, *Twice-Ramanujan sparsifiers*, SIAM Journal on Computing **41** (2012), no. 6, 1704--1721.
