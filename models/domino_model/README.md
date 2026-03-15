# Domino Model

## Purpose of This Folder

This folder contains the repository’s domino-style geomagnetic toy model, together with its associated parameter definitions, simulation script, and analysis utilities.

Among all model families in the project, this one is particularly important because it introduces a **collective-interaction picture** of geomagnetic reversals.

Instead of representing the field through only one effective variable, the domino approach typically imagines that the large-scale polarity emerges from the interaction of multiple effective elements or degrees of freedom. Global reversal is then interpreted as a collective reorganization.

---

## Scientific Motivation

The domino-family idea is attractive because geomagnetic reversals may not always be well represented as simple single-variable barrier crossings. In many dynamical systems, abrupt global transitions arise from:

- local interactions,
- changing coherence,
- frustration or competition,
- amplification of fluctuations through coupling,
- collective reorganization of many components.

A domino-style toy model captures that intuition.

In this picture, the global dipole state is an emergent property of the coupling among simpler units, rather than a variable imposed from the outset.

---

## Files in This Folder

```text
domino_model/
├── README.md
├── analysis.py
├── model_equations.md
├── parameters.py
└── simulate.py
```

### `simulate.py`

This is the main simulation entry point for the domino model. It is expected to generate trajectories of the interacting system and produce outputs from which a global polarity or dipole-like observable can be extracted.

Typical tasks include:

- running the coupled model,
- generating time series,
- exploring the effect of coupling and forcing,
- producing reversal-like trajectories.

### `parameters.py`

This file likely centralizes parameter choices. It is useful for keeping simulations reproducible and transparent.

Typical contents may include:

- coupling strengths,
- damping parameters,
- noise amplitudes,
- number of effective units,
- integration controls,
- output settings.

A dedicated parameter file is especially valuable in research workflows because it reduces ambiguity and makes parameter scans easier.

### `analysis.py`

This script is intended for post-processing and interpretation of the model outputs.

Typical uses may include:

- polarity extraction,
- reversal counting,
- summary statistics,
- time-series visualization,
- coherence measures,
- comparisons across runs.

### `model_equations.md`

This file documents the mathematical formulation of the model. It is an important complement to the code because the scientific interpretation of the domino model depends on understanding the coupling structure and the meaning of the effective variables.

---

## Conceptual Interpretation

The domino model is best understood as a reduced interacting-element system in which each unit contributes to a collective macroscopic state.

Depending on the precise formulation, the units may be interpreted as:

- effective spins,
- local dipole-like elements,
- mode amplitudes,
- abstract interacting components.

The key point is that a global polarity emerges through interaction.

This makes the domino model especially suitable for studying:

- collective alignment,
- loss of coherence,
- interaction-driven switching,
- emergent reversals,
- sensitivity to coupling structure.

---

## What Makes This Folder Distinct

Compared with the bistable models, the domino model introduces more internal structure.

### In bistable models
The system is usually represented by one or a few effective variables moving between two preferred states.

### In the domino model
The system contains multiple interacting components, and the global state is emergent.

This difference matters scientifically because it changes the interpretation of reversal events. In the domino picture, reversals may reflect **collective reorganizations** rather than only stochastic barrier crossings.

---

## Scientific Questions This Model Can Address

This folder is particularly useful for questions such as:

- How does coupling strength affect reversal frequency?
- How robust is the global polarity to local fluctuations?
- Under what conditions does collective alignment break down?
- Can irregular reversals emerge from simple interacting units?
- Which observables best summarize coherence or disorder in the system?

These are important mechanism-level questions that complement the simpler bistable interpretation.

---

## Strengths of the Domino Approach

### 1. Emergent dynamics

The model allows the macroscopic field state to arise from interactions rather than being built in directly.

### 2. Richer structure

Even with relatively simple units, the system can display nontrivial global behavior.

### 3. Good for studying coherence

This model family naturally supports questions about alignment, disorder, and reorganization.

### 4. Good bridge to more realistic intuition

Although still highly reduced, a coupled many-element picture feels closer to the idea of interacting dynamical subsystems than a one-variable model.

---

## Limitations

The domino model still remains a toy model.

It generally does not provide:

- three-dimensional geomagnetic morphology,
- resolved induction physics,
- explicit outer-core flow structure,
- direct quantitative Earth calibration.

Its strength lies in collective dynamics and interpretability, not in full physical realism.

---

## Recommended Workflow

A useful workflow in this folder is:

1. inspect `model_equations.md` to understand the mathematical structure;
2. review `parameters.py` to identify the main control parameters;
3. run `simulate.py` to generate trajectories;
4. run `analysis.py` to extract reversal and coherence diagnostics;
5. compare the results with bistable or oscillator-based models.

---

## Example Terminal Commands

Run the main simulation:

```bash
python3 models/domino_model/simulate.py
```

Run the analysis script:

```bash
python3 models/domino_model/analysis.py
```

Inspect the equations from terminal:

```bash
less models/domino_model/model_equations.md
```

Search parameters quickly:

```bash
grep -n ".*" models/domino_model/parameters.py
```

Run both simulation and analysis in sequence:

```bash
python3 models/domino_model/simulate.py && python3 models/domino_model/analysis.py
```

---

## Suggested Quantities to Analyze

Useful outputs from a domino-style model often include:

- global polarity proxy,
- average alignment or coherence,
- reversal count,
- waiting-time distribution,
- local-vs-global variability,
- spectral content,
- transient breakdown of order.

These can then be compared with the common diagnostics available elsewhere in the repository.

---

## Relation to the Repository as a Whole

This folder is one of the central model families in the repository because it provides a perspective that is neither purely single-variable nor fully data-driven.

It complements the rest of the framework by offering:

- more internal dynamical structure than bistable models,
- more mechanistic clarity than purely empirical reductions,
- a useful comparison point for oscillator-style models.

---

## Final Perspective

The domino model is valuable because it treats reversals as a **collective phenomenon**.

That makes it one of the strongest tools in the repository for studying how simple interacting elements can generate rich global polarity dynamics.
