## 9 Algebraic relations among scaled quadri-linear determinant tensors

### Problem

Let \( n \geq 5 \). Let \( A^{(1)}, \ldots, A^{(n)} \in \mathbb{R}^{3 \times 4} \) be Zariski-generic. For \( \alpha, \beta, \gamma, \delta \in [n] \), construct \( Q^{(\alpha\beta\gamma\delta)} \in \mathbb{R}^{3 \times 3 \times 3 \times 3} \) so that its \( (i, j, k, \ell) \) entry for \( 1 \leq i, j, k, \ell \leq 3 \) is given by

\[
Q^{(\alpha\beta\gamma\delta)}_{ijk\ell} = \det[A^{(\alpha)}(i,:); A^{(\beta)}(j,:); A^{(\gamma)}(k,:); A^{(\delta)}(\ell,:)].
\]

Here \( A(i,:) \) denotes the \( i \)th row of a matrix \( A \), and semicolon denotes vertical concatenation. We are interested in algebraic relations on the set of tensors \( \{Q^{(\alpha\beta\gamma\delta)} : \alpha, \beta, \gamma, \delta \in [n]\} \).

More precisely, does there exist a polynomial map \( \mathbf{F} : \mathbb{R}^{81n^4} \to \mathbb{R}^N \) that satisfies the following three properties?

- The map \( \mathbf{F} \) does not depend on \( A^{(1)}, \ldots, A^{(n)} \).

- The degrees of the coordinate functions of \( \mathbf{F} \) do not depend on \( n \).

- Let \( \lambda \in \mathbb{R}^{n \times n \times n \times n} \) satisfy \( \lambda_{\alpha\beta\gamma\delta} \neq 0 \) for precisely \( \alpha, \beta, \gamma, \delta \in [n] \) that are not identical. Then \( \mathbf{F}(\lambda_{\alpha\beta\gamma\delta} Q^{(\alpha\beta\gamma\delta)} : \alpha, \beta, \gamma, \delta \in [n]) = 0 \) holds if and only if there exist \( u, v, w, x \in (\mathbb{R}^*)^n \) such that \( \lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta \) for all \( \alpha, \beta, \gamma, \delta \in [n] \) that are not identical.

### Solution

We give an explicit construction of such a map \( \mathbf{F} \) (in fact, with uniform degree 5). In the proof it is a little cleaner to work first over the algebraic closure \( \mathbb{C} \). At the end of the argument I explain why, for real data, the factors which are obtained over \( \mathbb{C} \) may in fact be chosen real. All polynomials which occur have real (indeed integral) coefficients.

### Step 0: packaging the tensors

Let

\[
R := [n] \times \{1, 2, 3\}, \qquad s = (\alpha, i) \in R,
\]

and write \( c(s) = \alpha \) (camera index) and \( r(s) = i \) (row index). Given an array \( x = (x_{ijk\ell}^{(\alpha\beta\gamma\delta)}) \in \mathbb{C}^{81n^4} \), define a single tensor \( \mathcal{X} \in (\mathbb{C}^{3n})^{\otimes 4} \) by

\[
\mathcal{X}_{stuv} := x_{r(s)r(t)r(u)r(v)}^{(c(s)c(t)c(u)c(v))}, \qquad s, t, u, v \in R. \tag{80}
\]

This identifies \( \mathbb{C}^{81n^4} \) with \( \mathbb{C}^{(3n)^4} \).

For \( p \in \{1, 2, 3, 4\} \), let \( \operatorname{Flat}_p(\mathcal{X}) \) be the mode-\( p \) flattening: it is the matrix obtained by grouping the \( p \)th index as a row index and the other three indices as a column index. Thus

\[
\operatorname{Flat}_p(\mathcal{X}) \in \mathbb{C}^{3n \times (3n)^3}.
\]

### Step 1: the polynomial map

Define \( \mathbf{F} \) by

\[
\mathbf{F}(x) := \Big( \text{all } 5 \times 5 \text{ minors of } \operatorname{Flat}_p(\mathcal{X}) \text{ for } p = 1, 2, 3, 4 \Big), \tag{81}
\]

where \( \mathcal{X} \) is obtained from \( x \) via (80). Each coordinate of \( \mathbf{F} \) is a determinant of a \( 5 \times 5 \) submatrix of a flattening, hence is a polynomial of degree 5 in the entries of \( x \). The definition uses only the input tensor \( x \) (and \( n \) through the index ranges), and does not involve the matrices \( A^{(\alpha)} \).

### Step 2: genericity hypotheses on the cameras

Stack all camera rows into a single matrix

\[
M \in \mathbb{C}^{3n \times 4}, \qquad \text{whose rows are } a_s \in \mathbb{C}^{1 \times 4} \quad (s \in R),
\]

so that the \( 3 \times 4 \) block of rows indexed by \( \{(\alpha, 1), (\alpha, 2), (\alpha, 3)\} \) equals \( A^{(\alpha)} \). After removing a proper algebraic subset of \( (\mathbb{C}^{3 \times 4})^n \), we may assume:

(G1) each \( A^{(\alpha)} \) has rank 3 (so its row space \( U_\alpha \subset \mathbb{C}^{1 \times 4} \) is a hyperplane);

(G2) \( M \) has rank 4 (equivalently, \( \operatorname{im}(M) \subset \mathbb{C}^{3n} \) is 4-dimensional);

(G3) for every ordered triple \( (\beta, \gamma, \delta) \in [n]^3 \) that is not constant,

\[
\operatorname{span}\{ u \wedge v \wedge w :\; u \in U_\beta,\; v \in U_\gamma,\; w \in U_\delta \} = \bigwedge^3 \mathbb{C}^4.
\]

Let us spell out why this open set is non-empty. All three requirements are conditions given by the non-vanishing of polynomial functions of the entries of the matrices. Thus it is enough to know that none of these polynomials is identically equal to zero. For (G1) this is clear (one \( 3 \times 3 \) minor of \( A^{(\alpha)} \) has to be non-zero), and for (G2) it suffices to note, for instance, that one may take a first camera whose three rows are the standard row vectors \( e_1, e_2, e_3 \) and a second camera with rows \( e_1, e_2, e_4 \) (along with arbitrary further blocks); the stacked matrix then has rank 4.

For the reader's convenience I also record an explicit verification for (G3). Put \( V = \mathbb{C}^4 \) and fix an ordered triple of indices which is not constant. The span which occurs in (G3) is the image of the multilinear map \( U_\beta \otimes U_\gamma \otimes U_\delta \to \bigwedge^3 V \), \( (u, v, w) \mapsto u \wedge v \wedge w \); after bases have been chosen in the three hyperplanes, the condition that this image have dimension four is the non-vanishing of some \( 4 \times 4 \) minor and hence is polynomial. This polynomial is not identically zero. Indeed, if two of the hyperplanes are equal we may (after a change of coordinates) take \( U_\beta = U_\gamma = \langle e_1, e_2, e_3 \rangle \) and \( U_\delta = \langle e_1, e_2, e_4 \rangle \); the wedges

\[
e_2 \wedge e_3 \wedge e_1, \quad e_2 \wedge e_4 \wedge e_1, \quad e_3 \wedge e_4 \wedge e_1, \quad e_2 \wedge e_3 \wedge e_4
\]

(which are obtained from suitable choices of \( u, v, w \)) already form a basis of \( \bigwedge^3 V \). If the three hyperplanes are pairwise distinct we may take \( U_\beta = \langle e_2, e_3, e_4 \rangle \), \( U_\gamma = \langle e_1, e_3, e_4 \rangle \) and \( U_\delta = \langle e_1, e_2, e_4 \rangle \), from which the four basis wedges of \( \bigwedge^3 V \) are obtained just as easily (for example \( e_2 \wedge e_3 \wedge e_1, e_2 \wedge e_4 \wedge e_1, e_3 \wedge e_4 \wedge e_1, e_2 \wedge e_3 \wedge e_4 \)). Permuting the roles of the indices gives the remaining cases. Consequently, for every fixed triple the failure of (G3) is a proper algebraic subset of the parameter space.

The ambient space \( (\mathbb{C}^{3 \times 4})^n \) is irreducible, and a finite intersection of non-empty Zariski open subsets of an irreducible variety is non-empty. Thus there are cameras satisfying (G1)--(G3), and in fact the set of such cameras is a Zariski open dense subset. All the defining polynomials have real coefficients, so this open subset contains real points (equivalently its real points are Euclidean dense). Hence a Zariski-generic real choice of \( A^{(1)}, \ldots, A^{(n)} \) satisfies (G1)--(G3).

### Step 3: linear-algebra preliminaries

Let \( W := \operatorname{im}(M) \subset \mathbb{C}^{3n} \), so \( \dim W = 4 \) by (G2).

**Lemma 9.1** (Cofactor vector). *For any \( t, u, v \in R \) there exists a (unique) vector \( \omega_{tuv} \in \mathbb{C}^4 \) such that*

\[
\det(x, a_t, a_u, a_v) = x\,\omega_{tuv}^T \qquad \forall\, x \in \mathbb{C}^{1 \times 4}.
\]

*Moreover, the column of \( \operatorname{Flat}_1(\mathcal{Y}) \) indexed by \( (t, u, v) \), where \( \mathcal{Y}_{stuv} = \det(a_s, a_t, a_u, a_v) \), equals \( M\,\omega_{tuv} \).*

**Proof.** The map \( x \mapsto \det(x, a_t, a_u, a_v) \) is linear in \( x \in \mathbb{C}^{1 \times 4} \), hence is given by \( x \mapsto x\,\omega^T \) for a unique \( \omega \in \mathbb{C}^4 \). The second claim is immediate since \( \bigl(\det(a_s, a_t, a_u, a_v)\bigr)_{s \in R} = \bigl(a_s\,\omega_{tuv}^T\bigr)_{s \in R} = M\,\omega_{tuv} \). \(\square\)

**Lemma 9.2** (Diagonal stabilizer is scalar). *Assume (G1)--(G2) and let \( D = \operatorname{diag}(d_\alpha I_3)_{\alpha=1}^n \in \mathbb{C}^{3n \times 3n} \) with each \( d_\alpha \in \mathbb{C} \). If \( DW \subseteq W \), then all \( d_\alpha \) are equal.*

**Proof.** Since \( \operatorname{rank}(M) = 4 \), the columns of \( M \) form a basis of \( W \). The inclusion \( DW \subseteq W \) therefore defines a (unique) linear endomorphism \( H \in M_4(\mathbb{C}) \) by

\[
DM = MH.
\]

(The matrix \( H \) need not be invertible if some of the \( d_\alpha \) vanish.) Restricting to the block of rows belonging to camera \( \alpha \) gives

\[
d_\alpha A^{(\alpha)} = A^{(\alpha)} H.
\]

Thus every row of \( A^{(\alpha)} \), and hence every vector in the row space \( U_\alpha \), is a left eigenvector of \( H \) with eigenvalue \( d_\alpha \). Any two hyperplanes in \( \mathbb{C}^4 \) have non-zero intersection (in fact of dimension at least two), so if \( y \in U_\alpha \cap U_{\alpha'} \) is non-zero we have \( yH = d_\alpha y = d_{\alpha'} y \), which forces \( d_\alpha = d_{\alpha'} \). Hence all \( d_\alpha \) are equal. \(\square\)

**Step 4: the tensor slice and the "easy" direction.** Given scalars \( \lambda \in \mathbb{C}^{n \times n \times n \times n} \), consider the tensor \( \mathcal{T} \in (\mathbb{C}^{3n})^{\otimes 4} \) defined by

\[
\mathcal{T}_{stuv} := \lambda_{c(s)c(t)c(u)c(v)} \det(a_s, a_t, a_u, a_v). \tag{82}
\]

This \( \mathcal{T} \) is exactly the packaging (80) of the family \( (\lambda_{\alpha\beta\gamma\delta} Q^{(\alpha\beta\gamma\delta)})_{\alpha,\beta,\gamma,\delta} \).

Assume first that \( \lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta \) for all non-identical quadruples and some \( u, v, w, x \in (\mathbb{C}^*)^n \). Fix a triple \( (\beta, \gamma, \delta) \) that is not constant. For the mode-1 flattening, the column indexed by \( (t, u, v) \) with \( c(t) = \beta, c(u) = \gamma, c(v) = \delta \) equals

\[
\bigl(\mathcal{T}_{stuv}\bigr)_{s \in R} = \operatorname{diag}(u_\alpha I_3)_{\alpha=1}^n \cdot \Big( v_\beta w_\gamma x_\delta \cdot (M\,\omega_{tuv}) \Big) \in \operatorname{diag}(u_\alpha I_3) W,
\]

by Lemma 9.1. If the suffix happens to be constant, say \( (\beta, \beta, \beta) \), the very same formula is still valid. Indeed \( \omega_{tuv} \) is then the covector associated with \( a_t \wedge a_u \wedge a_v \in \bigwedge^3 U_\beta \), so the entries of \( M\,\omega_{tuv} \) in the block of rows belonging to camera \( \beta \) are all zero (the determinant vanishes on the whole hyperplane \( U_\beta \)); multiplying by \( v_\beta w_\beta x_\beta \operatorname{diag}(u_\alpha I_3) \) therefore reproduces the column of \( \mathcal{T} \) as well -- for the row block \( \alpha = \beta \) both sides are simply zero, independently of the value of \( \lambda_{\beta\beta\beta\beta} \). Hence all columns of \( \operatorname{Flat}_1(\mathcal{T}) \), for arbitrary suffixes, lie in the fixed 4-plane \( \operatorname{diag}(u_\alpha I_3) W \), so \( \operatorname{rank}(\operatorname{Flat}_1(\mathcal{T})) \leq 4 \). The same argument applies to the other three flattenings. Therefore all \( 5 \times 5 \) minors in (81) vanish, i.e. \( \mathbf{F}(\mathcal{T}) = 0 \).

**Step 5: vanishing of minors forces one-mode factorization.** Assume now that \( \mathbf{F}(\mathcal{T}) = 0 \), i.e. every \( 5 \times 5 \) minor of every \( \operatorname{Flat}_p(\mathcal{T}) \) vanishes. Equivalently,

\[
\operatorname{rank}\bigl(\operatorname{Flat}_p(\mathcal{T})\bigr) \leq 4 \qquad \text{for } p = 1, 2, 3, 4. \tag{83}
\]

We use the standing assumption on \( \lambda \):

\[
\lambda_{\alpha\beta\gamma\delta} \neq 0 \quad \text{iff} \quad (\alpha, \beta, \gamma, \delta) \text{ is not all identical.} \tag{84}
\]

In particular, if a triple \( (\beta, \gamma, \delta) \) is not constant, then \( \lambda_{\alpha\beta\gamma\delta} \neq 0 \) for *all* \( \alpha \), hence the diagonal matrix

\[
D_{\beta\gamma\delta} := \operatorname{diag}(\lambda_{\alpha\beta\gamma\delta} I_3)_{\alpha=1}^n \tag{85}
\]

is invertible.

Fix a triple \( (\beta, \gamma, \delta) \) that is not constant. Consider the subcollection of columns of \( \operatorname{Flat}_1(\mathcal{T}) \) with fixed camera suffix \( (\beta, \gamma, \delta) \) and varying row choices within those cameras. By Lemma 9.1 these columns are precisely

\[
D_{\beta\gamma\delta} \cdot M\,\omega_{tuv} \quad \text{with } c(t) = \beta,\; c(u) = \gamma,\; c(v) = \delta.
\]

Condition (G3) implies that the vectors \( \omega_{tuv} \) (with this suffix) span \( \mathbb{C}^4 \): by (G1) the three rows in each camera form a basis of the corresponding hyperplane, and the cofactor construction is precisely the standard isomorphism \( \bigwedge^3 \mathbb{C}^4 \simeq (\mathbb{C}^4)^* \) (we have identified a covector with a column vector by means of the chosen coordinates). Hence these columns span \( D_{\beta\gamma\delta} W \). Therefore:

\[
\operatorname{span}\{\text{columns of } \operatorname{Flat}_1(\mathcal{T}) \text{ with suffix } (\beta, \gamma, \delta)\} = D_{\beta\gamma\delta} W. \tag{86}
\]

Now choose three distinct cameras \( b, c, d \) (possible since \( n \geq 5 \)) and let \( U_1 \) denote the full column space of \( \operatorname{Flat}_1(\mathcal{T}) \). By (86) applied to \( (b, c, d) \) we have \( D_{bcd} W \subseteq U_1 \), and since \( D_{bcd} \) is invertible and \( \dim W = 4 \), we get \( \dim(D_{bcd} W) = 4 \). Combined with (83) for \( p = 1 \), this forces

\[
U_1 = D_{bcd} W.
\]

Applying (86) to any non-constant triple \( (\beta, \gamma, \delta) \) yields \( D_{\beta\gamma\delta} W \subseteq U_1 = D_{bcd} W \), equivalently

\[
H_{\beta\gamma\delta} W = W, \qquad H_{\beta\gamma\delta} := D_{bcd}^{-1} D_{\beta\gamma\delta}.
\]

But \( H_{\beta\gamma\delta} \) is diagonal of the form \( \operatorname{diag}(h_\alpha I_3)_{\alpha=1}^n \). By Lemma 9.2, \( H_{\beta\gamma\delta} \) must be a scalar multiple of the identity, so there exists \( f_{\beta\gamma\delta} \in \mathbb{C}^* \) such that

\[
\frac{\lambda_{\alpha\beta\gamma\delta}}{\lambda_{\alpha bcd}} = f_{\beta\gamma\delta} \qquad \forall\,\alpha.
\]

Setting \( u_\alpha := \lambda_{\alpha bcd} \) gives the *mode-1 factorization*

\[
\lambda_{\alpha\beta\gamma\delta} = u_\alpha\, f_{\beta\gamma\delta} \qquad \text{whenever } (\beta, \gamma, \delta) \text{ is not constant.} \tag{87}
\]

Repeating the same argument for the other flattenings (choosing, for the reference triples, any three distinct cameras such as the \( b, c, d \) above with the roles of the modes permuted) gives vectors \( v, w \in (\mathbb{C}^*)^n \) -- one may take for instance \( v_\beta = \lambda_{b\beta cd} \) and \( w_\gamma = \lambda_{bc\gamma d} \) -- and functions \( g, h \) such that

\[
\lambda_{\alpha\beta\gamma\delta} = v_\beta\, g_{\alpha\gamma\delta} \qquad \text{whenever } (\alpha, \gamma, \delta) \text{ is not constant,} \tag{88}
\]

\[
\lambda_{\alpha\beta\gamma\delta} = w_\gamma\, h_{\alpha\beta\delta} \qquad \text{whenever } (\alpha, \beta, \delta) \text{ is not constant.} \tag{89}
\]

### Step 6: gluing the one-mode factorizations

Let

\[
E_1 := \{(\beta, \gamma, \delta) \in [n]^3 :\; (\beta, \gamma, \delta) \text{ is not constant}\}.
\]

From (87)--(88) we produce a function of two indices. Fix \( (\gamma, \delta) \in [n]^2 \). Choose indices \( \alpha_0, \beta_0 \) such that \( (\beta_0, \gamma, \delta) \in E_1 \) and \( (\alpha_0, \gamma, \delta) \) is not constant (e.g. if \( \gamma = \delta \), take \( \alpha_0 \neq \gamma \) and \( \beta_0 \neq \gamma \); otherwise any choice works). Define

\[
r_{\gamma\delta} := \frac{\lambda_{\alpha_0 \beta_0 \gamma\delta}}{u_{\alpha_0} v_{\beta_0}}. \tag{90}
\]

This is well-defined (independent of the choice): indeed, whenever both (87) and (88) apply we have

\[
\frac{\lambda_{\alpha\beta\gamma\delta}}{u_\alpha v_\beta} = \frac{f_{\beta\gamma\delta}}{v_\beta} = \frac{g_{\alpha\gamma\delta}}{u_\alpha},
\]

so the quotient depends only on \( (\gamma, \delta) \). In particular, for any fixed \( (\gamma, \delta) \) and any \( \beta \) with \( (\beta, \gamma, \delta) \in E_1 \) we may choose an index \( \alpha' \) (different from \( \gamma = \delta \) if these two are equal) for which \( (\alpha', \gamma, \delta) \) is not constant; applying the displayed equality to \( (\alpha', \beta) \) shows that \( f_{\beta\gamma\delta}/v_\beta = r_{\gamma\delta} \). Substituting this value in (87) gives, for every \( \alpha \) (even if \( (\alpha, \gamma, \delta) \) should be constant),

\[
\lambda_{\alpha\beta\gamma\delta} = u_\alpha\, v_\beta\, r_{\gamma\delta} \qquad \text{for all } (\beta, \gamma, \delta) \in E_1 \text{ and all } \alpha. \tag{91}
\]

Now use (89) to split \( r_{\gamma\delta} \) multiplicatively. Fix \( \delta \in [n] \) and choose \( \alpha_0, \beta_0 \) with \( \alpha_0 \neq \delta \) and \( \beta_0 \neq \delta \). Then \( (\alpha_0, \beta_0, \delta) \) is not constant, so (89) applies, and moreover \( (\beta_0, \gamma, \delta) \in E_1 \) for every \( \gamma \) (since \( \beta_0 \neq \delta \)). Thus, for all \( \gamma \),

\[
u_{\alpha_0} v_{\beta_0}\, r_{\gamma\delta} = \lambda_{\alpha_0 \beta_0 \gamma\delta} = w_\gamma\, h_{\alpha_0 \beta_0 \delta}.
\]

Hence \( r_{\gamma\delta}/w_\gamma \) is independent of \( \gamma \); define \( x_\delta \in \mathbb{C}^* \) by

\[
x_\delta := \frac{h_{\alpha_0 \beta_0 \delta}}{u_{\alpha_0} v_{\beta_0}}.
\]

Then \( r_{\gamma\delta} = w_\gamma x_\delta \), and substituting into (91) yields

\[
\lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta \qquad \text{whenever } (\beta, \gamma, \delta) \in E_1. \tag{92}
\]

It remains to treat the triples *not* in \( E_1 \), i.e. \( (\beta, \gamma, \delta) = (\beta, \beta, \beta) \). For \( \alpha \neq \beta \), the quadruple \( (\alpha, \beta, \beta, \beta) \) is not all identical, so \( \lambda_{\alpha\beta\beta\beta} \neq 0 \) by (84). Fix such \( \alpha \neq \beta \) and choose \( \eta \in [n] \) with \( \eta \neq \beta \). Then (89) (with \( \delta = \beta \) and \( (\alpha, \beta, \beta) \) not constant) gives

\[
\lambda_{\alpha\beta\gamma\beta} = w_\gamma\, h_{\alpha\beta\beta} \qquad \forall\,\gamma. \tag{93}
\]

Taking \( \gamma = \eta \) and using (92) for the quadruple \( (\alpha, \beta, \eta, \beta) \) (which has \( (\beta, \eta, \beta) \in E_1 \) since \( \eta \neq \beta \)) yields

\[
w_\eta\, h_{\alpha\beta\beta} = \lambda_{\alpha\beta\eta\beta} = u_\alpha v_\beta w_\eta x_\beta,
\]

so \( h_{\alpha\beta\beta} = u_\alpha v_\beta x_\beta \). Plugging \( \gamma = \beta \) into (93) gives

\[
\lambda_{\alpha\beta\beta\beta} = w_\beta\, h_{\alpha\beta\beta} = u_\alpha v_\beta w_\beta x_\beta.
\]

Thus the factorization holds for all quadruples that are not all identical:

\[
\lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta \qquad \text{for every } (\alpha, \beta, \gamma, \delta) \text{ not all identical.}
\]

**Step 7: returning to real scalars.** It remains only to justify the passage from the complex argument to the real statement formulated in the problem. We shall use the following elementary observation. Suppose that all the numbers \( \lambda_{\alpha\beta\gamma\delta} \) are real and satisfy (84), and suppose that for some complex vectors \( u, v, w, x \in (\mathbb{C}^*)^n \) the equality

\[
\lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta \tag{94}
\]

holds for every non-identical quadruple. Then the four vectors may be chosen with real (non-zero) entries.

For completeness I give the short proof. Choose three distinct indices \( p, q, r \in [n] \) (this is the only place where fewer than five indices would in fact have sufficed). From (94) we get, for example,

\[
\frac{u_\alpha}{u_p} = \frac{\lambda_{\alpha pqr}}{\lambda_{ppqr}} \in \mathbb{R}^* \quad (\alpha \in [n]),
\]

and in the same way \( v_\beta / v_p = \lambda_{p\beta qr}/\lambda_{ppqr} \), \( w_\gamma / w_p = \lambda_{pq\gamma r}/\lambda_{pqpr} \) and \( x_\delta / x_p = \lambda_{pqr\delta}/\lambda_{pqrp} \) are real and non-zero. (Every displayed denominator is legitimate because the corresponding quadruple is not all identical.) Thus all entries of (say) \( u \) have the same complex phase up to a sign, and the same is true for \( v, w, x \). Write \( u_p = |u_p| e^{i\theta} \), \( v_p = |v_p| e^{i\phi} \), \( w_p = |w_p| e^{i\psi} \) and \( x_p = |x_p| e^{i\chi} \). Since, for example, the product corresponding to the non-identical quadruple \( (p, p, q, r) \), \( u_p v_p w_q x_r = \lambda_{ppqr} \), is a non-zero real number, the sum \( \theta + \phi + \psi + \chi \) is congruent to 0 modulo \( \pi \) (the possible signs of the real ratios such as \( w_q/w_p \) and \( x_r/x_p \) only add integer multiples of \( \pi \)).

Define \( \tilde{u}_\alpha = e^{-i\theta} u_\alpha \), \( \tilde{v}_\beta = e^{-i\phi} v_\beta \), \( \tilde{w}_\gamma = e^{-i\psi} w_\gamma \) and \( \tilde{x}_\delta = e^{-i\chi} x_\delta \). These numbers are all real and non-zero, and for every non-identical quadruple their product equals \( e^{-i(\theta + \phi + \psi + \chi)} \lambda_{\alpha\beta\gamma\delta} \). If this common factor is \( -1 \) rather than \( +1 \), we simply change the sign of one of the four real vectors. In either case (94) holds with real factors.

**Conclusion.** The map \( \mathbf{F} \) defined by (81) is independent of the cameras, each coordinate has degree 5 (independent of \( n \)), and for Zariski-generic \( A^{(1)}, \ldots, A^{(n)} \) it satisfies the desired characterization. More explicitly, for every real array \( \lambda \) obeying (84),

\[
\mathbf{F}\bigl((\lambda_{\alpha\beta\gamma\delta} Q^{(\alpha\beta\gamma\delta)})_{\alpha,\beta,\gamma,\delta}\bigr) = 0 \quad \Longleftrightarrow \quad \exists\, u, v, w, x \in (\mathbb{R}^*)^n \text{ such that } \lambda_{\alpha\beta\gamma\delta} = u_\alpha v_\beta w_\gamma x_\delta
\]

for all non-identical quadruples. Conversely, any such real factorization (and a fortiori any complex one) makes all the minors in (81) vanish, as was shown in Step 4. This is precisely the polynomial map required in the statement of the problem. \(\square\)
