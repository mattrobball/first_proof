# Grading Transcript

- Problem: `10`
- Attempt: `oai10`
- Started (UTC): `2026-02-17T19:15:48.805202+00:00`
- Finished (UTC): `2026-02-17T19:19:00.461326+00:00`
- Grade: **4/4** (Complete Solution)

## Question

Given a $d$-way tensor $\mathcal{T} \in \mathbb{R}^{n_1 \times n_2 \times \cdots \times n_d}$
such that the data is unaligned (meaning the tensor $\mathcal{T}$ has missing entries),
we consider the problem of computing a CP decomposition of rank $r$ where some modes are infinite-dimensional and constrained to be in a Reproducing Kernel Hilbert Space (RKHS).
We want to solve this using an alternating optimization approach, and our question is focused on the mode-$k$ subproblem for an infinite-dimensional mode.
For the subproblem, then CP factor matrices
$A_1, \dots, A_{k-1}, A_{k+1}, \dots, A_d$ are fixed, and we are solving for $A_k$.

Our notation is as follows.
Let $N = \prod_i n_i$ denote the product of all sizes.
Let $n \equiv n_k$ be the size of mode $k$, let
$M = \prod_{i\neq k} n_i$ be the product of all dimensions except $k$, and assume $n \ll M$.
Since the data are unaligned, this means only a subset of $\mathcal{T}$'s entries are observed, and we let $q \ll N$ denote the number of observed entries.
We let $T \in \mathbb{R}^{n \times M}$ denote the mode-$k$ unfolding of the tensor $\mathcal{T}$ with all missing entries set to zero.
The $\operatorname{vec}$ operations creates a vector from a matrix by stacking its columns,
and we let $S \in \mathbb{R}^{N \times q}$ denote the selection matrix (a subset of the $N \times N$ identity matrix) such that $S^T \operatorname{vec}(T)$ selects the $q$ known entries of the tensor $\mathcal{T}$ from the vectorization of its mode-$k$ unfolding.
We let $Z = A_d \odot \cdots \odot A_{k+1} \odot A_{k-1} \odot \cdots \odot A_1 \in \mathbb{R}^{M \times r}$ be the Khatri-Rao product of the factor matrices corresponding to all modes except mode $k$.
We let $B = TZ$ denote the MTTKRP of the tensor $\mathcal{T}$ and Khatri-Rao product $Z$.

We assume $A_k = KW$ where
$K \in \mathbb{R}^{n \times n}$ denotes the psd RKHS kernel matrix for mode $k$.
The matrix $W$ of size $n \times r$ is the unknown for which we must solve.
The system to be solved is
\begin{equation}
	\left[
    (Z \otimes K)^T S
    S^T (Z \otimes K)
    + \lambda (I_r \otimes K)
  \right]\operatorname{vec}(W)
	= (I_r \otimes K)
	\operatorname{vec}( B ). \nonumber
\end{equation}
Here, $I_r$ denotes the $r \times r$ identity matrix.
This is a system of size $nr \times nr$
Using a standard linear solver costs $O(n^3 r^3)$,
and explicitly forming the matrix is an additional expense.

Explain how an iterative preconditioned conjugate gradient linear solver can be used to solve this problem more efficiently. Explain the method and choice of preconditioner. Explain in detail how the matrix-vector products are computed and why this works. Provide complexity analysis.
We assume $n,r < q \ll N$. Avoid any computation of order $N$.

## Solution Attempt

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

## Editor Dispatch

Based on the mathematical and algorithmic nature of the proof (Matrix-free PCG for Tensor Decomposition), here are the assignments:

**Reasoning:**
1.  **Correctness & Completeness**: Assigned to **claude_code**. This perspective requires verifying complex linear algebra derivations (Kronecker products, vectorization identities) and ensuring the logic of the preconditioning strategy holds. Claude is the strongest reasoning engine for tracing multi-step mathematical deductions and identifying logical gaps.
2.  **Clarity & Rigor**: Assigned to **codex_cli**. The text describes a numerical algorithm. Codex excels at "linting" procedural descriptions—checking for variable definition consistency, dimensional mismatches (type safety), and ensuring the algorithmic steps are precisely defined, which constitutes the bulk of "rigor" for this computational problem.
3.  **Reference Validity**: Assigned to **gemini_api**. The proof relies on "standard" identities (CP Gram matrix, PCG convergence bounds) rather than explicit citations. Gemini's broad knowledge base is best suited to confirm that these invoked theorems are indeed standard, correctly stated, and applicable in this context.

```json
{
  "assignments": {
    "Correctness & Completeness": "claude_code",
    "Clarity & Rigor": "codex_cli",
    "Reference Validity": "gemini_api"
  },
  "reasoning": "Claude is assigned to Correctness for its strong mathematical reasoning capabilities to verify the linear algebra derivations. Codex is assigned to Clarity to check the algorithmic precision and notational consistency (acting as a 'linter' for the math). Gemini is assigned to Reference Validity to verify the standard theorems and identities invoked in the text."
}
```

## Reviewer — Correctness & Completeness

# Review: Correctness & Completeness

## Perspective: Validity of logical inferences, soundness of deductions, mathematical gaps, missing lemmas, unstated assumptions, and incomplete case analysis.

---

### Overall Assessment

This is a well-structured and largely correct exposition of matrix-free PCG for the kernelized CP-ALS subproblem with missing data. The core ideas — working only with observed indices, exploiting Kronecker structure for preconditioning, and avoiding any $\mathcal{O}(N)$ computation — are sound. However, there are several correctness and completeness issues ranging from a significant sign/structure error in the operator derivation to missing justifications and unstated assumptions.

---

### Detailed Issue Analysis

**1. The operator in (99) is missing the contribution from the regularizer's kernel structure.**

Equation (95) has the regularizer $\lambda(I_r \otimes K)$, so the full operator applied to $\text{vec}(X)$ should yield $\text{vec}(K R_\Omega^T \text{Diag}(s(X)) Z_\Omega + \lambda K X)$. Equation (99) does write exactly this. This is correct — the regularizer term $\lambda(I_r \otimes K)\text{vec}(X) = \text{vec}(\lambda K X)$ is properly included. ✓

**2. The elementwise (Hadamard) product in equation (97) conflates matrix and vector operations.**

In (97), the expression $(R_\Omega K X \odot Z_\Omega) \mathbf{1}_r$ uses $\odot$ to denote elementwise product of two $q \times r$ matrices, then sums across columns. This produces the correct $q$-vector of scalars $s_\ell$. However, earlier in the document, $\odot$ is used for the Khatri-Rao product (face-splitting product). Using the same symbol for both the Khatri-Rao product and the Hadamard (elementwise) product is a notational collision that could cause confusion, though in context each usage is distinguishable.

**3. The scatter-add derivation in (98) has a gap in justification.**

The chain of equalities in (98) moves from $\sum_{\ell=1}^{q} s_\ell(X)(z_\ell \otimes K e_{i_\ell})$ to $\text{vec}(K \sum_\ell e_{i_\ell} s_\ell(X) z_\ell^T)$ to $\text{vec}(K R_\Omega^T \text{Diag}(s(X)) Z_\Omega)$. The middle step uses the identity $z_\ell \otimes K e_{i_\ell} = \text{vec}(K e_{i_\ell} z_\ell^T)$. This is correct by the standard vec-Kronecker identity $\text{vec}(ABC) = (C^T \otimes A)\text{vec}(B)$ with $B = e_{i_\ell}$, $A = K$, $C = z_\ell^T$ (noting dimensions). However, this key identity is never stated or cited; the reader must infer it.

**4. The preconditioner motivation via $SS^T \approx \rho I$ is incomplete.**

The approximation $SS^T \approx \rho I$ is stated but not properly justified. $S \in \mathbb{R}^{N \times q}$ is a selection matrix (subset of columns of $I_N$), so $SS^T$ is a diagonal $N \times N$ matrix with ones at observed positions and zeros elsewhere — it is a projection, not $\rho I$. The claim is that under uniform random sampling, $SS^T$ behaves spectrally like $\rho I$ in expectation (since $\mathbb{E}[SS^T] = \rho I$ when each entry is observed independently with probability $\rho$). This expected-value argument is missing and is important for justifying the preconditioner's effectiveness.

**5. SPD claim for the full operator requires explicit justification.**

The proof states that the operator in (95) is SPD when $K$ is positive definite, but does not verify this. For SPD: $x^T A x = \|S^T(Z \otimes K)x\|^2 + \lambda x^T(I_r \otimes K)x$. The first term is PSD. The second term is positive definite when $K \succ 0$ and $\lambda > 0$. So $A$ is SPD. This is straightforward but should be stated, especially since the entire PCG framework depends on it.

**6. The preconditioner $P$ in (102) uses $K^2$ but the regularizer uses $K$, creating a structural mismatch.**

The preconditioner is $P = \rho \Gamma \otimes K^2 + \lambda I_r \otimes K$. This mixes $K^2$ (from the data term approximation) with $K$ (from the regularizer). In eigenspace, $P$ has diagonal entries $\rho \gamma_a \sigma_i^2 + \lambda \sigma_i$. For this to be SPD, we need $\sigma_i > 0$ for all $i$ (i.e., $K \succ 0$) or the nugget $\varepsilon$. The proof mentions the nugget but doesn't formally verify that $P \succ 0$ under the nugget. This is a minor gap since it follows immediately from $\sigma_i > 0 \Rightarrow \rho \gamma_a \sigma_i^2 + \lambda \sigma_i > 0$.

**7. The formula for $\Gamma$ via Hadamard products of Gram matrices (103) is stated without proof.**

Equation (103) is a well-known identity for the Gram matrix of a Khatri-Rao product, but it is presented without derivation or citation. For completeness at the graduate level, a one-line proof or reference would be appropriate: $(Z^T Z)_{s,t} = \sum_j \prod_{m \neq k} A_m(i_m^{(j)}, s) A_m(i_m^{(j)}, t) = \prod_{m \neq k} (A_m^T A_m)_{s,t}$ where the last step uses the fact that summing over all multi-indices $j$ factors into independent sums over each mode.

**8. Complexity of building $Z_\Omega$ is understated.**

The proof claims $Z_\Omega$ costs $\mathcal{O}(qr(d-1))$ multiplications. Each row $\ell$ requires computing $\prod_{m \neq k} A_m(i_m^{(\ell)}, s)$ for $s = 1, \ldots, r$. This is $(d-1)$ multiplications per component, giving $qr(d-1)$ total. This is correct. However, the parenthetical "$\mathcal{O}(qr)$ if factor rows are accessed efficiently" is misleading — the $(d-1)$ factor cannot be removed by efficient access patterns; it is inherent in the product. It can only be hidden by treating $d$ as a constant.

**9. The right-hand side derivation (100) needs verification.**

Equation (100) claims $B = TZ = R_\Omega^T \text{Diag}(t) Z_\Omega$. Let's verify: $(TZ)_{i,s} = \sum_j T_{i,j} Z_{j,s}$. Since $T$ has zeros at missing entries, only observed entries contribute. For observed entry $(i_\ell, j_\ell)$ with value $t_\ell$: $(TZ)_{i,s} = \sum_{\ell: i_\ell = i} t_\ell (Z_\Omega)_{\ell, s}$. And $(R_\Omega^T \text{Diag}(t) Z_\Omega)_{i,s} = \sum_\ell (R_\Omega)_{\ell,i} t_\ell (Z_\Omega)_{\ell,s} = \sum_{\ell: i_\ell = i} t_\ell (Z_\Omega)_{\ell,s}$. ✓ This checks out.

**10. No discussion of CG convergence when $P^{-1}A$ is not well-conditioned.**

The proof argues PCG converges quickly when the mask is "approximately uniform random," but provides no quantitative bound on $\kappa(P^{-1}A)$ in terms of problem parameters. The convergence guarantee is only the generic CG bound, which is always true. The claim of fast convergence is heuristic, not proven.

**11. Missing treatment of the case when mode $k$ is infinite-dimensional.**

The problem statement says "some modes are infinite-dimensional and constrained to be in an RKHS," and the question focuses on an infinite-dimensional mode $k$. The solution works entirely in the finite $n \times n$ kernel matrix representation $K$, implicitly using the representer theorem to reduce the infinite-dimensional problem to finite dimensions. This crucial step — *why* the infinite-dimensional RKHS optimization reduces to solving for $W \in \mathbb{R}^{n \times r}$ with $A_k = KW$ — is assumed without justification. At graduate rigor, the representer theorem argument should be at least sketched.

---

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Preconditioner motivation (SS^T ≈ ρI)",
      "reason": "SS^T is a binary diagonal matrix (a projection), not ρI. The approximation requires an expected-value argument under uniform random sampling that is never stated. Without this, the preconditioner has no formal justification.",
      "required_fix": "State that under independent uniform sampling with probability ρ, E[SS^T] = ρI, and that concentration inequalities (or empirical experience) ensure spectral closeness for large q. Cite or sketch the argument.",
      "suggestion": "Add a paragraph: 'When entries are observed independently with probability ρ, E[SS^T] = ρI_N. By matrix concentration (e.g., matrix Chernoff bounds), SS^T ≈ ρI spectrally with high probability when q is large, justifying the Kronecker approximation.'"
    },
    {
      "severity": "major",
      "location": "Problem setup / representer theorem",
      "reason": "The problem states mode k is infinite-dimensional in an RKHS, but the solution assumes without justification that the optimization reduces to a finite n×n system via A_k = KW. The representer theorem argument that justifies this reduction is missing entirely.",
      "required_fix": "Add a paragraph establishing that by the representer theorem, the optimal solution for the RKHS-constrained mode lies in the span of the kernel evaluations at the n data points, reducing the infinite-dimensional problem to solving for W ∈ R^{n×r}.",
      "suggestion": "Before the main derivation, state: 'By the representer theorem for RKHS-regularized problems, the optimal A_k lies in the span of {k(x_i, ·)}_{i=1}^n, so A_k = KW for some W ∈ R^{n×r}, where K_{ij} = k(x_i, x_j). This reduces the infinite-dimensional problem to the finite system (95).'"
    },
    {
      "severity": "minor",
      "location": "Notation (⊙ overloading)",
      "reason": "The symbol ⊙ is used for both the Khatri-Rao product (Z = A_d ⊙ ··· ⊙ A_1) and the Hadamard (elementwise) product in equation (97). This dual usage is standard in tensor literature but creates ambiguity within a single document.",
      "required_fix": "Use distinct notation: e.g., ⊙ for Khatri-Rao and * or ∘ for Hadamard, or explicitly clarify at each use.",
      "suggestion": "Add a note after the notation section: 'We use ⊙ for the Khatri-Rao product between tall factor matrices and ∘ (or *) for the elementwise (Hadamard) product between matrices of equal size.' Then update (97) accordingly."
    },
    {
      "severity": "minor",
      "location": "SPD verification of operator A",
      "reason": "The proof claims the operator is SPD and that CG applies, but does not verify positive definiteness. While straightforward (λ > 0 and K ≻ 0 suffice), the claim should be justified since it is a prerequisite for the entire method.",
      "required_fix": "Add a brief verification: x^T A x = ||S^T(Z⊗K)x||² + λ x^T(I_r⊗K)x > 0 for x ≠ 0 when K ≻ 0 and λ > 0.",
      "suggestion": "Insert after equation (95): 'The operator is SPD: for any nonzero x, x^TAx = ||S^T(Z⊗K)x||² + λ·x^T(I_r⊗K)x. The first term is nonneg and the second is positive when K ≻ 0 and λ > 0, so CG is applicable.'"
    },
    {
      "severity": "minor",
      "location": "Equation (98), vec-Kronecker identity",
      "reason": "The derivation jumps from Σ s_ℓ(z_ℓ ⊗ Ke_{i_ℓ}) to vec(K Σ e_{i_ℓ} s_ℓ z_ℓ^T) without citing the identity vec(abc^T) = (c ⊗ a)b used here. At graduate rigor, this step should be explicit.",
      "required_fix": "State the identity: z_ℓ ⊗ Ke_{i_ℓ} = vec(Ke_{i_ℓ} z_ℓ^T) by the standard vec-Kronecker relation.",
      "suggestion": "Add inline: 'Using the identity vec(uv^T) = v ⊗ u, we have z_ℓ ⊗ Ke_{i_ℓ} = vec(Ke_{i_ℓ}z_ℓ^T), so the sum becomes vec(K Σ_ℓ e_{i_ℓ} s_ℓ z_ℓ^T).'"
    },
    {
      "severity": "minor",
      "location": "Complexity of Z_Ω construction",
      "reason": "The parenthetical claim that Z_Ω can be built in O(qr) 'if factor rows are accessed efficiently' is incorrect — the (d-1) factor is inherent in computing products over d-1 modes and cannot be removed by access patterns alone.",
      "required_fix": "Remove the parenthetical or clarify that O(qr) holds only when d is treated as a constant.",
      "suggestion": "Replace with: 'O(qr(d−1)) multiplications, or O(qr) when d is treated as a fixed constant.'"
    },
    {
      "severity": "minor",
      "location": "PCG convergence analysis",
      "reason": "The convergence section only states the generic CG convergence bound and a heuristic argument that eigenvalues cluster when the mask is uniform. No quantitative bound on κ(P^{-1}A) is given in terms of (n, r, q, ρ). The 'fast convergence' claim is empirical, not proven.",
      "required_fix": "Either provide a bound on κ(P^{-1}A) under stated assumptions (e.g., using matrix concentration results) or explicitly acknowledge that the fast convergence claim is heuristic/empirical.",
      "suggestion": "Add: 'A rigorous bound on κ(P^{-1}A) under random sampling can be obtained via matrix concentration inequalities (e.g., [cite relevant work]), but in practice T_cg is observed to be small and roughly independent of problem size. We note that the convergence claim here is supported by empirical evidence rather than a formal spectral bound.'"
    },
    {
      "severity": "minor",
      "location": "Gram matrix identity (103)",
      "reason": "The Hadamard-product identity for the Gram matrix of a Khatri-Rao product is stated without proof or reference. While well-known, at graduate rigor a one-line verification or citation strengthens the exposition.",
      "required_fix": "Add a brief derivation or cite a standard reference (e.g., Kolda & Bader 2009).",
      "suggestion": "Add: 'This follows because (Z^TZ)_{s,t} = Σ_j Π_{m≠k} A_m(i_m^(j),s)A_m(i_m^(j),t) = Π_{m≠k} Σ_{i_m} A_m(i_m,s)A_m(i_m,t) = Π_{m≠k}(A_m^TA_m)_{s,t}; see [Kolda & Bader, SIAM Review 2009].'"
    }
  ],
  "residual_concerns": [
    "The solution does not address numerical stability concerns: when kernel eigenvalues σ_i span many orders of magnitude, the diagonal scaling in (104) may suffer from catastrophic cancellation or overflow. A brief discussion of numerical safeguards would be appropriate.",
    "The relationship between the nugget parameter ε and the regularization parameter λ is not discussed — in practice these interact and affect both the preconditioner quality and the condition number.",
    "No mention is made of how to choose a stopping criterion for PCG that is appropriate for the outer ALS loop (e.g., inexact solves with decreasing tolerance)."
  ]
}
```

## Reviewer — Clarity & Rigor

No listed skill applies (available skills are for skill creation/installation), so this is a direct Clarity & Rigor review.

Overall, the write-up is technically strong and mostly well-structured, but it falls short of graduate-level rigor in a few places where assumptions, notation discipline, and justification strength are not explicit enough.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "PCG formulation (system (95), SPD claim paragraph)",
      "reason": "CG/PCG requires an SPD operator, but the assumptions ensuring SPD are not fully stated (notably lambda > 0). The text discusses K being PD or nuggeted, but does not explicitly enforce lambda > 0 in the theorem-level statement.",
      "required_fix": "State explicit solvability assumptions: lambda > 0 and K ⪰ 0 (or K + epsilon I with epsilon > 0), then prove A is SPD under these assumptions.",
      "suggestion": "Add a short lemma: x^T A x = ||S^T(Z ⊗ K)x||_2^2 + lambda x^T(I_r ⊗ K)x, and conclude strict positivity under the stated conditions."
    },
    {
      "severity": "major",
      "location": "A Kronecker preconditioner from mean masking (Eq. 102)",
      "reason": "The replacement SS^T ≈ rho I is introduced as a practical step but without a precise sampling model; as written it can read like an identity rather than a model-based approximation.",
      "required_fix": "Specify the mask model (e.g., uniformly random observed entries) and clarify that the preconditioner is based on an expected operator approximation, not exact algebra.",
      "suggestion": "Add one sentence with E[SS^T] = rho I under the model, plus a caveat that performance may degrade under structured missingness."
    },
    {
      "severity": "major",
      "location": "Why PCG converges quickly",
      "reason": "The claim that SS^T is spectrally close to rho I and that eigenvalues cluster is asserted without quantitative conditions, proof sketch, or citation.",
      "required_fix": "Either provide a concrete bound with conditions (sample size/coherence assumptions) or label this as heuristic/empirical behavior with citation.",
      "suggestion": "Include a citation to a concentration result for random masks and tie it explicitly to kappa(P^{-1/2}AP^{-1/2})."
    },
    {
      "severity": "major",
      "location": "Eq. (104) and matrix-free matvec algorithm",
      "reason": "Notation collisions reduce precision: r denotes both CP rank and residual vector; U denotes both eigenvectors of K and a temporary matrix U = KX.",
      "required_fix": "Rename overloaded symbols to avoid conflicts (e.g., rank R, residual g, temporary Q = KX).",
      "suggestion": "Add a compact notation table with dimensions and reserve symbols globally."
    },
    {
      "severity": "minor",
      "location": "Observed-index notation and Eq. (100)",
      "reason": "The mapping from tensor multi-index to unfolding column index j_l is implicit, and duplicate observations are not discussed; this leaves scatter formulas slightly under-specified.",
      "required_fix": "Define the unfolding map explicitly and state whether Omega is duplicate-free (or how duplicates are aggregated).",
      "suggestion": "Add one line defining j_l = pi_k((i_m^(l))_{m ≠ k}) and a note on pre-aggregation if duplicates exist."
    },
    {
      "severity": "minor",
      "location": "Eqs. (97)–(99)",
      "reason": "z_l is used as both row and column in different places; transposes are inferable but not consistently explicit.",
      "required_fix": "Fix a single convention (e.g., z_l in R^r column) and write z_l^T only when a row is required.",
      "suggestion": "At first use, annotate key objects with shapes and keep that convention throughout derivations."
    },
    {
      "severity": "minor",
      "location": "Complexity section",
      "reason": "Complexity statements rely on hidden assumptions (dense K matvec at O(n^2 r), cheap row access for all fixed factors), which are not stated explicitly.",
      "required_fix": "State computational assumptions upfront and separate dense-kernel cost from structured/approximate-kernel variants.",
      "suggestion": "Add a short assumptions line before complexity and optionally one alternative line for low-rank/fast-kernel settings."
    }
  ],
  "residual_concerns": [
    "The algorithm specification omits an explicit stopping rule (relative residual tolerance, max iterations), which weakens reproducibility at graduate rigor."
  ]
}
```

## Reviewer — Reference Validity

The solution presents a derivation of a matrix-free PCG method for a kernelized CP-ALS subproblem. From the perspective of **Reference Validity**, the content is mathematically self-contained and relies on standard linear algebra identities and numerical optimization principles. The derivation correctly employs properties of the Kronecker and Khatri-Rao products without misstating them.

However, as a graduate-level text, it appeals to "standard" theories and "common" approximations without explicit bibliographic citations. While the results invoked are indeed standard in the field, rigorous academic writing requires attribution for specific convergence bounds and heuristic approximations (like the mean-field approximation for masking).

### Issues

```json
{
  "issues": [
    {
      "severity": "minor",
      "location": "Section 'A Kronecker preconditioner from mean masking'",
      "reason": "The text justifies the preconditioner by stating that $S S^T \\approx \\rho I$ is a 'common and effective approximation' when the mask is uniform. This appeals to external results regarding the spectral properties of random sampling operators (concentration of measure) without citation or proof.",
      "required_fix": "Cite a standard reference in the matrix or tensor completion literature that establishes the validity or common usage of this approximation.",
      "suggestion": "Include a citation to foundational works in tensor completion (e.g., Kolda & Bader) or matrix completion (e.g., Candès & Recht) where this spectral approximation is discussed."
    },
    {
      "severity": "minor",
      "location": "Section 'Why PCG converges quickly'",
      "reason": "The text invokes 'standard PCG theory' to provide a specific convergence bound inequality. While the result is correct, graduate-level rigor requires citing a specific source when invoking a named theorem or bound.",
      "required_fix": "Provide a bibliographic reference for the PCG convergence theorem.",
      "suggestion": "Cite a standard numerical linear algebra text, such as Saad's 'Iterative Methods for Sparse Linear Systems' or Golub & Van Loan."
    }
  ],
  "residual_concerns": []
}
```

## Grading Decision

The solution attempt provides a complete, correct, and efficient method for solving the specified Kernelized CP-ALS subproblem using Preconditioned Conjugate Gradient (PCG). The author correctly identifies that the core difficulty lies in the efficient application of the system matrix and the preconditioner without forming large tensors. The derivation of the matrix-free matrix-vector product using observed-index scatter-gather operations (Eq. 99) is algebraically correct and avoids the forbidden $O(N)$ complexity. The proposed Kronecker product preconditioner (Eq. 102), derived from a mean-field approximation of the sampling operator, is the standard and appropriate choice for this class of problems. The inversion of this preconditioner using eigendecompositions is correctly handled. The complexity analysis is detailed and accurate.

Regarding the reviewer findings:
1.  **Justification of Preconditioner:** The reviewers correctly note that the approximation $S S^T \approx \rho I$ lacks a rigorous probabilistic derivation (e.g., citing matrix concentration inequalities). However, the solution explicitly frames this as a "common and effective approximation" under uniform sampling, which is sufficient for describing the *construction* of the numerical method. The lack of a formal spectral bound is a minor gap in theoretical rigor, not a flaw in the algorithm itself.
2.  **Representer Theorem:** The reviewer complaint that the solution fails to derive the reduction $A_k = KW$ is invalid. The problem statement explicitly provides this assumption and the resulting linear system, asking only for the solution method for that system.
3.  **Notation and Rigor:** There are minor notation collisions (e.g., $r$ used for both rank and residual) and slight ambiguities (e.g., explicit conditions for $\lambda > 0$ to ensure SPD status), but these are cosmetic issues that do not hinder the understanding or correctness of the proposed solver.

Overall, the solution demonstrates a high level of understanding and provides a practical, expert-level algorithm.

```json
{
  "progress_grade": 4,
  "error_incorrect_logic": "false",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "The solution correctly derives a matrix-free PCG algorithm with a Kronecker-structured preconditioner, efficiently handling the sparse observations and RKHS constraints. The approach avoids O(N) computations as required. Reviewer critiques regarding the rigorous probabilistic justification of the preconditioner and the representer theorem are either minor expositional points or outside the scope of the specific prompt."
}
```
