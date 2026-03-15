# Data-Driven Models

## Purpose of This Folder

This folder contains reduced models that are designed to sit closer to **observables, benchmark data, or reduced coordinates extracted from more complex systems**.

Whereas some toy models begin from an abstract dynamical idea such as bistability or coupling, data-driven reduced models begin from a different question:

**Which low-dimensional variables best summarize the behavior we want to compare against data or more realistic simulations?**

This makes the folder especially important for connecting conceptual modeling with empirical or simulation-derived evidence.

---

## Scientific Motivation

In geomagnetism, there is a constant tension between:

- highly interpretable but abstract toy models,
- and highly realistic but complex data or full simulations.

Data-driven reduced models help bridge that gap. Their role is not necessarily to reproduce every physical process from first principles, but to construct effective variables and reduced descriptions that remain meaningfully comparable to reference behavior.

These models are useful when one wants to move beyond purely conceptual time series and ask:

- Which observables matter most?
- Which reduced coordinates carry useful information?
- Can simplified dynamics still be benchmarked against data?
- How should one compare toy-model outputs to reference series?

---

## Files in This Folder

```text
data_driven_models/
├── README.md
└── reduced_observables.py
```

### `reduced_observables.py`

This script is the core content of the folder. Its role is likely to construct, manipulate, or analyze low-dimensional observables intended to summarize larger dynamical behavior.

Possible scientific uses include:

- defining effective dipole proxies,
- reducing multivariate outputs to a small set of descriptors,
- comparing synthetic outputs to paleomagnetic-style series,
- preparing benchmark observables for diagnostics and notebooks.

Even when the code is simple, the conceptual role of this script is important: it provides a bridge between raw model state and interpretable comparison variables.

---

## What “Data-Driven” Means Here

Within this repository, “data-driven” should be interpreted carefully.

It does **not necessarily** imply black-box machine learning. Instead, it refers more broadly to models or procedures that are informed by:

- empirical time series,
- paleomagnetic reference data,
- observables derived from larger numerical models,
- summary statistics,
- reduced coordinates chosen for interpretability.

Thus, the emphasis is on reduced observables and practical comparison, not only on predictive algorithms.

---

## Scientific Use Cases

This folder is useful for problems such as:

- comparing toy-model outputs with reference polarity or dipole-strength records,
- defining robust summary variables,
- constructing benchmark low-dimensional observables,
- checking whether two different model classes produce similar effective signatures,
- preparing simplified time series for notebook demonstration and diagnostic analysis.

---

## Strengths of This Approach

### 1. Closer connection to evidence

Data-driven reduced models help prevent toy modeling from drifting too far into purely abstract behavior.

### 2. Useful for benchmarking

They provide common observables that can be compared across:

- bistable models,
- domino models,
- oscillator models,
- notebooks,
- synthetic and reference datasets.

### 3. Good for scientific interpretation

A carefully chosen reduced observable may reveal more than a very large raw state vector.

### 4. Supports future expansion

This folder can later grow toward:

- dimensionality reduction,
- feature extraction,
- surrogate observables,
- empirical comparison frameworks.

---

## Limitations

Data-driven reduced models also require caution.

Their weaknesses may include:

- dependence on the chosen observable,
- risk of becoming descriptive rather than explanatory,
- possible loss of mechanistic transparency,
- uncertainty in how strongly a reduced coordinate maps to real core dynamics.

For that reason, the best use of this folder is often in combination with the more mechanistic toy-model families.

---

## Recommended Workflow

A practical workflow for this folder is:

1. identify the observable or reduced variable of interest;
2. run `reduced_observables.py`;
3. inspect the resulting time series or descriptors;
4. compare them against outputs from other toy-model families;
5. analyze them with common diagnostics such as spectra, polarity statistics, or trend summaries.

---

## Example Terminal Commands

Run the main reduced-observables script:

```bash
python3 models/data_driven_models/reduced_observables.py
```

Run it after setting up the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements.txt
python3 models/data_driven_models/reduced_observables.py
```

Open the notebooks for comparison-oriented exploration:

```bash
jupyter lab
```

---

## Suggested Future Growth

This folder is one of the best candidates for future development. It could eventually include:

- preprocessing of benchmark time series,
- comparison metrics,
- dimensionality-reduction utilities,
- simple machine-learning baselines,
- calibration of toy-model observables against reference datasets,
- interfaces to paleomagnetic or simulation-derived proxies.

---

## Relation to the Repository as a Whole

In the larger repository, this folder plays a strategic role.

- `bistable_models/` emphasizes interpretable switching,
- `domino_model/` emphasizes collective interaction,
- `phase_oscillator_models/` emphasizes coherence and synchronization,
- `data_driven_models/` emphasizes reduced observables and comparison.

That makes this folder especially valuable for tying together the different scientific layers of the project.

---

## Final Perspective

This folder is where the repository begins to move from **conceptual dynamical systems** toward **comparative reduced science**.

Its value lies in helping the user ask not only “what does the toy model do?” but also “which part of that behavior is comparable, interpretable, and worth measuring?”
