## 7 Uniform lattices with 2-torsion arising as fundamental groups of closed manifolds with \(\mathbb{Q}\)-acyclic universal cover

**Problem**

Suppose that \(\Gamma\) is a uniform lattice in a real semisimple group, and that \(\Gamma\) contains some 2-torsion. Is it possible for \(\Gamma\) to be the fundamental group of a compact manifold without boundary whose universal cover is acyclic over the rational numbers \(\mathbb{Q}\)?

**Solution**

We construct a uniform lattice \(\Gamma\) in a real semisimple group, containing a central element of order 2, and a closed manifold \(M\) with \(\pi_1(M) \cong \Gamma\) such that \(\widetilde{M}\) is \(\mathbb{Q}\)-acyclic.

### 7.0.1 Step 0: A torsion-free uniform lattice in \(SO^+(n,1)\)

Fix an odd integer \(n = 2m + 1 \geq 5\). It is classical that there exist closed hyperbolic \(n\)-manifolds in every dimension. For example, standard arithmetic constructions using anisotropic quadratic forms over totally real fields give compact hyperbolic orbifolds in all dimensions (see [1] and the discussion in [4, Ch. II]). Passing to the identity component and using Selberg's lemma [6] we obtain a torsion-free finite index subgroup. Thus we may choose a torsion-free cocompact lattice

\[
L \; < \; SO^+(n,1)
\]

such that

\[
N \; = \; L \backslash \mathbb{H}^n \tag{43}
\]

is a closed orientable hyperbolic \(n\)-manifold (hence an aspherical \(K(L,1)\)).

### 7.0.2 Step 1: The spin-lift lattice with central 2-torsion

Consider the spin covering

\[
1 \longrightarrow \{\pm 1\} \longrightarrow \mathrm{Spin}(n,1) \xrightarrow{p} SO^+(n,1) \longrightarrow 1.
\]

Define

\[
\Gamma \; := \; p^{-1}(L) \; < \; \mathrm{Spin}(n,1).
\]

Then \(\Gamma\) is discrete and cocompact in \(\mathrm{Spin}(n,1)\) (because \(p\) is a finite covering and \(L\) is discrete and cocompact in \(SO^+(n,1)\)). Thus \(\Gamma\) is a uniform lattice in the real semisimple group \(\mathrm{Spin}(n,1)\). We shall use below that \(\Gamma\) is finitely presented; this follows for lattices in Lie groups (for instance from the theorem of Borel--Serre on arithmetic groups, or from the fact that a compact fundamental domain gives a finite presentation, cf. [4, Ch. II, Thm. 4.7]).

Let \(z := -1 \in \mathrm{Spin}(n,1)\) be the nontrivial element of the kernel. Then \(z \in \Gamma\) is central and has order 2, hence \(\Gamma\) contains 2-torsion.

**Remark 7.1** (Only 2-torsion). Since \(L\) is torsion-free, any finite order element \(\gamma \in \Gamma\) satisfies \(p(\gamma) \in L\) finite order, hence \(p(\gamma) = 1\) and \(\gamma \in \ker(p) = \{\pm 1\}\). Therefore the only nontrivial finite order element in \(\Gamma\) is the central involution \(z\).

### 7.0.3 Step 2: A projective \(\mathbb{Q}\Gamma\)-Poincar\(\acute{\text{e}}\) complex by extension of scalars

Let \(\mathbb{Q}\Gamma\) be the rational group ring, and define the central idempotent

\[
e \; := \; \frac{1+z}{2} \; \in \mathbb{Q}\Gamma.
\]

We now relate the corner algebra \(e(\mathbb{Q}\Gamma)e\) to \(\mathbb{Q}L\).

**Lemma 7.2** (The corner algebra). *There is a canonical ring isomorphism*

\[
e(\mathbb{Q}\Gamma)e \; \cong \; \mathbb{Q}L,
\]

*and \(e\mathbb{Q}\Gamma\) is free as a left module over \(e(\mathbb{Q}\Gamma)e\).*

**Proof.** Choose a set-theoretic section \(s : L \to \Gamma\) of the projection \(p|_\Gamma : \Gamma \to L\) (i.e. \(p(s(\lambda)) = \lambda\)). Since \(\ker(p) = \{\pm 1\} = \langle z \rangle\) is central, there is a 2-cocycle \(\varepsilon : L \times L \to \{0,1\}\) such that

\[
s(\lambda)s(\mu) \; = \; s(\lambda\mu) \, z^{\varepsilon(\lambda,\mu)}.
\]

Multiplying by \(e\) kills the ambiguity \(z^{\varepsilon(\lambda,\mu)}\) because \(ez = e\). Hence in \(\mathbb{Q}\Gamma\) we have

\[
(e\,s(\lambda))(e\,s(\mu)) \; = \; e\,s(\lambda)s(\mu) \; = \; e\,s(\lambda\mu)\,z^{\varepsilon(\lambda,\mu)} \; = \; e\,s(\lambda\mu).
\]

Thus the rule \(\lambda \mapsto e\,s(\lambda)\) defines a multiplicative map \(\mathbb{Q}L \to e(\mathbb{Q}\Gamma)e\) sending the group basis of \(L\) to elements of the corner. If \(s'(\lambda) = s(\lambda)z^{\delta(\lambda)}\) is another section, then \(e\,s'(\lambda) = e\,s(\lambda)\), so the resulting map is independent of the choice of section. It is an isomorphism for the following elementary reason. The elements \(\{s(\lambda), z s(\lambda) \mid \lambda \in L\}\) are pairwise distinct and form a subset of the group basis of \(\mathbb{Q}\Gamma\); hence a relation \(\sum a_\lambda e\,s(\lambda) = 0\) would give \(\sum a_\lambda s(\lambda) + \sum a_\lambda z s(\lambda) = 0\) and all \(a_\lambda\) are zero. Thus the displayed map identifies the bases \(\{\lambda\}\) and \(\{e\,s(\lambda)\}\) of the two \(\mathbb{Q}\)-vector spaces, and it is onto because every element of the corner is a \(\mathbb{Q}\)-linear combination of the \(e\,s(\lambda)\).

For the module statement we use that the idempotent \(e\) is central. Consequently \(e\mathbb{Q}\Gamma = e\mathbb{Q}\Gamma e\) (for \(ex = exe\)). Thus, viewed as a left module over the corner algebra \(e(\mathbb{Q}\Gamma)e\), the module \(e\mathbb{Q}\Gamma\) is just the regular module of this ring, in particular it is free of rank one. This proves the lemma. \(\square\)

Now fix a finite CW structure on \(N\) and let \(c_i\) be the number of \(i\)-cells. The universal cover \(\widetilde{N} \simeq \mathbb{H}^n\) is contractible, so the cellular chain complex \(C_*(\widetilde{N};\mathbb{Q})\) is a finite free chain complex of right \(\mathbb{Q}L\)-modules which resolves the trivial right \(\mathbb{Q}L\)-module \(\mathbb{Q}\). We extend scalars along \(\mathbb{Q}L \cong e(\mathbb{Q}\Gamma)e\) by tensoring with the \((\mathbb{Q}L, \mathbb{Q}\Gamma)\)-bimodule \(e\mathbb{Q}\Gamma\):

\[
P_* \; := \; C_*(\widetilde{N};\mathbb{Q}) \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma.
\]

Then each chain group is

\[
P_i \; \cong \; (e\mathbb{Q}\Gamma)^{c_i} \qquad (0 \leq i \leq n), \tag{44}
\]

hence \(P_*\) is a finite chain complex of finitely generated projective right \(\mathbb{Q}\Gamma\)-modules.

**Lemma 7.3** (Homology of \(P_*\)). *The complex \(P_*\) is acyclic in positive degrees and has \(H_0(P_*) \cong \mathbb{Q}\) with the trivial \(\Gamma\)-action. More precisely,*

\[
H_i(P_*) \; = \; 0 \quad (i > 0), \qquad H_0(P_*) \; \cong \; \mathbb{Q}.
\]

**Proof.** Because \(e\mathbb{Q}\Gamma\) is free as a left \(\mathbb{Q}L\)-module (Lemma 7.2), it is flat, so tensoring the exact augmented cellular complex of \(\widetilde{N}\) over \(\mathbb{Q}L\) preserves exactness in positive degrees. Thus \(H_i(P_*) = 0\) for \(i > 0\) and

\[
H_0(P_*) \; \cong \; \mathbb{Q} \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma \; \cong \; \mathbb{Q} \otimes_{\mathbb{Q}L} \mathbb{Q}L \; \cong \; \mathbb{Q}
\]

as a vector space (using the corner isomorphism of Lemma 7.2 in the middle).

It remains to identify the residual right action of \(\Gamma\). Let \([1 \otimes e]\) be the generator displayed above. If \(\gamma = s(\mu)z^\varepsilon \in \Gamma\) then, in the tensor product over \(\mathbb{Q}L\),

\[
[1 \otimes e]\gamma = [1 \otimes e\,s(\mu)z^\varepsilon] = [1 \otimes e\,s(\mu)] = [1 \cdot \mu \otimes e] = [1 \otimes e],
\]

because the augmentation makes \(1 \cdot \mu = 1\) and \(ez = e\). Thus the right action is trivial and \(H_0(P_*) \cong \mathbb{Q}\) as a trivial right \(\Gamma\)-module. \(\square\)

For later use we make explicit that induction by the central idempotent is compatible with the duality which enters the definition of a symmetric Poincar\(\acute{\text{e}}\) complex. Recall that our chain modules are right modules and that the dual of a right module is again regarded as a right module by means of the standard involution on the group ring.

**Lemma 7.4** (Induction and duality). *Let \(A = \mathbb{Q}\Gamma\) and put \(A_+ = eAe (= eA)\). Via Lemma 7.2 we identify \(A_+\) with \(\mathbb{Q}L\). The functor*

\[
- \otimes_{\mathbb{Q}L} eA \; : \quad \mathbf{Proj}(\mathbb{Q}L) \longrightarrow \mathbf{Proj}(A)
\]

*identifies the category of finitely generated projective right \(\mathbb{Q}L\)-modules with the full subcategory of finitely generated projective right \(A\)-modules \(P\) satisfying \(Pe = P\). Under this identification the duality \(P \mapsto \mathrm{Hom}_A(P, A)\) (with the involution convention just mentioned) corresponds to the usual duality over \(\mathbb{Q}L\). Consequently a symmetric Poincar\(\acute{\text{e}}\) chain equivalence on a finite projective \(\mathbb{Q}L\)-complex tensors to a symmetric Poincar\(\acute{\text{e}}\) chain equivalence on the induced \(A\)-complex.*

**Proof.** Because \(e\) is a central idempotent the ring \(A\) is the direct product \(eA \times (1 - e)A\), and a right \(A\)-module is the same thing as a pair of modules over the two factors. The induction functor sends a \(\mathbb{Q}L(= A_+)\)-module \(C\) to the pair \((C, 0)\); the inverse on the indicated full subcategory is \(P \mapsto Pe = P\). Projectivity and exactness are preserved by this equivalence.

It remains only to note that the duals match. If \(P = Pe\) and \(f : P \to A\) is \(A\)-linear, then \(f(P) = f(Pe) = f(P)e \subset Ae = eA\); hence

\[
\mathrm{Hom}_A(P, A) = \mathrm{Hom}_A(P, eA) = \mathrm{Hom}_{eAe}(Pe, eAe).
\]

Via the isomorphism \(eAe \cong \mathbb{Q}L\) this is precisely the ordinary dual of the corresponding \(\mathbb{Q}L\)-module, and the involutions agree because \(e^* = e\). Applying the equivalence degreewise to a chain complex shows that a chain equivalence and its adjoint remain such after tensoring, which is the Poincar\(\acute{\text{e}}\) assertion. \(\square\)

The manifold \(N\) determines an \(n\)-dimensional (symmetric) Poincar\(\acute{\text{e}}\) chain complex structure on \(C_*(\widetilde{N};\mathbb{Q})\) over \(\mathbb{Q}L\) (coming from the fundamental class and a cellular diagonal approximation). By Lemma 7.4 and the exactness of \(- \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma\) this Poincar\(\acute{\text{e}}\) structure extends to \(P_*\) by extension of scalars. Thus:

**Proposition 7.5** (A projective \(\mathbb{Q}\Gamma\)-Poincar\(\acute{\text{e}}\) complex). *The chain complex \(P_*\) is a finite \(n\)-dimensional projective Poincar\(\acute{\text{e}}\) chain complex over \(\mathbb{Q}\Gamma\) with \(H_0(P_*) \cong \mathbb{Q}\) and \(H_i(P_*) = 0\) for \(i > 0\).*

It is useful to keep track of orientations for the later surgery step. The orientation module of this Poincar\(\acute{\text{e}}\) complex (and hence of all subsequent \(\mathbb{Q}\)-Poincar\(\acute{\text{e}}\) spaces we construct) is trivial: the manifold \(N\) is orientable and the homomorphism \(\Gamma \to SO^+(n,1)\) factors through the orientation-preserving group, while the central element \(z\) acts trivially on the fundamental class.

### 7.0.4 Step 3: Vanishing of Wall's finiteness obstruction and realization by a finite CW complex

We now compute the Wall finiteness obstruction and then appeal to the standard realization theorem over subrings of \(\mathbb{Q}\).

The Wall finiteness obstruction of a finitely dominated CW complex (or, equivalently, of a finite projective chain complex modeling its universal cover) lies in the reduced group \(\widetilde{K}_0(\mathbb{Q}\Gamma)\). In our setting it is represented by the alternating sum of chain modules:

\[
o(P_*) \; = \; \sum_{i=0}^{n} (-1)^i [P_i] \; = \; \sum_{i=0}^{n} (-1)^i c_i \, [e\mathbb{Q}\Gamma] \; = \; \chi(N) \, [e\mathbb{Q}\Gamma] \; \in K_0(\mathbb{Q}\Gamma). \tag{45}
\]

Since \(N\) is a closed orientable manifold of odd dimension \(n\), we have \(\chi(N) = 0\). Therefore \(o(P_*) = 0\) already in \(K_0(\mathbb{Q}\Gamma)\), hence also in \(\widetilde{K}_0(\mathbb{Q}\Gamma)\).

We shall use the following precise form of Wall's realization theorem. Recall that \(\Gamma\) is finitely presented (Step 1).

**Theorem 7.6** (Wall--Ranicki realization over localizations). *Let \(R \subset \mathbb{Q}\) be a subring and let \(\pi\) be a finitely presented group. Let \(C_*\) be a finite chain complex of finitely generated projective right \(R\pi\)-modules, concentrated in degrees \(0, \ldots, n\), with \(H_i(C_*) = 0\) for \(i > 0\) and \(H_0(C_*) \cong R\) (trivial action). Its Wall obstruction is the class \(\sum (-1)^i[C_i] \in \widetilde{K}_0(R\pi)\). If this class is zero, then there exists a finite connected CW complex \(X\) with \(\pi_1(X) \cong \pi\) such that*

\[
C_*(\widetilde{X}; R) \; \simeq \; C_*
\]

*as chain complexes of \(R\pi\)-modules. If in addition \(C_*\) carries an \(n\)-dimensional symmetric Poincar\(\acute{\text{e}}\) chain-complex structure, \(X\) may be chosen to be a finite \(R\)-Poincar\(\acute{\text{e}}\) complex of formal dimension \(n\) (elementary algebraic expansions do not change the Poincar\(\acute{\text{e}}\) type).*

For the reader's convenience let us also indicate references for this statement. Wall constructs, from an algebraic \(R\pi\)-complex (for \(R\) a localization of \(\mathbb{Z}\), in particular a subring of \(\mathbb{Q}\)), a finitely dominated CW complex with the prescribed cellular \(R\pi\)-chains and proves that the obstruction above is the only one to making it finite; see Wall [8, Thm. F and \S\S 2--5]. The algebraic reformulation for projective complexes, and the fact that elementary expansions do not change symmetric structures, is spelled out in Ranicki [5]. Let us also make explicit the small piece of algebra which allows one to pass from rational matrices to honest cell attachments. If the obstruction vanishes, adding finitely many elementary contractible projective complexes replaces a finite projective resolution by a *based free* resolution. Choose a finite presentation of \(\pi\) and choose the bases in degrees 0 and 1 (and a relator summand in degree 2) so that the corresponding part of the differential is the cellular differential of the presentation 2-complex. By elementary changes of basis over \(R\pi\) one may further suppose that any additional basis vectors in degree 2 have zero boundary (the relator columns already generate \(\ker \partial_1\)). In the present paper we only need the case \(R = \mathbb{Q}\). The remaining boundary matrices have entries in \(\mathbb{Q}\pi\), and then there is a simple simultaneous clearing of denominators: writing these matrices in the chosen bases, pick diagonal change-of-basis matrices \(T_i\) (with non-zero integer entries) inductively for \(i \geq 2\), starting with \(T_0 = T_1 = 1\), so that \(T_{i-1}^{-1}\partial_i T_i\) has coefficients in \(\mathbb{Z}\pi\) for every \(i\) (for a fixed \(T_{i-1}\) one merely takes the entries of the diagonal of \(T_i\) large enough to clear the denominators in each column). The conjugated complex is isomorphic to the original over \(R\pi\). Wall's cellular realization then starts from the presentation 2-complex for \(\pi\) and attaches cells in dimensions \(\geq 3\) to realize this integral free complex up to \(R\)-chain equivalence; the relative Hurewicz theorem identifies the necessary homotopy and homology classes.

**Proposition 7.7** (Realization by a finite CW complex). *There exists a finite CW complex \(X\) with \(\pi_1(X) \cong \Gamma\) such that, as chain complexes of right \(\mathbb{Q}\Gamma\)-modules,*

\[
C_*(\widetilde{X};\mathbb{Q}) \; \simeq \; P_*. \tag{46}
\]

*Moreover \(X\) is a finite \(\mathbb{Q}\)-Poincar\(\acute{\text{e}}\) complex of formal dimension \(n\), and \(\widetilde{X}\) is \(\mathbb{Q}\)-acyclic in positive degrees.*

**Proof.** The computation (45) gives a vanishing obstruction. Applying Theorem 7.6 with \(R = \mathbb{Q}\), \(\pi = \Gamma\) and \(C_* = P_*\) yields a finite CW complex whose cellular rational chain complex is chain-homotopy equivalent to \(P_*\). The last assertions follow from the Poincar\(\acute{\text{e}}\) structure on \(P_*\) (Proposition 7.5) and from Lemma 7.3. \(\square\)

For later use let us spell out explicitly why the finite complex just obtained is a genuine Poincar\(\acute{\text{e}}\) space (and not merely a complex with the right algebraic chains). The symmetric Poincar\(\acute{\text{e}}\) chain equivalence on the finite projective resolution \(P_*\) is equivalent to the following cohomological statement: there is a class

\[
\alpha \in H_n(\Gamma;\mathbb{Q})
\]

whose cap product induces isomorphisms \(H^i(\Gamma; M) \xrightarrow{\cong} H_{n-i}(\Gamma; M)\) (with the usual orientation twist) for every \(\mathbb{Q}\Gamma\)-module \(M\). This is simply another way of expressing the algebraic Poincar\(\acute{\text{e}}\) condition; see for example Brown's discussion of duality over coefficient rings in [2, Ch. VIII, \S\S 9--10] or Ranicki [5].

Since \(C_*(\widetilde{X};\mathbb{Q})\) is a free resolution of the trivial module, the classifying map induces isomorphisms \(H_*(X; M) \cong H_*(\Gamma; M)\) and \(H^*(X; M) \cong H^*(\Gamma; M)\) for every local system of \(\mathbb{Q}\)-vector spaces \(M\). Let \([X] \in H_n(X;\mathbb{Q})\) be the image of \(\alpha\) under this identification (equivalently, using the rational homology equivalence \(g : X \to N\) constructed in Step 4, the inverse image of the hyperbolic fundamental class). By the naturality of the cap product, capping with \([X]\) yields the Poincar\(\acute{\text{e}}\) duality isomorphisms on \(X\) with arbitrary local coefficients. Thus \(X\) is a finite \(\mathbb{Q}\)-Poincar\(\acute{\text{e}}\) complex of formal dimension \(n\), and the duality agrees with the algebraic symmetric structure transported from \(P_*\).

### 7.0.5 Step 4: Construction of a *geometric* rational normal invariant

The point at which one has to be a little careful is the passage from the algebraic Poincar\(\acute{\text{e}}\) complex of Step 2 to a datum to which the (geometric) surgery machine applies. We give the details here. We shall exhibit an honest stable real vector bundle over the finite complex \(X\) which is a *rational reduction* of the Spivak normal fibration of \(X\), and we shall check that the algebraic normal complex associated to it is exactly the one obtained by tensoring the normal complex of the hyperbolic manifold \(N\) with the idempotent module.

We begin by fixing a map to the hyperbolic manifold. Let \(c_X : X \to B\Gamma\) be the classifying map of the universal covering of the finite complex furnished by Proposition 7.7. Since \(C_*(\widetilde{X};\mathbb{Q})\) is a free resolution of the trivial \(\mathbb{Q}\Gamma\)-module, \(c_X\) induces isomorphisms on homology with trivial rational coefficients. The extension \(1 \to \{\pm 1\} \to \Gamma \xrightarrow{p} L \to 1\) gives a map of classifying spaces \(Bp : B\Gamma \to BL\) and, because the order of the kernel is invertible in \(\mathbb{Q}\), the transfer (or the Lyndon--Hochschild--Serre spectral sequence) shows that \(Bp\) is a \(\mathbb{Q}\)-homology equivalence [2, Ch. VII, \S 6]. Finally \(BL\) is (canonically up to homotopy) the aspherical manifold \(N = L \backslash \mathbb{H}^n\). We choose once and for all a cellular representative of the composite

\[
g \; : \; X \xrightarrow{c_X} B\Gamma \xrightarrow{Bp} BL \simeq N. \tag{47}
\]

It is a rational homology equivalence. Orient \(X\) in such a way that \(g_*[X] = [N]\) in \(H_n(-;\mathbb{Q})\).

Let \(\nu_N\) be the stable normal bundle of the smooth manifold \(N\) and put

\[
\xi \; := \; g^*\nu_N \tag{48}
\]

(up to adding a trivial summand in order to have an honest vector bundle of large rank over the finite skeleton of \(BO\)). We shall use the following elementary fact, which is often left implicit in accounts of rational surgery.

**Lemma 7.8** (Rational reductions of the Spivak fibration). *Let \(Y^n\) be a finite \(\mathbb{Q}\)-Poincar\(\acute{\text{e}}\) complex and let \(\eta\) be an oriented stable real vector bundle over \(Y\). Denote by \(U \in H^r(T(\eta);\mathbb{Q})\) the rational Thom class \((r = \mathrm{rank}\,\eta)\). Then there is, after adding a trivial summand to \(\eta\) if necessary, a stable map of spectra*

\[
\rho \; : \; S^{n+r} \longrightarrow T(\eta) \tag{49}
\]

*such that the Hurewicz image of \(\rho\) is the Thom image of the fundamental class of \(Y\) (over \(\mathbb{Q}\)). Consequently \((\eta, \rho)\) is a \(\mathbb{Q}\)-normal invariant of \(Y\): the sphere fibration of \(\eta\) is fibre homotopy equivalent to the Spivak normal fibration after rationalization and the cap product with the Thom class realizes the prescribed Poincar\(\acute{\text{e}}\) duality.*

**Proof.** We spell out the standard facts which enter. First of all a finite \(R\)-Poincar\(\acute{\text{e}}\) complex (with \(R\) a localization of \(\mathbb{Z}\)) has an \(R\)-Spivak normal fibration: this is a stable oriented spherical fibration \(\nu_Y^R\) over \(Y\) together with an \(R\)-local Thom--Pontryagin collapse \(c_\nu : S^{n+k} \to T(\nu_Y)\) whose cap product realizes the Poincar\(\acute{\text{e}}\) fundamental class. The construction and uniqueness are due to Spivak and Wall; for localizations see Sullivan's notes on localization and, in the form used in surgery with fundamental group, Hausmann [3, \S 1, Prop. 1.1 and Cor. 1.4] or Ranicki [5, Ch. 9, esp. \S\S 9.2--9.3]. We shall use this result with \(R = \mathbb{Q}\).

We next recall why such a fibration is automatically reducible after rationalization. Let \(BSG\) denote the classifying space of stable *oriented* spherical fibrations (the identity component of the stable group of homotopy self-equivalences of spheres). For \(i > 0\) one has \(\pi_i(BSG) = \pi_{i-1}^S\), the stable homotopy groups of spheres. By Serre's theorem these groups are finite. Consequently the rationalization \(BSG_{(0)}\) is contractible (the spaces involved are nilpotent). If \(\eta\) is an oriented stable real vector bundle over \(Y\), its underlying stable sphere fibration is classified by the composite \(Y \to BO \to BSG\); after rationalization this map is null. The same is true for the Spivak fibration, and there is therefore a fibre-homotopy equivalence of stable spherical fibrations over \(Y\)

\[
J(\eta)_{(0)} \; \simeq \; \nu_{Y(0)}. \tag{50}
\]

(The choice is unique up to homotopy.) Stabilizing by adding a trivial bundle we may suppose that the two representatives have the same fibre dimension, say \(r\).

The equivalence (50) induces a rational equivalence of Thom spectra and carries the rational Thom class of the Spivak fibration to a Thom class \(U \in H^r(T(\eta);\mathbb{Q})\). Composing the Spivak collapse \(c_\nu\) with the inverse Thom-space equivalence gives a stable map in the rational stable category \(S^{n+r}_{(0)} \to T(\eta)_{(0)}\). Since Thom spaces of bundles over finite complexes are finite spectra, such a rational map can be represented by an honest stable map after multiplying by a non-zero integer: the stable Hurewicz theorem (or, equivalently, the Atiyah--Hirzebruch spectral sequence together with the finiteness of the stable stems; see [7, Ch. IX, Thm. 3.1]) shows that \(\pi_*^S(E) \otimes \mathbb{Q} \cong H_*(E;\mathbb{Q})\) for finite spectra. We choose a representative and, if necessary, rescale the Thom class by the inverse integer (over the coefficient field \(\mathbb{Q}\)). This gives the map (49). By construction its Hurewicz image is precisely the Thom image of \([Y]\), and capping with the Thom class (equivalently, transporting the Thom class of the Spivak fibration) yields the Poincar\(\acute{\text{e}}\) duality isomorphisms with arbitrary local systems of \(\mathbb{Q}\)-vector spaces. Thus \((\eta, \rho)\) is a rational reduction of the Spivak fibration, i.e. a \(\mathbb{Q}\)-normal invariant in the sense used in rational surgery. \(\square\)

We apply the lemma to the bundle \(\xi = g^*\nu_N\). It remains to check that this *geometric* invariant is compatible with the algebraic calculations of Step 5. We make this explicit because the idempotent construction is slightly unusual.

**Proposition 7.9** (Identification with the idempotent normal complex). *Let the chain equivalence (46) be chosen as follows. Lift the map (47) to a cellular \(p\)-equivariant map of universal covers \(\widetilde{g} : \widetilde{X} \to \widetilde{N} = \mathbb{H}^n\); it induces a chain map of right \(\mathbb{Q}\Gamma\)-complexes*

\[
C_*(\widetilde{X};\mathbb{Q}) \longrightarrow C_*(\widetilde{N};\mathbb{Q}) \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma = P_* \tag{51}
\]

*(the module \(e\mathbb{Q}\Gamma\) is just the regular \(\mathbb{Q}L\)-module with the right action inflated along \(p\), so the formula is the evident one). Since both complexes are projective resolutions of the trivial module, the comparison theorem shows that (51) is a chain-homotopy equivalence; we take this as the equivalence in (46). With this choice the algebraic normal structure on \(C_*(\widetilde{X};\mathbb{Q})\) associated, in Ranicki's sense, to the rational normal invariant \((\xi, \rho)\) of Lemma 7.8 is exactly the structure obtained from the normal complex of the manifold \(N\) by tensoring over \(\mathbb{Q}L\) with the bimodule \(e\mathbb{Q}\Gamma\).*

**Proof.** Only naturality has to be checked. The cellular symmetric Poincar\(\acute{\text{e}}\) structure on \(C_*(\widetilde{N};\mathbb{Q})\) is obtained from a diagonal approximation and from the fundamental class of \(N\); the algebraic normal structure associated to \(\nu_N\) is represented by a Thom cocycle for this bundle. Pulling the Thom cocycle back by \(g\) gives the Thom cocycle of \(\xi\), and our orientation of \(X\) was chosen so that fundamental classes correspond. The diagonal approximation on \(X\) may be taken cellularly natural with respect to \(g\) (two choices give chain-homotopic symmetric structures). Ranicki's "symmetric construction" and his definition of an algebraic normal complex are functorial for exact functors of projective module categories compatible with involution and for maps of spaces: see [5, Chs. 1--3]. Applying this functoriality to the exact functor \(- \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma\) and to the chain equivalence (51) gives the asserted identification. Concretely, on the level of modules the equality follows from the identities \(e\,s(\lambda\mu) = e\,s(\lambda)s(\mu)\) (Lemma 7.2), and on homology from the naturality of cap product. \(\square\)

In particular the finite Poincar\(\acute{\text{e}}\) complex \(X\) constructed in Step 3 is equipped with an explicit stable vector bundle (indeed the pull-back of a bundle from a manifold) representing the algebraic normal datum whose surgery obstruction we compute next. This fills the gap between the idempotent algebra and the geometric input required by the rational surgery theorem.

### 7.0.6 Step 5: Vanishing of the rational surgery obstruction

Let \(n = 2m + 1 \geq 5\). Given an \(n\)-dimensional \(\mathbb{Q}\)-Poincar\(\acute{\text{e}}\) complex \(X\) with fundamental group \(\Gamma\) and a chosen normal invariant, there is a surgery obstruction in the (quadratic/symmetric) \(L\)-group \(L_n^h(\mathbb{Q}\Gamma)\) for the standard involution (we are in the orientable, trivial-orientation case); if it vanishes then \(X\) is normally cobordant to a closed manifold, and in fact can be realized by a closed manifold mapping to \(X\) inducing \(\pi_1\)-isomorphism and \(\mathbb{Q}\Gamma\)-homology equivalence. This is the rational surgery theorem in the presence of fundamental group, due to Hausmann and Ranicki (building on Sullivan--Wall), see [3, 5].

The key point in this construction is that the surgery obstruction of this normal datum is zero for a very concrete reason. Because the idempotent \(e\) is central (and is fixed by the involution) the rational group ring splits as a product of rings with involution

\[
\mathbb{Q}\Gamma \; \cong \; e\mathbb{Q}\Gamma e \times (1 - e)\mathbb{Q}\Gamma(1 - e),
\]

and algebraic \(L\)-theory is additive for such products. The normal complex chosen in Step 4 was obtained on the projective complex \(P_*\). The finite CW complex \(X\) of Step 3 has cellular chains free over \(\mathbb{Q}\Gamma\), but the chain equivalence (46) is obtained from \(P_*\) by adding elementary (contractible) summands. In the cobordism group \(L_n^h(\mathbb{Q}\Gamma)\) such summands represent the zero element. Consequently the surgery obstruction of \(X\) is represented by the induced normal complex on \(P_*\), and all of its chain modules are of the form \((e\mathbb{Q}\Gamma)^{c_i}\); the class therefore lies entirely in the first factor of the displayed product. Under the ring isomorphism \(e\mathbb{Q}\Gamma e \cong \mathbb{Q}L\) this first component is precisely the result of tensoring the identity normal complex of the manifold \(N\) with the bimodule \(e\mathbb{Q}\Gamma\).

Now the identity normal map \(\mathrm{id}_N : N \to N\) has surgery obstruction \(0 \in L_n^h(\mathbb{Q}L)\) (indeed it is already a manifold). Algebraic surgery is functorial for exact functors of projective module categories compatible with duality: applying \(- \otimes_{\mathbb{Q}L} e\mathbb{Q}\Gamma\) to a null-cobordism of the identity normal complex gives a null-cobordism of the induced normal complex (see Ranicki [5]). Thus the component of the obstruction in \(L_n^h(e\mathbb{Q}\Gamma e)\) is zero, and hence the obstruction of \(X\) in \(L_n^h(\mathbb{Q}\Gamma)\) is zero as well.

### 7.0.7 Step 6: Rational surgery produces a closed manifold with \(\mathbb{Q}\)-acyclic universal cover

We now apply the rational surgery theorem.

**Theorem 7.10** (Rational surgery realization). *Let \(R \subset \mathbb{Q}\) be a subring (equivalently a localization of \(\mathbb{Z}\)) and let \(Y^q\) be a finite connected \(R\)-Poincar\(\acute{\text{e}}\) complex, \(q \geq 5\), with fundamental group \(\pi\). Suppose that \(Y\) is equipped with an \(R\)-normal invariant: by this we mean, in the topological language, a stable real vector bundle (or stable spherical fibration) over \(Y\) together with an \(R\)-Thom class whose cap product realizes the Poincar\(\acute{\text{e}}\) fundamental class, and in the algebraic language equivalently an algebraic normal structure on the symmetric chain complex \(C_*(\widetilde{Y}; R)\) in Ranicki's sense. Associated to this datum is a surgery obstruction*

\[
\sigma(Y) \; \in \; L_q^h(R\pi)
\]

*(for the standard orientation character). If \(\sigma(Y) = 0\), then there exists a closed smooth \(q\)-manifold \(M\) and a normal map \(f : M \to Y\) representing the chosen invariant such that*

\[
\pi_1(M) \xrightarrow{\cong} \pi_1(Y) = \pi, \qquad f_* : H_*(M; R\pi) \xrightarrow{\cong} H_*(Y; R\pi).
\]

*In dimensions \(q \not\equiv 0 \pmod{4}\) no further numerical conditions occur; in dimension \(4k\) the equality of the signature with the Hirzebruch \(L\)-class determined by the chosen Pontryagin data is the additional requirement built into the choice of normal invariant.*

For the reader who wants precise sources we spell out where this statement is proved. Hausmann constructs, for localizations of \(\mathbb{Z}\), normal maps which are homology equivalences modulo the chosen localization and develops the corresponding obstruction theory in [3, \S\S 1--3]. The translation between such (localized) normal invariants and algebraic normal complexes, and the functoriality of the obstruction under exact functors of module categories, is part of Ranicki's algebraic surgery framework; see [5]. Because in our application the normal invariant is represented by an honest stable vector bundle (Lemma 7.8 and Proposition 7.9) the output of the theorem may be taken in the smooth category.

We apply Theorem 7.10 with \(R = \mathbb{Q}\), \(q = n = 2m + 1\), \(\pi = \Gamma\), and \(Y = X\) equipped with the normal invariant chosen in Step 4. The obstruction vanishes by Step 5. Hence we obtain:

**Proposition 7.11.** *There exists a closed smooth \(n\)-manifold \(M\) and a map \(f : M \to X\) inducing an isomorphism on \(\pi_1\) and an isomorphism on \(\mathbb{Q}\Gamma\)-homology:*

\[
\pi_1(M) \xrightarrow{\cong} \pi_1(X) = \Gamma, \qquad H_*(M;\mathbb{Q}\Gamma) \xrightarrow{\cong} H_*(X;\mathbb{Q}\Gamma).
\]

### 7.0.8 Step 7: The universal cover of \(M\) is \(\mathbb{Q}\)-acyclic

Let \(\widetilde{f} : \widetilde{M} \to \widetilde{X}\) be the lift of \(f\) to universal covers. Recall that with our convention of cellular right \(\Gamma\)-modules the chain complex computing homology of a connected complex with coefficients in the left regular module \(\mathbb{Q}\Gamma\) is \(C_*(\widetilde{Y};\mathbb{Z}) \otimes_{\mathbb{Z}\Gamma} \mathbb{Q}\Gamma\) for such a complex \(Y\), which identifies (by choosing one lift of each cell) with the ordinary cellular complex of the universal cover with rational coefficients. Thus the \(\mathbb{Q}\Gamma\)-homology equivalence in Proposition 7.11 is equivalently the statement that \(\widetilde{f}\) induces an isomorphism

\[
H_*(\widetilde{M};\mathbb{Q}) \xrightarrow{\cong} H_*(\widetilde{X};\mathbb{Q}).
\]

Using Proposition 7.7 and Lemma 7.3 we have

\[
H_i(\widetilde{X};\mathbb{Q}) \; \cong \; H_i(P_*) \; = \;
\begin{cases}
\mathbb{Q}, & i = 0, \\
0, & i > 0.
\end{cases}
\]

Therefore

\[
H_i(\widetilde{M};\mathbb{Q}) \; = \;
\begin{cases}
\mathbb{Q}, & i = 0, \\
0, & i > 0,
\end{cases}
\]

so the universal cover \(\widetilde{M}\) is \(\mathbb{Q}\)-acyclic in positive degrees.

### 7.0.9 Conclusion

We have produced, for each odd \(n = 2m + 1 \geq 5\), a uniform lattice \(\Gamma < \mathrm{Spin}(n,1)\) containing the central involution \(z = -1\) and a closed smooth \(n\)-manifold \(M\) with \(\pi_1(M) \cong \Gamma\) such that \(\widetilde{M}\) is acyclic over \(\mathbb{Q}\).

**Theorem 7.12.** *Yes: there exist uniform lattices \(\Gamma\) in real semisimple groups containing 2-torsion which occur as the fundamental groups of closed manifolds whose universal covers are \(\mathbb{Q}\)-acyclic.*

### 7.0.10 Compatibility with complete Euler characteristic obstructions

For context, we briefly explain why this example does not contradict familiar torsion/Euler characteristic obstructions. Brown defines the *complete Euler characteristic* \(\widetilde{\chi}(\Gamma)\) of a group of finite type, whose coefficients at conjugacy classes of finite order elements can be expressed, for cocompact lattices, in terms of Euler characteristics of centralizers (see [2, Ch. IX, \S 7]). In many settings, existence of a finite \(\mathbb{Q}\)-acyclic universal cover forces these coefficients to vanish away from the identity class.

In our example, by Remark 7.1, the only nontrivial finite order element is the central involution \(z\), and its centralizer is all of \(\Gamma\). The (rational) Euler characteristic of a group with a finite normal subgroup is multiplicative with the factor \(1/|F|\) (Brown [2, Ch. IX, \S 7]); consequently

\[
\chi_{\mathbb{Q}}(\Gamma) = \chi(L)/2 = \chi(N)/2.
\]

Equivalently, applying the Hattori--Stallings trace to the Wall element (45) shows that the complete Euler characteristic has coefficient \(\chi(N)/2\) both at the identity class and at the class of \(z\) (and no other finite classes). For odd \(n\) we have \(\chi(N) = 0\), so the coefficient at \(z\) indeed vanishes. In contrast, in even dimensions the Gauss--Bonnet formula for a compact hyperbolic manifold gives \(\chi(N) \neq 0\), and already the finiteness obstruction (45) is detected by this trace and is nonzero. Thus the odd-dimensional spin-lift construction gives a genuine positive answer precisely in the case compatible with these obstructions.

## References

[1] A. Borel and Harish-Chandra, *Arithmetic subgroups of algebraic groups*, Ann. of Math. (2) **75** (1962), 485--535.

[2] K. S. Brown, *Cohomology of Groups*, Graduate Texts in Mathematics **87**, Springer-Verlag, New York, 1982.

[3] J.-C. Hausmann, *Manifolds with a given homology and fundamental group*, Comment. Math. Helv. **53** (1978), 113--134.

[4] M. S. Raghunathan, *Discrete Subgroups of Lie Groups*, Ergebnisse der Mathematik und ihrer Grenzgebiete **68**, Springer-Verlag, 1972.

[5] A. Ranicki, *Algebraic and Geometric Surgery*, Oxford Mathematical Monographs, Oxford University Press, 2002.

[6] A. Selberg, *On discontinuous groups in higher-dimensional symmetric spaces*, in *Contributions to Function Theory (Internat. Colloq. Function Theory, Bombay, 1960)*, Tata Institute of Fundamental Research, Bombay, 1960, pp. 147--164.

[7] R. M. Switzer, *Algebraic Topology---Homotopy and Homology*, Classics in Mathematics, Springer-Verlag, Berlin, 2002.

[8] C. T. C. Wall, *Finiteness conditions for CW complexes*, Ann. of Math. (2) **81** (1965), 56--69.
