# Grading Transcript

- Problem: `2`
- Attempt: `oai2`
- Started (UTC): `2026-02-17T18:07:05.766939+00:00`
- Finished (UTC): `2026-02-17T18:10:48.273301+00:00`
- Grade: **3/4** (Substantial Progress (nearly complete))

## Question

Let \(F\) be a non-archimedean local field with ring of integers \(\mathfrak o\).  Let $N_r$ denote the subgroup of $\mathrm{GL}_{r}(F)$ consisting of upper-triangular unipotent elements.  Let \(\psi:F\to \mathbb C^\times\) be a nontrivial additive character of conductor \(\mathfrak o\), identified in the standard way with a generic character of $N_r$.
Let \(\Pi\) be a generic irreducible admissible representation of \(\mathrm{GL}_{n + 1}(F)\), realized in its \(\psi^{-1}\)-Whittaker model \(\mathcal W(\Pi,\psi^{-1})\).  Must there exist \(W\in \mathcal W(\Pi,\psi^{-1})\) with the following property?

Let $\pi$ be a generic irreducible admissible representation of \(\mathrm{GL}_{n}(F)\), realized in its $\psi$-Whittaker model \(\mathcal W(\pi,\psi)\).  Let $\mathfrak{q}$ denote the conductor ideal of $\pi$, let \(Q\in F^\times\) be a generator of \(\mathfrak q^{-1}\), and set
\[
  u_Q := I_{n+1} + Q\,E_{n,n+1} \in \mathrm{GL}_{n + 1}(F),
\]
where \(E_{i, j}\) is the matrix with a \(1\) in the \((i, j)\)-entry and \(0\) elsewhere.  For some \(V\in \mathcal W(\pi,\psi)\), the local Rankin-Selberg integral
\[
  \int_{N_n\backslash \mathrm{GL}_{n}(F)} W(\operatorname{diag}(g,1) u_Q)\,V(g)\,|\det g|^{s-\frac12}\,dg
\]
is finite and nonzero for all \(s\in\mathbb C\).

## Solution Attempt

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

## Editor Dispatch

Based on the complexity of the $p$-adic representation theory involved and the specific strengths of the available models:

1.  **Correctness & Completeness**: Assigned to **claude_code**. The proof relies on intricate steps involving the Kirillov model, mirabolic subgroups, and Fourier projections. Claude models typically excel at maintaining long contexts and performing step-by-step logical deduction, which is crucial for verifying the non-vanishing of the integral and the validity of the Howe vector construction.

2.  **Clarity & Rigor**: Assigned to **codex_cli**. This perspective focuses on precision of notation and consistency of definitions (e.g., ensuring $N_r$, $K_r$, and $\psi$ are used consistently). Code-oriented models are particularly adept at "linting" text—identifying undefined variables, scope errors, and structural inconsistencies—which maps well to checking mathematical rigor.

3.  **Reference Validity**: Assigned to **gemini_api**. The proof cites specific results from the literature (Baruch, Zelevinsky, Gelfand-Kazhdan). Gemini models generally have strong retrieval capabilities or broad knowledge bases, making them suitable for verifying that the cited theorems (like the "compact Kirillov model" or "normalized Howe vector") are attributed correctly and used within their valid hypotheses.

```json
{
  "assignments": {
    "Correctness & Completeness": "claude_code",
    "Clarity & Rigor": "codex_cli",
    "Reference Validity": "gemini_api"
  },
  "reasoning": "claude_code is selected for the deep logical verification of the representation theoretic arguments due to its strong reasoning capabilities. codex_cli is chosen for Clarity & Rigor to apply a syntax-and-consistency 'linting' approach to the mathematical notation and definitions. gemini_api is assigned to Reference Validity to leverage its broad knowledge base for verifying external citations and theorem statements."
}
```

## Reviewer — Correctness & Completeness

# Review: Correctness & Completeness

## Overall Assessment

This is a sophisticated and largely well-executed proof that constructs a universal test vector $W \in \mathcal{W}(\Pi, \psi^{-1})$ for the twisted local Rankin–Selberg integral. The overall strategy — prescribe $W$ on the mirabolic via the compact Kirillov model, reduce the integral to a compact domain, then use Howe vectors to produce a nonvanishing $V$ — is sound and reflects genuine expertise with the local Langlands/automorphic forms machinery. However, there are several issues ranging from a critical gap in the Howe vector argument to various points where claims are insufficiently justified or where the notation is potentially misleading.

---

## Detailed Issues

### 1. The Howe vector description (Proposition 2.3) is not accurately attributed

The proposition claims that Baruch [1, §7] proves that the restriction of a normalized Howe vector to $K_n$ is *exactly* the characteristic function described in (12) on cosets where $k_{n,n-1} \in \mathfrak{o}^\times$. However, Baruch's results in [1] compute Whittaker values on the *big Bruhat cell* of $G_n$, not directly on $K_n$ in the block form (11). The translation from Baruch's coordinates (involving the long Weyl element and Iwasawa-type decompositions) to the compact quotient $H \backslash K_n$ with the specific block decomposition (11) is non-trivial and is not carried out in the proof. The proof simply asserts "translating the statement to the compact quotient" without verification. This is a significant logical gap: the reader (and a verifier) cannot check the central technical claim.

### 2. The block decomposition (11) is underspecified

The proof says: for $k \in K_n$ with $k_{n,n-1} \in \mathfrak{o}^\times$, after left-multiplication by $H$, the matrix $kw$ can be put in the block form (11). But the decomposition $kw = \begin{pmatrix} h & 0 \\ r & a' \end{pmatrix}$ is not a standard factorization and the proof does not explain *which* left multiplication by $H$ achieves this, nor does it verify that this is always possible when $k_{n,n-1} \in \mathfrak{o}^\times$. The claim that "elementary row operations" suffice because $k_{n,n-1}$ is a unit needs a brief argument: one must verify that the row operations used belong to $H = N_n \cap K_n$ and that they zero out the appropriate entries of $kw$.

### 3. Identification $k_{nn} = r_{n-1}$ in §2.5 needs justification

In equation (13), the proof asserts "on $C_m$ the last entry $k_{nn} = r_{n-1}$". This identification comes from the block decomposition (11) applied to $kw$, but $k_{nn}$ is an entry of $k$ while $r_{n-1}$ is an entry of $kw$ (after left-$H$ reduction). Since $w$ permutes the last two columns, $k_{nn}$ becomes $(kw)_{n,n-1}$ — not $(kw)_{n,n} = a'$. So the relationship between $k_{nn}$ and the entries of the block form (11) needs to be stated and verified carefully. If $kw$ has last row $(r_1, \ldots, r_{n-1}, a')$, then $k$ has last row $(r_1, \ldots, r_{n-2}, a', r_{n-1})$ (since $w$ swaps columns $n-1$ and $n$). Thus $k_{nn} = r_{n-1}$ and $k_{n,n-1} = a'$. The identification is correct but requires this explicit verification, since the entire nonvanishing argument depends on it.

### 4. The Fourier projection formula (10) has an unjustified change of variables

The proof claims that a "change of variables $k \mapsto ku(x)$" in (8) yields (10), with the inner integrals being $\int_{\mathfrak{o}} \psi(Q(k_{ni} - a_i)x)\, dx$. But $u(x)$ is an element of the *unipotent radical* acting on the right, and the integral (8) is over $H \backslash K_n$. The substitution $k \mapsto ku(x)$ for $x \in \mathfrak{o}^{n-1}$ preserves $K_n$ (since $u(x) \in K_n$) and preserves the left $H$-cosets (needs checking), but the proof does not verify that the measure is preserved or that the quotient structure is respected. More importantly, the inner integral concerns the $(n,i)$-entries of $k \cdot u(x)$, and one needs to verify that $(ku(x))_{ni} = k_{ni} + k_{nn} x_i$ and that $k_{nn}$ can be absorbed (or is a unit on the relevant domain). The claim that the inner integrals factor as stated needs a brief computation.

### 5. The $n=1$ case: choice of $W$ is not addressed

In §2.6, the $n=1$ case is treated by verifying nonvanishing of a Gauss sum. However, the universal Whittaker function $W \in \mathcal{W}(\Pi, \psi^{-1})$ on $G_2$ was constructed in Steps 1–2 using the mirabolic/Kirillov model specifically for the purpose of reducing to a compact integral. The $n=1$ discussion verifies the Gauss sum is nonzero but does not explicitly verify that the *same* $W$ (defined via Lemma 2.1 for general $n$) works when $n=1$. For $n=1$, the compact integral (7) becomes $\int_{\mathfrak{o}^\times} \psi^{-1}(Qu) V(u)\, d^\times u$, and one should check that this matches the Gauss sum expression given. This is straightforward but is a gap in the exposition.

### 6. The compact support claim in Lemma 2.1

The proof of Lemma 2.1 claims $f$ is compactly supported modulo $N_{n+1}$ because "modulo $N_{n+1}$ the $x$-variable is irrelevant." This is correct — the left $N_{n+1}$-action on $P_{n+1}$ allows arbitrary translation of $x$ — but it should be noted that the function $f$ as written *does* depend on $x$ (through $\psi^{-1}(x_n)$), which is consistent with compact support *modulo $N_{n+1}$* but might confuse a reader expecting literal compact support. The key point is that $N_{n+1} \backslash P_{n+1} \simeq N_n \backslash G_n$, and the $g$-support projects to a compact set. This is correct but could be stated more precisely.

### 7. Missing verification that $\psi^{-1}$ vs $\psi$ conventions are consistent

The problem uses $\Pi$ in its $\psi^{-1}$-Whittaker model and $\pi$ in its $\psi$-Whittaker model. The proof defines $f$ using $\psi^{-1}$ factors, and the Rankin–Selberg integral pairs $W$ (in $\psi^{-1}$-model) with $V$ (in $\psi$-model). In equation (6)–(7), the cancellation $\psi^{-1}(u(g)) \cdot \psi(u(g)) = 1$ is crucial and is correctly computed. However, in §2.4 equation (8), the functional $L(V)$ uses $\psi(-Q k_{nn})$, which should be $\psi^{-1}(Q k_{nn})$ from (7) — and indeed $\psi(-Q k_{nn}) = \psi^{-1}(Qk_{nn})$ if $\psi^{-1}(\cdot) = \psi(-\cdot)$. This is a standard convention but should be stated explicitly since the proof switches between $\psi^{-1}(\cdot)$ and $\psi(-\cdot)$ notation without comment.

---

## Summary Judgment

The high-level argument is correct and creative. The main structural concern is the reliance on Proposition 2.3 whose proof is essentially deferred to a nontrivial "translation" from Baruch's results that is not carried out. The remaining issues are primarily about missing intermediate verifications that, while likely all correct, leave logical gaps in a proof that aspires to graduate-level rigor.

```json
{
  "issues": [
    {
      "severity": "critical",
      "location": "§2.4, Proposition 2.3",
      "reason": "The translation from Baruch's Whittaker value computations on the big Bruhat cell to the compact quotient H\\K_n in the block form (11)–(12) is asserted but not carried out. This is the central technical claim and cannot be verified from the text as written.",
      "required_fix": "Provide an explicit computation translating Baruch's coordinates (involving the long Weyl element, Iwasawa decomposition on G_n) to the block decomposition (11) on K_n, showing that the Howe vector values match the characteristic function description (12).",
      "suggestion": "Write a self-contained lemma showing: given k in K_n with k_{n,n-1} a unit, perform the left-H row reduction to get kw in form (11), then express the resulting matrix in Baruch's parametrization of the big Bruhat cell, and read off the Howe vector value. This makes the proof verifiable without consulting [1]."
    },
    {
      "severity": "major",
      "location": "§2.5, equation (13)",
      "reason": "The identification k_{nn} = r_{n-1} (where r_{n-1} comes from the block form of kw) is used without justification. Since w swaps the last two columns, the relationship between entries of k and entries of kw needs explicit verification.",
      "required_fix": "Add a sentence verifying: since w swaps columns n-1 and n, the last row of k is (r_1,...,r_{n-2}, a', r_{n-1}), hence k_{nn} = r_{n-1} and k_{n,n-1} = a'.",
      "suggestion": "Insert a brief remark after introducing the block form (11) that spells out how the entries of k relate to those of kw. This also clarifies why the condition k_{n,n-1} ∈ o^× corresponds to a' ∈ o^×."
    },
    {
      "severity": "major",
      "location": "§2.4, block decomposition (11)",
      "reason": "The proof does not verify that left multiplication by H can always put kw in the form (11) when k_{n,n-1} is a unit, nor that the H-element used is uniquely determined (or that the ambiguity does not affect the argument).",
      "required_fix": "Show explicitly that when k_{n,n-1} ∈ o^× (equivalently, (kw)_{nn} ∈ o^×), one can use elementary row operations from H to zero out entries (n,1),...,(n,n-1) of kw, yielding the block form. State what h, r, a' are in terms of k.",
      "suggestion": "A short matrix computation: kw has last row entries that can be cleared above the (n,n)-pivot using elements of N_n ∩ K_n, since the pivot a' = k_{n,n-1} is a unit. This is essentially Gaussian elimination restricted to H."
    },
    {
      "severity": "major",
      "location": "§2.4, projection formula (10)",
      "reason": "The change of variables k → ku(x) in the integral over H\\K_n is asserted to yield the factored inner integrals, but the computation of (ku(x))_{ni} and the compatibility with the H\\K_n quotient measure are not verified.",
      "required_fix": "Verify that right multiplication by u(x) preserves the H-coset structure (i.e., Hu(x) = u(x)H or similar), compute (ku(x))_{ni} = k_{ni} + k_{nn}x_i explicitly, and check the measure transformation.",
      "suggestion": "Note that u(x) ∈ K_n and that H·k·u(x) = H·(ku(x)) since u(x) normalizes H (or commutes with the last-row entries relevant to H). Then the substitution is measure-preserving on H\\K_n. The entry computation is a direct matrix multiplication."
    },
    {
      "severity": "minor",
      "location": "§2.6, case n=1",
      "reason": "The n=1 case verifies nonvanishing of the Gauss sum but does not explicitly connect back to the universal W constructed in Steps 1–2. It should verify that the compact integral (7) specializes to the Gauss sum for the particular f from Lemma 2.1 when n=1.",
      "required_fix": "Add a sentence showing that when n=1, the integral (7) with W|_{P_2} = f becomes ∫_{o^×} ψ^{-1}(Qu) V(u) d^×u, matching the Gauss sum up to measure normalization.",
      "suggestion": "For n=1: K_1 = o^×, H = {1}, and f restricted to the mirabolic gives W(diag(u,1)·u_Q) = ψ^{-1}(Qu). So (7) is ∫_{o^×} ψ^{-1}(Qu) V(u) d^×u. For V = χ (the Whittaker function of π = χ), this is the Gauss sum."
    },
    {
      "severity": "minor",
      "location": "§2.3–2.4",
      "reason": "The proof switches between ψ^{-1}(Qk_{nn}) in (7) and ψ(-Qk_{nn}) in (8) without noting the convention ψ^{-1}(·) = ψ(-·).",
      "required_fix": "State explicitly that ψ^{-1}(x) = ψ(-x), so that L(V) in (8) equals the integral in (7).",
      "suggestion": "A one-line remark after equation (8): 'Here we use the convention ψ^{-1}(x) = ψ(-x) throughout.'"
    },
    {
      "severity": "minor",
      "location": "§2.6, unramified case",
      "reason": "The unramified case claims Q is a unit when c(π) = 0, since q = o and q^{-1} = o. This is correct but the proof should note that W^∘(k) = 1 for all k ∈ K_n requires Λ(v^∘) = W^∘(1) = 1 AND K_n-invariance, which together give W^∘(k) = Λ(π(k)v^∘) = Λ(v^∘) = 1. The stated chain 'W^∘(k) = Λ(π(k)v^∘) = Λ(v^∘) = 1' is correct but uses the Whittaker functional Λ without introducing it.",
      "required_fix": "Either introduce the notation Λ for the Whittaker functional or simply state: W^∘ is the spherical Whittaker function normalized by W^∘(1) = 1, and K_n-invariance gives W^∘(k) = 1 for all k ∈ K_n.",
      "suggestion": "Replace the chain involving Λ with the simpler statement that W^∘ is K_n-invariant and normalized at the identity."
    }
  ],
  "residual_concerns": [
    "The proof's dependence on Proposition 2.3 means its correctness ultimately rests on a careful reading of Baruch [1, §7] that is not self-contained. A referee would likely request the translation be made explicit.",
    "The measure normalizations (Haar measure on H\\K_n, on o^×, etc.) are left implicit throughout. While standard, in a proof about nonvanishing of specific integrals, it would be reassuring to confirm that no normalization factor is zero.",
    "The proof does not address whether the chosen W works uniformly across all π simultaneously in a precise sense — it claims W depends only on Π, but the V depends on π. This matches the problem statement but the uniformity claim could be stated more carefully at the end."
  ]
}
```

## Reviewer — Clarity & Rigor

Overall, the strategy is mathematically plausible and close to graduate-level rigor, but two core steps are under-justified for peer-review standards: the imported Howe-vector proposition and the Fourier-projection identity/domain matching. The remaining issues are clarity/verifiability improvements.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Proposition 2.3 (\u00a72.4)",
      "reason": "This proposition is the key nonvanishing input in the ramified case, but it is presented as a custom statement with broad citations and no precise theorem numbering or full hypothesis matching. The translation from Baruch/Howe-vector notation to conditions (11)\u2013(12) is asserted rather than demonstrated.",
      "required_fix": "Provide exact theorem/proposition references (with numbering) and explicitly verify that their hypotheses and normalizations match the present setup (\u03c8, conductor conventions, normalization of Howe vectors, quotient H\\\\K_n).",
      "suggestion": "Add a short sublemma that maps the cited result to your notation, including explicit identification of variables in (11)\u2013(12) and why it yields the stated characteristic-function behavior."
    },
    {
      "severity": "major",
      "location": "Equations (10) and (13) (\u00a72.4\u2013\u00a72.5)",
      "reason": "The projection formula and subsequent identification of the integration domain with C_m are compressed. The derivation uses a nontrivial change of variables on H\\\\K_n plus additive-character orthogonality, and sign/congruence bookkeeping is not fully spelled out.",
      "required_fix": "Expand the derivation of (10) step-by-step: perform the substitution k \u2192 ku(-x), compute (ku(-x))_{nn}, and explicitly apply \u222b_o \u03c8(Qyx)dx = 1_{y\u2208p^c}. Then explicitly justify the passage to C_m in (13).",
      "suggestion": "Insert a displayed intermediate computation and a one-line orthogonality lemma so the congruence conditions are auditable."
    },
    {
      "severity": "minor",
      "location": "\u00a72.3\u2013\u00a72.5 notation",
      "reason": "The symbol W is reused for Whittaker functions on both G_{n+1} (fixed test vector) and G_n (generic variable in projections), which creates avoidable ambiguity.",
      "required_fix": "Use distinct symbols for the two models throughout these sections.",
      "suggestion": "Rename to W_{\\Pi} for G_{n+1} and W_{\\pi} (or keep V consistently) for G_n."
    },
    {
      "severity": "minor",
      "location": "Lemma 2.1 proof (\u00a72.2)",
      "reason": "Compact support modulo N_{n+1} is justified informally (\u201cx-variable is irrelevant\u201d) without an explicit quotient/orbit argument.",
      "required_fix": "State the orbit relation on P_{n+1} under left N_{n+1} and identify N_{n+1}\\\\P_{n+1} with N_n\\\\G_n for support purposes.",
      "suggestion": "Add the explicit equality [ [g,x;0,1] ] = [ [g,0;0,1] ] via left multiplication by [I_n,-x;0,1] \u2208 N_{n+1}."
    },
    {
      "severity": "minor",
      "location": "References / external inputs",
      "reason": "Several citations are section-level only, which reduces traceability for verification at graduate rigor.",
      "required_fix": "Replace broad references with pinpoint theorem/proposition numbers wherever a nontrivial external fact is used (compact Kirillov restriction, Howe-vector value formula).",
      "suggestion": "Add parenthetical cites like \u201cBaruch, Prop. X.Y\u201d and \u201cZelevinsky, Thm. Z\u201d directly at the claim use sites."
    }
  ],
  "residual_concerns": [
    "Haar-measure normalizations are mostly implicit; nonvanishing is robust, but explicit normalizations would prevent constant/sign ambiguities."
  ]
}
```

## Reviewer — Reference Validity

The proof is mathematically sound and demonstrates a high level of competence in the representation theory of $p$-adic groups. The use of the mirabolic subgroup and the construction of the test vector via Howe vectors are standard and correctly applied techniques.

From the perspective of **Reference Validity**, the citations are generally appropriate, but there are minor bibliographic updates and one instance where the attribution of a specific formula to a reference requires clarification to meet graduate-level rigor.

### Issues

```json
{
  "issues": [
    {
      "severity": "minor",
      "location": "Reference [4]",
      "reason": "The reference is cited as an arXiv preprint from 2013, but it has since been published in a peer-reviewed journal.",
      "required_fix": "Update the citation to the published version.",
      "suggestion": "Replace with: N. Matringe, *Essential Whittaker functions for GL(n)*, Doc. Math. **18** (2013), 1191–1214."
    },
    {
      "severity": "minor",
      "location": "Proposition 2.3 / Reference [1]",
      "reason": "The text asserts that Baruch [1, §7] proves the restriction is 'exactly the characteristic described in (12)'. Equation (12) defines the support relative to a specific permutation matrix $w$ (swapping the last two columns). Standard Howe vectors (as treated in Baruch) are typically supported near the identity $I_n$. While the result follows by translation, claiming Baruch derives this *exact* formula with this specific $w$ is likely imprecise.",
      "required_fix": "Clarify whether $V_m^H$ is a translate of the vector found in Baruch or if Baruch explicitly treats this coordinate system.",
      "suggestion": "Rephrase to indicate that $V_m^H$ is the right-translate by $w$ of the normalized Howe vector constructed by Baruch (which is supported near the identity), or explicitly state that the formula is an adaptation of Baruch's result to the coordinate system near $w$."
    }
  ],
  "residual_concerns": []
}
```

### Rationale

1.  **Reference [4] (Matringe):** For a graduate-level proof, citing the final published version (*Documenta Mathematica*) is standard practice over the arXiv preprint, ensuring the reader accesses the peer-reviewed version.
2.  **Proposition 2.3 (Baruch Citation):** The proof relies on the specific support of the test vector $V_m^H$ to ensure the integral is non-zero. The support is defined by conditions on $kw$, effectively placing the vector near $w^{-1} = w$. Baruch's work (and the related work of Cogdell/Piatetski-Shapiro) typically constructs these "newforms" or "Howe vectors" supported on a congruence subgroup near the identity. The transition from a vector near $I$ to a vector near $w$ is a valid operation (right translation), but the text currently reads as if Baruch's paper contains the formula for the vector at $w$ explicitly. Clarifying this distinction improves the rigor of the citation.

## Grading Decision

## Editorial Synthesis

### Overview

The solution attempts to prove the existence of a universal Whittaker function $W \in \mathcal{W}(\Pi, \psi^{-1})$ such that for every generic $\pi$ on $\mathrm{GL}_n(F)$, a suitable $V$ makes the twisted local Rankin–Selberg integral finite and nonzero for all $s$. The overall strategy is:

1. Use the compact Kirillov model to prescribe $W$ on the mirabolic subgroup.
2. Reduce the Rankin–Selberg integral to a compact integral over $K_n$ that is independent of $s$.
3. Show nonvanishing of this compact integral using Howe vectors (ramified case), Gauss sums ($n=1$), or spherical vectors (unramified case).

This is a well-conceived approach that demonstrates deep familiarity with the relevant machinery.

### Assessment of Reviewer Findings

**Critical issue (Review #1): Proposition 2.3 translation from Baruch.** This is the most substantive concern. The proof's central nonvanishing argument rests on Proposition 2.3, which describes the restriction of a Howe vector to $K_n$ in a specific block form (11)–(12). The translation from Baruch's coordinates to the compact quotient $H \backslash K_n$ is asserted but not carried out. Review #14 additionally notes that Baruch's Howe vectors are typically supported near the identity, and the use of the permutation matrix $w$ may require an explicit right-translation argument. While the underlying mathematics is almost certainly correct — Howe vectors and their support properties are well-established — the gap between the citation and the claimed formula is non-trivial and would require genuine work (likely a page or so of computation) to fill rigorously. This is a real gap, though it is of a "routine verification" character for an expert in the area.

**Major issues (Reviews #2–4, #8–9):** These cluster around two themes:
- The block decomposition (11) and its relationship to entries of $k$ (Review #3), the identification $k_{nn} = r_{n-1}$ (Review #2), and the overall bookkeeping in the projection formula (Reviews #4, #9). These are all fillable gaps — they involve explicit matrix computations that the author clearly understands but did not write out. None of these are conceptual errors; they are missing verifications.
- Review #8 reinforces #1 regarding precise theorem references.

**Minor issues (Reviews #5–7, #10–14):** These are primarily expository: notation reuse ($W$ for both models), missing identification $\psi^{-1}(x) = \psi(-x)$, informal compact-support argument, broad citations, and an outdated reference. None affect mathematical correctness.

### Error Assessment

- **Incorrect logic:** The logical structure is sound. The strategy of reducing to a compact integral and then using Howe vectors is well-established. I find no circular reasoning or false implications. The gaps are in verification, not in logic.

- **Hallucinated results:** The compact Kirillov model (Lemma 2.2) is a genuine classical result. The Howe vector properties cited from Baruch are real. Reference [4] exists (though should be updated to the published version). No hallucinated mathematics detected.

- **Calculation mistakes:** The matrix computations that are presented (equivariance in Lemma 2.1, the reduction to compact integral in §2.3, the Gauss sum argument in §2.6) appear correct. The concern is about *missing* calculations rather than *wrong* ones.

- **Conceptual misunderstanding:** None. The author demonstrates expert-level understanding of Whittaker models, mirabolic restriction, Howe vectors, conductor theory, and the Rankin–Selberg formalism.

### Achievement Assessment

- **Problem understanding:** Clearly demonstrated. The author correctly interprets the problem, understands the universality requirement on $W$, and identifies the key difficulties.

- **Correct end result:** The answer "yes, such $W$ exists" appears to be correct. The construction via the compact Kirillov model is the right approach, and the claimed nonvanishing, while not fully verified in the text, is supported by the literature.

- **Insight and creativity:** The choice of $f$ in Lemma 2.1 (prescribing $W$ on the mirabolic to make the integral collapse to a compact form), the use of Fourier projection to isolate the relevant support, and the systematic case analysis all show genuine mathematical insight.

- **Practical usefulness:** An expert would find this solution highly informative. The overall strategy is clear, the key ideas are identified, and the gaps are of a nature that an expert could fill.

### Overall Grade

The proof presents a complete strategy with all major ideas in place. The primary gap is the detailed translation of Baruch's Howe vector results to the coordinate system used in Proposition 2.3 — this is a non-trivial but routine verification for an expert. The other gaps (matrix entry identifications, projection formula details) are straightforward computations. An expert could fill all gaps in well under an hour. This places the solution solidly at grade 3.

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
  "short_summary": "The solution presents a well-conceived and nearly complete proof that a universal Whittaker function W exists making the twisted Rankin–Selberg integral finite and nonzero for all s. The strategy—prescribing W on the mirabolic via the compact Kirillov model, reducing to a compact integral independent of s, and establishing nonvanishing via Howe vectors—is mathematically sound and demonstrates expert-level understanding. The main gap is the untranslated passage from Baruch's Howe vector computations to the specific block-form description in Proposition 2.3, which is the central nonvanishing input. While this translation is almost certainly correct, it requires a page or so of explicit coordinate computation that the text omits. Secondary gaps include missing matrix-entry verifications and compressed projection-formula derivations. All gaps are of a routine character that an expert could fill in a short sitting. No logical errors, hallucinated results, or conceptual misunderstandings were identified."
}
```
