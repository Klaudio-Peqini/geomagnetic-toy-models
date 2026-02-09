# Geomagnetic Toy Models

**Low-dimensional, conceptual, and stochastic models of the geomagnetic field**

---

## Overview

This repository collects a curated set of **reduced, low-dimensional “toy models”** designed to explore the long-term dynamics of the Earth's magnetic field, with particular emphasis on:

- geomagnetic **reversals** and **excursions**
- stochastic transitions and bistability
- dipole dominance and breakdown
- scaling arguments and interpretability
- links between conceptual models and full geodynamo simulations

These models are **not intended to replace full 3D magnetohydrodynamic (MHD) simulations** of the geodynamo (e.g. XSHELLS or similar frameworks). Instead, they serve as **complementary tools** aimed at physical insight, rapid experimentation, pedagogical clarity, and hypothesis testing.

---

## Motivation

Full geodynamo simulations are computationally expensive and often difficult to interpret at a mechanistic level. Toy models, by contrast, allow one to:

- isolate essential degrees of freedom,
- test conceptual mechanisms for reversals and excursions,
- explore parameter space efficiently,
- connect paleomagnetic observations to dynamical systems theory,
- provide interpretable bridges between theory, data, and simulation.

This repository embraces the philosophy that **understanding often begins with reduction**.

---

## Scope of the Repository

The models included here span several conceptual families:

- **Domino and coupled-element models**  
  (collective polarity reversals, interaction-driven dynamics)

- **Bistable and double-well systems**  
  (noise-induced transitions, stochastic resonance)

- **Phase and oscillator-based models**  
  (synchronization, coherence loss, collective modes)

- **Data-informed reduced models**  
  (low-dimensional observables extracted from simulations or paleodata)

Each model family lives in its own subdirectory under `models/`, with local documentation and examples.

---

## Repository Structure

geomagnetic-toy-models/

│

├── models/ # Individual toy models and formulations

├── diagnostics/ # Common diagnostics (dipole moment, reversals, spectra)

├── notebooks/ # Exploratory and pedagogical Jupyter notebooks

├── experiments/ # Parameter scans, scaling tests, sensitivity studies

├── data/ # Paleomagnetic or synthetic data (lightweight)

├── docs/ # Conceptual and theoretical documentation

├── utils/ # Numerical and plotting utilities

├── tests/ # Basic correctness and regression tests

└── environment/ # Reproducible Python environments


---

## Diagnostics and Observables

Across models, we aim to compute consistent diagnostics such as:

- axial dipole moment
- polarity time series
- reversal and excursion statistics
- power spectra and characteristic timescales
- tilt angles and dipole dominance measures

This allows **cross-model comparison** and meaningful confrontation with data.

---

## Intended Audience

This repository is intended for:

- researchers in geomagnetism and geodynamo theory
- physicists interested in stochastic and nonlinear dynamical systems
- graduate students and advanced undergraduates
- educators seeking interpretable models for teaching purposes

---

## Relation to Full Geodynamo Simulations

Where relevant, toy-model outputs can be compared with:

- 3D MHD simulations (e.g. XSHELLS)
- paleomagnetic field models and reversal records
- scaling laws and phenomenological arguments

The long-term goal is to **connect insight across levels of description**.

---

## Status

This repository is under active development.  
Models, diagnostics, and documentation will expand progressively.

---

## Citation

If you use this repository in academic work, please cite it using the provided `CITATION.cff` file or the recommended citation shown on GitHub.

---

## License

See the `LICENSE` file for usage terms.

---

*Reduction is not simplification — it is clarification.*
