# Propp-Wilson

The Coupling from the Past (CFTP) algorithm is a technique used in statistical physics and probabilistic graphical models to sample
from the stationary distribution of a Markov chain. It was introduced by Propp and Wilson in 1996 as a method for exact sampling from
a Markov chain without the need for burn-in or mixing time considerations.

The CFTP algorithm is particularly useful when dealing with models that exhibit irreducibility and aperiodicity, as it guarantees that 
the generated samples will be distributed according to the stationary distribution of the Markov chain. This property makes CFTP 
advantageous for tasks such as Bayesian inference, where obtaining samples from the target distribution is crucial.

The main idea behind the CFTP algorithm is to simulate the entire history of the Markov chain from the infinite past until the present,
without requiring any knowledge about the initial state of the chain. By effectively coupling multiple copies of the Markov chain and 
letting them evolve simultaneously, the algorithm constructs a path that reaches the stationary distribution. Once this path is established,
the samples generated at different time points along the path can be treated as independent samples from the stationary distribution.

# Coupling from the Past (CFTP) Sampling Algorithm
1. Initialize system to time t = 0.
2. Set t = 1.
3. Initialize an empty history array, H = [].
4. Generate an initial state, X, for the system at time t.
5. Append X to H: H.append(X).
6. Repeat steps 7-10 until t = T:\
    7. Generate a proposal state, Y, for the system at time t.\
    8. Compute the acceptance probability, p = min(1, P(Y)/P(X)), where P(.) is the target distribution.\
    9. Generate a random number, u, from a uniform distribution between 0 and 1.\
    10. If u <= p, set X = Y; otherwise, set X = X.\
    11. Append X to H: H.append(X).\
    12. Increment t: t = t + 1.
7. Set t = T - 1.
8. Repeat steps 7-12 until t = 0:\
    9. Generate a proposal state, Y, for the system at time t.\
    10. Compute the acceptance probability, p = min(1, P(Y)/P(X)).\
    11. Generate a random number, u, from a uniform distribution between 0 and 1.\
    12. If u <= p, set X = Y; otherwise, set X = X.\
    13. Append X to H: H.append(X).\
    14. Decrement t: t = t - 1.
15. The final history array, H, contains a sample from the target distribution at time T.
