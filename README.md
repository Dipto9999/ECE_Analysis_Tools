# Plot Tools : Electrical and Computer Engineering

## Contents

* [Overview](#Overview)
    * [Phasor](#Phasor)
    * [Root Locus](#Root-Locus)

## Overview

I wrote these **Python** scripts as a complementary tool in courses I took as part of <b>The University of British Columbia Electrical and Computer Engineering</b> undergraduate program.

This made my life easier in sharing data and producing reports. Please feel free to contribute to this repo and use these tools as part of your degree.

### Phasor

The [`phasor.py`](Scripts/phasor.py) script can be used to generate a phasor plot with `matplotlib`. The `plot_phasor(poles, real_lim, imag_lim)` function can be modified with the chart limits.

<div align="center">
    <img src="Figures/Butterworth_Filter_Phasor_Radius_10000_Poles_10000_∠_-45.0°__10000_∠_45.0°.png" width=300 height=250 title="Ex : Butterworth Filter Phasor Plot">
</div>

### Root Locus

The [`root_locus.py`](Scripts/root_locus.py) script can be used to generate root locus plots with `matplotlib`. The `root_locus(R, C, Am)` function can be modified with the resistance, capacitance, midband gain values.

Note that this is for the predetermined transfer function below. This is implemented as part of the script, but a few changes to the underlying formulas and calculations can be used to generate plots for like transfer functions.

$$ H(s) = \frac{1}{(R \times C)^{2} \times s^{2} + \frac{(3 - A_m)}{(R \times C)} \times s + \frac{1}{(R \times C)^{2}}} $$

<div align="center">
    <img src="Figures/Butterworth_Filter_Root_Locus_am_1.586.png" width=400 height=250 title="Ex : Butterworth Filter Root Locus Critically Damped">
</div>