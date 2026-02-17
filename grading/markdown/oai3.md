## 3 A Markov chain from interpolation polynomials?

### Problem

Let \(\lambda = (\lambda_1 > \cdots > \lambda_n \geq 0)\) be a partition with distinct parts. Assume moreover that \(\lambda\) is *restricted*, in the sense that it has a unique part of size 0 and no part of size 1. Does there exist a nontrivial Markov chain on \(S_n(\lambda)\) whose stationary distribution is given by

\[
\frac{F^*_\mu(x_1, \ldots, x_n; q = 1, t)}{P^*_\lambda(x_1, \ldots, x_n; q = 1, t)} \text{ for } \mu \in S_n(\lambda) \tag{3}
\]

where \(F^*_\mu(x_1, \ldots, x_n; q, t)\) and \(P^*_\lambda(x_1, \ldots, x_n; q, t)\) are the interpolation ASEP polynomial and interpolation Macdonald polynomial, respectively? If so, prove that the Markov chain you construct has the desired stationary distribution. By "nontrivial" we mean that the transition probabilities of the Markov chain should not be described using the polynomials \(F^*_\mu(x_1, \ldots, x_n; q, t)\).

### Solution

It may be useful first of all to say in which sense the question can be read. I shall explain that, with the notation which is written in the statement, it is not a well posed question. In particular it has a negative answer if one interprets it as a statement which should be true for arbitrary numerical values of the variables.

Let me recall a small amount of notation from the paper which is quoted in the question. In H. Ben Dali–L. K. Williams, *A combinatorial formula for interpolation Macdonald polynomials*, arXiv:2510.02587, the letter \(f^*_\mu\) is used for the interpolation ASEP polynomial. Their "Main theorem", Theorem 1.3 in § 1 says that this polynomial is equal to the generating series \(F^*_\mu\) of signed multiline queues. I shall use the letter \(f^*_\mu\) below. The same paper contains a factorisation which is special to the specialisation \(q = 1\). More precisely, if \(\operatorname{Supp}(\mu) = \{i : \mu_i > 0\}\) and if \(\ell(\lambda)\) denotes the number of non-zero parts of the partition, Theorem 7.1, equations (7.1)–(7.2), of loc. cit. asserts that for every subset \(S \subset \{1, \ldots, n\}\) of cardinality \(\ell(\lambda)\)

\[
\sum_{\mu \in S_n(\lambda),\, \operatorname{Supp}(\mu) = S} f^*_\mu(x_1, \ldots, x_n; 1, t) = \prod_{i \in S} \left( x_i - \frac{t^{\#(S^c \cap \{1, \ldots, i-1\})}}{t^{n-1}} \right) \prod_{j=2}^{\lambda_1} e^*_{\lambda'_j}(x_1, \ldots, x_n; t) \tag{15}
\]

and that the interpolation Macdonald polynomial is

\[
P^*_\lambda(x_1, \ldots, x_n; 1, t) = \prod_{j=1}^{\lambda_1} e^*_{\lambda'_j}(x_1, \ldots, x_n; t). \tag{16}
\]

Here \(\lambda'\) is the conjugate partition and

\[
e^*_k(x_1, \ldots, x_n; t) = \sum_{\substack{S \subset \{1, \ldots, n\} \\ |S| = k}} \prod_{i \in S} \left( x_i - \frac{t^{\#(S^c \cap \{1, \ldots, i-1\})}}{t^{n-1}} \right) \tag{17}
\]

(this is the definition immediately preceding Theorem 7.1). I shall use these formulas only in the very small example below. The equality between the symbols \(F^*_\mu\) which occur in the statement of the present problem and the polynomials \(f^*_\mu\) is precisely the "Main theorem" just cited.

Recall what a Markov chain on a finite set means. Its transition matrix has non-negative real entries and its stationary distribution is a probability vector, i.e. a list of non-negative real numbers which add up to 1. In the problem, however, the symbols \(x_1, \ldots, x_n\) and \(t\) are left as indeterminates. Over the field of rational functions in these indeterminates there is no notion of "non-negative", and consequently the words Markov chain and probability distribution do not have a mathematical meaning. One might try to repair the statement by demanding that, after every real specialisation of the variables for which the denominator in (3) is non-zero, the displayed formula should give the stationary probabilities of a stochastic matrix depending on the same parameters. With this (the most generous) interpretation the assertion is simply false. The obstruction already appears for the smallest restricted partition.

Indeed take \(n = 2\) and \(\lambda = (2, 0)\). This partition has distinct parts, contains a unique zero and has no part equal to 1. In this case \(\ell(\lambda) = 1\) and, for a fixed support, there is only one permutation of \(\lambda\). Formula (15) therefore gives the individual interpolation ASEP polynomials themselves. Since \(\lambda' = (1, 1)\), from (15)–(17) we obtain

\[
f^*_{(2,0)}(x_1, x_2; 1, t) = (x_1 - t^{-1})\, e^*_1(x_1, x_2; t), \tag{18}
\]

\[
f^*_{(0,2)}(x_1, x_2; 1, t) = (x_2 - 1)\, e^*_1(x_1, x_2; t), \tag{19}
\]

where

\[
e^*_1(x_1, x_2; t) = (x_1 - t^{-1}) + (x_2 - 1). \tag{20}
\]

Equation (16) gives at the same time \(P^*_{(2,0)} = (e^*_1)^2\). Hence the putative stationary weights in (3) would have to be

\[
\pi(2, 0) = \frac{x_1 - t^{-1}}{x_1 + x_2 - 1 - t^{-1}}, \qquad \pi(0, 2) = \frac{x_2 - 1}{x_1 + x_2 - 1 - t^{-1}}. \tag{21}
\]

Now specialise the (so far completely arbitrary) parameters to real numbers, for instance

\[
t = 2, \qquad x_1 = 0, \qquad x_2 = 10.
\]

The denominator in (21) is then \(17/2\), and the two numbers in (21) are respectively

\[
\pi(2, 0) = -\frac{1}{17}, \qquad \pi(0, 2) = \frac{18}{17}.
\]

They add up to 1, as they should algebraically, but they are not a probability vector: one entry is negative (and the other is bigger than 1). No stochastic matrix on the two-point set \(S_2(2, 0) = \{(2, 0), (0, 2)\}\) can have such a stationary distribution, because the stationary distribution of a finite Markov chain is always a list of non-negative real numbers.

This example shows two things. First, if the problem is read literally, with \(x_i\) and \(t\) regarded as formal variables, the phrase "Markov chain with stationary distribution" has no defined meaning. Secondly, under the natural alternative reading that a single statement should hold for arbitrary numerical values of the parameters, the answer is negative (already for the restricted partition \((2, 0)\)). To obtain a genuine and non-trivial problem one would have to add extra hypotheses, for example a specified real chamber of the parameters in which all the quantities in the target are known to be non-negative, and then give an explicit stochastic rule in that chamber. Such additional data are not part of the question as stated, so no Markov chain satisfying the requested property can be constructed from the present formulation.

### References

[1] H. Ben Dali and L. K. Williams, *A combinatorial formula for interpolation Macdonald polynomials*, preprint arXiv:2510.02587. The Main theorem on signed multiline queues is stated in § 1, and the factorisation used above is Theorem 7.1, equations (7.1)–(7.2).
