# Model Taxonomy

## Purpose of This Taxonomy

This document organizes the main classes of toy models used in the repository and clarifies the scientific logic behind grouping them. The classification is not purely technical. It reflects differences in:

- physical interpretation,
- mathematical structure,
- level of abstraction,
- type of observable produced,
- usefulness for reversal studies.

A taxonomy is important because many reduced models can generate superficially similar time series while relying on very different mechanisms.

---

## Taxonomy by Dynamical Idea

### 1. Bistable effective-state models

These models describe the geomagnetic dipole through one or a few effective variables evolving in a landscape with multiple stable or metastable states.

Typical ingredients include:

- double-well potentials,
- damping,
- stochastic forcing,
- barrier crossing,
- low-dimensional state evolution.

#### Scientific interpretation

These models are especially useful when reversals are interpreted as transitions between two preferred polarity states. They are often the clearest framework for residence-time and waiting-time studies.

#### Strengths

- strong interpretability,
- simple phase-space structure,
- natural treatment of reversals as switching events,
- convenient for stochastic analysis.

#### Limitations

- may be too coarse to represent collective internal structure,
- often require careful interpretation of noise terms,
- usually provide only a small number of observables.

---

### 2. Domino and interacting-unit models

These models describe the field as emerging from the collective behavior of multiple effective units, elements, or spins. Their behavior depends on interaction structure, coupling strength, and stochastic or deterministic perturbations.

Typical ingredients include:

- local or global coupling,
- alignment and competition,
- effective spins or units,
- emergent coherence,
- collective transitions.

#### Scientific interpretation

These models are useful when reversals are seen as emergent collective reorganizations rather than single-variable barrier crossings.

#### Strengths

- richer internal structure than one-variable models,
- intuitive collective behavior,
- useful for studying coherence breakdown,
- can generate abrupt emergent transitions.

#### Limitations

- less directly interpretable than simple bistable systems,
- mapping to physical core processes is often indirect,
- diagnostic outputs may require more processing.

---

### 3. Oscillator and phase-based models

These models treat the system in terms of phases, oscillatory modes, or synchronization dynamics. The relevant questions concern order, coherence, and phase relationships.

Typical ingredients include:

- phase variables,
- coupling between oscillators,
- synchronization thresholds,
- phase drift,
- coherent and incoherent regimes.

#### Scientific interpretation

Such models are relevant when geomagnetic variability is interpreted in terms of interacting modes whose coherence changes in time.

#### Strengths

- strong connection to nonlinear dynamics theory,
- useful for studying order-disorder transitions,
- mathematically elegant,
- suitable for collective timing or mode-interaction studies.

#### Limitations

- direct geophysical interpretation may be less immediate,
- polarity itself may need to be constructed from effective observables,
- some outputs may be more abstract than in bistable models.

---

### 4. Data-driven reduced models

These models aim to infer or construct effective low-dimensional behavior from data, reduced observables, or summaries of higher-dimensional systems.

Typical ingredients include:

- empirical observables,
- reduced coordinates,
- proxy variables,
- calibration or comparison against reference datasets.

#### Scientific interpretation

These models help connect conceptual reduced descriptions to actual paleomagnetic records or outputs of larger simulations.

#### Strengths

- closer to observations,
- useful for benchmarking,
- supports comparison and model selection,
- can guide more physically grounded simplifications.

#### Limitations

- may lose some mechanistic transparency,
- quality depends on the choice of observables,
- may become descriptive rather than explanatory if not used carefully.

---

## Taxonomy by Mechanism of Reversal

A second useful classification is by **reversal mechanism** rather than by mathematical form.

### Noise-triggered transitions
Reversals occur because stochastic fluctuations push the system across a barrier or out of a metastable attractor.

### Collective reorganization
Reversals emerge because interactions among many effective components reorganize the global polarity.

### Mode competition
Reversals arise through competition between dynamical modes with different signs, amplitudes, or phases.

### Loss of coherence
Reversals or excursions occur when a coherent state breaks down and later reforms, possibly with the opposite polarity.

This second taxonomy helps compare models that look mathematically different but are physically related.

---

## Taxonomy by Level of Abstraction

### Highly conceptual
Very small numbers of variables; emphasis on mechanism rather than data comparison.

### Intermediate reduced
Still low-dimensional, but with some physically motivated observables or coupling structures.

### Data-informed reduced
Reduced systems built with explicit reference to data, reconstructions, or outputs of more realistic models.

This scale matters because users should not expect the same type of conclusion from all model classes.

---

## Taxonomy by Observable Output

Different models are more naturally suited to different outputs.

### Best for polarity trajectories
- bistable models
- domino models

### Best for collective coherence measures
- domino models
- phase-oscillator models

### Best for residence-time statistics
- bistable stochastic models

### Best for benchmark comparison
- data-driven reduced models

### Best for educational introduction
- bistable models and simple interacting-element models

This perspective is practical when deciding which model to use for a given study.

---

## Choosing the Right Model Family

A good model choice depends on the scientific question.

### Use bistable models when:
- you want strong interpretability,
- you care about switching statistics,
- you want a clear analogy with metastable states.

### Use domino models when:
- you want emergent collective dynamics,
- you care about interaction effects,
- you want to study coherence and reorganization.

### Use oscillator models when:
- your interest is synchronization,
- you want a nonlinear-dynamics perspective,
- phase relationships are central.

### Use data-driven reduced models when:
- you want closer comparison to reference data,
- you need effective observables,
- you aim to connect conceptual models to empirical structure.

---

## Why Taxonomy Improves the Repository

A repository with multiple toy models becomes much more scientifically useful when the user understands not only *how to run* each model, but *why the models differ*. A proper taxonomy:

- prevents conceptual confusion,
- clarifies interpretation,
- supports better comparison,
- helps students navigate the framework,
- makes future extensions easier.

---

## Final Remark

No single toy model can capture the full richness of geomagnetic dynamics. The strength of this repository lies precisely in the coexistence of several model classes.

A taxonomy helps transform that diversity from a collection of scripts into a coherent scientific framework.
