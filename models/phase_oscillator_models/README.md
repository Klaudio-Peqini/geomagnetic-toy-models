# Phase Oscillator Models

## Purpose of This Folder

This folder contains oscillator-based and phase-based reduced models for geomagnetic variability.

The key idea is that some aspects of complex geomagnetic behavior may be usefully interpreted in terms of:

- interacting phases,
- synchronization,
- coherence and decoherence,
- collective oscillatory structure,
- transitions between ordered and disordered regimes.

This gives a perspective that differs from both bistable switching models and interacting spin-like domino models.

---

## Scientific Motivation

Many nonlinear systems display rich emergent behavior when described as coupled oscillators. Even when each element is simple, the system can exhibit:

- synchronization,
- phase locking,
- incoherence,
- abrupt collective transitions,
- sensitivity to coupling strength and disorder.

In geomagnetic toy modeling, this perspective is useful because one may think of the large-scale field as reflecting the changing coordination of effective modes or components.

This does not imply that the Earth's core is literally a Kuramoto system. Rather, it means that synchronization theory can provide a fruitful reduced analogy.

---

## Files in This Folder

```text
phase_oscillator_models/
├── README.md
└── kuramoto_like.py
```

### `kuramoto_like.py`

This script contains the main oscillator-style model of the folder. As the name suggests, it is likely inspired by Kuramoto-type coupling or by a related phase-interaction framework.

Typical uses include:

- exploring synchronization thresholds,
- studying coherence loss,
- generating collective phase dynamics,
- examining how global order changes with coupling or disorder.

Even when highly reduced, such a model can reveal whether phase coordination alone can generate interesting large-scale signatures.

---

## Conceptual Interpretation

In a phase-oscillator formulation, the main state variables are not usually amplitudes in a double-well potential, but phases and their interactions.

A common interpretation is:

- each unit has a phase,
- coupling tends to align or correlate phases,
- disorder or frequency mismatch tends to separate them,
- the degree of synchronization measures global order.

A geomagnetic analogy may then be built from how coherent collective organization strengthens or weakens a large-scale effective observable.

---

## Scientific Questions This Model Can Address

This folder is especially useful for questions such as:

- How does synchronization depend on coupling strength?
- Can loss of coherence mimic reversal-like or excursion-like behavior?
- What collective observables best summarize oscillator organization?
- Do transitions between coherent and incoherent regimes generate geomagnetically interesting signatures?
- How different is a synchronization-based explanation from a bistable one?

These questions are highly relevant when one wants a nonlinear-dynamics perspective on polarity variability.

---

## Strengths of the Oscillator Approach

### 1. Strong connection to nonlinear dynamics theory

Phase-oscillator models are mathematically rich and conceptually elegant.

### 2. Natural coherence measures

Order parameters and synchronization metrics arise naturally.

### 3. Good for collective-order questions

These models are ideal when the scientific focus is not only polarity sign, but also the organization of the effective system.

### 4. Useful comparison framework

They help test whether reversal-like behavior might emerge from changing coherence rather than from simple barrier crossing.

---

## Limitations

Oscillator models also require careful interpretation.

They may be less direct than bistable models when the goal is to model clear polarity switching. In addition:

- the mapping to geomagnetic observables may be less immediate,
- polarity proxies may need to be constructed indirectly,
- some outputs may remain more abstract than those of other model classes.

Thus, these models are often most powerful in comparative studies rather than as standalone final descriptions.

---

## Recommended Workflow

A practical workflow is:

1. run `kuramoto_like.py`;
2. inspect the degree of phase synchronization;
3. define or extract an effective macroscopic observable;
4. compare coherent and incoherent regimes;
5. analyze the resulting time series with common repository diagnostics.

This helps place the oscillator model alongside the other toy-model families.

---

## Example Terminal Commands

Run the oscillator model:

```bash
python3 models/phase_oscillator_models/kuramoto_like.py
```

Run after environment setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements.txt
python3 models/phase_oscillator_models/kuramoto_like.py
```

Launch notebooks for exploratory comparison:

```bash
jupyter notebook notebooks/
```

---

## Suggested Outputs to Analyze

Depending on the exact implementation, useful observables may include:

- synchronization order parameter,
- average phase alignment,
- phase dispersion,
- effective polarity proxy,
- coherence breakdown intervals,
- low-frequency spectral content,
- transition statistics between coherent and incoherent states.

These outputs can help determine whether oscillator-like organization offers a plausible qualitative explanation for some features of geomagnetic variability.

---

## Relation to the Repository as a Whole

This folder gives the repository a distinctly nonlinear-dynamical dimension.

- `bistable_models/` focus on switching between preferred states,
- `domino_model/` focuses on interacting effective units,
- `data_driven_models/` focus on reduced observables and comparison,
- `phase_oscillator_models/` focus on synchronization and coherence.

That makes this folder especially important for broadening the conceptual scope of the project.

---

## Final Perspective

The value of this folder lies in asking a different kind of question:

what if some geomagnetically interesting variability reflects not only polarity preference, but also changing collective coherence?

That is the central insight offered by the oscillator-based approach.
