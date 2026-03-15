# Bistable Models

## Purpose of This Folder

This folder contains reduced geomagnetic toy models in which the large-scale dipole is represented as an **effective variable evolving between two preferred polarity states**.

In the language of dynamical systems, the core idea is that the system admits two competing attractor-like or metastable configurations:

- one corresponding to one dominant polarity,
- the other corresponding to the opposite polarity.

A reversal is then interpreted as a transition from one state to the other.

This is one of the clearest conceptual frameworks for studying polarity switching in a low-dimensional setting.

---

## Scientific Motivation

Bistable models are among the most useful toy models for geomagnetic reversals because they compress the problem to its qualitative essence:

- there are two preferred polarity states,
- the field may spend long intervals near one state,
- fluctuations can destabilize the system,
- crossing the effective barrier leads to a reversal.

These models are attractive because they provide a direct route to studying:

- residence times,
- waiting-time statistics,
- reversal probabilities,
- the influence of stochastic forcing,
- the distinction between full reversals and failed excursions.

---

## Files in This Folder

```text
bistable_models/
├── README.md
├── double_well.py
└── stochastic_forcing.py
```

### `double_well.py`

This script represents the core bistable picture. The usual interpretation is that the geomagnetic dipole evolves in an effective double-well landscape, where each well corresponds to one dominant polarity state.

Typical uses of such a model include:

- visualizing two stable or metastable states,
- examining deterministic drift toward preferred polarities,
- studying barrier crossing,
- understanding how potential shape affects stability.

### `stochastic_forcing.py`

This script emphasizes the role of noise or unresolved fluctuations. In a geomagnetic context, stochastic forcing is often interpreted as a reduced representation of unresolved turbulent or multiscale core dynamics.

It is particularly useful for studying:

- noise-induced transitions,
- intermittent switching,
- residence-time broadening,
- the sensitivity of reversals to forcing amplitude.

---

## Physical Interpretation

The bistable framework should not be interpreted too literally as a full physical representation of the outer core. Rather, it is an **effective dynamical analogy**.

A common interpretation is:

- the dipole behaves like an order parameter,
- the two wells represent two preferred global magnetic polarities,
- noise represents unresolved fluctuations,
- the barrier height controls how difficult reversals are,
- damping or drift terms regulate how the system relaxes toward preferred states.

This makes the model simple, interpretable, and computationally cheap.

---

## What Questions These Models Can Address

This folder is especially useful for questions such as:

- How often do reversals occur as a function of noise amplitude?
- How long does the system remain in one polarity state?
- Under what conditions do excursions occur instead of full reversals?
- How does barrier shape affect reversal asymmetry?
- Which statistics are robust across many stochastic realizations?

These are scientifically meaningful questions even in a reduced-order setting.

---

## Strengths of the Bistable Approach

### 1. Strong interpretability

The two-state structure makes the logic of reversal dynamics very transparent.

### 2. Low computational cost

Large ensembles can usually be run quickly, which is ideal for parameter scans.

### 3. Natural statistical analysis

Waiting times, polarity durations, and transition rates are straightforward to define.

### 4. Educational clarity

This is one of the best model classes for introducing students to reversal dynamics.

---

## Limitations

Bistable models are powerful, but they also have limitations.

They generally do not provide:

- realistic field morphology,
- spatial structure,
- explicit core-flow dynamics,
- direct Earth-like calibration,
- self-consistent magnetohydrodynamics.

They should therefore be used as mechanism-level models, not as full geodynamo substitutes.

---

## Typical Workflow

A practical workflow for this folder is:

1. run `double_well.py` to inspect the baseline effective landscape;
2. run `stochastic_forcing.py` to add unresolved variability;
3. extract time series of the effective dipole variable;
4. compute polarity, reversal statistics, and spectra using the repository diagnostics;
5. compare results across parameter values and noise strengths.

---

## Example Terminal Commands

Run the deterministic or baseline bistable script:

```bash
python3 models/bistable_models/double_well.py
```

Run the stochastic version:

```bash
python3 models/bistable_models/stochastic_forcing.py
```

Activate a virtual environment first if needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements.txt
```

---

## Suggested Outputs to Analyze

After simulation, useful derived quantities include:

- sign of the effective dipole variable,
- residence-time distributions,
- reversal counts,
- mean waiting time,
- histogram of state occupancy,
- power spectrum of the trajectory,
- excursion frequency.

These outputs make the bistable model directly comparable to other model families in the repository.

---

## Relation to the Repository as a Whole

Within the larger `geomagnetic-toy-models` framework, the bistable models serve as perhaps the most conceptually minimal class of reversal models.

They are especially valuable as:

- baseline models,
- pedagogical entry points,
- statistical benchmarks,
- interpretable references for more complex model classes.

---

## Final Perspective

If the scientific goal is to understand reversals as transitions between two effective polarity states, this folder provides one of the cleanest starting points in the repository.

Its great strength is clarity: the model is simple enough to reason about, yet rich enough to generate nontrivial reversal statistics.
