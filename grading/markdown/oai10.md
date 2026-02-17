## 10 Kernelized CP--ALS subproblem with missing data: matrix-free PCG with Kronecker preconditioning

### Problem

Given a \(d\)-way tensor \(\mathcal{T} \in \mathbb{R}^{n_1 \times n_2 \times \cdots \times n_d}\) such that the data is unaligned (meaning the tensor \(\mathcal{T}\) has missing entries), we consider the problem of computing a CP decomposition of rank \(r\) where some modes are infinite-dimensional and constrained to be in a Reproducing Kernel Hilbert Space (RKHS). We want to solve this using an alternating optimization approach, and our question is focused on the mode-\(k\) subproblem for an infinite-dimensional mode. For the subproblem, then CP factor matrices \(A_1, \ldots, A_{k-1}, A_{k+1}, \ldots, A_d\) are fixed, and we are solving for \(A_k\).

Our notation is as follows. Let \(N = \prod_i n_i\) denote the product of all sizes. Let \(n \equiv n_k\) be the size of mode \(k\), let \(M = \prod_{i \neq k} n_i\) be the product of all dimensions except \(k\), and assume \(n \ll M\). Since the data are unaligned, this means only a subset of \(\mathcal{T}\)'s entries are observed, and we let \(q \ll N\) denote the number of observed entries. We let \(T \in \mathbb{R}^{n \times M}\) denote the mode-\(k\) unfolding of the tensor \(\mathcal{T}\) with all missing entries set to zero. The vec operations create a vector from a matrix by stacking its columns, and we let \(S \in \mathbb{R}^{N \times q}\) denote the selection matrix (a subset of the \(N \times N\) identity matrix) such that \(S^T \operatorname{vec}(T)\) selects the \(q\) known entries of the tensor \(\mathcal{T}\) from the vectorization of its mode-\(k\) unfolding. We let \(Z = A_d \odot \cdots \odot A_{k+1} \odot A_{k-1} \odot \cdots \odot A_1 \in \mathbb{R}^{M \times r}\) be the Khatri--Rao product of the factor matrices corresponding to all modes except mode \(k\). We let \(B = TZ\) denote the MTTKRP of the tensor \(\mathcal{T}\) and Khatri--Rao product \(Z\).

We assume \(A_k = KW\) where \(K \in \mathbb{R}^{n \times n}\) denotes the psd RKHS kernel matrix for mode \(k\). The matrix \(W\) of size \(n \times r\) is the unknown for which we must solve. The system to be solved is

\[
\bigl[(Z \otimes K)^T S S^T (Z \otimes K) + \lambda (I_r \otimes K)\bigr] \operatorname{vec}(W) = (I_r \otimes K) \operatorname{vec}(B). \tag{95}
\]

Here, \(I_r\) denotes the \(r \times r\) identity matrix. This is a system of size \(nr \times nr\). Using a standard linear solver costs \(O(n^3 r^3)\), and explicitly forming the matrix is an additional expense.

Explain how an iterative preconditioned conjugate gradient linear solver can be used to solve this problem more efficiently. Explain the method and choice of preconditioner. Explain in detail how the matrix-vector products are computed and why this works. Provide complexity analysis. We assume \(n, r < q \ll N\). Avoid any computation of order \(N\).

### Solution (matrix-free PCG with Kronecker preconditioning)

We show how to solve (95) efficiently using a matrix-free preconditioned conjugate gradient (PCG) method. The central idea is (i) to express all masked contractions using only the observed indices, and (ii) to choose a preconditioner that is spectrally close to the true operator and admits a fast inverse via Kronecker eigenstructure.

**Observed-index notation (eliminating \(S\) and avoiding \(Z\)).** Let the set of observed entries in the mode-\(k\) unfolding be

\[
\Omega = \{(i_\ell, j_\ell)\}_{\ell=1}^{q}, \quad i_\ell \in \{1, \ldots, n\}, \quad j_\ell \in \{1, \ldots, M\}.
\]

(Here \(j_\ell\) encodes the multi-index over modes \(\neq k\).) For each observation \(\ell\), define the corresponding row of the Khatri--Rao product by

\[
z_\ell^T := e_{j_\ell}^T Z \in \mathbb{R}^{1 \times r}, \quad \ell = 1, \ldots, q,
\]

and collect these rows into the matrix \(Z_\Omega \in \mathbb{R}^{q \times r}\). Crucially, \(Z_\Omega\) can be formed without ever constructing \(Z \in \mathbb{R}^{M \times r}\): for \(s = 1, \ldots, r\),

\[
(z_\ell)_s = \prod_{m \neq k} A_m(i_m^{(\ell)}, s),
\]

where \((i_m^{(\ell)})_{m \neq k}\) is the multi-index corresponding to \(j_\ell\). Thus \(Z_\Omega\) is only \(q \times r\).

Also define the row-selection matrix \(R_\Omega \in \mathbb{R}^{q \times n}\) by

\[
(R_\Omega)_{\ell, i_\ell} = 1, \qquad (R_\Omega)_{\ell, i} = 0 \text{ for } i \neq i_\ell.
\]

Then for any \(U \in \mathbb{R}^{n \times r}\), \((R_\Omega U)_{\ell,:} = U_{i_\ell,:}\).

**Matrix-free operator application.** It is convenient to work with matrices rather than the vectorized unknown. For any \(X \in \mathbb{R}^{n \times r}\), define \(x = \operatorname{vec}(X)\). The Kronecker identity

\[
(Z \otimes K) \operatorname{vec}(X) = \operatorname{vec}(K X Z^T) \tag{96}
\]

implies that the masked product \(S S^T (Z \otimes K) \operatorname{vec}(X)\) extracts exactly the \(q\) scalars

\[
s_\ell(X) := e_{i_\ell}^T K X \, z_\ell = (KX)_{i_\ell,:} \cdot z_\ell, \quad \ell = 1, \ldots, q.
\]

Equivalently, with \(\mathbf{1}_r\) the \(r\)-vector of ones,

\[
s(X) = \bigl(R_\Omega K X \odot Z_\Omega\bigr) \mathbf{1}_r \in \mathbb{R}^q. \tag{97}
\]

A direct expansion shows

\[
(Z \otimes K)^T S S^T (Z \otimes K) \operatorname{vec}(X) = \sum_{\ell=1}^{q} s_\ell(X) \,(z_\ell \otimes K e_{i_\ell}) = \operatorname{vec}\!\left(K \sum_{\ell=1}^{q} e_{i_\ell}\, s_\ell(X)\, z_\ell^T\right) = \operatorname{vec}\bigl(K\, R_\Omega^T \operatorname{Diag}(s(X))\, Z_\Omega\bigr). \tag{98}
\]

Therefore the full coefficient operator in (95) can be applied without forming any \(N\)- or \(M\)-dimensional objects:

\[
A \operatorname{vec}(X) = \operatorname{vec}\bigl(K\, R_\Omega^T \operatorname{Diag}(s(X))\, Z_\Omega + \lambda K X\bigr), \quad \text{where } s(X) \text{ is given by (97).} \tag{99}
\]

**Right-hand side without forming \(B = TZ\).** Let \(t \in \mathbb{R}^q\) collect the observed tensor values in the unfolding: \(t_\ell := T_{i_\ell, j_\ell}\). Then the sparse MTTKRP satisfies

\[
B = TZ = R_\Omega^T \operatorname{Diag}(t)\, Z_\Omega \in \mathbb{R}^{n \times r}, \tag{100}
\]

and the right-hand side becomes

\[
b = (I_r \otimes K) \operatorname{vec}(B) = \operatorname{vec}(KB). \tag{101}
\]

Again, no \(M \times r\) matrix \(Z\) is formed, and no computation scales with \(N\).

**PCG formulation.** Assume \(K\) is positive definite, or replace it by \(K + \varepsilon I\) with a small nugget \(\varepsilon > 0\) (standard in kernel methods). Then the operator in (95) is symmetric positive definite (SPD), and CG applies. PCG iterates on the linear system

\[
A\,w = b, \qquad w = \operatorname{vec}(W),
\]

using only: (i) matrix-free applications of \(A\) via (99), and (ii) applications of a preconditioner inverse \(P^{-1}\) described next.

**A Kronecker preconditioner from mean masking.** Let \(\rho := q/N\) be the observation density. If the observed set is approximately uniform, a common and effective approximation is

\[
S S^T \approx \rho\, I.
\]

Under this replacement,

\[
(Z \otimes K)^T (\rho\, I)(Z \otimes K) = \rho\,(Z^T Z) \otimes (K^T K) = \rho\,\Gamma \otimes K^2, \quad \Gamma := Z^T Z \in \mathbb{R}^{r \times r}.
\]

This motivates the SPD preconditioner

\[
P := \rho\,\Gamma \otimes K^2 + \lambda\, I_r \otimes K. \tag{102}
\]

The matrix \(\Gamma\) is cheap to form without \(Z\) by the standard CP identity

\[
\Gamma = Z^T Z = (A_d^T A_d) * \cdots * (A_{k+1}^T A_{k+1}) * (A_{k-1}^T A_{k-1}) * \cdots * (A_1^T A_1), \tag{103}
\]

where \(*\) denotes the Hadamard product. This requires only the \(r \times r\) Gram matrices of the other modes.

**Fast application of \(P^{-1}\) via eigendecompositions.** Compute once the eigendecompositions

\[
K = U \operatorname{Diag}(\sigma_1, \ldots, \sigma_n)\, U^T, \qquad \Gamma = V \operatorname{Diag}(\gamma_1, \ldots, \gamma_r)\, V^T,
\]

with \(U \in \mathbb{R}^{n \times n}\), \(V \in \mathbb{R}^{r \times r}\) orthogonal and \(\sigma_i, \gamma_a \geq 0\). Then (102) becomes

\[
P = (V \otimes U)\, \operatorname{Diag}\!\bigl(\rho\,\gamma_a\,\sigma_i^2 + \lambda\,\sigma_i\bigr)_{i=1,\ldots,n;\; a=1,\ldots,r}\, (V \otimes U)^T.
\]

Hence for any residual \(r = \operatorname{vec}(R)\) with \(R \in \mathbb{R}^{n \times r}\),

\[
\widehat{R} := U^T R V, \qquad \widehat{Y}_{i,a} := \frac{\widehat{R}_{i,a}}{\rho\,\gamma_a\,\sigma_i^2 + \lambda\,\sigma_i}, \qquad P^{-1} r = \operatorname{vec}\bigl(U \widehat{Y} V^T\bigr). \tag{104}
\]

Importantly, \(K^2\) is never formed explicitly; only the eigenvalues \(\sigma_i^2\) are used. If some \(\sigma_i = 0\), either add a nugget \(K \leftarrow K + \varepsilon I\) or restrict to \(\operatorname{range}(K)\); in either case, \(P\) remains SPD.

**Matrix-free matvec algorithm (what PCG actually computes).** Given \(x = \operatorname{vec}(X)\) with \(X \in \mathbb{R}^{n \times r}\), compute \(y = Ax\) as:

1. \(U \leftarrow KX\).

2. For \(\ell = 1, \ldots, q\), compute \(s_\ell \leftarrow U_{i_\ell,:} \cdot z_\ell\) (rowwise dot product).

3. Accumulate \(G \in \mathbb{R}^{n \times r}\) by scatter-add:

\[
G_{i_\ell,:} \mathrel{+}= s_\ell\, z_\ell^T \quad (\ell = 1, \ldots, q), \qquad \text{equivalently } G = R_\Omega^T \operatorname{Diag}(s)\, Z_\Omega.
\]

4. Return \(y = \operatorname{vec}(KG + \lambda U)\).

The right-hand side is computed once using (100)--(101): form \(H = R_\Omega^T \operatorname{Diag}(t)\, Z_\Omega\) by the same scatter pattern as in step 3 (with \(s\) replaced by \(t\)), then set \(b = \operatorname{vec}(KH)\).

**Why PCG converges quickly.** Let \(e_m\) denote the PCG error after \(m\) iterations. Since \(A\) and \(P\) are SPD, standard PCG theory yields

\[
\frac{\|e_m\|_A}{\|e_0\|_A} \leq 2 \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^m, \qquad \kappa := \kappa\bigl(P^{-1/2} A\, P^{-1/2}\bigr).
\]

When the mask is approximately uniform random, \(S S^T\) is spectrally close to \(\rho\, I\) and thus \(A\) is close (in a spectral sense) to the Kronecker-structured approximation (102), which typically clusters the eigenvalues of \(P^{-1}A\) and yields small iteration counts.

**Complexity (avoiding any \(\mathcal{O}(N)\) work).** All costs below are expressed in terms of \((n, r, q)\) (and small mode sizes for forming Gram matrices), and no object of size \(N\) or \(M\) is ever formed.

*Precomputation.*

- Build \(Z_\Omega \in \mathbb{R}^{q \times r}\) from observed multi-indices: \(\mathcal{O}(qr(d-1))\) multiplications (or \(\mathcal{O}(qr)\) if factor rows are accessed efficiently).

- Form \(\Gamma = Z^T Z\) via (103): \(\mathcal{O}\bigl(\sum_{m \neq k} n_m r^2\bigr)\) to form each \(A_m^T A_m\) plus \(\mathcal{O}((d-1)r^2)\) Hadamard products.

- Eigendecompositions: \(\mathcal{O}(n^3 + r^3)\).

- Right-hand side \(b = \operatorname{vec}(KH)\) with \(H = R_\Omega^T \operatorname{Diag}(t)\, Z_\Omega\): \(\mathcal{O}(qr + n^2 r)\).

*Per PCG iteration.*

- Two dense kernel multiplies (\(KX\) and \(KG\)): \(\mathcal{O}(n^2 r)\) each, i.e.\ \(\mathcal{O}(n^2 r)\) up to constants.

- Two observation-driven contractions (compute \(s_\ell\) and scatter-add \(G\)): \(\mathcal{O}(qr)\).

- Apply \(P^{-1}\) via (104) (two basis changes and diagonal scaling): \(\mathcal{O}(n^2 r + nr^2)\).

- Vector inner products and saxpys on \(\mathbb{R}^{nr}\): \(\mathcal{O}(nr)\) (lower order).

Thus one PCG iteration costs

\[
\mathcal{O}\bigl(qr + n^2 r + nr^2\bigr),
\]

and \(T_{\mathrm{cg}}\) iterations cost

\[
\mathcal{O}\!\left(T_{\mathrm{cg}}(qr + n^2 r + nr^2)\right).
\]

This is substantially smaller than the \(\mathcal{O}((nr)^3)\) cost of a dense solve, and the method never performs any computation of order \(N\).
