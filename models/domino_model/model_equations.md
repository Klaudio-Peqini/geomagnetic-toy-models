# Domino Model Equations

## Purpose of This Document

This file provides a **detailed mathematical formulation** for a domino-style geomagnetic toy model, suitable for the `models/domino_model/` folder of the `geomagnetic-toy-models` repository.

At the moment, the repository folder contains `simulate.py`, `parameters.py`, and `analysis.py`, but the raw file views for those Python files currently appear empty in the public repository snapshot I checked, and `model_equations.md` is also empty. Therefore, the equations written here are a **carefully structured canonical formulation** of a domino-type geomagnetic toy model that is consistent with the scientific purpose of the folder, rather than a transcription of implementation details from non-empty code.

---

## 1. Physical Idea Behind the Domino Model

The domino model represents the geomagnetic field as the collective effect of many interacting effective units. Each unit can be thought of as an elementary dipole-like degree of freedom, a spin-like variable, or a reduced mode. The large-scale field is then obtained as a macroscopic average over these units.

The central scientific idea is:

- each element tends to align with its neighbors or with a global mean field,
- each element is subject to damping and fluctuations,
- the global polarity emerges from collective order,
- Reversals occur when the coherent global state collapses and reforms with opposite sign.

This makes the model qualitatively different from a single-variable double-well model.

---

## 2. Choice of State Variables

Let the system contain $N$ interacting effective elements. We denote by

$\theta_i(t), \qquad i = 1,2,\dots,N$

the angular orientation of the $i$-th element relative to a preferred axis, usually interpreted as the rotation axis or dipole axis.

A convenient magnetic proxy associated with each element is its axial projection:

$m_i(t) = \cos \theta_i(t).$

The global dipole-like observable is then defined as the mean projection:

$M(t) = \frac{1}{N}\sum_{i=1}^{N} \cos \theta_i(t).$

This quantity plays the role of the effective axial dipole moment or polarity indicator.

### Interpretation

- $M(t) > 0$: dominant positive polarity,
- $M(t) < 0$: dominant negative polarity,
- $M(t) \approx 0$: weak global coherence or transition state.

---

## 3. Canonical Dynamical Equation

A standard domino-style formulation uses second-order stochastic dynamics for each effective element:

$\ddot{\theta_i} + \gamma \dot{\theta_i}=-\frac{\partial V(\theta_i)}{\partial \theta_i} + \lambda \sum_{j=1}^{N} A_{ij}\,\sin(\theta_j-\theta_i) + \sigma\eta_i(t).$

Here:

- $\gamma$ is a damping coefficient,
- $V(\theta)$ is an effective single-element potential,
- $\lambda$ is the coupling strength,
- $A_{ij}$ is the interaction matrix,
- $\sigma$ is the noise amplitude,
- $\eta_i(t)$ is a stochastic forcing term.

This equation says that each element evolves under the competition between:

1. **local restoring dynamics**,  
2. **interaction with other elements**,  
3. **dissipation**,  
4. **random forcing**.

---

## 4. Effective Potential Term

A commonly used form for the local potential is

$V(\theta) = -\alpha \cos^{2}\theta,$

which favors orientations near $\theta = 0$ and $\theta = \pi$, corresponding to the two opposite axial polarities.

Then

$-\frac{\partial V}{\partial \theta} = - \frac{d}{d\theta}\left(-\alpha \cos^{2}\theta\right) = -2\alpha \sin\theta \cos\theta = -\alpha \sin(2\theta).$

Thus, the dynamical equation becomes

$$\ddot{\theta}_i + \gamma \dot{\theta}_i = -\alpha \sin(2\theta_i) + \lambda \sum_{j=1}^{N} A_{ij}\,\sin(\theta_j-\theta_i) + \sigma\,\eta_i(t).$$

### Interpretation of the potential

The term $-\alpha \sin(2\theta_i)$ drives each element toward the two preferred states:

- $\theta_i \approx 0$,
- $\theta_i \approx \pi$.

These correspond to positive and negative axial alignment.

---

## 5. Coupling Term

The interaction term is

$\lambda \sum_{j=1}^{N} A_{ij}\,\sin(\theta_j-\theta_i).$

This is analogous to coupling terms used in phase and spin-like systems.

### Meaning

- If $\theta_j > \theta_i$, the term tends to increase $\theta_i$,
- if $\theta_j < \theta_i$, it tends to decrease $\theta_i$,
- In general, it tends to reduce angular differences and promote coherence.

### Interaction matrix

The matrix $A_{ij}$ determines the network structure:

- **all-to-all coupling**:
  $A_{ij} = \frac{1}{N} \quad \text{for } i \neq j,$
- **nearest-neighbor coupling** on a ring:
  $$A_{ij} =
  \begin{cases}
  1, & j = i \pm 1 \pmod{N}, \\
  0, & \text{otherwise}
  \end{cases}$$
- **weighted or random coupling**, if desired.

A simple all-to-all version is often the most convenient in toy modeling.

---

## 6. Noise Model

The stochastic terms $\eta_i(t)$ are commonly taken to be independent Gaussian white noises with:

$\langle \eta_i(t) \rangle = 0,$

and

$\langle \eta_i(t)\eta_j(t') \rangle = \delta_{ij}\,\delta(t-t').$

Thus, the parameter $\sigma$ sets the forcing amplitude.

### Physical interpretation

The noise is not meant to be literal thermal noise. Instead, it is a reduced representation of unresolved multiscale fluctuations, such as:

- turbulent convective variability,
- unresolved interactions,
- fast core-scale rearrangements,
- effective stochastic forcing from neglected degrees of freedom.

---

## 7. First-Order Form for Numerical Integration

For implementation, it is often convenient to rewrite the system as first-order equations by introducing angular velocities:

$\omega_i = \dot{\theta}_i.$\]

Then the system becomes

$\dot{\theta}_i = \omega_i,$

$\dot{\omega}_i = -\gamma \omega_i - \alpha \sin(2\theta_i) + \lambda \sum_{j=1}^{N} A_{ij}\,\sin(\theta_j-\theta_i) + \sigma\,\eta_i(t).$

This form is usually the most practical for coding in `simulate.py`.

---

## 8. Mean-Field Simplification

If the coupling is all-to-all, the interaction can be expressed in terms of a global order parameter.

Define

$R e^{i\Phi} = \frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j},$

where:

- $R \in [0,1]$ is the coherence amplitude,
- $\Phi$ is the mean phase.

Then one can show that

$\frac{1}{N}\sum_{j=1}^{N}\sin(\theta_j-\theta_i) = R\sin(\Phi-\theta_i).$

So the equation becomes

$\ddot{\theta}_i + \gamma \dot{\theta}_i = - \alpha \sin(2\theta_i) + \lambda R \sin(\Phi-\theta_i) + \sigma\,\eta_i(t).$

This is a very useful form because it makes explicit that each element interacts with the collective mean state.

---

## 9. Global Magnetic Observables

The most important macroscopic observable is the mean axial projection:

$M(t) = \frac{1}{N}\sum_{i=1}^{N}\cos\theta_i(t).$

This is the simplest polarity proxy.

Other useful observables include:

### 9.1 Mean phase coherence

$R(t) = \left|\frac{1}{N}\sum_{i=1}^{N} e^{i\theta_i(t)}\right|.$

This measures how synchronized the system is.

- $R \approx 1$: strong coherence,
- $R \ll 1$: disordered state.

### 9.2 Angular velocity average

$\Omega(t) = \frac{1}{N}\sum_{i=1}^{N}\omega_i(t).$

This can help detect rapid collective reorganizations.

### 9.3 Polarity sign

$P(t) = \operatorname{sgn}(M(t)).$

This is useful for reversal detection.

---

## 10. Criterion for Reversals

A practical reversal can be defined as a persistent sign change in \(M(t)\):

\[
M(t^-)\,M(t^+) < 0,
\]

with an additional persistence condition to avoid counting short-lived fluctuations.

For example, one may count a reversal only if:

1. \(M(t)\) crosses zero,
2. the new sign persists for at least a threshold time \(\tau_{\min}\),
3. the dipole amplitude recovers to a substantial absolute value after the crossing.

This distinction helps separate:

- **full reversals**,  
- **excursions**,  
- **small noisy oscillations near zero**.

---

## 11. Energy-Like Interpretation

Although the stochastic system is dissipative and driven, one can still define a formal energy-like quantity in the deterministic limit:

\[
E
=
\sum_{i=1}^{N}
\left[
\frac{1}{2}\omega_i^2 + V(\theta_i)
\right]
-\frac{\lambda}{2}\sum_{i,j=1}^{N} A_{ij}\cos(\theta_i-\theta_j).
\]

With \(V(\theta_i) = -\alpha \cos^2\theta_i\), this becomes

\[
E
=
\sum_{i=1}^{N}
\left[
\frac{1}{2}\omega_i^2 - \alpha \cos^2\theta_i
\right]
-\frac{\lambda}{2}\sum_{i,j=1}^{N} A_{ij}\cos(\theta_i-\theta_j).
\]

### Interpretation

- the kinetic term measures rotational activity,
- the local potential favors axial alignment,
- the coupling term favors mutual alignment.

In the presence of damping and noise, \(E\) is not conserved, but it remains a useful conceptual guide.

---

## 12. Dimensionless Parameters and Their Meaning

The most important control parameters are:

### \(N\): number of interacting elements
Controls the system size.

### \(\alpha\): local axial preference
Determines how strongly each element prefers alignment with the dipole axis.

### \(\gamma\): damping
Controls relaxation of angular motion.

### \(\lambda\): interaction strength
Controls how strongly elements align collectively.

### \(\sigma\): noise amplitude
Controls the strength of unresolved forcing.

### \(A_{ij}\): network structure
Controls who interacts with whom.

Together these parameters determine whether the system is:

- strongly ordered,
- weakly ordered,
- intermittently switching,
- or largely disordered.

---

## 13. Limiting Regimes

The model becomes especially interpretable in several limiting cases.

### 13.1 No coupling: \(\lambda = 0\)

Each element evolves independently:

\[
\ddot{\theta}_i + \gamma \dot{\theta}_i
=
-\alpha \sin(2\theta_i)
+ \sigma\,\eta_i(t).
\]

This reduces the model to many uncoupled bistable units.

### 13.2 No noise: \(\sigma = 0\)

The evolution becomes deterministic:

\[
\ddot{\theta}_i + \gamma \dot{\theta}_i
=
-\alpha \sin(2\theta_i)
+ \lambda \sum_{j=1}^{N} A_{ij}\,\sin(\theta_j-\theta_i).
\]

This highlights purely interaction-driven organization.

### 13.3 Strong coupling: \(\lambda \gg 1\)

The units tend to synchronize strongly, producing long intervals of coherent polarity.

### 13.4 Strong noise: \(\sigma \gg 1\)

The system becomes more disordered, and reversals or excursions become more frequent.

---

## 14. Discrete-Time Numerical Approximation

With time step \(\Delta t\), an Euler-Maruyama style discretization for the first-order system is:

\[
\theta_i^{n+1} = \theta_i^n + \omega_i^n \Delta t,
\]

\[
\omega_i^{n+1}
=
\omega_i^n
+
\left[
-\gamma \omega_i^n
-\alpha \sin(2\theta_i^n)
+ \lambda \sum_{j=1}^{N} A_{ij}\sin(\theta_j^n-\theta_i^n)
\right]\Delta t
+
\sigma \sqrt{\Delta t}\,\xi_i^n,
\]

where

\[
\xi_i^n \sim \mathcal{N}(0,1)
\]

are independent standard Gaussian random variables.

This is one of the simplest practical discretizations for `simulate.py`.

---

## 15. Suggested Parameter File Structure

A corresponding `parameters.py` could logically define quantities like:

```python
N = 16
alpha = 1.0
gamma = 0.2
lambda_coupling = 1.5
sigma = 0.3
dt = 0.01
n_steps = 200000
seed = 42
```

as well as optional choices for:

- coupling topology,
- initial conditions,
- output saving frequency,
- reversal threshold and persistence time.

This is only a suggested structure, not a recovered one, because the currently visible raw `parameters.py` content is empty in the public snapshot I checked. citeturn951554view1

---

## 16. Suggested Analysis Quantities

A corresponding `analysis.py` would naturally compute:

- \(M(t)\): dipole proxy,
- \(P(t)=\operatorname{sgn}(M)\): polarity,
- reversal count,
- waiting-time distribution,
- coherence \(R(t)\),
- power spectrum of \(M(t)\),
- probability density of \(M\),
- excursion statistics.

Again, this is a scientifically consistent recommendation, not a reconstruction of non-empty code. The raw public `analysis.py` view appeared empty when checked. citeturn951554view2

---

## 17. Comparison with Simpler Bistable Models

A bistable model usually starts directly from one effective variable \(x(t)\), for example:

\[
\dot{x} = -U'(x) + \sigma \eta(t).
\]

By contrast, the domino model first evolves many interacting units \(\theta_i\) and defines the macroscopic dipole only afterwards through:

\[
M(t) = \frac{1}{N}\sum_{i=1}^{N}\cos\theta_i(t).
\]

This gives the domino model an important conceptual advantage:

the reversal is a **collective phenomenon**, not just the motion of one variable in a prescribed landscape.

---

## 18. Final Scientific Interpretation

The domino model should be viewed as a reduced theory of collective polarity organization.

Its core message is that geomagnetic-like reversals may arise from the interaction of many simple components, each only weakly informative on its own, but capable of generating rich macroscopic behavior when coupled.

In that sense, the model is not just a computational toy. It is a compact way to test a real scientific idea:

**global magnetic polarity may be an emergent property of collective dynamics.**
