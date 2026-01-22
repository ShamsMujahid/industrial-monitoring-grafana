# industrial-monitoring-grafana
Data-driven monitoring and digital solution for industrial time-series data for SOEC

# Stack Health Monitoring & Reliability Assessment for SOEC Electrolysis Systems

## Overview
This project presents a **data-driven condition monitoring and reliability assessment framework** for **Solid Oxide Electrolysis Cell (SOEC) stacks** operating under dynamic industrial conditions. The focus is on detecting early degradation, abnormal operating behavior, and reliability risks using electrical and operational time-series data.

High-temperature electrolysis systems are exposed to significant thermal and electrical stress, particularly during **transient load changes**. Reliable monitoring solutions are therefore essential to ensure safe operation, minimize downtime, and support predictive maintenance strategies.

---

## Problem Statement
SOEC stacks operate under harsh conditions involving:
- High temperatures
- Dynamic electrical loads
- Frequent operating transients

These conditions can accelerate degradation mechanisms that are not immediately visible through raw sensor signals. Traditional threshold-based monitoring is often insufficient to distinguish between **nominal transient behavior** and **early signs of abnormal operation or degradation**.

The goal of this project is to develop a **robust, data-driven monitoring concept** that:
- Separates normal operational variability from abnormal behavior
- Detects early reliability risks
- Supports operator-oriented decision-making

---

## Methodology

### Data Analysis
- Analysis of **real-time electrical and operational time-series data**, including current and voltage signals
- Evaluation of system response during **transient load changes** and stress scenarios
- Focus on identifying patterns indicative of degradation or abnormal stack behavior

### Reference Model
- Development of a **rolling median–based reference model** to represent nominal system behavior
- The rolling median provides robustness against noise and short-term fluctuations
- Residuals between measured signals and the reference model are used as health indicators

### Anomaly Detection & Reliability Assessment
- Calculation of **residual signals** to isolate abnormal electrical behavior
- Definition of **rule-based alarm logic** based on residual trends, magnitude, and persistence
- Detection targets:
  - Early degradation indicators
  - Abnormal operating conditions
  - Potential reliability risks affecting stack lifetime

---

## Monitoring & Visualization

The monitoring and alarm concepts are implemented using **Grafana**, enabling:

- Real-time visualization of electrical and operational KPIs
- Residual-based health indicators
- Rule-based alarm states for early intervention
- Operator-oriented dashboards supporting transparent system assessment

### Dashboard Example
![SOEC Monitoring Dashboard](screenshots/overview.png)

---

## System Architecture
