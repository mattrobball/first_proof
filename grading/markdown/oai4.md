## 4 Finite additive convolution and a harmonic-mean inequality for \(\Phi_n\)

**Problem**

Let \(p(x)\) and \(q(x)\) be two monic polynomials of degree \(n\):

\[
p(x) = \sum_{k=0}^{n} a_k x^{n-k} \quad \text{and} \quad q(x) = \sum_{k=0}^{n} b_k x^{n-k}
\]

where \(a_0 = b_0 = 1\). Define \(p \boxplus_n q(x)\) to be the polynomial

\[
(p \boxplus_n q)(x) = \sum_{k=0}^{n} c_k x^{n-k}
\]

where the coefficients \(c_k\) are given by the formula:

\[
c_k = \sum_{i+j=k} \frac{(n-i)!(n-j)!}{n!(n-k)!} a_i b_j
\]

for \(k = 0, 1, \ldots, n\). For a monic polynomial \(p(x) = \prod_{i \leq n} (x - \lambda_i)\), define

\[
\Phi_n(p) := \sum_{i \leq n} \Bigl(\sum_{j \neq i} \frac{1}{\lambda_i - \lambda_j}\Bigr)^2
\]

and \(\Phi_n(p) := \infty\) if \(p\) has a multiple root. Is it true that if \(p(x)\) and \(q(x)\) are monic real-rooted polynomials of degree \(n\), then

\[
\frac{1}{\Phi_n(p \boxplus_n q)} \geq \frac{1}{\Phi_n(p)} + \frac{1}{\Phi_n(q)}?
\]

**Solution**

We give a self-contained proof. The few coefficient identities and conventions used later are recorded explicitly.

### 0. Two conventions (extension to non-monic/leading-zero inputs; \(n \geq 2\))

Throughout let \(n \geq 2\) and put \(m := n - 1\).

**Extension of \(\boxplus_n\) to degree \(\leq n\) (leading zeros allowed).** For a polynomial \(f\) of degree \(\leq n\), write it in the *degree-\(n\) coefficient array form*

\[
f(x) = \sum_{k=0}^{n} \alpha_k x^{n-k} \qquad \text{(so } \alpha_0 = 0 \text{ is allowed).}
\]

Given two such arrays \((\alpha_k)_{k=0}^n\) and \((\beta_k)_{k=0}^n\), define their \(\boxplus_n\)-convolution by the *same coefficient rule*

\[
(f \boxplus_n g)(x) := \sum_{k=0}^{n} \gamma_k x^{n-k}, \qquad \gamma_k := \sum_{i+j=k} \frac{(n-i)!(n-j)!}{n!(n-k)!} \alpha_i \beta_j.
\]

This is bilinear in the arrays and agrees with the original definition when both inputs are monic of degree \(n\) (then \(\alpha_0 = \beta_0 = 1\)). We will use this extension whenever one of the inputs has leading coefficient 0 in degree \(n\) (e.g. \(R_p\) in the centered case, or \(\ell_j\) in degree \(m\)).

**Remark on \(n = 1\).** For \(n = 1\) one has \(\Phi_1(p) = 0\) for every monic linear polynomial, so \(1/\Phi_1\) is not meaningful; hence we restrict to \(n \geq 2\).

### 1. The \(\mathcal{E}_n\) transform and the basic identities

For a nonnegative integer \(r\) and \(k \geq 0\) write the falling factorial

\[
r^{\underline{k}} := r(r-1) \cdots (r-k+1), \qquad r^{\underline{0}} := 1.
\]

If \(f(x) = \sum_{k=0}^{r} \alpha_k x^{r-k}\) has degree at most \(r\) define

\[
\mathcal{E}_r(f)(t) := \sum_{k=0}^{r} \alpha_k \frac{t^k}{r^{\underline{k}}}. \tag{2.1}
\]

Then the convolution is equivalently:

\[
\mathcal{E}_n(p \boxplus_n q) = \bigl(\mathcal{E}_n(p)\,\mathcal{E}_n(q)\bigr)_{\leq n}, \tag{2.2}
\]

where the right-hand side multiplies the two polynomials in \(t\) and discards terms of degree \(> n\). We use (2.2) also for the leading-zero extension described above; the convention (2.1) makes this unambiguous and all formulas below are linear in coefficients.

**Translations.** If \(p_a(x) = p(x - a)\) and \(q_b(x) = q(x - b)\), then

\[
p_a \boxplus_n q_b(x) = (p \boxplus_n q)(x - a - b). \tag{2.3}
\]

*Proof (coefficient check, included for normalization).* Write \(p(x) = \sum_{k=0}^n \alpha_k x^{n-k}\). Taylor's formula gives that the coefficient of \(x^{n-k}\) in \(p(x-a)\) equals

\[
\sum_{j=0}^{k} \frac{(-a)^j}{j!}\, \alpha_{k-j}\, (n-k+j)^{\underline{j}}.
\]

Dividing by \(n^{\underline{k}}\) gives exactly the coefficient of \(t^k\) in \(e^{-at}\,\mathcal{E}_n(p)(t)\), hence

\[
\mathcal{E}_n(p_a) = (e^{-at}\,\mathcal{E}_n(p))_{\leq n}.
\]

Applying (2.2) yields (2.3), since discarding terms before multiplying cannot affect degrees \(\leq n\). \(\square\)

**Derivatives and the polar part.** Define

\[
r_p := \frac{1}{n}p', \qquad R_p := p - x\,r_p, \tag{2.4}
\]

and similarly for \(q\). Then, with \(m = n-1\),

\[
\frac{1}{n}(p \boxplus_n q)' = r_p \boxplus_m r_q, \tag{2.5}
\]

and

\[
(p \boxplus_n q) - x\,\frac{1}{n}(p \boxplus_n q)' = (R_p \boxplus_n q) + (p \boxplus_n R_q). \tag{2.6}
\]

*Proof (sketch; both are coefficient checks from (2.2)).* For (2.5), view \(r_p\) as degree-\(m\); its normalized coefficients (2.1) are those of \(p\) with the last one missing, so multiplying the truncated \(\mathcal{E}\)-polynomials gives the derivative identity. For (2.6), compare the coefficient of \(x^{n-k}\) on both sides: the left coefficient is

\[
\frac{k}{n} \sum_{i+j=k} \frac{n^{\underline{k}}}{n^{\underline{i}}\,n^{\underline{j}}}\, a_i\, b_j,
\]

while the right-hand side produces the same sum split into \(i/n\) and \(j/n\) contributions. \(\square\)

### 2. Centering and the critical values \(w_i(p)\)

By (2.3) we may translate \(p\) and \(q\) independently. We therefore assume from now on that \(p\) and \(q\) are *centered*, i.e. the coefficient of \(x^{n-1}\) in each is 0 (equivalently the sum of roots of each is 0). Then \(R_p\) has degree at most \(m - 1\) and, regarded as a degree-\(m\) polynomial, it has leading coefficient 0.

Assume \(p\) has simple real zeros and is centered. Let \(r_p = p'/n\) and denote its zeros by

\[
\nu_1 < \nu_2 < \cdots < \nu_m \qquad (m = n-1).
\]

Define

\[
w_i(p) := -\frac{R_p(\nu_i)}{r'_p(\nu_i)}. \tag{2.7}
\]

**Lemma 4.1** (Residue formula for \(\Phi_n\)). *If \(p\) has simple real zeros and is centered, then all \(w_i(p)\) are positive and*

\[
\Phi_n(p) = \frac{n}{4} \sum_{i=1}^{m} \frac{1}{w_i(p)}. \tag{2.8}
\]

*Proof.* Consider the rational function

\[
\frac{p''(z)^2}{4\,p'(z)\,p(z)}.
\]

At a zero \(\lambda\) of \(p\), the residue is \(\bigl(p''(\lambda)/(2p'(\lambda))\bigr)^2\), and these are precisely the summands defining \(\Phi_n(p)\). The other finite poles are the zeros \(\nu_i\) of \(p'\), and the residue there is

\[
\frac{p''(\nu_i)}{4p(\nu_i)} = \frac{n\,r'_p(\nu_i)}{4R_p(\nu_i)}.
\]

The function is \(O(z^{-3})\) at infinity, hence the residue at infinity is 0. Therefore the sum of residues is 0, yielding (2.8) after rewriting with \(w_i(p)\). The sign in (2.7) (and thus positivity of \(w_i(p)\)) can also be read off from the local extrema: each \(\nu_i\) is a strict maximum or minimum of a real-rooted simple polynomial. At a maximum one has \(p(\nu_i) > 0\) and \(p''(\nu_i) < 0\), and at a minimum the signs are reversed, so \(-R_p(\nu_i)/r'_p(\nu_i) > 0\). \(\square\)

### 3. Tracking the \(w\)'s through convolution: the transport computation

Let \(p\) and \(q\) be centered with simple real zeros. Keep \(\nu_i\) for the zeros of \(r_p\) and define

\[
r = \frac{1}{n}(p \boxplus_n q)' = r_p \boxplus_m r_q, \tag{2.9}
\]

and write the zeros of \(r\) as \(\mu_1 < \cdots < \mu_m\). For each \(\nu_j\) define the monic degree-\((m-1)\) polynomial

\[
\ell_j(x) := \frac{r_p(x)}{x - \nu_j}. \tag{2.10}
\]

Define the \(m \times m\) matrix

\[
K_{ij} := \frac{(\ell_j \boxplus_m r_q)(\mu_i)}{r'(\mu_i)}. \tag{2.11}
\]

Here \(\ell_j\) is used in \(\boxplus_m\) as a degree-\(m\) polynomial with leading coefficient 0, per the extension stated in Section 0.

**Lemma 4.2** (Transport identity). *With the above notation,*

\[
-\frac{(R_p \boxplus_n q)(\mu_i)}{r'(\mu_i)} = \sum_{j=1}^{m} K_{ij}\, w_j(p) \qquad (i = 1, \ldots, m). \tag{2.12}
\]

*The analogous identity with \(p\) and \(q\) interchanged also holds.*

*Proof.* We spell out the coefficient computation, because the step where \(\boxplus_n\) becomes \(\boxplus_m\) is precisely where padding matters.

Write \(p(x) = \sum_{k=0}^n a_k x^{n-k}\) and set \(A_k := a_k / n^{\underline{k}}\); define \(B_k\) similarly from \(q\). For \(1 \leq I \leq m\), the coefficient of \(x^{n-1-I}\) in \(R_p \boxplus_n q\), divided by \((n-1)^{\underline{I}}\), equals

\[
\sum_{i+j=I+1} i\, A_i\, B_j. \tag{2.13}
\]

Indeed this is the definition (2.2), with the coefficient \((i/n)a_i\) of \(R_p\) in place of \(a_i\), and using \(n^{\underline{I+1}} = n(n-1)^{\underline{I}}\).

Now regard \(R_p\) as a degree-\(m\) polynomial with leading coefficient 0 (valid since \(p\) is centered). Its normalized coefficient of \(t^s\) for \(s \geq 1\) is \((s+1)A_{s+1}\). The coefficient of \(x^{m-I}\) in the order-\(m\) convolution \(R_p \boxplus_m r_q\), again divided by \((n-1)^{\underline{I}}\), equals

\[
\sum_{s+j=I} (s+1)A_{s+1}\, B_j = \sum_{i+j=I+1} i\, A_i\, B_j. \tag{2.14}
\]

(The \(i = 1\) term is absent because \(A_1 = 0\) for centered \(p\); for \(I = 0\) the leading coefficients on the two sides are likewise 0.) Comparing (2.13) and (2.14) yields the crucial padded identity

\[
R_p \boxplus_n q = R_p \boxplus_m r_q \quad \text{as polynomials of degree at most } m. \tag{2.15}
\]

Next, since \(\deg(R_p) \leq m - 1\), Lagrange interpolation at the nodes \(\nu_j\) gives

\[
R_p(x) = \sum_{j=1}^{m} R_p(\nu_j)\, \frac{r_p(x)}{r'_p(\nu_j)(x - \nu_j)} = -\sum_{j=1}^{m} w_j(p)\, \ell_j(x). \tag{2.16}
\]

Convolution of order \(m\) is linear in the first factor; combining (2.15) and (2.16) and evaluating at \(x = \mu_i\) gives (2.12) with \(K_{ij}\) as in (2.11). \(\square\)

### 4. The matrix \(K\) is doubly stochastic, and why

**Lemma 4.3** (Doubly stochasticity). *Assume \(r\) in (2.9) has real simple zeros. Then \(K\) satisfies*

\[
K_{ij} \geq 0, \qquad \sum_i K_{ij} = 1, \qquad \sum_j K_{ij} = 1. \tag{2.17}
\]

*The equalities do not use reality of the zeros.*

*Proof.* *Column sums.* Fix \(j\) and consider the rational function

\[
\frac{\ell_j \boxplus_m r_q}{r}.
\]

As a degree-\(m\) polynomial, \(\ell_j\) has leading coefficient 0 and coefficient 1 at \(x^{m-1}\). The convolution \(\ell_j \boxplus_m r_q\) therefore has leading coefficient 0 at \(x^m\) and leading coefficient 1 at \(x^{m-1}\) (a coefficient check from (2.2) with \(k = 1\)). Thus the numerator has degree \(m - 1\) with leading coefficient 1 at \(x^{m-1}\), while \(r\) is monic of degree \(m\). Hence the partial fraction expansion is

\[
\frac{\ell_j \boxplus_m r_q}{r}(x) = \sum_{i=1}^{m} \frac{K_{ij}}{x - \mu_i},
\]

and the expansion at infinity begins with \(1/x\). Therefore \(\sum_i K_{ij} = 1\).

*Row sums.* Use the identity \(\sum_{j=1}^m \ell_j = r'_p\) (obtained by writing \(r_p(x) = \prod_j (x - \nu_j)\) and differentiating), and claim

\[
\sum_{j=1}^{m} (\ell_j \boxplus_m r_q) = r'. \tag{2.18}
\]

This is again a coefficient check using \(\mathcal{E}_m\). Let \(\mathcal{E}_m(r_p)(t) = A(t)\) and \(\mathcal{E}_m(r_q)(t) = B(t)\). Then the normalized coefficient polynomial of the leading-zero derivative \(r'_p\) in degree \(m\) is \((tA(t))_{\leq m}\). After convolution with \(r_q\) it becomes \((tA(t)B(t))_{\leq m}\). On the other hand \(\mathcal{E}_m(r) = (A(t)B(t))_{\leq m}\) by (2.2), and the leading-zero derivative of \(r\) has normalized polynomial \((t(A(t)B(t))_{\leq m})_{\leq m}\). These coincide because any terms of \(A(t)B(t)\) of degree \(> m\) disappear after multiplying by \(t\) and truncating to degree \(m\). Thus (2.18) holds. Evaluating (2.18) at \(x = \mu_i\) gives

\[
\sum_{j=1}^{m} (\ell_j \boxplus_m r_q)(\mu_i) = r'(\mu_i),
\]

and dividing by \(r'(\mu_i)\) yields \(\sum_j K_{ij} = 1\).

*Nonnegativity.* Assume (for the moment) that the interlacing-preservation theorem of the next subsection is known for simple polynomials of the same (actual) degree. There is a small point of interpretation here, because in our application \(\ell_j\) has degree \(m - 1\) (it is being padded by a zero leading coefficient in the order-\(m\) convolution). We record explicitly the standard limiting device which reduces this case to the theorem just quoted.

For \(\varepsilon > 0\) put

\[
\ell_j^{(\varepsilon)}(x) := \ell_j(x) + \varepsilon\, r_p(x).
\]

Then \(\ell_j^{(\varepsilon)}\) has real zeros -- namely \(\nu_k\) for \(k \neq j\) and the additional zero \(\nu_j - 1/\varepsilon\) -- and is in non-strict proper position with \(r_p\). If one wants the hypotheses of the interlacing theorem literally, move the common zeros by arbitrarily small alternating perturbations (and divide by the positive leading coefficient) to obtain simple degree-\(m\) polynomials which interlace \(r_p\); after applying the theorem to those polynomials and to \(r_q\), let the perturbations tend to zero. By continuity of the zeros (Hurwitz's theorem, or elementary continuity of the roots as functions of the coefficients) it follows that \(\ell_j^{(\varepsilon)} \boxplus_m r_q\) interlaces \(r = r_p \boxplus_m r_q\). Finally we let \(\varepsilon \downarrow 0\) and use bilinearity of the convolution to get the desired interlacing of \(\ell_j \boxplus_m r_q\) with \(r\) (allowing coincidences).

Since the coefficient of \(\ell_j \boxplus_m r_q\) at \(x^{m-1}\) is positive, such an interlacing (even with coincidences) implies that \((\ell_j \boxplus_m r_q)(\mu_i)\) has the same sign as \(r'(\mu_i)\), or is zero, and hence \(K_{ij} \geq 0\). \(\square\)

### 5. Real-rootedness and interlacing preservation for \(\boxplus_n\) (non-circular)

We now prove the following key theorem. The proof proceeds by a self-contained induction and, at the same time, supplies the deferred nonnegativity of \(K\) in all degrees.

**Obreschkoff (Hermite--Kakeya--Obreschkoff) theorem.** *Let \(f, g\) be real polynomials of degree \(n\) without common zeros and with leading coefficients of the same sign. Then the zeros of \(f\) and \(g\) interlace if and only if every nontrivial linear combination \(af + bg\) has only real zeros.* (Proof: consider \(R = f/g\); interlacing \(\Leftrightarrow\) \(R\) strictly monotone between poles; strict monotonicity \(\Leftrightarrow\) every horizontal line meets the graph \(n\) times.)

**Theorem 4.4** (Real-rootedness and interlacing preservation). *If \(p, q\) are monic real-rooted polynomials of degree \(n\), then so does \(p \boxplus_n q\). Moreover, if \(p_1, p_2\) are two such polynomials and their zeros interlace, then \(p_1 \boxplus_n q\) and \(p_2 \boxplus_n q\) interlace.*

*Proof.* We first treat monic polynomials of exact degree \(n\) with simple zeros. Multiplying an input by a non-zero constant does not change its zeros (and merely scales the convolution in that factor), and polynomials with multiple zeros will be recovered at the end by approximation.

For the real-rootedness assertion translations allow us to assume that \(p\) and \(q\) are centered; once it is proved in that situation formula (2.3) removes the centering. We prove, by induction on \(n\), the slightly stronger statement that simple inputs give simple outputs. Simultaneously we use that in all smaller degrees the matrices of Lemma 4.3 are non-negative; this non-negativity was reduced in Lemma 4.3 to the interlacing part of the theorem in the smaller degree and is therefore part of the induction hypothesis.

Base \(n = 1\) is trivial. Assume these assertions known up to degree \(n - 1\). Let \(p, q\) be centered of degree \(n\) with simple real zeros, and define \(r_p = p'/n\), \(r_q = q'/n\). By the induction hypothesis,

\[
r = r_p \boxplus_{n-1} r_q
\]

has real simple zeros \(\mu_1 < \cdots < \mu_{n-1}\). Also, by the induction hypothesis again, the matrices \(K, \widetilde{K}\) arising from the degree \(n - 1\) derivative convolution are nonnegative doubly stochastic, so \((Kw^p)_i + (\widetilde{K}w^q)_i > 0\).

Lemma 4.2 applied to both \((R_p \boxplus_n q)\) and \((p \boxplus_n R_q)\) together with the split (2.6) yields, at the points \(\mu_i\),

\[
(p \boxplus_n q)(\mu_i) = -r'(\mu_i)\bigl((Kw^p)_i + (\widetilde{K}w^q)_i\bigr). \tag{2.19}
\]

The parenthesized quantity is strictly positive. For a monic degree-\((n-1)\) polynomial \(r\) the sign of \(r'(\mu_i)\) is \((-1)^{(n-1)-i}\); hence the values \((p \boxplus_n q)(\mu_i)\) alternate in sign.

A monic polynomial of degree \(n\) whose derivative has real simple zeros and whose values at these critical points alternate in sign has \(n\) real simple zeros (one in each interval \((-\infty, \mu_1), (\mu_1, \mu_2), \ldots, (\mu_{n-1}, \infty)\)). Indeed the sign just computed gives \((p \boxplus_n q)(\mu_{n-1}) < 0\) while the polynomial is positive for large positive \(x\), and \((p \boxplus_n q)(\mu_1)\) has sign \((-1)^{n-1}\), opposite to the sign \((-1)^n\) at large negative \(x\); between two consecutive critical points the derivative has a fixed sign, so the alternation yields exactly one crossing in each interval and none at a critical point. Thus \(p \boxplus_n q\) is real-rooted in the centered case, hence in general by (2.3).

This completes the induction for real-rootedness.

To prove interlacing preservation, let \(p_1, p_2\) be two interlacing degree-\(n\) polynomials. By Obreschkoff, every linear combination \(h = ap_1 + bp_2\) is real-rooted. If the leading coefficient of \(h\) is non-zero we divide by it and apply the real-rootedness part just proved (multiplying the convolution afterwards by the same constant); if the leading coefficient vanishes we approximate, say, by \(ap_1 + (b + \varepsilon)p_2\) and pass to the limit. Consequently

\[
(ap_1 + bp_2) \boxplus_n q
\]

is real-rooted for all \(a, b\). By linearity of \(\boxplus_n\) in the first factor,

\[
(ap_1 + bp_2) \boxplus_n q = a(p_1 \boxplus_n q) + b(p_2 \boxplus_n q).
\]

Hence every linear combination of \(p_1 \boxplus_n q\) and \(p_2 \boxplus_n q\) is real-rooted. Applying the Obreschkoff theorem in this limiting form (equivalently, factoring out any common zeros first) yields that \(p_1 \boxplus_n q\) and \(p_2 \boxplus_n q\) interlace.

It remains only to spell out the harmless limiting convention that was used in Lemma 4.3. The passage from simple to multiple roots in the real-rootedness assertion itself is obtained by the same coefficientwise approximation, since the set of real-rooted polynomials is closed. The interlacing theorem just proved for simple polynomials with non-zero leading coefficient also covers the padded leading-zero inputs occurring there: the approximation \(\ell_j^{(\varepsilon)} = \ell_j + \varepsilon r_p\) (together with an arbitrarily small perturbation to remove common zeros) reduces that situation to the strict case, and bilinearity plus continuity of the roots allow one to pass to the limit. Multiple common roots in the statement of the theorem itself are dealt with by the same perturbation.

Finally, the nonnegativity part of Lemma 4.3 now holds in every degree, because it was reduced to interlacing preservation in the relevant lower degree, which we have proved by induction. \(\square\)

### 6. The key decomposition of the convolved critical values

Keep \(p, q\) centered and simple, and keep the notation above. For the convolved polynomial define its \(w\)-numbers by

\[
w_i(p \boxplus_n q) := -\frac{(p \boxplus_n q - x\,r)(\mu_i)}{r'(\mu_i)}. \tag{2.20}
\]

Then by (2.6) and Lemma 4.2 (and its \(p \leftrightarrow q\) analogue),

\[
w_i(p \boxplus_n q) = (Kw^p)_i + (\widetilde{K}w^q)_i, \tag{2.21}
\]

where \(K, \widetilde{K}\) are nonnegative doubly stochastic matrices and \(w^p, w^q\) are the vectors of \(w\)-numbers of \(p\) and \(q\).

### 7. The one-line estimate and conclusion

Define

\[
A_p := \sum_{i=1}^{m} \frac{1}{w_i(p)}, \qquad A_q := \sum_{i=1}^{m} \frac{1}{w_i(q)},
\]

and similarly for \(p \boxplus_n q\). If \(S_i := (Kw^p)_i\), then by Jensen's inequality for the convex function \(x \mapsto 1/x\) (using the row sums of \(K\) to form convex combinations and the column sums afterwards),

\[
\sum_{i=1}^{m} \frac{1}{S_i} \leq \sum_{i=1}^{m} \frac{1}{w_i(p)} = A_p, \tag{2.22}
\]

and similarly for \(T_i := (\widetilde{K}w^q)_i\) one has \(\sum_i 1/T_i \leq A_q\).

For positive \(S, T\) and every real \(\alpha\),

\[
\frac{1}{S + T} \leq \frac{\alpha^2}{S} + \frac{(1 - \alpha)^2}{T}, \tag{2.23}
\]

since the difference is \((\alpha T - (1 - \alpha)S)^2/(ST(S + T))\). Summing (2.23) with \(S = S_i\), \(T = T_i\) and using (2.21) and (2.22) yields

\[
\sum_{i=1}^{m} \frac{1}{w_i(p \boxplus_n q)} \leq \alpha^2 A_p + (1 - \alpha)^2 A_q.
\]

Choosing \(\alpha = A_q/(A_p + A_q)\) gives

\[
\sum_{i=1}^{m} \frac{1}{w_i(p \boxplus_n q)} \leq \frac{A_p A_q}{A_p + A_q}. \tag{2.24}
\]

By Lemma 4.1,

\[
\Phi_n(p) = \frac{n}{4} A_p, \qquad \Phi_n(q) = \frac{n}{4} A_q, \qquad \Phi_n(p \boxplus_n q) = \frac{n}{4} \sum_{i=1}^{m} \frac{1}{w_i(p \boxplus_n q)}.
\]

Multiplying (2.24) by \(n/4\) and inverting gives

\[
\frac{1}{\Phi_n(p \boxplus_n q)} \geq \frac{1}{\Phi_n(p)} + \frac{1}{\Phi_n(q)}.
\]

This proves the inequality for centered simple-rooted polynomials.

### 8. Removing centering and multiple roots

If the roots are not centered, translate \(p\) and \(q\) to make them centered, apply the proved inequality, and translate back using (2.3). The value of \(\Phi_n\) is unchanged by a common translation of the roots.

If a polynomial has a multiple root we interpret \(1/\Phi_n\) as 0. Choose sequences \(p^{(s)}, q^{(s)}\) of monic real-rooted polynomials with simple roots converging coefficientwise to the given ones. The map \((p, q) \mapsto p \boxplus_n q\) is polynomial in the coefficients, hence continuous, and for simple polynomials the quantities in (2.8) are continuous functions of the roots. Moreover (2.8) shows that as two roots of a real-rooted polynomial coalesce the sum defining \(\Phi_n\) tends to \(+\infty\), so its reciprocal tends to 0. Applying the proved inequality to \(p^{(s)}, q^{(s)}\) and taking \(\liminf\) therefore gives the desired inequality in the limit. In particular, if the right-hand side has a positive limit the convolved polynomials cannot acquire a multiple root in the limit (otherwise the left-hand side would tend to 0), and if the right-hand side tends to 0 the estimate is immediate. Thus the convention on multiple roots is consistent and the inequality survives passage to the limit.

### Conclusion

For all \(n \geq 2\) and all monic real-rooted degree-\(n\) polynomials \(p, q\) (with \(\Phi_n = \infty\) on multiple roots),

\[
\boxed{\frac{1}{\Phi_n(p \boxplus_n q)} \geq \frac{1}{\Phi_n(p)} + \frac{1}{\Phi_n(q)}}.
\]
