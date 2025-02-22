# Analysis Tools : Electrical and Computer Engineering

## Contents

* [Overview](#Overview)
    * [HP Prime](#HP-Prime)
    * [Poles](#Poles)
    * [Root Locus](#Root-Locus)
    * [Phasors](#Phasors)

## Overview

I wrote these **Python** scripts and **HP PPL** programs as complementary tools in courses I took as part of <b>The University of British Columbia Electrical and Computer Engineering</b> undergraduate program.

These made my life easier in analyzing data and producing reports. Please feel free to contribute to this repo and use these tools as part of your degree.

### HP Prime

These **Computer Algebra Systems (CAS)** programs are used in the <a href ="https://en.wikipedia.org/wiki/HP_Prime">**HP-Prime Graphing Calculator**</a> to make it easier to perform circuit analysis with <a href = "https://en.wikipedia.org/wiki/Modified_nodal_analysis">**Modified Nodal Analysis (MNA)**</a>.

You can import the code in [`HP_Prime`](HP_Prime) to your virtual / physical device with the <a href = "https://www.hpcalc.org/details/8938">**HP Connectivity Kit**</a>

### Poles

The [`poles.py`](Scripts/poles.py) script can be used to generate a phasor plot of a filter with `matplotlib`. The `plot_poles(poles, real_lim, imag_lim)` function can be modified with the chart limits.

<div align="center">
    <img src="Figures/Butterworth_Filter_Plot_Radius_10000_Poles_10000_∠_-45.0°__10000_∠_45.0°.png" width=400 height=300 title="Ex : Butterworth Filter Poles Plot">
</div>

### Root Locus

The [`root_locus.py`](Scripts/root_locus.py) script can be used to generate root locus plots with `matplotlib`. The `root_locus(R, C, Am)` function can be modified with the resistance, capacitance, midband gain values.

Note that this is for the predetermined transfer function below. This is implemented as part of the script, but a few changes to the underlying formulas and calculations can be used to generate plots for like transfer functions.

$$ H(s) = \frac{1}{(R \times C)^{2} \times s^{2} + \frac{(3 - A_m)}{(R \times C)} \times s + \frac{1}{(R \times C)^{2}}} $$

<div align="center">
    <img src="Figures/Butterworth_Filter_Root_Locus_Am_1.586.png" width=450 height=300 title="Ex : Butterworth Filter Root Locus Critically Damped">
</div>

### Phasors

I have added a [`phasors.py`](Scripts/phasors.py) script for helping with three-phase system calculations and visualizing current-voltage relationships.

<div align="center">
    <img src="Figures/Three-Phase_RL_Balanced_Load_(Voltage_Phasor_Diagram)_10.0_∠_-3.4°__10.15_∠_-63.2°__10.09_∠_57.3°.png" width=450 height=450 title="Ex : Series RLC Circuit (Phasor Diagram)">
</div>
