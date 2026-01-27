# Electrolyser Digital Twin – Core Simulink Models

## Overview

This repository contains foundational **system-level Simulink models** for an **electrolyser digital twin**.  
The focus is on **physically interpretable core sub-models** that serve as the basis for:

- Electrochemical performance simulation  
- Thermal coupling  
- Aging and degradation analysis  

The current implementation includes **thermodynamic reversible voltage modeling** and **temperature-dependent ohmic loss modeling with explicit aging dynamics**.  
All models are designed in a **modular and extensible** manner to support future expansion toward full electrolyser system simulations.

---

## Implemented Models

### Reversible Voltage Model
- Derived from Gibbs free energy of water splitting  
- Linearized temperature dependence  
- Suitable for system-level and control-oriented simulations  

### Ohmic Loss Model with Aging
- Temperature-dependent electrical resistance  
- Continuous-time aging state driven by absolute stack current  
- Enables degradation analysis under dynamic operating conditions  

---

## Model Structure

The models are implemented within a **single top-level Simulink file** using clearly separated subsystems:

- `ReversibleVoltageModel`
- `OhmicLossModel`

All physical parameters are defined **externally** to ensure:
- Transparency  
- Reproducibility  
- Ease of parameter studies  

---

## Applications

- Electrolyser system-level simulation  
- Aging and degradation studies  
- Digital twin research  
- Power-to-X and hydrogen system modeling  

---

## Planned Extensions

- Hydrogen production model (Faraday-based)  
- Lumped thermal dynamics  
- Activation and concentration losses  
- Validation against experimental measurement data  

---

## How to Run

1. Open **MATLAB**
2. Set the repository as the working directory
3. Run the parameter script:
   ```matlab
   scripts/script_Electrolyzers.m
4. Open the Simulink mode:
   ```matlab
   model/Electrolyzer.slx
5. Run the simulation.

