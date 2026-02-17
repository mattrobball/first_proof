# Grading Transcript

- Problem: `8`
- Attempt: `oai8`
- Started (UTC): `2026-02-17T19:01:49.024020+00:00`
- Finished (UTC): `2026-02-17T19:09:32.702565+00:00`
- Grade: **3/4** (Substantial Progress (nearly complete))

## Question

A polyhedral Lagrangian surface $K$ in $\mathbb{R}^4$ is a finite polyhedral complex all of whose faces are Lagrangians, and which is a topological submanifold of $\mathbb{R}^4$. A Lagrangian smoothing of $K$ is a Hamiltonian isotopy $K_t$ of smooth Lagrangian submanifolds, parameterised by $(0,1]$, extending to a topological isotopy, parametrised by $[0,1]$, with endpoint $K_0 = K$.


Let $K$ be a polyhedral Lagrangian surface with the property that exactly $4$ faces meet at every vertex. Does $K$ necessarily have a Lagrangian smoothing?

## Solution Attempt

## 8 Quadrivalent polyhedral Lagrangian surfaces are Lagrangian-smoothable

**Problem**

A polyhedral Lagrangian surface \(K\) in \(\mathbb{R}^4\) is a finite polyhedral complex all of whose faces are Lagrangians, and which is a topological submanifold of \(\mathbb{R}^4\). A Lagrangian smoothing of \(K\) is a Hamiltonian isotopy \(K_t\) of smooth Lagrangian submanifolds, parameterised by \((0,1]\), extending to a topological isotopy, parametrised by \([0,1]\), with endpoint \(K_0 = K\).

Let \(K\) be a polyhedral Lagrangian surface with the property that exactly 4 faces meet at every vertex. Does \(K\) necessarily have a Lagrangian smoothing?

**Solution**

Yes. We construct explicit local smoothing models at each vertex and each edge, glue these models into \(K\) inside pairwise disjoint *affine symplectic* (hence Darboux) neighborhoods chosen compatibly from the outset, and then verify that the resulting Lagrangian isotopy has vanishing flux and hence is Hamiltonian.

**0. Conventions and standing hypotheses.**

*Symplectic conventions.* Work in \((\mathbb{R}^4, \omega)\) with \(\omega\) exact. Fix once and for all a global primitive

\[
\lambda := p_1 \, dq_1 + p_2 \, dq_2
\]

in some fixed global Darboux coordinates \((q_1, q_2, p_1, p_2)\), so \(d\lambda = \omega\). In these coordinates

\[
\omega = dp_1 \wedge dq_1 + dp_2 \wedge dq_2, \qquad \omega(\partial_{p_i}, \partial_{q_j}) = \delta_{ij}, \qquad \omega(\partial_{q_i}, \partial_{p_j}) = -\delta_{ij}.
\]

We use the Hamiltonian convention

\[
\iota_{X_H} \omega = -dH. \tag{52}
\]

(With \(\omega = \sum dp_i \wedge dq_i\), this is the convention giving Hamilton's equations \(\dot{q}_i = \partial H / \partial p_i\) and \(\dot{p}_i = -\partial H / \partial q_i\).)

If \(\lambda_{\mathrm{std}}\) denotes the standard primitive in some other Darboux chart, then \(\lambda_{\mathrm{std}} - \lambda\) is a closed 1-form on \(\mathbb{R}^4\) and hence exact. Thus, whenever we work in a local Darboux chart, we will freely replace the local primitive by adding an exact correction term so that all computations ultimately refer to the same fixed global \(\lambda\).

*Polyhedral hypotheses.* We make explicit the local cell-structure properties used below.

- \(K \subset \mathbb{R}^4\) is a compact (or, more generally, properly embedded) topological 2-manifold *without boundary*.

- \(K\) is given a *face-to-face* finite polyhedral structure: each 2-cell is a compact convex polygon contained in an affine Lagrangian plane, and the intersection of any two cells is a (possibly empty) common face of each.

- Every vertex is *quadrivalent*: exactly four 2-faces meet at each vertex (equivalently, the link of each vertex in \(K\) is a 4-cycle).

Under these hypotheses, each point of the interior of an edge has a neighborhood in \(K\) homeomorphic to a disk and modeled by exactly two faces meeting along that edge (no "branching" along edges). Likewise, at a vertex, the four incident faces appear as four planar sectors meeting cyclically.

**1. Linear normal form at a quadrivalent vertex, including all sign patterns.**

Let \(x\) be a vertex of \(K\), and let \(l_1, l_2, l_3, l_4\) be the four oriented edge rays emanating from \(x\), numbered in cyclic order in the link. Let

\[
P_i := \langle l_i, l_{i+1} \rangle \qquad (i \bmod 4)
\]

denote the affine Lagrangian planes of the four incident faces (after translating \(x\) to the origin we identify these planes with linear Lagrangian subspaces). Each incident face is a planar sector in \(P_i\) bounded by \(l_i\) and \(l_{i+1}\).

**Lemma 8.1** (Eliminating coplanar adjacencies). *Let \(K \subset (\mathbb{R}^4, \omega)\) be a polyhedral Lagrangian surface, and let \(x\) be a vertex with emanating rays \(l_1, l_2, l_3, l_4\) in cyclic order, and \(P_i = \langle l_i, l_{i+1} \rangle\) as above.*

*Assume that two adjacent faces are coplanar, i.e. \(P_i = P_{i+1}\) for some \(i\). Then \(x\) is not a genuine quadrivalent singularity of the underlying embedded surface \(K\): after a cyclic relabeling (so \(P_1 = P_2\)), exactly one of the following holds.*

*(a) \(P_1 = P_2 = P_3 = P_4\) (so \(x\) is a smooth point of \(K\)).*

*(b) \(l_1\) and \(l_3\) are collinear (opposite rays on a line \(\ell\)) and \(P_3 = P_4\) (so \(x\) lies in the interior of a geometric edge of \(K\)).*

*Consequently, since the existence of a Lagrangian smoothing depends only on the subset \(K\) and not on the chosen polyhedral structure, one may, without loss of generality, discard such inessential vertices and assume in the vertex analysis that no two adjacent faces are coplanar.*

**Proof.** By cyclic relabeling assume \(P_1 = P_2 =: L\). Choose nonzero vectors \(v_i \in l_i\). Then \(v_1, v_2, v_3 \in L\).

First suppose that \(v_1\) and \(v_3\) are linearly independent. Then \(L = \langle v_1, v_3 \rangle\). Since \(P_4 = \langle v_4, v_1 \rangle\) is Lagrangian, \(\omega(v_4, v_1) = 0\), and since \(P_3 = \langle v_3, v_4 \rangle\) is Lagrangian, \(\omega(v_4, v_3) = 0\). Hence \(v_4\) is \(\omega\)-orthogonal to \(\langle v_1, v_3 \rangle = L\), i.e. \(v_4 \in L^\omega\). Because \(L\) is Lagrangian, \(L^\omega = L\), so \(v_4 \in L\). It follows that \(P_3 = \langle v_3, v_4 \rangle \subset L\) and \(P_4 = \langle v_4, v_1 \rangle \subset L\), hence \(P_3 = P_4 = L\), proving (a). Since \(K\) is a topological 2-manifold and lies in the affine plane \(L\) near \(x\), \(x\) is a smooth point.

Now suppose that \(v_1\) and \(v_3\) are linearly dependent. Then \(l_1\) and \(l_3\) are collinear, hence opposite rays on a common line \(\ell\). Therefore

\[
P_3 = \langle l_3, l_4 \rangle = \langle \ell, l_4 \rangle = \langle l_1, l_4 \rangle = P_4,
\]

proving (b). The union of the two coplanar faces in \(P_1 = P_2\) is a polyhedral half-plane in \(P_1\) bounded by \(\ell\), and similarly the union of the two coplanar faces in \(P_3 = P_4\) is a half-plane in \(P_3\) bounded by \(\ell\). Thus the germ at \(x\) is an "edge wedge" and \(x\) is an interior point of that geometric edge.

In either case \(x\) is inessential as a vertex and may be removed from the polyhedral structure without changing the subset \(K\). \(\square\)

Henceforth assume *no two adjacent faces are coplanar*. Fix nonzero vectors \(v_i \in l_i\). Then \(v_3 \notin \langle v_1, v_2 \rangle\), so

\[
\dim \langle v_1, v_2, v_3, v_4 \rangle \geq 3. \tag{53}
\]

Because each \(P_i\) is Lagrangian, we have

\[
\omega(v_1, v_2) = \omega(v_2, v_3) = \omega(v_3, v_4) = \omega(v_4, v_1) = 0.
\]

Thus the only potentially nonzero pairings among the \(v_i\) are \(\omega(v_1, v_3)\) and \(\omega(v_2, v_4)\). If both were zero, then \(\omega\) would vanish on \(\langle v_1, v_2, v_3, v_4 \rangle\), making it isotropic of dimension \(\geq 3\), impossible in a symplectic 4-space. Hence at least one of \(\omega(v_1, v_3)\) or \(\omega(v_2, v_4)\) is nonzero; after a cyclic relabeling we may assume

\[
\omega(v_1, v_3) \neq 0. \tag{54}
\]

*Transversality of opposite planes.* Under the standing hypothesis that no adjacent faces are coplanar, the opposite planes \(P_1 = \langle v_1, v_2 \rangle\) and \(P_3 = \langle v_3, v_4 \rangle\) are transverse. Indeed, if \(P_1 \cap P_3 \neq \{0\}\) then there exists \(0 \neq w = av_3 + bv_4 \in P_1\). Pairing with \(v_1\) gives

\[
0 = \omega(v_1, w) = a\,\omega(v_1, v_3) + b\,\omega(v_1, v_4) = a\,\omega(v_1, v_3),
\]

since \(\omega(v_1, v_4) = 0\) (adjacent in the cyclic order). Thus \(a = 0\) and \(w = bv_4 \in P_1\), so \(v_4 \in P_1\) and hence \(P_4 = \langle v_4, v_1 \rangle \subset P_1\), i.e. \(P_4\) and \(P_1\) are coplanar, contradiction. Therefore \(P_1 \cap P_3 = \{0\}\).

Since \(P_1\) and \(P_3\) are transverse Lagrangian planes, \(\omega\) induces a nondegenerate pairing

\[
\omega|_{P_3 \times P_1} : P_3 \times P_1 \to \mathbb{R}, \qquad (w, u) \mapsto \omega(w, u),
\]

because if \(w \in P_3\) pairs trivially with all \(u \in P_1\), then \(w \in P_1^\omega = P_1\), hence \(w = 0\).

*Vertex Darboux coordinates and sign pattern.* Choose a basis \(e_1 = v_1\), \(e_2 = v_2\) of \(P_1\). Let \(f^1, f^2\) be the \(\omega\)-dual basis of \(P_3\) with respect to the pairing \(\omega|_{P_3 \times P_1}\), i.e.

\[
\omega(f^j, e_i) = \delta^j_i. \tag{55}
\]

Write

\[
v_3 = a_1 f^1 + a_2 f^2, \qquad v_4 = b_1 f^1 + b_2 f^2.
\]

Because \(P_2 = \langle v_2, v_3 \rangle\) is Lagrangian, \(\omega(v_2, v_3) = 0\). Using \(\omega(e_2, f^1) = -\omega(f^1, e_2) = 0\) and \(\omega(e_2, f^2) = -\omega(f^2, e_2) = -1\), we obtain

\[
0 = \omega(v_2, v_3) = a_1 \,\omega(e_2, f^1) + a_2 \,\omega(e_2, f^2) = -a_2,
\]

so \(a_2 = 0\) and hence \(v_3 = a_1 f^1\). Similarly, since \(P_4 = \langle v_4, v_1 \rangle\) is Lagrangian we have \(\omega(v_1, v_4) = 0\), and using \(\omega(e_1, f^1) = -1\) and \(\omega(e_1, f^2) = 0\) we get \(b_1 = 0\), hence \(v_4 = b_2 f^2\).

Thus \(v_3\) is a nonzero scalar multiple of \(f^1\) and \(v_4\) is a nonzero scalar multiple of \(f^2\). Define the *vertex sign pattern*

\[
\sigma_1 := \operatorname{sign}(a_1) \in \{\pm 1\}, \qquad \sigma_2 := \operatorname{sign}(b_2) \in \{\pm 1\}. \tag{56}
\]

These signs are determined by the oriented rays \(l_3\) and \(l_4\) and *cannot* be changed by rescaling rays, since only positive rescalings of half-lines are allowed.

Rescale \(v_3\) and \(v_4\) by positive factors so that \(v_3 = \sigma_1 f^1\) and \(v_4 = \sigma_2 f^2\). Let \((q_1, q_2, p_1, p_2)\) be the linear symplectic coordinate system determined by declaring

\[
e_i = \partial_{q_i}, \qquad f^i = \partial_{p_i},
\]

so \(\omega = dp_1 \wedge dq_1 + dp_2 \wedge dq_2\) and \(\lambda_{\mathrm{std}} = p_1 \, dq_1 + p_2 \, dq_2\) in these coordinates. Then the four rays take the signed standard form

\[
l_1 = \mathbb{R}_+ \,\partial_{q_1}, \quad l_2 = \mathbb{R}_+ \,\partial_{q_2}, \quad l_3 = \mathbb{R}_+ (\sigma_1 \partial_{p_1}), \quad l_4 = \mathbb{R}_+ (\sigma_2 \partial_{p_2}). \tag{57}
\]

In particular, there are *four* possible sign patterns \((\sigma_1, \sigma_2) \in \{\pm 1\}^2\) at a vertex.

Since each face is a planar sector bounded by the corresponding rays, after shrinking to a small ball around \(x\) (and identifying it with its image under this affine symplectomorphism) the polyhedral *star* of \(x\) is the Lagrangian cone

\[
(u, v) \longmapsto \bigl(u^+,\, v^+,\, \sigma_1(-u)^+,\, \sigma_2(-v)^+\bigr), \qquad s^+ := \max\{s, 0\}. \tag{58}
\]

This is the only place where the "four faces at each vertex" hypothesis is used.

**2. A one-dimensional rounded corner of zero action (with a genuine construction).**

We work first in the symplectic plane \((\mathbb{R}^2_{(q,p)},\, dp \wedge dq)\), compatible with the global convention, and we use the Liouville form \(\lambda_{(q,p)} := p\,dq\) (so \(d\lambda_{(q,p)} = dp \wedge dq\)).

**Lemma 8.2** (Embedded rounding with prescribed jets and zero Liouville action). *There exists a smooth embedded curve*

\[
\bar{\gamma} : \mathbb{R} \to \mathbb{R}^2_{(q,p)}, \qquad r \mapsto (\bar{q}(r), \bar{p}(r))
\]

*such that:*

1. *\(\bar{\gamma}(r) = (0, -r)\) for all \(r \leq -2\), and \(\bar{\gamma}(r) = (r, 0)\) for all \(r \geq 2\);*
2. *\(\bar{\gamma}\) agrees identically with these half-axes on open neighborhoods of \((-\infty, -2]\) and \([2, \infty)\) (hence all jets match at \(r = \pm 2\));*
3. *\(\bar{\gamma}\) is embedded;*
4. *its Liouville action is zero:*

\[
\int_{-\infty}^{\infty} \bar{p}(r)\,\bar{q}'(r)\,dr = 0. \tag{59}
\]

**Proof.** Step 1: choose a base rounding with good geometry. Choose once and for all a small number, say \(\eta = 1/4\). We first construct a smooth non-decreasing function \(\bar{q} : \mathbb{R} \to [0, \infty)\) such that

\[
\bar{q}(r) = 0 \text{ for } r \leq -2 + \eta, \qquad \bar{q}(r) = r \text{ for } r \geq 2 - \eta, \qquad \bar{q}'(r) > 0 \text{ for } -2 + \eta < r < 2 - \eta.
\]

(The function may be chosen flat to infinite order at the two points where it starts and where it joins the line \(r\).) In particular the identities required in (1) hold, and the stronger equalities on the slightly larger intervals give the "open neighbourhood" property (2).

Next choose a smooth function \(\bar{p}_0 : \mathbb{R} \to \mathbb{R}\) such that

\[
\bar{p}_0(r) = -r \text{ for } r \leq -2 + \eta, \qquad \bar{p}_0(r) = 0 \text{ for } r \geq 2 - \eta,
\]

and \(\bar{p}_0(r) > 0\) on the intermediate interval \((-2 + \eta, 2 - \eta)\). Then the curve \(\bar{\gamma}_0(r) := (\bar{q}(r), \bar{p}_0(r))\) is embedded: on the incoming axial neighbourhood it lies on the positive \(p\)-axis and on the outgoing neighbourhood on the positive \(q\)-axis, while on the middle interval it is a graph over the strictly increasing \(q\)-coordinate and hence has no self-intersections (nor does it meet the axial pieces except at the transition endpoints).

Let

\[
A_0 := \int_{-\infty}^{\infty} \bar{p}_0(r)\,\bar{q}'(r)\,dr
\]

(the integral converges because the product \(\bar{p}_0\,\bar{q}'\) is supported in the compact interval \([-2 + \eta, 2 - \eta]\)).

Step 2: adjust the action by a compactly supported vertical perturbation. Choose a nonzero smooth bump function \(\phi : \mathbb{R} \to \mathbb{R}\) supported in \((-1, 1)\) (so \(\phi\) vanishes identically near \(\pm 2\)), and set

\[
c := \int_{-\infty}^{\infty} \phi(r)\,\bar{q}'(r)\,dr.
\]

Since \(\bar{q}'(r) > 0\) throughout the support interval \((-1, 1)\) (by our choice of \(\eta = 1/4\)) and \(\phi\) is not identically zero, we can choose \(\phi\) so that \(c \neq 0\) (e.g. take \(\phi \geq 0\), not identically zero).

For \(s \in \mathbb{R}\) define

\[
\bar{p}_s(r) := \bar{p}_0(r) + s\,\phi(r), \qquad \bar{\gamma}_s(r) := (\bar{q}(r), \bar{p}_s(r)).
\]

Then \(\bar{\gamma}_s\) agrees with \(\bar{\gamma}_0\) (hence with the prescribed half-axes) for \(|r| \geq 1\), so the jets at \(r = \pm 2\) are unchanged. Moreover, the perturbation is supported in \((-1, 1) \subset (-2 + \eta, 2 - \eta)\) where the \(q\)-coordinate is strictly increasing, so for every \(s\) the curve remains a graph over \(q\) on the only region that changes and hence stays embedded.

Finally, the action depends affinely on \(s\):

\[
\int \bar{p}_s\,\bar{q}'\,dr = \int \bar{p}_0\,\bar{q}'\,dr + s \int \phi\,\bar{q}'\,dr = A_0 + s\,c.
\]

Choose \(s_* := -A_0/c\). Then \(\bar{\gamma} := \bar{\gamma}_{s_*}\) satisfies (59) and has all required properties. \(\square\)

Fix such a curve \(\bar{\gamma}(r) = (\bar{q}(r), \bar{p}(r))\) once and for all. For \(\varepsilon > 0\) define the rescaled curve \(\gamma_\varepsilon(r) = (q_\varepsilon(r), p_\varepsilon(r))\) by

\[
q_\varepsilon(r) = \varepsilon\,\bar{q}(r/\varepsilon), \qquad p_\varepsilon(r) = \varepsilon\,\bar{p}(r/\varepsilon), \tag{60}
\]

and define the \(\varepsilon = 0\) limit to be the union of half-axes

\[
q_0(r) = r^+, \qquad p_0(r) = (-r)^+.
\]

Then for each \(\varepsilon > 0\), \(\gamma_\varepsilon\) is smooth and embedded, equals the coordinate half-axes for \(|r| \geq 2\varepsilon\), and all derivatives match at the transition points \(r = \pm 2\varepsilon\) (because \(\bar{\gamma}\) was chosen to agree identically with axes near \(\pm 2\)).

Define

\[
F_\varepsilon(r) := \int_{-\infty}^{r} p_\varepsilon(s)\,q_\varepsilon'(s)\,ds. \tag{61}
\]

By construction and (59), choosing the integration constant so that \(F_\varepsilon\) vanishes along the incoming axis, we have

\[
F_\varepsilon(r) = 0 \quad \text{whenever} \quad \gamma_\varepsilon(r) \text{ lies on either coordinate axis.} \tag{62}
\]

**3. Vertex smoothing model (with the vertex sign pattern).**

Fix a vertex \(x\) and its Darboux coordinates (57) with sign pattern \((\sigma_1, \sigma_2)\). For \(\varepsilon > 0\) define the product map

\[
\Phi_\varepsilon^{(\sigma_1, \sigma_2)} : \mathbb{R}^2_{(u,v)} \to \mathbb{R}^4, \qquad \Phi_\varepsilon^{(\sigma_1, \sigma_2)}(u,v) = \bigl(q_\varepsilon(u),\, q_\varepsilon(v),\, \sigma_1 p_\varepsilon(u),\, \sigma_2 p_\varepsilon(v)\bigr). \tag{63}
\]

This is an embedding (product of embeddings). With \(\lambda_{\mathrm{std}} = p_1\,dq_1 + p_2\,dq_2\) in these vertex coordinates,

\[
\bigl(\Phi_\varepsilon^{(\sigma_1, \sigma_2)}\bigr)^* \lambda_{\mathrm{std}} = \sigma_1 p_\varepsilon(u)\,q_\varepsilon'(u)\,du + \sigma_2 p_\varepsilon(v)\,q_\varepsilon'(v)\,dv = d\bigl(\sigma_1 F_\varepsilon(u) + \sigma_2 F_\varepsilon(v)\bigr). \tag{64}
\]

Hence \(\Phi_\varepsilon^{(\sigma_1, \sigma_2)}\) parametrizes an *exact* Lagrangian surface.

Moreover, for \(|u| \geq 2\varepsilon\) the \(u\)-factor is already in the axial regime so \(F_\varepsilon(u) = 0\) and (64) restricts to \(\sigma_2\,dF_\varepsilon(v)\), which will match the primitive on the corresponding edge strip. If both \(|u| \geq 2\varepsilon\) and \(|v| \geq 2\varepsilon\) then the primitive vanishes identically. As \(\varepsilon \to 0\), \(\Phi_\varepsilon^{(\sigma_1, \sigma_2)}\) converges uniformly on compact sets to the signed cone (58).

To use this as a local replacement near \(x\) we shall not fix the parameter domain once for all at this point. After the edge charts have been chosen (Step 4) we take a small polyhedral ball \(U_x\) in the above affine coordinates and we let \(D_x\) be the inverse image, in the cone parametrisation (58), of \(K \cap U_x\). The boundary of this set is then rounded slightly in the parameter plane. What will be important for the gluing is the following elementary property, which we impose by shrinking \(U_x\) and by choosing the rounding in collars. There is a collar of \(\partial D_x\) which, for the fixed scale \(\varepsilon_0\), lies in the union of the axial regions \(\{|u| \geq 2\varepsilon_0\}\) and \(\{|v| \geq 2\varepsilon_0\}\); moreover the portions of the boundary that do not belong to the planned overlaps with edge strips lie where both inequalities hold. On such collars the parametrization is literally planar (in fact affine linear) and all jets match the adjoining pieces. In particular only a small neighbourhood of the corner, not the whole product surface, is inserted into \(K\). Notice that \(D_x\) need not be a rectangle: on the collars which will overlap an edge its boundary may be a graph in the other variable. This harmless flexibility will be used below in order that the vertex and edge images coincide as subsets of \(\mathbb{R}^4\).

**4. Edge normal form and an edge smoothing model compatible with vertices, including edge signs.**

*Linear normal form along an edge, with sign.* Let \(P, P' \subset \mathbb{R}^4\) be Lagrangian planes meeting along a line \(\ell = P \cap P'\). Choose \(0 \neq e \in \ell\). Choose \(a \in P \setminus \ell\) and \(b \in P' \setminus \ell\) pointing to the prescribed inward sides of the corresponding faces (these choices are well-defined up to positive scaling). Then \(\omega(b, a) \neq 0\), for otherwise \(\langle e, a, b \rangle\) would be a 3-dimensional isotropic subspace, impossible in \((\mathbb{R}^4, \omega)\). Define

\[
\varepsilon(P, P'; a, b) := \operatorname{sign}\bigl(\omega(b, a)\bigr) \in \{\pm 1\}.
\]

By positive rescaling of \(a\) and/or \(b\), we may and do assume

\[
\omega(b, a) = \varepsilon(P, P'; a, b) \in \{\pm 1\}. \tag{65}
\]

Choose \(f \in \mathbb{R}^4\) such that

\[
\omega(f, e) = 1, \qquad \omega(f, a) = 0, \qquad \omega(f, b) = 0. \tag{66}
\]

The three vectors \(e, a, b\) are linearly independent. Indeed, if (say) \(b\) belonged to the span of \(e\) and \(a\), then the two incident faces would lie in the same affine Lagrangian plane and the edge would be inessential; alternatively this would contradict the preceding non-isotropy argument. The non-degeneracy of \(\omega\) identifies \(\mathbb{R}^4\) with its dual. Prescribing the values in (66) on the independent subspace \(\langle e, a, b \rangle\) and extending them arbitrarily to a covector on all of \(\mathbb{R}^4\) therefore gives a solution \(f\); any two such solutions differ by a multiple of the common line \(\langle e \rangle = (\langle e, a, b \rangle)^\omega\), and all of them will serve our purpose. Since a vector in the span of \(e, a, b\) pairs trivially with \(e\), no solution lies in that span, so \((e, a, f, b)\) is automatically a basis. With this choice the only non-zero pairings among the ordered quadruple are

\[
\omega(f, e) = 1, \qquad \omega(\varepsilon^{-1} b, a) = 1
\]

(up to skew-symmetry). This is precisely the symplectic normal form stated below.

In the associated affine symplectic coordinates

\[
(x, y, p_x, p_y) \tag{67}
\]

defined by

\[
e = \partial_x, \quad a = \partial_y, \quad f = \partial_{p_x}, \quad b = \varepsilon\,\partial_{p_y} \qquad (\varepsilon := \varepsilon(P, P'; a, b)),
\]

we have \(\omega = dp_x \wedge dx + dp_y \wedge dy\) and \(\lambda_{\mathrm{std}} = p_x\,dx + p_y\,dy\), and the two incident half-planes take the standard signed form

\[
\{p_x = p_y = 0,\ y \geq 0\} \quad \text{and} \quad \{p_x = 0,\ y = 0,\ \varepsilon\,p_y \geq 0\}. \tag{68}
\]

(When \(\varepsilon = +1\) the second half-plane is \(p_y \geq 0\); when \(\varepsilon = -1\) it is \(p_y \leq 0\).)

*Edge data and scale functions.* Fix a geometric edge \(e\) of \(K\) with endpoints \(x_-\) and \(x_+\). Let \(P_e\) and \(P_e'\) be the two Lagrangian face planes containing \(e\), and let \(\ell_e = P_e \cap P_e'\) be the edge line.

Choose a nonzero tangent vector \(e_e \in \ell_e\) pointing along the edge (any choice is fine; it only affects the parametrization along the edge, not the subset we construct). Choose inward-pointing transverse vectors \(a_e \in P_e \setminus \ell_e\) and \(b_e \in P_e' \setminus \ell_e\), and normalize them by (65); denote the resulting sign by

\[
\varepsilon_e := \operatorname{sign}\bigl(\omega(b_e, a_e)\bigr) \in \{\pm 1\}, \qquad \omega(b_e, a_e) = \varepsilon_e. \tag{69}
\]

Choose \(f_e\) satisfying (66) for \((e, a, b) = (e_e, a_e, b_e)\) and define the associated affine symplectic coordinates (67) on a tubular neighborhood \(U_e\) of the interior of \(e\) (and, after shrinking \(U_e\), also on endpoint collars inside \(U_e\)). In these coordinates \(K \cap U_e\) is exactly the wedge (68).

Recall that in Step 1 the non-zero vectors chosen on the vertex rays were arbitrary up to positive scale. We now fix those choices once and for all. Thus, at each endpoint \(x_\pm\), when the face \(P_e\) is the one spanned by the edge under consideration and its adjacent ray, we take as representative of that adjacent ray exactly the vector used in the vertex Darboux coordinates. Since it points into the same inward half-plane as \(a_e\) it can be written

\[
v_{\mathrm{adj},\pm} = \kappa_\pm\, a_e + \alpha_\pm\, e_e, \tag{70}
\]

with \(\kappa_\pm > 0\). In the vertex normal form at \(x_\pm\) we take the basis vector \(e_2\) to be precisely this representative. The construction of the symplectically dual basis in Step 1 then fixes a representative of the adjacent ray in the other face \(P_e'\): it is the unique positive multiple for which the pairing with \(v_{\mathrm{adj},\pm}\) has absolute value 1. Using the normalization \(\omega(b_e, a_e) = \varepsilon_e = \pm 1\) (and the fact that the pairings with the tangent direction \(e_e\) vanish), this representative has the expression

\[
v'_{\mathrm{adj},\pm} = \kappa_\pm^{-1}\, b_e + \beta_\pm\, e_e, \tag{71}
\]

for some \(\beta_\pm \in \mathbb{R}\). Thus no extra sign is hidden in the coefficients: all \(\kappa_\pm\) are *positive* and the only sign information of the wedge is carried by \(\varepsilon_e\). (The equality of the sign \(\varepsilon_e\) with the vertex sign used below is checked explicitly in the compatibility argument.)

Choose a smooth function \(\kappa_e(s) > 0\) of the edge coordinate \(s = x\) such that \(\kappa_e(s) = \kappa_-\) on a collar near \(x_-\) and \(\kappa_e(s) = \kappa_+\) on a collar near \(x_+\).

*Edge smoothing strip (including the edge sign).* Define

\[
\Psi_{\varepsilon,e}(s, r) = \Bigl(s,\ \kappa_e(s)\,q_\varepsilon(r),\ -\varepsilon_e\,\frac{\kappa_e'(s)}{\kappa_e(s)}\,p_\varepsilon(r)\,q_\varepsilon(r),\ \varepsilon_e\,\kappa_e(s)^{-1}\,p_\varepsilon(r)\Bigr), \tag{72}
\]

defined on a finite strip \((s, r) \in I_e \times [-R_e, R_e]\) inside the chosen tube \(U_e\) (with \(I_e\) an interval parameterizing the portion of the edge we modify, and \(R_e\) chosen so that the axial regime already holds on the boundary \(|r| = R_e\) for all \(\varepsilon \leq \varepsilon_0\)).

For all sufficiently small \(\varepsilon\) (and after possibly shrinking the strip once and for all) this parametrization is an embedding. Indeed the vector \(\partial_s \Psi_{\varepsilon,e}\) has \(x\)-component 1 whereas \(\partial_r \Psi_{\varepsilon,e}\) has \(x\)-component 0, so the immersion property reduces to the fact that the rounded curve \(\gamma_\varepsilon\) is a regular embedding in the \((q,p)\)-plane. If two image points have different \(s\)-coordinates they are obviously distinct; for fixed \(s\) the pair \((q_\varepsilon(r), p_\varepsilon(r))\) (and hence also \((\kappa(s)\,q_\varepsilon(r),\, \varepsilon_e\,\kappa(s)^{-1}\,p_\varepsilon(r))\)) determines \(r\) because \(\gamma_\varepsilon\) is embedded, so no self-intersections occur. Finally the corrective \(p_x\)-coordinate in (72) is of size \(O(\varepsilon^2)\) on the support of the rounding; by taking \(\varepsilon_0\) small we ensure that the whole image lies in the prescribed tubular neighbourhood \(U_e\).

With \(\lambda_{\mathrm{std}} = p_x\,dx + p_y\,dy\) in these edge coordinates, a direct computation gives

\[
\Psi_{\varepsilon,e}^* \lambda_{\mathrm{std}} = p_x\,ds + p_y\,dy
= \Bigl(-\varepsilon_e\,\frac{\kappa'}{\kappa}\,p_\varepsilon\,q_\varepsilon\Bigr)\,ds + \bigl(\varepsilon_e\,\kappa^{-1}\,p_\varepsilon\bigr)\bigl(\kappa\,q_\varepsilon'\,dr + \kappa'\,q_\varepsilon\,ds\bigr)
= \varepsilon_e\,p_\varepsilon(r)\,q_\varepsilon'(r)\,dr = d\bigl(\varepsilon_e\,F_\varepsilon(r)\bigr), \tag{73}
\]

so \(\Psi_{\varepsilon,e}\) parametrizes an *exact* Lagrangian strip. The third coordinate in (72) is precisely the correction term ensuring (73) when \(\kappa_e\) varies with \(s\). By (62), the primitive \(\varepsilon_e F_\varepsilon(r)\) vanishes on collars where the strip has already entered the axial regime. When \(\kappa_e\) is constant (near the endpoints), the third coordinate vanishes and the strip is simply a rescaled copy of the one-dimensional rounding (with the correct sign \(\varepsilon_e\) in the \(p_y\)-direction).

*Compatibility with the vertex model on an* ***open*** *collar.* We now make explicit choices ensuring that the vertex and edge charts match on overlaps as *subsets* (and with matching primitives), not merely at the level of tangent cones.

Fix an endpoint \(x\) of the edge \(e\). Choose the vertex Darboux coordinates at \(x\) as in Step 1 so that the edge ray corresponding to \(e\) is

\[
l_1 = \mathbb{R}_+\,\partial_{q_1}
\]

(in particular, the two incident face planes along \(e\) at \(x\) are \(P_1 = \langle \partial_{q_1}, \partial_{q_2} \rangle\) and \(P_4 = \langle \partial_{q_1}, \sigma_2 \partial_{p_2} \rangle\) for the appropriate vertex sign \(\sigma_2\)). In the edge coordinates (67) chosen above, \(e\) is the \(x\)-axis and the same two faces are in the standard position (68) with edge sign \(\varepsilon_e = \operatorname{sign}(\omega(b_e, a_e))\).

At the same time we recall the harmless freedom, noted in Step 1, to rescale a chosen non-zero vector on any ray by a positive constant (and similarly to rescale the tangent vector used to parametrize the edge). One may use this to arrange that the coordinate along the common edge in the vertex chart has the same absolute scale as the edge coordinate---in which case the scale factor \(\rho_x\) below equals 1 at the endpoint. We keep a factor in the formulas to cover the case where no such simultaneous normalization is imposed.

Because both the vertex coordinates and the edge coordinates were chosen to be *affine symplectic* coordinates on \(\mathbb{R}^4\), the transition map between them on the overlap \(U_x \cap U_e\) is the restriction of a *linear* symplectic map (after translating \(x\) to the origin). The requirement that it preserve the two incident Lagrangian planes and the common edge line forces the transition to have a concrete finite-dimensional form. Concretely:

**Lemma 8.3** (Vertex--edge transition normal form on the wedge). *Let \((q_1, q_2, p_1, p_2)\) and \((x, y, p_x, p_y)\) be linear symplectic coordinates on \((\mathbb{R}^4, \omega)\) with*

\[
\omega = dp_1 \wedge dq_1 + dp_2 \wedge dq_2 = dp_x \wedge dx + dp_y \wedge dy.
\]

*Assume that the common edge line is the \(q_1\)-axis in the first coordinates and the \(x\)-axis in the second, and that the two incident Lagrangian planes are*

\[
P_1 = \{p_1 = p_2 = 0\}, \qquad P_4 = \{p_1 = q_2 = 0\}
\]

*in \((q, p)\)-coordinates and*

\[
\{p_x = p_y = 0\}, \qquad \{p_x = y = 0\}
\]

*in \((x, y, p)\)-coordinates. After replacing the symplectic pair \((x, p_x)\) by \((c^{-1}x,\, c\,p_x)\) for some positive constant \(c\) (which leaves the two half-planes in the same normal form), there are numbers \(\delta \in \{\pm 1\}\), \(\kappa > 0\) and \(\alpha, \beta, \gamma \in \mathbb{R}\) such that the coordinate change has the form*

\[
\begin{aligned}
x &= \delta\,q_1 + \alpha\,q_2 + \beta\,p_2 + \gamma\,p_1, \\
y &= \kappa\,q_2 + \delta\,\kappa\,\beta\,p_1, \\
p_x &= \delta\,p_1, \\
p_y &= \kappa^{-1}\,p_2 - \delta\,\alpha\,\kappa^{-1}\,p_1.
\end{aligned} \tag{74}
\]

*Here \(\delta\) records the relative orientation of the two coordinates along the edge (if the positive \(q_1\)-ray is sent to the positive \(x\)-ray then \(\delta = +1\)). In particular, restricting to the union \(P_1 \cup P_4\) (where \(p_1 = 0\)) we obtain the simpler formulas*

\[
x = \delta\,q_1 + \alpha\,q_2 + \beta\,p_2, \qquad y = \kappa\,q_2, \qquad p_y = \kappa^{-1}\,p_2. \tag{75}
\]

**Proof.** We spell out the elementary linear algebra since we shall use the signs below. Let \(T\) be the linear change of coordinates. The conditions that \(T(P_1) = \{p_x = p_y = 0\}\) imply that \(p_x\) and \(p_y\) contain no \(q\)-terms, and the condition that \(T(P_4) = \{p_x = y = 0\}\) implies in addition that \(p_x\) is a non-zero multiple of \(p_1\) and that \(y\) contains no \(q_1\)- or \(p_2\)-term. Thus, before imposing the symplectic equations, we may write

\[
x = Gq_1 + Hq_2 + Ip_1 + Jp_2, \qquad y = Eq_2 + Fp_1,
\]

\[
p_x = Ap_1, \qquad p_y = Cp_1 + Dp_2,
\]

with \(A, G, E \neq 0\). (The coefficient \(G\) has the sign of the orientation with which the edge is parametrised in the two charts.) The equality \(T^*(dp_x \wedge dx + dp_y \wedge dy) = dp_1 \wedge dq_1 + dp_2 \wedge dq_2\) is obtained by a direct comparison of coefficients:

\[
dp_x \wedge dx + dp_y \wedge dy = AG\,dp_1 \wedge dq_1 + (AH + CE)\,dp_1 \wedge dq_2 + (AJ - DF)\,dp_1 \wedge dp_2 + DE\,dp_2 \wedge dq_2.
\]

Hence

\[
AG = 1, \qquad AH + CE = 0, \qquad AJ - DF = 0, \qquad DE = 1. \tag{76}
\]

We are still free to rescale the *edge* symplectic coordinates by a positive constant, \(x \mapsto x/|G|\), \(p_x \mapsto |G|\,p_x\) (leaving \(y, p_y\) fixed). This preserves the normal form of the two half-planes and replaces \(G\) by \(\delta := \operatorname{sign}(G)\). By the first equation in (76) the same operation then gives \(A = \delta\). The sign of \(E\) records whether the inward half-line in the vertex face is sent to the inward half-line in the edge chart. With our choices it is positive, and we put \(\kappa := E\). Set \(\alpha := H\), \(\beta := J\), \(\gamma := I\), and use the remaining equations in (76) to solve for \(C\) and \(F\). We obtain precisely (74). Formula (75) is the restriction to \(p_1 = 0\). \(\square\)

Return to the geometric situation at the endpoint \(x\) of the edge \(e\). Let \(s_x \in \mathbb{R}\), \(\delta_x \in \{\pm 1\}\), a positive scale \(\rho_x > 0\), and \(\kappa_x > 0\), \(\alpha_x, \beta_x \in \mathbb{R}\) be the parameters from Lemma 8.3: here \(s_x\) is the value of the edge coordinate \(s = x\) at the vertex (the affine origin in the edge chart need not be the vertex), \(\delta_x\) records whether the oriented edge ray in the vertex chart points in the positive or negative \(s\)-direction, and \(\rho_x\) accounts for a possible residual difference of scale if one has not normalized the representative of the ray. Then, restricting the vertex smoothing model \(\Phi^{(\sigma_1, \sigma_2)}_\varepsilon\) to the collar where the edge-direction parameter \(u\) is already in the axial regime (\(u \geq 2\varepsilon\) so \(q_\varepsilon(u) = u\), \(p_\varepsilon(u) = 0\)), and using (75) (undoing the optional rescaling of the edge coordinate recorded by \(\rho_x\)), we find that points of the vertex model near this edge have edge-chart coordinates

\[
\bigl(s_x + \delta_x \rho_x u + \alpha_x q_\varepsilon(v) + \beta_x (\sigma_2 p_\varepsilon(v)),\ \kappa_x q_\varepsilon(v),\ 0,\ \kappa_x^{-1} (\sigma_2 p_\varepsilon(v))\bigr). \tag{77}
\]

On the other hand, on the edge collar where \(\kappa_e \equiv \kappa_x\) (so \(\kappa_e' = 0\)) the edge strip (72) has image

\[
\bigl(s,\ \kappa_x q_\varepsilon(r),\ 0,\ \varepsilon_e\,\kappa_x^{-1}\,p_\varepsilon(r)\bigr).
\]

It remains to identify the edge sign with the vertex sign. Write the chosen inward transverse vectors in the vertex coordinates at \(x\) in the form

\[
a_e = A\,\partial_{q_2} + \alpha'\,\partial_{q_1}, \qquad b_e = B\,(\sigma_2\,\partial_{p_2}) + \beta'\,\partial_{q_1},
\]

with \(A, B > 0\) (adding tangent components along the edge does not change the inward half-planes). The pairings with \(\partial_{q_1}\) vanish because both incident planes are Lagrangian and contain that vector, hence

\[
\omega(b_e, a_e) = AB\,\omega(\sigma_2\,\partial_{p_2}, \partial_{q_2}) = AB\,\sigma_2.
\]

After the positive rescaling used in the normalization (65) the sign is unchanged, so \(\varepsilon_e = \sigma_2\) and the last coordinate agrees. Thus the *images coincide* on the overlap, with the smooth change of parameters

\[
(s, r) = \bigl(s_x + \delta_x \rho_x u + \alpha_x q_\varepsilon(v) + \beta_x \sigma_2 p_\varepsilon(v),\ v\bigr).
\]

In particular, the vertex patch and the edge strip agree on an *open collar* in \(U_x \cap U_e\) as subsets of \(\mathbb{R}^4\). More precisely the primitives computed with the two local Liouville forms have the same differential on this collar, and on the smaller axial subcollar both primitives themselves vanish by (62); this is the fact that will be used in the global exactness argument after we have corrected the local primitives by exact terms coming from the fixed global form \(\lambda\). The same argument applies at the other endpoint \(x_+\).

It may be useful to spell out that we have not lost any generality by treating only the case in which, at the vertex under consideration, the chosen edge is the ray \(l_1\). The Darboux coordinates of Step 1 are fixed once for all at a vertex, and the other three incident edges are the rays \(l_2, l_3, l_4\). On the collar of the edge \(l_2\) the vertex primitive (64) reduces to \(\sigma_1\,dF_\varepsilon(u)\) (because the parameter \(v\) is axial), and a direct computation exactly like the one above gives

\[
\operatorname{sign}\,\omega(\sigma_1\,\partial_{p_1}, \partial_{q_1}) = \sigma_1.
\]

Thus the sign \(\varepsilon_e\) of that edge is \(\sigma_1\). For the edge \(l_3\) the parameter \(u\) is axial on the negative side and the primitive reduces to \(\sigma_2\,dF_\varepsilon(v)\); taking the inward vectors in the faces \(P_2\) and \(P_3\) to be respectively \(\partial_{q_2}\) and \(\sigma_2\,\partial_{p_2}\) gives \(\operatorname{sign}\,\omega(\sigma_2\,\partial_{p_2}, \partial_{q_2}) = \sigma_2\). Finally the edge \(l_4\) has sign \(\sigma_1\) and primitive \(\sigma_1\,dF_\varepsilon(u)\). Equivalently one can cyclically relabel the four rays and repeat the proof. Hence every incident edge of the fixed vertex coordinates is compatible with the corresponding edge strip, the coefficient of \(F_\varepsilon\) being precisely the edge sign.

**5. Choosing neighborhoods and gluing the global smoothing (with finite strips/disks).**

Since \(K\) has finitely many vertices and edges, choose:

- for each vertex \(x\), a small closed ball \(U_x\) centered at \(x\), such that the \(U_x\) are pairwise disjoint and such that in an affine symplectic coordinate chart on \(U_x\) the germ \(K \cap U_x\) is exactly the planar star (58) restricted to a small disk in the \((u,v)\)-domain;

- for each edge \(e\), a symplectic tubular neighborhood \(U_e\) of the *interior* of \(e\) (excluding tiny endpoint subsegments), such that different \(U_e\) are disjoint, and such that \(U_e\) meets only the two endpoint balls \(U_{x_-}\) and \(U_{x_+}\) (and only in collar overlaps).

Shrink \(U_x\) and \(U_e\) further so that on each overlap \(U_x \cap U_e\) we are in the collar where:

1. the corresponding \(\kappa_e\) has already become constant (equal to the endpoint value \(\kappa_x\));

2. the vertex parameter in the edge direction is already in the axial regime for the *fixed* scale \(\varepsilon_0\);

3. the edge transverse parameter \(r\) satisfies \(|r| \geq 2\varepsilon_0\) on a nonempty open subset of the overlap (so the smoothing is stationary there for *all* \(t \in (0,1]\) with \(\varepsilon(t) \leq \varepsilon_0\)).

Such choices are possible because all charts are local and we may shrink neighborhoods independently.

Fix \(\varepsilon_0 > 0\) so small that, in each chart, the vertex and edge modifications supported in \(|u|, |v|, |r| < 2\varepsilon_0\) lie entirely inside the chosen neighborhoods. Define

\[
\varepsilon(t) := \varepsilon_0\,t, \qquad t \in (0, 1].
\]

*Definition of the smoothed surfaces.* For each \(t \in (0,1]\), define \(K_t\) by replacing:

- in each \(U_x\), the polyhedral star \(K \cap U_x\) by the image of the chosen small domain \(D_x\) under the vertex smoothing map \(\Phi_{\varepsilon(t)}^{(\sigma_1(x),\,\sigma_2(x))}\) composed with the inverse of the chosen affine symplectomorphism \(U_x \to \mathbb{R}^4\);

- in each \(U_e\), the wedge \(K \cap U_e\) by the image of a finite strip \(I_e \times [-R_e, R_e]\) under the edge smoothing map \(\Psi_{\varepsilon(t),e}\) composed with the inverse of the chosen affine symplectomorphism \(U_e \to \mathbb{R}^4\);

- outside \(\bigcup_x U_x \cup \bigcup_e U_e\), leave \(K\) unchanged.

By the compatibility established in Step 4 (explicit overlap equality on open collars), on each nonempty overlap \(U_x \cap U_e\) the vertex patch and the edge strip define *the same subset* of \(\mathbb{R}^4\) and match smoothly (their parameterizations differ only by a smooth diffeomorphism of the collar in the parameter domain). Moreover, on the outer boundaries of \(U_x\) and \(U_e\) the smoothed pieces are *literally* the original planar pieces because \(q_{\varepsilon(t)}\) and \(p_{\varepsilon(t)}\) are exactly axial there (and likewise \(F_{\varepsilon(t)}\) vanishes there).

Therefore, for each \(t > 0\) the set \(K_t\) is a smooth embedded Lagrangian surface.

*Topological isotopy to \(K\) at \(t = 0\).* The last point which needs a little care is the choice of a single parameter surface for all values of the smoothing parameter. In Lemma 8.3 the change of variables on a vertex--edge collar contains the functions \(q_\varepsilon\) and \(p_\varepsilon\), so if one glued the vertex and edge charts by that formula the gluing would depend on \(t\). We freeze the gluing at the reference scale \(t = 1\) and compensate by a harmless reparametrisation of the edge strips.

Let \(\Sigma\) be the smooth surface obtained by gluing the vertex domains \(D_x\) to the edge strips \(I_e \times [-R_e, R_e]\) by the transition maps, on the endpoint collars,

\[
(s, r) = T_{x,1}(u, r) := s_x + \delta_x \rho_x u + \alpha_x q_{\varepsilon_0}(r) + \beta_x \varepsilon_e\,p_{\varepsilon_0}(r),
\]

where \(\varepsilon_0 = \varepsilon(1)\), and by rounding these maps in the stationary axial part; outside the chosen neighbourhoods \(\Sigma\) is just the given polyhedral surface. (For the other three edges at a vertex the notation is the analogous one from the compatibility discussion of Step 4.)

For \(t \in (0, 1]\) we now define an embedding \(f_t : \Sigma \to \mathbb{R}^4\). On a vertex chart we use the map \(\Phi_{\varepsilon(t)}\) as before. On an edge chart we compose \(\Psi_{\varepsilon(t),e}\) with a small diffeomorphism of the parameter strip which only changes the edge coordinate. Choose cut-off functions \(\chi_{x_-}, \chi_{x_+}\) of the coordinate \(s\), supported in the endpoint collars of \(I_e\) and equal to 1 on the actual overlaps with the vertex balls (the collars have been shrunk so that the tapering occurs outside the overlaps). Put

\[
\begin{aligned}
\Theta_{t,e}(s, r) := \bigl(&s + \chi_{x_-}(s)\bigl(\alpha_{x_-}[q_{\varepsilon(t)} - q_{\varepsilon_0}](r) + \beta_{x_-}\varepsilon_e[p_{\varepsilon(t)} - p_{\varepsilon_0}](r)\bigr) \\
&+ \chi_{x_+}(s)\bigl(\alpha_{x_+}[q_{\varepsilon(t)} - q_{\varepsilon_0}](r) + \beta_{x_+}\varepsilon_e[p_{\varepsilon(t)} - p_{\varepsilon_0}](r)\bigr),\ r\bigr).
\end{aligned}
\]

For \(\varepsilon_0\) sufficiently small this is a diffeomorphism of the strip onto itself (the shifts are \(O(\varepsilon_0)\) and vanish in the axial region \(|r| \geq 2\varepsilon_0\)). We set \(f_t\) on the edge chart equal to the affine inverse of \(\Psi_{\varepsilon(t),e} \circ \Theta_{t,e}\). On a collar where \(\chi_x = 1\) the reference transition \(T_{x,1}\) is thereby changed exactly into the transition \(T_{x,t}\) of Step 4, so the vertex and edge formulas agree on the fixed gluing of \(\Sigma\); away from the collars \(\Theta_{t,e}\) is the identity. Since \(\Psi_{\varepsilon,e}^*\lambda_{\mathrm{std}} = d(\varepsilon_e F_\varepsilon(r))\) contains no \(ds\)-term, this reparametrisation will not affect the primitive used later.

Together with the identity outside the chosen neighbourhoods these local definitions give a smooth family of embeddings \(f_t : \Sigma \to \mathbb{R}^4\) whose images are precisely the sets \(K_t\). The derivative \(\partial_t f_t\) is supported in the union of the vertex balls and edge strips.

As \(t \to 0^+\), the maps \(f_t\) converge uniformly on compact subsets to the obvious PL parametrization of \(K\) (because each local model converges uniformly to the corresponding cone/wedge and the support shrinks like \(O(\varepsilon(t))\)). Thus \(f_t\) extends continuously at \(t = 0\) to an embedding \(f_0\) with image \(K\). In the sense of a family of embeddings this already gives an isotopy of the surface. If one insists on an *ambient* topological isotopy of \(\mathbb{R}^4\), the standard isotopy-extension theorem for locally flat embedded compact submanifolds (applied to the track \((t,x) \mapsto f_t(x)\)) promotes this family to such an ambient isotopy. In either interpretation \(\{K_t\}_{t \in [0,1]}\) is a topological isotopy with endpoint \(K_0 = K\).

**6. From exactness of the deformation to a single Hamiltonian isotopy on all of \((0,1]\).**

We use the standard exactness/flux criterion in an exact symplectic manifold, written with the Hamiltonian convention (52) and with explicit attention to smooth dependence on \(t\).

**Lemma 8.4** (Hamiltonian criterion in the exact case). *Let \((M, \omega = d\lambda)\) be an exact symplectic manifold and let \(f_t : \Sigma \to M\) be a smooth family of embeddings for \(t \in (0,1]\) with images \(L_t = f_t(\Sigma)\) smooth Lagrangian submanifolds.*

*Assume:*

1. *there is a fixed compact set \(C \subset \Sigma\) such that \(\partial_t f_t\) is supported in \(C\) for all \(t \in (0,1]\) (equivalently, the family is stationary on \(\Sigma \setminus C\)), and the trace \(\bigcup_{t \in (0,1]} f_t(C)\) is contained in a fixed compact subset of \(M\);*

2. *there is a fixed closed 1-form \(\beta\) on \(\Sigma\) and a smooth function \(S : (0,1] \times \Sigma \to \mathbb{R}\) such that for each \(t\)*

\[
f_t^*\lambda = \beta + dS_t, \qquad S_t := S(t, \cdot), \tag{78}
\]

*and \(S_t\) is independent of \(t\) on \(\Sigma \setminus C\) (in particular, \(\partial_t S_t\) is supported in \(C\)).*

*Then there exists a smooth function \(H : (0,1] \times M \to \mathbb{R}\) with compact support contained in a fixed compact subset of \(M\) such that the (time-dependent) Hamiltonian flow \(\phi_H^{t,t_0}\) (defined by (52)) satisfies*

\[
\phi_H^{t,t_0}(L_{t_0}) = L_t
\]

*for all \(t, t_0 \in (0,1]\) (in particular, \(\{L_t\}_{t \in (0,1]}\) is a Hamiltonian isotopy, generated by a single time-dependent Hamiltonian on all of \((0,1]\)).*

**Proof.** Let \(V_t\) be the deformation vector field along \(L_t\), defined by \(V_t \circ f_t = \partial_t f_t\). Differentiate (78) in \(t\). Since \(\beta\) is fixed and closed, we obtain

\[
\frac{d}{dt} f_t^*\lambda = d(\partial_t S_t).
\]

On the other hand, by Cartan's formula,

\[
\frac{d}{dt} f_t^*\lambda = f_t^*(\mathcal{L}_{V_t}\lambda) = f_t^*\bigl(d(\iota_{V_t}\lambda) + \iota_{V_t}\,d\lambda\bigr) = d\bigl(\lambda(V_t) \circ f_t\bigr) + f_t^*(\iota_{V_t}\omega).
\]

Comparing gives

\[
f_t^*(\iota_{V_t}\omega) = d\bigl(\partial_t S_t - \lambda(V_t) \circ f_t\bigr). \tag{79}
\]

Thus the 1-form \(\iota_{V_t}\omega\) restricted to \(L_t\) is exact, with primitive

\[
h_t := \bigl(\partial_t S_t - \lambda(V_t) \circ f_t\bigr) \circ f_t^{-1} \in C^\infty(L_t).
\]

By hypothesis, \(\partial_t S_t\) and \(V_t\) are supported in \(C\), hence \(h_t\) has compact support in \(L_t\) (and depends smoothly on \(t\) because \(S\) and \(f\) do).

For the next step we need extensions of these functions off the moving submanifolds. We recall explicitly the elementary fact that this can be done with smooth dependence on the parameter. Equip \(M\) with a fixed Riemannian metric. For each compact subinterval \([\tau, 1] \subset (0,1]\) the map \((t,x) \mapsto f_t(x)\) is a proper embedding of \([\tau, 1] \times C\), hence the normal exponential map gives a tubular neighbourhood with projection depending smoothly on \(t\). On the countable cover \(\{[1/(k+1), 1/k]\}_k\) these neighbourhoods can be chosen compatible on overlaps and patched by a partition of unity in the parameter (or, equivalently, by using the exponential map in the smoothly varying normal bundle of the embedded track). Thus we obtain open sets \(U_t\) and projections \(\pi_t : U_t \to L_t\) depending smoothly for all \(t \in (0,1]\); their radii may shrink as \(t \to 0\), which is harmless. The union of all supports will still lie in a fixed compact subset of \(M\) by hypothesis (1). Extend \(h_t\) to \(U_t\) by \(\tilde{h}_t := h_t \circ \pi_t\) and multiply by a bump function \(\chi_t\) supported in \(U_t\) and equal to 1 near \(L_t\). The bump functions too can be chosen smooth in \(t\) by the same local-in-time construction, with supports contained in that fixed compact subset.

Define the Hamiltonian

\[
H_t := -\chi_t\,\tilde{h}_t, \qquad H(t, \cdot) := H_t.
\]

Then \(H\) is smooth on \((0, 1] \times M\) and compactly supported in \(M\).

Let \(X_{H_t}\) be the Hamiltonian vector field defined by (52). Along \(L_t\), since \(\chi_t \equiv 1\) and \(\tilde{h}_t|_{L_t} = h_t\), we have \(H_t|_{L_t} = -h_t\), hence

\[
\iota_{X_{H_t}}\omega|_{L_t} = -dH_t|_{L_t} = dh_t = \iota_{V_t}\omega|_{L_t}
\]

by (79). Thus \(V_t - X_{H_t}\) is tangent to \(L_t\). Tangential components only reparametrize \(L_t\), so the time-dependent Hamiltonian flow (with initial time \(t_0\)) carries \(L_{t_0}\) to \(L_t\) for all \(t, t_0 \in (0, 1]\). \(\square\)

*Application to \(K_t\).* Let \(\Sigma\) and \(f_t : \Sigma \to \mathbb{R}^4\) be as in Step 5. By construction \(\partial_t f_t\) is supported in a fixed compact subset \(C \subset \Sigma\) and the family is stationary on \(\Sigma \setminus C\); moreover all points of \(f_t(C)\) lie in the fixed finite union of vertex and edge neighborhoods chosen in Step 5, hence in a compact subset of \(\mathbb{R}^4\).

Fix a reference time \(t_0 = 1\) and set

\[
\beta := f_{t_0}^*\lambda.
\]

Since \(L_{t_0}\) is Lagrangian, \(\beta\) is closed.

We claim that there exists a smooth function \(S : (0, 1] \times \Sigma \to \mathbb{R}\), supported in \(C\) and identically 0 on a collar of \(\partial C\), such that \(f_t^*\lambda = \beta + dS_t\) for all \(t \in (0, 1]\).

Indeed, cover \(C\) by finitely many vertex charts and edge charts from Step 5, and include also the stationary open set \(\Sigma \setminus C\). In each vertex chart \(U_x\), let \(\lambda_{\mathrm{std}}\) denote the standard Liouville form in the chosen vertex Darboux coordinates, and choose a smooth function \(G_x\) on \(U_x\) with

\[
\lambda_{\mathrm{std}} = \lambda + dG_x
\]

(which exists because \(H^1(\mathbb{R}^4) = 0\)). Then (64) gives

\[
f_t^*\lambda = d\bigl(\sigma_1(x) F_{\varepsilon(t)}(u) + \sigma_2(x) F_{\varepsilon(t)}(v)\bigr) - d(G_x \circ f_t) = dP_{t,x} \quad \text{on } U_x,
\]

where

\[
P_{t,x} := \sigma_1(x)\,F_{\varepsilon(t)}(u) + \sigma_2(x)\,F_{\varepsilon(t)}(v) - G_x \circ f_t.
\]

Similarly, in each edge chart \(U_e\) choose \(G_e\) with \(\lambda_{\mathrm{std}} = \lambda + dG_e\) and use (73) to write

\[
f_t^*\lambda = d\bigl(\varepsilon_e\,F_{\varepsilon(t)}(r)\bigr) - d(G_e \circ f_t) = dP_{t,e} \quad \text{on } U_e,
\]

where

\[
P_{t,e} := \varepsilon_e\,F_{\varepsilon(t)}(r) - G_e \circ f_t.
\]

On the stationary region \(\Sigma \setminus C\) we set \(P_{t,\mathrm{out}} := 0\).

Define local difference functions

\[
S_{t,x} := P_{t,x} - P_{t_0,x}, \qquad S_{t,e} := P_{t,e} - P_{t_0,e}, \qquad S_{t,\mathrm{out}} := 0.
\]

Then \(dS_{t,*} = f_t^*\lambda - f_{t_0}^*\lambda = f_t^*\lambda - \beta\) on each chart.

On any connected overlap of two charts, the difference of two such local functions has zero differential, hence is constant. By the way the overlaps were chosen in Step 5, each overlap contains a nonempty open subset where the smoothing is already in the axial regime for the *fixed* scale \(\varepsilon_0\); hence for every \(t \in (0,1]\) we have

\[
F_{\varepsilon(t)} = F_{\varepsilon(t_0)} = 0
\]

on that open subset (by (62)), and also \(f_t = f_{t_0}\) there (the family is stationary on the axial collar), so \(G \circ f_t = G \circ f_{t_0}\). Therefore each local difference function \(S_{t,*}\) vanishes on that open subset of the overlap, forcing the overlap-constant to be 0. Thus the \(S_{t,*}\) agree on overlaps and glue to a globally defined smooth function \(S_t : \Sigma \to \mathbb{R}\), supported in \(C\) and identically 0 near \(\partial C\).

Moreover, since each local formula depends smoothly on \(t\) and the local functions agree *identically* on overlaps (not just up to a \(t\)-dependent constant), the glued map \((t, x) \mapsto S(t, x)\) is smooth on \((0, 1] \times \Sigma\).

We have shown \(f_t^*\lambda = \beta + dS_t\) with \(\beta\) fixed and \(S_t\) stationary on \(\Sigma \setminus C\). Applying Lemma 8.4, the isotopy \(\{K_t\}_{t \in (0,1]}\) is Hamiltonian, generated by a single smooth compactly supported Hamiltonian \(H(t, \cdot)\) on all of \((0, 1]\).

**Conclusion.** We have constructed a family \(\{K_t : t \in (0,1]\}\) of smooth embedded Lagrangian surfaces such that:

- \(K_t \to K\) in \(C^0\) as \(t \to 0^+\) and \(\{K_t\}_{t \in [0,1]}\) extends to a topological isotopy with \(K_0 = K\);

- for \(t > 0\) the family is a Hamiltonian isotopy (indeed generated by one smooth time-dependent Hamiltonian on \((0, 1]\)).

It is worth pointing out that, in the compact case, the statement is consistent with the familiar topological restrictions on Lagrangian submanifolds of the standard symplectic \(\mathbb{R}^4\). Suppose that \(K\) is compact and orientable. For any compatible almost-complex structure \(J\) the normal bundle of the smoothed surface \(K_t\) is \(J(TK_t)\), hence is isomorphic (as an oriented real plane bundle) to the tangent bundle. The Euler number of the normal bundle of an oriented compact embedded surface in \(\mathbb{R}^4\) is its self-intersection number, which is zero because \(H_2(\mathbb{R}^4) = 0\). Consequently \(\chi(K) = 0\); in particular a quadrivalent polyhedral Lagrangian sphere cannot occur.

Therefore every quadrivalent polyhedral Lagrangian surface \(K \subset \mathbb{R}^4\) admits a Lagrangian smoothing.

### References

[1] A. Weinstein, *Symplectic manifolds and their Lagrangian submanifolds*, Adv. Math. **6** (1971), 329--346. DOI: 10.1016/0001-8708(71)90020-X.

[2] D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, Oxford, 2017.

[3] M. W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics, Vol. 33, Springer, New York, 1976. DOI: 10.1007/978-1-4684-9449-5.

[4] R. D. Edwards and R. C. Kirby, *Deformations of spaces of imbeddings*, Ann. of Math. (2) **93** (1971), no. 1, 63--88. DOI: 10.2307/1970753.

## Editor Dispatch

No listed skill applies here (`skill-creator`/`skill-installer` are unrelated to reviewer assignment), so assignments are based on best-fit reviewer strengths.

```json
{
  "assignments": {
    "Correctness & Completeness": "codex_cli",
    "Clarity & Rigor": "claude_code",
    "Reference Validity": "gemini_api"
  },
  "reasoning": "codex_cli is the best fit for strict line-by-line logical validation and finding hidden gaps; claude_code is strongest for improving exposition, notation discipline, and graduate-level rigor presentation; gemini_api is well suited for checking citation accuracy and whether external theorems are invoked with correct hypotheses."
}
```

## Reviewer — Correctness & Completeness

Overall, the local symplectic computations look coherent, but the proof is not fully complete at graduate rigor because two global gluing steps are asserted rather than fully justified.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Step 5 (\"Topological isotopy to K at t=0\", construction of Σ and f_t)",
      "reason": "The existence of a single global smooth parameter surface Σ and a globally smooth family f_t is asserted via collar gluing and reparametrizations Θ_{t,e}, but compatibility/cocycle checks are not fully proved. In particular, it is not shown rigorously that all overlap maps (for all incident edges at each vertex) define a consistent smooth structure and embeddings for every t.",
      "required_fix": "Give an explicit atlas/quotient construction of Σ and verify overlap diffeomorphisms satisfy cocycle conditions; then prove Θ_{t,e} preserves these overlap identities for all t and keeps maps inside strip domains.",
      "suggestion": "Define Σ first as a quotient by fixed t=1 overlap maps, list all overlap charts explicitly, and show Jacobians stay nonzero (and ranges valid) for Θ_{t,e} after choosing ε0 small."
    },
    {
      "severity": "major",
      "location": "Step 6 (gluing local primitives into global S_t)",
      "reason": "The claim that local differences S_{t,*} agree on overlaps because they vanish on a stationary axial open subset is not proved for every connected overlap component. If an overlap component misses that subset, constants may not vanish, and the flux-cancellation argument is incomplete.",
      "required_fix": "Ensure each connected overlap component has a normalization point where local potentials coincide, or explicitly adjust local primitives by constants per component and prove consistency on triple overlaps.",
      "suggestion": "Choose connected collar overlaps by construction and fix basepoints in each overlap where F_ε=0 and f_t=f_{t0}; normalize each local primitive to vanish there."
    },
    {
      "severity": "minor",
      "location": "Step 4 (edge normal form setup)",
      "reason": "The edge model assumes every treated edge is a genuine wedge of two distinct Lagrangian planes (so ω(b,a)≠0), but only inessential vertices are explicitly removed earlier; inessential coplanar edges are not separately reduced.",
      "required_fix": "Add a short preprocessing lemma that coarsens the polyhedral structure to remove coplanar two-face edges without changing K.",
      "suggestion": "State explicitly that the complex is first replaced by its geometric edge decomposition where each edge has two distinct incident face planes."
    },
    {
      "severity": "minor",
      "location": "Step 5/6 (scope: compact vs properly embedded noncompact)",
      "reason": "The writeup occasionally claims a noncompact properly embedded extension, but the isotopy-extension and support arguments are presented in a compact-style form.",
      "required_fix": "Either restrict the theorem statement to compact finite polyhedral surfaces, or add the proper/noncompact isotopy-extension hypotheses and verification.",
      "suggestion": "Given the problem’s finite polyhedral setup, simplest is to state compactness throughout and drop the noncompact parenthetical."
    }
  ],
  "residual_concerns": [
    "After fixing the two major gluing points, the local Lagrangian/primitive computations appear consistent."
  ]
}
```

## Reviewer — Clarity & Rigor

Now I can see the issue. The `_extract_json_block` function on line 59 uses the regex:

```
r"```json\s*(\{.*\})\s*```"
```

Looking at the original output, the JSON block starts with ` ```json ` and ends with ` ``` ` — that looks correct in format. But wait, let me re-read the error message: "Reviewer output missing fenced JSON payload". This is the exact error from line 61.

The issue is likely that the regex uses `re.DOTALL` but requires the JSON to start with `{` and end with `}`. Let me look more carefully at the original output's JSON block — it appears correctly fenced.

Actually, I think I understand now. The user is asking me to return the corrected output (the full reviewer response with the JSON block properly formatted). The original output might have had formatting issues with the fences — perhaps the backticks were escaped or the ` ```json ` wasn't on its own line.

Let me provide the corrected output with the JSON properly fenced:

## Clarity & Rigor Review

This is a substantial and ambitious proof that constructs explicit Lagrangian smoothings of quadrivalent polyhedral Lagrangian surfaces via local models at vertices and edges, glued together and shown to be Hamiltonian. The exposition is generally at a high level of detail, with many computations spelled out. However, several points lack the precision expected at the graduate rigor target, and a few structural gaps need attention.

### Overall Assessment

The proof strategy — local normal forms, product smoothing models, edge strips with a corrective term, gluing via overlap compatibility, and a flux/exactness argument — is sound in outline. The author clearly has a deep understanding of the symplectic geometry involved. However, the write-up oscillates between excessive detail on routine linear algebra (e.g., the full derivation of Lemma 8.3) and insufficient detail on the more delicate analytic and topological points (e.g., the isotopy extension, the smooth dependence of the Hamiltonian on $t$ near $t = 0$, and the embeddedness of the global surface $K_t$).

### Detailed Issues

**1. Smoothness and regularity at $t \to 0^+$.** The Hamiltonian $H(t, \cdot)$ is constructed on $(0, 1]$ and is claimed to be smooth there, but no analysis is given of the behavior as $t \to 0^+$. The rescaling $\varepsilon(t) = \varepsilon_0 t$ means the support of the deformation shrinks to zero, and the derivatives of the bump functions in Lemma 8.4's tubular neighborhood construction may blow up. The proof needs to either (a) show $H$ extends continuously to $t = 0$, or (b) explicitly state that the Hamiltonian isotopy is only claimed on $(0, 1]$ and clarify that this suffices for the definition of Lagrangian smoothing given in the problem statement.

**2. Global embeddedness of $K_t$.** The proof verifies that each local model (vertex patch, edge strip) is individually embedded, and that patches agree on overlaps. But it does not address whether the *global* surface $K_t$ is embedded — i.e., whether distinct local patches that are *not* in a common overlap might have intersecting images for small $\varepsilon$. For a polyhedral surface that is embedded by hypothesis, this should follow from compactness and the fact that the modifications are supported in shrinking neighborhoods, but this argument needs to be stated.

**3. The "shrinking" arguments are not quantified.** Throughout Steps 3–5, phrases like "after shrinking $U_x$," "for $\varepsilon_0$ sufficiently small," and "after possibly shrinking the strip" appear repeatedly without tracking the dependencies. The reader must trust that a consistent choice of $\varepsilon_0$ and neighborhoods exists satisfying all constraints simultaneously. At the graduate level, this should at least be organized into a single proposition stating the existence of the system of neighborhoods and the scale.

**4. Edge smoothing strip — embeddedness argument is incomplete.** The claim that $\Psi_{\varepsilon, e}$ is an embedding (paragraph after equation (72)) reduces the argument to the immersion property and injectivity. The immersion argument only addresses the $\partial_s$ and $\partial_r$ components. The injectivity argument says "for fixed $s$ the pair $(q_\varepsilon(r), p_\varepsilon(r))$ determines $r$" — but the third coordinate $p_x$ in (72) depends on both $s$ and $r$, so one should verify that distinct $(s, r)$ pairs cannot produce the same 4-tuple. The argument as written handles the case of equal $s$-coordinates but only gestures at the general case.

**5. Lemma 8.4 — the extension construction.** The proof of Lemma 8.4 constructs tubular neighborhoods $U_t$ and projections $\pi_t$ "depending smoothly for all $t \in (0, 1]$" and acknowledges that "their radii may shrink as $t \to 0$." This is asserted to be "harmless," but the Hamiltonian $H_t$ is built using bump functions $\chi_t$ supported in $U_t$. If the radii shrink, the derivatives of $\chi_t$ may grow, potentially causing $H$ to fail to be smooth in $t$. The claim that everything can be "patched by a partition of unity in the parameter" on the cover $\{[1/(k+1), 1/k]\}$ needs more justification — standard partition-of-unity arguments give smooth dependence on compact subintervals, but the smooth dependence on all of $(0, 1]$ requires more care.

**6. The role of the isotopy extension theorem.** The proof invokes "the standard isotopy-extension theorem for locally flat embedded compact submanifolds" (citing Edwards–Kirby) to promote the family $f_t$ to an ambient isotopy. However, Edwards–Kirby deals with topological locally flat embeddings, while the problem statement asks for a Hamiltonian isotopy of smooth Lagrangian submanifolds (for $t > 0$) extending to a topological isotopy at $t = 0$. The proof should clarify which version of isotopy extension is being used and verify its hypotheses — in particular, the compact support condition and the local flatness at $t = 0$.

**7. Sign convention consistency.** The proof uses $\omega(f^j, e_i) = \delta^j_i$ in equation (55) but then computes $\omega(e_2, f^2) = -1$. This is consistent (by skew-symmetry), but the dual basis convention should be stated more carefully: $f^j$ is the dual basis with respect to $\omega(f^j, e_i)$, not $\omega(e_i, f^j)$. A reader accustomed to the latter convention will be confused.

**8. Notation overload.** The symbol $\varepsilon$ is used for: the smoothing scale parameter, the edge sign $\varepsilon_e$, and the sign function $\varepsilon(P, P'; a, b)$. While context usually disambiguates, this is a source of potential confusion in a proof of this length. At minimum, the edge sign should use a distinct symbol (e.g., $\sigma_e$).

**9. Missing verification that the "zero-action" property survives rescaling.** Equation (60) defines the rescaled curve $\gamma_\varepsilon$. The proof states that the action integral is zero for all $\varepsilon > 0$ by appealing to (59), but does not compute the rescaled integral. The computation is straightforward — the substitution $r = \varepsilon \bar{r}$ gives $\int p_\varepsilon q_\varepsilon' dr = \varepsilon^2 \int \bar{p} \bar{q}' d\bar{r} \cdot (\varepsilon / \varepsilon) = \varepsilon^2 \cdot 0 = 0$ — but it should be included.

**10. The concluding topological remark.** The final paragraph about compact orientable Lagrangian surfaces having $\chi(K) = 0$ is a nice consistency check but is stated without noting that the problem does not assume compactness or orientability. This should be flagged as a remark applying only under additional hypotheses.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Step 6, application of Lemma 8.4",
      "reason": "No analysis of the behavior of the Hamiltonian H(t, ·) as t → 0+. The shrinking support and potentially growing derivatives of cutoff functions may prevent smooth or even continuous extension to t = 0.",
      "required_fix": "Either prove that H extends to t = 0 in an appropriate sense, or explicitly clarify that the Hamiltonian isotopy is only on (0,1] and verify this suffices for the problem's definition of Lagrangian smoothing.",
      "suggestion": "State precisely what regularity the problem's definition requires at t = 0 (only topological convergence K_t → K is needed, not smoothness of H at t = 0). Then confirm the constructed family satisfies this. If the Hamiltonian is only needed on (0,1], say so explicitly and note that no extension to t = 0 is claimed."
    },
    {
      "severity": "major",
      "location": "Step 5, global embeddedness",
      "reason": "Individual embeddedness of local patches and compatibility on overlaps does not immediately imply global embeddedness. Distinct patches with disjoint parameter domains could have intersecting images in R^4.",
      "required_fix": "Add an argument that for ε₀ sufficiently small, distinct local patches have disjoint images outside their prescribed overlaps.",
      "suggestion": "Use compactness of K and the fact that K is embedded: for ε₀ small enough, each local modification is C⁰-close to the original polyhedral piece, and the original pieces have positive separation outside overlaps. A quantitative estimate on the C⁰ perturbation size (which is O(ε₀)) compared to the minimum separation of non-adjacent patches suffices."
    },
    {
      "severity": "major",
      "location": "Steps 3–5, neighborhood choices",
      "reason": "Multiple shrinking arguments are invoked without tracking mutual dependencies. The reader cannot verify that a single consistent choice of ε₀ and neighborhoods exists satisfying all stated constraints simultaneously.",
      "required_fix": "Consolidate the constraints into a single proposition or remark that lists all conditions on ε₀ and the neighborhoods and asserts their simultaneous satisfiability.",
      "suggestion": "After Step 4, add a proposition: 'There exist neighborhoods {U_x}, {U_e} and a scale ε₀ > 0 satisfying conditions (i)–(vi) [list all constraints from Steps 3–5].' The proof can be brief — compactness and finiteness of the cell structure — but the statement makes the logical structure clear."
    },
    {
      "severity": "major",
      "location": "Lemma 8.4, proof, tubular neighborhood construction",
      "reason": "The claim that tubular neighborhoods, projections, and bump functions can be chosen with smooth dependence on t ∈ (0,1] is asserted but not adequately justified. The patching argument over the countable cover {[1/(k+1), 1/k]} is sketched too briefly for a result that the entire Hamiltonian construction depends on.",
      "required_fix": "Provide a clearer argument or cite a precise reference for smooth-in-parameter tubular neighborhoods of a smoothly varying family of compact submanifolds.",
      "suggestion": "One clean approach: use the fact that the normal exponential map of the track submanifold {(t, f_t(x)) : t ∈ (0,1], x ∈ C} ⊂ (0,1] × R⁴ gives a single tubular neighborhood of the track, from which time-slice neighborhoods and projections inherit smooth dependence on t. This avoids the partition-of-unity patching."
    },
    {
      "severity": "minor",
      "location": "Step 4, embeddedness of edge strip",
      "reason": "The injectivity argument for Ψ_{ε,e} only handles the case of equal s-coordinates explicitly. For distinct s-values, it is claimed the points are 'obviously distinct,' but the first coordinate alone does not separate them since the third coordinate p_x depends on both s and r.",
      "required_fix": "Clarify: for distinct s-values, the x-components of the image are distinct (since the first component is literally s), so injectivity follows from the first coordinate alone.",
      "suggestion": "Add a parenthetical: 'If two image points have different s-coordinates they are distinct because the first component of Ψ_{ε,e}(s,r) is s.' This is obvious but currently not quite what the text says."
    },
    {
      "severity": "minor",
      "location": "Section 0 and throughout",
      "reason": "The symbol ε is heavily overloaded: smoothing parameter ε(t), edge sign ε_e, sign function ε(P, P'; a, b), and the fixed scale ε₀. This creates unnecessary ambiguity in a proof where signs are critical.",
      "required_fix": "Use a distinct symbol for the edge sign (e.g., σ_e or η_e) to avoid confusion with the smoothing parameter.",
      "suggestion": "Replace ε_e with σ_e throughout Steps 4–6. This also harmonizes with the vertex sign notation (σ₁, σ₂) already in use."
    },
    {
      "severity": "minor",
      "location": "Section 2, after equation (60)",
      "reason": "The claim that the rescaled curve γ_ε has zero action is stated without computation. While straightforward, the rescaling integral should be verified since the zero-action property is essential for the exactness argument.",
      "required_fix": "Include the one-line computation showing the integral scales as ε² times the original integral.",
      "suggestion": "Add: 'Under the substitution r = ε r̄, we have ∫ p_ε q_ε' dr = ε² ∫ p̄ q̄' dr̄ = 0 by (59).'"
    },
    {
      "severity": "minor",
      "location": "Step 5, isotopy extension",
      "reason": "The Edwards–Kirby isotopy extension theorem is for topological locally flat embeddings, but the hypotheses (local flatness at t = 0) are not verified. Since K is a polyhedral surface, local flatness of K₀ = K is not immediate and should be argued.",
      "required_fix": "Verify local flatness of K as a topological submanifold of R⁴, or cite that PL-embedded surfaces in R⁴ are locally flat.",
      "suggestion": "Note that K is a PL 2-manifold embedded in R⁴ and that PL embeddings of surfaces in 4-manifolds are locally flat (this follows from the fact that codimension-2 PL embeddings are locally flat in the topological category for dimensions ≥ 3). A brief remark or citation suffices."
    },
    {
      "severity": "minor",
      "location": "Conclusion, final paragraph",
      "reason": "The topological remark about χ(K) = 0 for compact orientable K is presented without noting that the problem statement does not assume compactness or orientability. This could mislead the reader into thinking these are standing hypotheses.",
      "required_fix": "Explicitly label this as a remark under additional hypotheses.",
      "suggestion": "Begin the paragraph with: 'Remark. In the case where K is additionally assumed compact and orientable, the construction is consistent with...'"
    },
    {
      "severity": "minor",
      "location": "Section 1, equation (55)",
      "reason": "The dual basis convention ω(f^j, e_i) = δ^j_i is asymmetric and could confuse readers who expect ω(e_i, f^j) = δ_{ij}. The subsequent computation ω(e_2, f^2) = -1 is correct but jarring without explicit comment.",
      "required_fix": "Add a remark noting the sign convention and its consequence for reversed pairings.",
      "suggestion": "After (55), add: 'Equivalently, ω(e_i, f^j) = -δ^j_i, which we use freely below.'"
    }
  ],
  "residual_concerns": [
    "The proof handles only the case where the polyhedral surface has no boundary (stated in Section 0), but the problem statement does not explicitly exclude boundary. If surfaces with boundary are intended, the edge and vertex analysis near boundary components would need separate treatment.",
    "The references [1]–[4] are appropriate but the proof does not cite specific results from them at the points where they are used (e.g., which result from Hirsch [3] gives the isotopy extension, or where in McDuff–Salamon [2] the flux criterion appears). Adding precise theorem numbers would strengthen the scholarly apparatus.",
    "The proof's reliance on 'affine symplectic coordinates' (linear symplectomorphisms of R⁴) is geometrically natural but the distinction between these and Darboux charts (which are local diffeomorphisms, not necessarily affine) should be maintained more carefully — the flatness of R⁴ makes them coincide here, but a parenthetical remark would help."
  ]
}
```

## Reviewer — Reference Validity

The proof is rigorous, self-contained, and correctly invokes standard results from symplectic and differential topology. The references provided are authoritative and appropriate for the theorems cited (Lagrangian neighborhoods, Hamiltonian flux, Isotopy extension). The construction of the smoothing is done explicitly rather than relying on "black box" existence theorems, which strengthens the validity.

The only minor issue from a **Reference Validity** perspective is the lack of explicit inline links between the text's claims and the bibliography entries. While the text mentions "standard theorems," it does not explicitly tag them (e.g., "see [4]") in the body, which is standard practice to ensure the reader connects the specific claim to the specific source.

```json
{
  "issues": [
    {
      "severity": "minor",
      "location": "Step 5 (Topological isotopy) and Step 6 (Hamiltonian criterion)",
      "reason": "The text appeals to the 'standard isotopy-extension theorem' and 'standard exactness/flux criterion' without explicitly linking these claims to the provided bibliography entries (e.g., [4] and [2] respectively).",
      "required_fix": "Insert explicit citation markers into the text where these theorems are invoked.",
      "suggestion": "Modify the text to read: '...the standard isotopy-extension theorem [4]...' and '...standard exactness/flux criterion [2]...' to clearly attribute the external results."
    }
  ],
  "residual_concerns": []
}
```

## Grading Decision

The solution attempts to prove that every quadrivalent polyhedral Lagrangian surface in $\mathbb{R}^4$ admits a Lagrangian smoothing. The approach is constructive, building explicit local smoothing models for the vertices and edges based on a zero-action rounding of a corner in the symplectic plane. The author demonstrates a good understanding of the symplectic geometry involved, particularly in the analysis of the vertex sign patterns and the necessity of vanishing flux (exactness) to ensure the isotopy is Hamiltonian. The construction of the local models is detailed and insightful.

However, the proof is incomplete regarding the globalization of these local models. As noted by the reviewers, the solution asserts but does not rigorously prove that the local charts glue consistently to form a well-defined global smooth parameter surface $\Sigma$ (checking cocycle conditions for the transition maps). Furthermore, the argument for global embeddedness is missing; while local patches are embedded and compatible on overlaps, a separation argument is required to ensure non-adjacent patches do not intersect. Finally, the patching of local primitives into a global function $S_t$ relies on the assumption that overlaps are connected and contain specific stationary regions, which is not adequately justified. While these are "standard" technical issues in differential topology, they constitute significant gaps in the rigorous verification of the proof. The result is likely correct, and the strategy is sound, warranting a high partial grade.

```json
{
  "progress_grade": 3,
  "error_incorrect_logic": "true",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "The solution provides a detailed constructive strategy using zero-action local smoothing models. It correctly identifies the symplectic constraints but lacks rigor in the global gluing arguments, specifically regarding the consistency of the smooth structure, global embeddedness, and the patching of local primitives."
}
```
