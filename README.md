# Geomagnetic Toy Models

Low-dimensional, conceptual, and stochastic models for exploring the
long-term dynamics of the geomagnetic field.

------------------------------------------------------------------------

## Scientific Purpose

This repository collects reduced-order and interpretable models designed
to study core qualitative phenomena of the Earth's magnetic field,
especially:

-   geomagnetic reversals,
-   geomagnetic excursions,
-   stochastic transitions between metastable states,
-   dipole dominance and its breakdown,
-   synchronization and collective behavior,
-   connections between conceptual models, paleomagnetic records, and
    full geodynamo simulations.

The goal is **not** to replace full 3D magnetohydrodynamic geodynamo
simulations. Instead, this repository provides a framework for:

-   physical intuition,
-   rapid prototyping,
-   pedagogical exploration,
-   hypothesis testing,
-   reduced-order comparison against observations and large simulations.

In other words, this is a repository for **understanding before scaling
up**.

------------------------------------------------------------------------

## Why Toy Models Matter

Full geodynamo simulations are computationally demanding and often
difficult to interpret mechanistically. Low-dimensional models are
useful because they allow us to:

-   isolate essential degrees of freedom,
-   study reversal mechanisms in controlled settings,
-   scan parameter space quickly,
-   separate deterministic structure from stochastic forcing,
-   connect dynamical-systems language to geomagnetic observables,
-   build bridges between theory, numerical simulation, and
    paleomagnetic data.

This repository embraces the idea that reduction is not
oversimplification when it is done carefully; it is often the first step
toward interpretation.

------------------------------------------------------------------------

## What This Repository Contains

The project is organized around several complementary families of
models.

### 1. Domino and coupled-element models

These models represent the field through interacting effective units,
often inspired by collective alignment, polarity competition, or
interacting degrees of freedom. They are useful for exploring:

-   collective polarity reversals,
-   interaction-driven state switching,
-   emergent coherence and loss of coherence.

### 2. Bistable and double-well models

These formulations represent the geomagnetic dipole as an effective
state evolving in a potential landscape with one or more stable wells.
They are especially useful for:

-   noise-induced transitions,
-   residence-time statistics,
-   stochastic resonance,
-   excursion-like vs reversal-like dynamics.

### 3. Phase and oscillator-based models

These models borrow ideas from nonlinear dynamics and synchronization
theory. They are relevant when one wants to explore:

-   coherence,
-   collective phase behavior,
-   synchronization/desynchronization,
-   oscillatory reduced descriptions of field variability.

### 4. Data-driven reduced models

These models sit closer to observables extracted from paleomagnetic
records or high-dimensional simulations. Their purpose is to help
connect:

-   reduced observables,
-   effective dynamical variables,
-   geodynamo-inspired low-dimensional descriptions,
-   comparison with more realistic datasets.

### 5. Numerical integrators

Included:
-    deterministic integrators: Euler, RK2, RK4
-    stochastic integrators: Euler-Maruyama, stochastic Heun, Milstein

### 6. Other

The repo further contains:
-    reduced observable comparison utilities
-    generic diagnostics
-    basic tests

------------------------------------------------------------------------

## Current Repository Structure

``` text
geomagnetic-toy-models/
│
├── data/
├── diagnostics/
│   ├── dipole_moment.py
│   ├── polarity.py
│   ├── power_spectra.py
│   ├── reversal_statistics.py
│   └── tilt_angle.py
│
├── docs/
│   ├── comparison_with_full_MHD.md
│   ├── model_taxonomy.md
│   ├── overview.md
│   └── physical_background.md
│
├── environment/
│   ├── environment.yml
│   └── requirements.txt
│
├── models/
│   ├── bistable_models/
│   │   ├── double_well.py
│   │   └── stochastic_forcing.py
│   │
│   ├── data_driven_models/
│   │   └── reduced_observables.py
│   │
│   ├── domino_model/
│   │   ├── analysis.py
│   │   ├── parameters.py
│   │   └── simulate.py
│   │
│   └── phase_oscillator_models/
│       └── kuramoto_like.py
│
├── notebooks/
│   ├── 01_basic_dynamics.ipynb
│   ├── 02_reversals_and_excursions.ipynb
│   ├── 03_noise_induced_transitions.ipynb
│   └── 04_comparison_with_CALS10k.ipynb
│
├── tests/
├── utils/
│
├── CITATION.cff
├── LICENSE
└── README.md
```

------------------------------------------------------------------------

## Installation

### Clone the repository

``` bash
git clone https://github.com/Klaudio-Peqini/geomagnetic-toy-models.git
cd geomagnetic-toy-models
```

### Create a virtual environment

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

``` bash
pip install --upgrade pip
pip install -r environment/requirements.txt
```

------------------------------------------------------------------------

## Using Conda

``` bash
git clone https://github.com/Klaudio-Peqini/geomagnetic-toy-models.git
cd geomagnetic-toy-models
conda env create -f environment/environment.yml
conda activate geomagnetic-toy-models
```

------------------------------------------------------------------------

## Quick Start

Launch the notebooks:

``` bash
jupyter notebook notebooks/
```

or

``` bash
jupyter lab
```

------------------------------------------------------------------------

## Bash Command Cookbook

### Run the domino model

``` bash
python3 models/domino_model/simulate.py
```

### Run domino analysis

``` bash
python3 models/domino_model/analysis.py
```

### Run the bistable model

``` bash
python3 models/bistable_models/double_well.py
```

### Run stochastic forcing

``` bash
python3 models/bistable_models/stochastic_forcing.py
```

### Run phase oscillator model

``` bash
python3 models/phase_oscillator_models/kuramoto_like.py
```

### Run reduced observable model

``` bash
python3 models/data_driven_models/reduced_observables.py
```

------------------------------------------------------------------------

## Diagnostics

You can also execute diagnostic tools independently:

``` bash
python3 diagnostics/dipole_moment.py
python3 diagnostics/polarity.py
python3 diagnostics/power_spectra.py
python3 diagnostics/reversal_statistics.py
python3 diagnostics/tilt_angle.py
```

------------------------------------------------------------------------

## Running Tests

``` bash
pytest -v
```

or

``` bash
python3 -m pytest tests/
```

------------------------------------------------------------------------

## Typical commands:

``` bash
python3 models/bistable_models/double_well.py --method rk4
python3 models/bistable_models/double_well.py --method euler-maruyama --sigma 0.6
python3 models/bistable_models/stochastic_forcing.py --method stochastic-heun
python3 models/domino_model/simulate.py --method euler-maruyama --topology nearest --save domino_run.npz
python3 models/domino_model/analysis.py domino_run.npz
python3 models/phase_oscillator_models/kuramoto_like.py --method rk4 --sigma 0.0
python3 models/data_driven_models/reduced_observables.py pytest -v
```

------------------------------------------------------------------------

## Export Notebooks

Execute notebook from terminal:

``` bash
jupyter nbconvert --to notebook --execute notebooks/01_basic_dynamics.ipynb
```

Export notebook to HTML:

``` bash
jupyter nbconvert --to html notebooks/02_reversals_and_excursions.ipynb
```

------------------------------------------------------------------------

## Recommended Scientific Workflow

1.  Explore notebooks to understand qualitative dynamics.
2.  Run individual model scripts.
3.  Compute diagnostics.
4.  Compare reversal statistics across models.
5.  Relate results to paleomagnetic observations or geodynamo
    simulations.

------------------------------------------------------------------------

## Future Improvements

Potential next developments:

-   Convert repository into a full Python package (`pyproject.toml`)
-   Add CLI interface
-   Standardize model input/output
-   Add parameter-scan scripts
-   Expand test coverage
-   Add automated figure generation
-   Introduce experiment pipelines

------------------------------------------------------------------------

## Reproducibility

For scientific work it is recommended to record:

-   random seeds
-   time step
-   simulation duration
-   parameter values
-   diagnostic configuration
-   dataset versions

------------------------------------------------------------------------

## Intended Audience

This repository is suitable for:

-   geomagnetism researchers
-   nonlinear dynamics researchers
-   geodynamo modelers
-   graduate students
-   computational physics courses

------------------------------------------------------------------------

## Citation

Please cite this repository using the `CITATION.cff` file provided in
the project.

------------------------------------------------------------------------

## License

See the `LICENSE` file for details.

------------------------------------------------------------------------

## Philosophy

**Reduction is not simplification --- it is clarification.**
