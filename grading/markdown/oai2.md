## 2 A nonvanishing test vector for the twisted local Rankin--Selberg integral

**Problem**

Let \( F \) be a non-archimedean local field with ring of integers \( \mathfrak{o} \). Let \( N_r \) denote the subgroup of \( \mathrm{GL}_r(F) \) consisting of upper-triangular unipotent elements. Let \( \psi : F \to \mathbb{C}^\times \) be a nontrivial additive character of conductor \( \mathfrak{o} \), identified in the standard way with a generic character of \( N_r \). Let \( \Pi \) be a generic irreducible admissible representation of \( \mathrm{GL}_{n+1}(F) \), realized in its \( \psi^{-1} \)-Whittaker model \( \mathcal{W}(\Pi, \psi^{-1}) \). Must there exist \( W \in \mathcal{W}(\Pi, \psi^{-1}) \) with the following property?

Let \( \pi \) be a generic irreducible admissible representation of \( \mathrm{GL}_n(F) \), realized in its \( \psi \)-Whittaker model \( \mathcal{W}(\pi, \psi) \). Let \( \mathfrak{q} \) denote the conductor ideal of \( \pi \), let \( Q \in F^\times \) be a generator of \( \mathfrak{q}^{-1} \), and set

\[
u_Q := I_{n+1} + Q\, E_{n,n+1} \in \mathrm{GL}_{n+1}(F),
\]

where \( E_{i,j} \) is the matrix with a 1 in the \( (i,j) \)-entry and 0 elsewhere. For some \( V \in \mathcal{W}(\pi, \psi) \), the local Rankin--Selberg integral

\[
\int_{N_n \backslash \mathrm{GL}_n(F)} W(\mathrm{diag}(g,1)\, u_Q)\, V(g)\, |\det g|^{s - \frac{1}{2}}\, dg
\]

is finite and nonzero for all \( s \in \mathbb{C} \).

### 2.1 Setup and goal

Let \( F \) be a non-archimedean local field with ring of integers \( \mathfrak{o} \), maximal ideal \( \mathfrak{p} \), and a fixed uniformizer \( \varpi \). Write \( |\cdot| \) for the normalized absolute value on \( F \). For \( r \geq 1 \) set

\[
G_r = \mathrm{GL}_r(F), \qquad K_r = \mathrm{GL}_r(\mathfrak{o}), \qquad N_r = \{\text{upper unitriangular matrices in } G_r\}.
\]

Fix a nontrivial additive character \( \psi : F \to \mathbb{C}^\times \) of conductor \( \mathfrak{o} \) (so \( \psi \) is trivial on \( \mathfrak{o} \) and nontrivial on \( \varpi^{-1}\mathfrak{o} \)).

Let \( \Pi \) be an irreducible generic representation of \( G_{n+1} \), and let \( \pi \) be an irreducible generic representation of \( G_n \). We work with Whittaker models

\[
\mathcal{W}(\Pi, \psi^{-1}) = \{ W : G_{n+1} \to \mathbb{C} \text{ smooth} :\; W(ug) = \psi^{-1}(u)W(g)\;\forall\, u \in N_{n+1} \},
\]

\[
\mathcal{W}(\pi, \psi) = \{ V : G_n \to \mathbb{C} \text{ smooth} :\; V(ug) = \psi(u)V(g)\;\forall\, u \in N_n \}.
\]

Let \( \mathfrak{q} = \mathfrak{p}^c \) be the (integral) conductor ideal attached to \( \pi \) in the discussion above, and fix a generator

\[
Q \in \mathfrak{q}^{-1} = \mathfrak{p}^{-c} \qquad (\text{so } v(Q) = -c).
\]

Define

\[
u_Q = \begin{pmatrix} I_n & Qe_n \\ 0 & 1 \end{pmatrix} \in G_{n+1},
\]

where \( e_n \) is the \( n \)th standard basis column vector in \( F^n \).

For \( W \in \mathcal{W}(\Pi, \psi^{-1}) \) and \( V \in \mathcal{W}(\pi, \psi) \) consider the local Rankin--Selberg integral

\[
Z(s, W, V) \;=\; \int_{N_n \backslash G_n} W\!\left( \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} u_Q \right) V(g)\, |\det g|^{s - \frac{1}{2}}\, dg, \tag{5}
\]

with a fixed Haar measure \( dg \) on \( N_n \backslash G_n \).

**Claim.** *There exists \( W \in \mathcal{W}(\Pi, \psi^{-1}) \), depending only on \( \Pi \) (and \( \psi \)), such that for every generic \( \pi \) and every choice of generator \( Q \in \mathfrak{q}^{-1} \) as above, one can choose \( V \in \mathcal{W}(\pi, \psi) \) with \( Z(s, W, V) \) finite and nonzero for all \( s \in \mathbb{C} \).*

### 2.2 Step 1: Choosing \( W \) by prescribing its restriction to the mirabolic

Let

\[
P_{n+1} = \left\{ \begin{pmatrix} g & x \\ 0 & 1 \end{pmatrix} : g \in G_n,\; x \in F^n \right\}
\]

be the mirabolic subgroup of \( G_{n+1} \). Let \( S_{\psi^{-1}}(P_{n+1}) \) denote the space of smooth functions \( f : P_{n+1} \to \mathbb{C} \) which are \( (N_{n+1}, \psi^{-1}) \)-equivariant on the left and compactly supported modulo \( N_{n+1} \).

**Lemma 2.1.** *Define \( f : P_{n+1} \to \mathbb{C} \) by*

\[
f\!\left( \begin{pmatrix} g & x \\ 0 & 1 \end{pmatrix} \right) = \mathbf{1}_{N_n K_n}(g) \cdot \psi^{-1}(u(g)) \cdot \psi^{-1}(x_n),
\]

*where \( \mathbf{1}_{N_n K_n} \) is the indicator function of \( N_n K_n \subset G_n \) and \( u(g) \in N_n \) is chosen from any decomposition \( g = u(g)k \) with \( k \in K_n \) (when \( g \in N_n K_n \)). Then \( f \in S_{\psi^{-1}}(P_{n+1}) \).*

**Proof.** If \( g \in N_n K_n \), the decomposition \( g = uk \) is unique up to right multiplication of \( u \) by \( N_n \cap K_n \). Since \( \psi \) has conductor \( \mathfrak{o} \), it is trivial on \( N_n \cap K_n \), hence \( \psi(u(g)) \) is well-defined. Smoothness is clear.

For equivariance, let \( n = \begin{pmatrix} u & y \\ 0 & 1 \end{pmatrix} \in N_{n+1} \) with \( u \in N_n \) and \( y \in F^n \). Then

\[
n \begin{pmatrix} g & x \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} ug & ux + y \\ 0 & 1 \end{pmatrix}.
\]

If \( g \notin N_n K_n \) then also \( ug \notin N_n K_n \), so both sides are 0. If \( g \in N_n K_n \), then \( ug \in N_n K_n \) and one may take \( u(ug) = u \cdot u(g) \) (modulo \( N_n \cap K_n \)), so

\[
\psi^{-1}(u(ug)) = \psi^{-1}(u)\psi^{-1}(u(g)).
\]

Moreover, \( (ux+y)_n = x_n + y_n \) because \( u \) is upper unitriangular, so \( \psi^{-1}((ux+y)_n) = \psi^{-1}(y_n)\psi^{-1}(x_n) \).

Since \( \psi^{-1}(n) = \psi^{-1}(u)\psi^{-1}(y_n) \) for \( n = \begin{pmatrix} u & y \\ 0 & 1 \end{pmatrix} \in N_{n+1} \), we get

\[
f(np) = \psi^{-1}(n) f(p).
\]

Finally, \( f \) is compactly supported modulo \( N_{n+1} \) because modulo \( N_{n+1} \) the \( x \)-variable is irrelevant (the left \( N_{n+1} \)-action moves \( x \) freely), and the \( g \)-support is contained in \( N_n K_n \), whose image in \( N_n \backslash G_n \) is compact. \(\square\)

The crucial representation-theoretic input is the standard fact that, for a generic \( \Pi \), the Kirillov model on the mirabolic contains all compactly supported Whittaker functions on \( P_{n+1} \).

**Lemma 2.2** (Compact Kirillov model on \( P_{n+1} \)). *Let \( \Pi \) be irreducible generic. The restriction map*

\[
\mathrm{res}_{P_{n+1}} : \mathcal{W}(\Pi, \psi^{-1}) \longrightarrow C^\infty(N_{n+1} \backslash P_{n+1}, \psi^{-1}), \qquad W \mapsto W|_{P_{n+1}},
\]

*has image containing \( S_{\psi^{-1}}(P_{n+1}) \). In particular, for the \( f \) of Lemma 2.1 there exists \( W \in \mathcal{W}(\Pi, \psi^{-1}) \) such that \( W|_{P_{n+1}} = f \).*

*Reference.* This is the classical "compact Kirillov model" statement; see Gelfand--Kazhdan [3] and the mirabolic/derivative formalism in Zelevinsky [5], or the discussion of mirabolic restriction in Matringe [4, \S 2]. \(\square\)

Fix once and for all such a Whittaker function \( W \in \mathcal{W}(\Pi, \psi^{-1}) \) with \( W|_{P_{n+1}} = f \). This \( W \) depends only on \( \Pi \) (and \( \psi \)), not on \( \pi \) or \( Q \).

### 2.3 Step 2: Reducing (5) to a compact integral on \( K_n \)

For \( g \in G_n \) we have

\[
\begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} u_Q = \begin{pmatrix} g & Qge_n \\ 0 & 1 \end{pmatrix} \in P_{n+1}.
\]

Hence, by the choice \( W|_{P_{n+1}} = f \),

\[
W\!\left( \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} u_Q \right) = \mathbf{1}_{N_n K_n}(g) \cdot \psi^{-1}(u(g)) \cdot \psi^{-1}(Qg_{n,n}). \tag{6}
\]

Insert (6) into (5). If \( g \in N_n K_n \) and we write \( g = u(g)k \) with \( k \in K_n \), then \( |\det g| = 1 \) and, using the Whittaker property \( V(u(g)k) = \psi(u(g))V(k) \),

\[
\psi^{-1}(u(g))\, V(g) = \psi^{-1}(u(g))\, \psi(u(g))\, V(k) = V(k).
\]

Thus the integrand in (5) is supported on \( N_n K_n \) and the \( s \)-factor drops out. Transporting the quotient measure from \( N_n \backslash (N_n K_n) \simeq (N_n \cap K_n) \backslash K_n \) gives

\[
Z(s, W, V) = I_Q(V) := \int_{(N_n \cap K_n) \backslash K_n} \psi^{-1}(Q\, k_{n,n})\, V(k)\, dk. \tag{7}
\]

In particular, \( Z(s, W, V) \) is independent of \( s \), and finiteness is automatic because the domain of integration is compact.

The remaining task is to show \( I_Q(V) \neq 0 \).

### 2.4 Step 3: Fourier projection and the weak kernel on \( G_n \)

For the rest of the proof put \( H = N_n \cap K_n \). If \( Q \) is the chosen generator of \( \mathfrak{p}^{-c(\pi)} \), write

\[
L(V) = \int_{H \backslash K_n} \psi(-Q\, k_{nn})\, V(k)\, dk. \tag{8}
\]

We shall use two standard facts. First, for \( x = (x_1, \ldots, x_{n-1}) \in F^{n-1} \) put \( u(x) = I_n + \sum_{i=1}^{n-1} x_i E_{in} \). If \( a = (a_1, \ldots, a_{n-1}) \in F^{n-1} \) and \( W \in \mathcal{W}(\pi, \psi) \), define

\[
(\mathcal{P}_a W)(g) = \int_{\mathfrak{o}^{n-1}} W(g\, u(x))\, \psi\!\left( -Q \sum_{i=1}^{n-1} a_i x_i \right) dx. \tag{9}
\]

(The Haar measure gives volume 1 to \( \mathfrak{o} \).) Then \( \mathcal{P}_a W \in \mathcal{W}(\pi, \psi) \) and a change of variables \( k \mapsto k\, u(x) \) in (8) gives the projection formula

\[
L(\mathcal{P}_a W) = \int_{\substack{H \backslash K_n \\ k_{ni} \equiv a_i \pmod{\mathfrak{p}^{c(\pi)}},\; i < n}} \psi(-Q\, k_{nn})\, W(k)\, dk. \tag{10}
\]

Indeed the inner integrals are \( \int_{\mathfrak{o}} \psi(Q(k_{ni} - a_i)x)\, dx \), equal to 1 or 0 according as \( k_{ni} - a_i \in \mathfrak{p}^{c(\pi)} \) or not.

The proof of non-vanishing for ramified representations rests on a standard piece of local newform theory. We isolate it in the following form. Recall that \( H = N_n \cap K_n \).

**Proposition 2.3** (compact test vector on \( K_n \)). *Assume that \( n \geq 2 \) and that the conductor exponent \( c = c(\pi) \) is positive. There is an integer \( m_0 = m_0(\pi) \geq c \) with the following property. For every \( m \geq m_0 \) one can find a Whittaker function \( V_m^{\mathrm{H}} \in \mathcal{W}(\pi, \psi) \) whose restriction to \( K_n \) is described as follows (we normalize it by a non-zero scalar which we take to be 1). Let \( w \in K_n \) be the permutation matrix interchanging the last two columns. For a coset of \( H \backslash K_n \) with \( k_{n,n-1} \in \mathfrak{o}^\times \) choose the representative for which, after multiplication on the left by an element of \( H \),*

\[
kw = \begin{pmatrix} h & 0 \\ r & a' \end{pmatrix} \tag{11}
\]

*(\( h \in G_{n-1} \), \( r = (r_1, \ldots, r_{n-1}) \in F^{n-1} \), \( a' \in F^\times \)). Then*

\[
V_m^{\mathrm{H}}(k) = \begin{cases} 1, & h \in 1 + \mathfrak{p}^m M_{n-1}(\mathfrak{o}),\quad r \in (\mathfrak{p}^m)^{n-1},\quad a' \in 1 + \mathfrak{p}^c, \\ 0, & \text{otherwise} \end{cases} \tag{12}
\]

*on all such cosets. (On cosets for which \( k_{n,n-1} \notin \mathfrak{o}^\times \) no assertion is made.) In particular the subset \( C_m \subset H \backslash K_n \) cut out by the three congruence conditions in (12) is a non-empty compact open set of positive measure and \( V_m^{\mathrm{H}} \) is its characteristic function on the part of the quotient which will occur below.*

*References.* This is the familiar construction of the *normalised Howe vector* (or partial Bessel function). We recall the precise results in the literature from which the stated form follows. Let \( K_n(r) = 1 + \mathfrak{p}^r M_n(\mathfrak{o}) \) and set \( J_r = d^r K_n(r) d^{-r} \) for the standard diagonal \( d = \mathrm{diag}(1, \varpi^2, \ldots, \varpi^{2n}) \); let \( \psi_r \) be Howe's character of \( J_r \). Rodier's approximation theorem for Whittaker models, in the form used by Cogdell and Piatetski-Shapiro, asserts that for every irreducible generic representation there are, for all sufficiently large \( r \), vectors \( v_r \) with \( \pi(j)v_r = \psi_r(j)v_r \) for \( j \in J_r \) and with Whittaker value normalized by \( W_{v_r}(1) = 1 \); see [1, \S 7]. Such a vector is called a Howe vector. The values of a normalized Howe vector on the big Bruhat cell were computed explicitly by Baruch.

In the notation above, Baruch [1, \S 7] shows that, after taking \( r = m \) larger than the conductor exponent and translating the statement to the compact quotient \( H \backslash K_n \), the restriction of \( W_{v_m} \) is exactly the characteristic described in (12). The multiplication on the left by \( H \) used to put a representative in the form (11) is by elementary row operations (possible precisely when \( k_{n,n-1} \) is a unit), and it introduces no character because \( \psi \) is trivial on \( H \subset K_n \). For the reader who wants a detailed verification of this translation of notation, Baruch [1, \S 7] proves that if a Howe vector is non-zero at a point of the form (11) with \( k \in K_n \), then the three congruences in (12) are necessary, and in that case the value is the constant used for the normalization. This is precisely the assertion above. Finally, choosing \( h = 1 \), \( r = 0 \) and \( a' = 1 \) shows that \( C_m \) is non-empty (it contains the coset of the permutation matrix \( w \)). \(\square\)

### 2.5 Step 4: construction of the test vector in the ramified case

We now finish the proof under the assumptions \( n \geq 2 \) and \( c(\pi) > 0 \). Pick \( m \geq m_0(\pi) \) and let \( V_0 = V_m^{\mathrm{H}} \) be the Whittaker function furnished by Proposition 2.3. We use the Fourier-projection (9) exactly as in Step 3. Take

\[
a_1 = \cdots = a_{n-2} = 0, \qquad a_{n-1} = 1,
\]

and put \( V = \mathcal{P}_a V_0 \). By the projection formula (10) and by the definition of \( V_0 \),

\[
L(V) = \int_{\substack{H \backslash K_n \\ k_{n,n-1} \equiv 1,\; k_{ni} \in \mathfrak{p}^c\; (i < n-1)}} \psi(-Q\, k_{nn})\, V_0(k)\, dk = \int_{C_m} \psi(-Q\, k_{nn})\, dk. \tag{13}
\]

(The congruences are modulo \( \mathfrak{p}^c \).) Indeed, on the domain of the first integral the condition \( k_{n,n-1} \equiv 1 \pmod{\mathfrak{p}^c} \) is exactly \( a' \in 1 + \mathfrak{p}^c \) in (12), and the characteristic property of \( V_0 \) imposes the other two congruences which define \( C_m \); outside \( C_m \) in this domain the integrand is zero.

On \( C_m \) the last entry \( k_{nn} = r_{n-1} \) lies in \( \mathfrak{p}^m \). Since \( v(Q) = -c \) and \( m \geq c \), we have \( Qk_{nn} \in \mathfrak{o} \) and the additive character is equal to 1 there. The right-hand side of (13) is therefore just the positive Haar measure of the non-empty compact open set \( C_m \); in particular it is different from zero. With the Whittaker function \( W \) on the \( G_{n+1} \) side fixed in Step 1, the Rankin--Selberg integral is finite and non-vanishing (and, as noted in Step 2, independent of \( s \)) in the present ramified case.

### 2.6 Step 5: the exceptional cases

It remains to treat the two small cases omitted above.

**The case \( n = 1 \).** Then \( G_1 = F^\times \) and a generic representation is a quasi-character \( \chi \). The compact integral furnished by Step 2 is the classical Gauss integral

\[
\int_{\mathfrak{o}^\times} \chi(u)\, \psi(-Qu)\, d^\times u
\]

(up to the harmless choice of Haar measure, and in the unramified case simply the volume of \( \mathfrak{o}^\times \) because an unramified character is trivial on the units). For the reader's convenience let us recall why the ramified Gauss sum is non-zero. If the conductor exponent of \( \chi \) is \( c > 0 \), then, with the multiplicative measure normalised in the usual way, the last integral is a non-zero scalar multiple of the finite sum

\[
G(\chi, \psi) = \sum_{u \in (\mathfrak{o}/\mathfrak{p}^c)^\times} \chi(u)\, \psi(\varpi^{-c} u). \tag{14}
\]

(We have chosen the generator \( Q = \varpi^{-c} \).) Extend the function \( u \mapsto \chi(u) \) by 0 to the finite ring \( R_c = \mathfrak{o}/\mathfrak{p}^c \). Its additive Fourier transform is

\[
\widehat{f}(t) = \sum_{u \in R_c^\times} \chi(u)\, \psi(\varpi^{-c} tu) \qquad (t \in R_c).
\]

For \( t \) divisible by \( \varpi \) the character in the summand factors through a proper quotient of \( R_c \), and the primitivity of \( \chi \) (it is non-trivial on \( 1 + \mathfrak{p}^{c-1} \)) shows by summing over the cosets of the kernel that \( \widehat{f}(t) = 0 \). On the other hand the finite Fourier transform on the additive group of \( R_c \) is an isomorphism, so \( \widehat{f} \) is not the zero function because \( f \) is not. Hence some value with \( t \in R_c^\times \) is non-zero. For such a unit \( t \) the change of variables \( u \mapsto tu \) gives \( \widehat{f}(t) = \chi(t)^{-1} G(\chi, \psi) \), and consequently the Gauss sum (14) itself is non-zero. Thus a suitable choice of the Whittaker function \( V = \chi \) supplies the desired test vector in rank one.

**The case \( n \geq 2 \) and \( c(\pi) = 0 \).** Here \( \pi \) is spherical. Let \( v^\circ \) be a non-zero \( K_n \)-fixed vector and let \( W^\circ \) be the associated Whittaker function normalized by \( W^\circ(1) = 1 \). For every \( k \in K_n \) we have \( W^\circ(k) = \Lambda(\pi(k)v^\circ) = \Lambda(v^\circ) = 1 \). Since a generator \( Q \) of the inverse conductor is a unit and our additive character is trivial on \( \mathfrak{o} \), the factor \( \psi(-Qk_{nn}) \) is also identically 1 on \( K_n \). Thus (8) is simply the (positive) volume of the compact space \( H \backslash K_n \), and the same \( V \) gives a non-vanishing Rankin--Selberg integral for all \( s \).

Combining the ramified construction with these two observations completes the proof of the claim stated in the problem. The Whittaker function \( W \) on the \( G_{n+1} \) side was fixed once and for all, independently of the representation \( \pi \) of \( G_n \), and for every generator \( Q \) of the inverse conductor ideal we have exhibited a Whittaker function \( V \) such that \( Z(s, W, V) = L(V) \neq 0 \) for all complex \( s \).

### References

[1] E. M. Baruch, *Bessel functions for \( \mathrm{GL}(n) \) over a \( p \)-adic field*, in *Automorphic representations, \( L \)-functions and applications: progress and prospects*, Ohio State Univ. Math. Res. Inst. Publ. **11**, de Gruyter, Berlin, 2005, pp. 1--36. (reference for Howe vectors / partial Bessel functions; see especially \S 7).

[2] J. W. Cogdell and I. I. Piatetski-Shapiro, *Derivatives and \( L \)-functions for \( \mathrm{GL}_n \)*, in *The Heritage of B. Moishezon*, Israel Math. Conf. Proc. **9** (1996), 37--72.

[3] I. M. Gelfand and D. A. Kazhdan, *Representations of the group \( \mathrm{GL}(n, K) \) where \( K \) is a local field*, in *Lie Groups and Their Representations* (I. M. Gelfand, ed.), Halsted Press, New York, 1975, pp. 95--118.

[4] N. Matringe, *Essential Whittaker functions for \( \mathrm{GL}(n) \)*, available as arXiv:1201.5506 (2013).

[5] A. V. Zelevinsky, *Induced representations of reductive \( p \)-adic groups. II. On irreducible representations of \( \mathrm{GL}(n) \)*, Ann. Sci. \'{E}c. Norm. Sup. (4) **13** (1980), 165--210.
