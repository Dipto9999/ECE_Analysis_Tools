import control as ctl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np

def root_locus(R = 10E3, C = 1.6E-9, Am = 1.586) :
    # The transfer function is H(s) = (1 / (R*C)^2) / (s^2 + (3-Am) / (R*C) * s + 1 / (R*C)^2)
    # This can be simplified to H(s) = 1 / ((R*C)^2 * s^2 + (3-Am) * (R*C) * s + 1)
    H_s = ctl.tf([1], [(R*C)**2, (3-Am) * (R*C), 1])
    poles = ctl.poles(H_s)

    fig = plt.figure(figsize=(12, 6))  # Size for better visibility
    ax = fig.add_subplot(111)
    ax.set_title('Butterworth Filter: Root Locus', fontsize=20)  # Title font size

    # Generate the root locus plot on the provided axes
    ctl.root_locus(H_s, ax=ax, grid = True)

    # Stylizing the plot
    ax.set_xlabel('Real Axis', fontsize=18)
    ax.set_ylabel('Imaginary Axis', fontsize=18)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.tick_params(axis='both', which='major', labelsize=14)

    plot_title = f'Butterworth Filter: Root Locus (Am = {Am} < 3)' if Am < 3\
        else f'Butterworth Filter: Root Locus (Am = {Am} > 3)' if Am > 3\
        else 'Butterworth Filter: Root Locus (Am = 3)'

    ax.set_title(plot_title, fontsize=20)
    ax.set_xlabel('Real Axis (σ)', fontsize=15)
    ax.set_ylabel('Imaginary Axis (jω)', fontsize=15)

    pole_annotations = []
    for pole in poles:
        current_real, current_imag = round(np.real(pole), 1), round(np.imag(pole), 1)
        current_magnitude, current_phase = int(round(np.sqrt(current_real**2 + current_imag**2), 0)), int(round(np.degrees(np.arctan2(current_imag, current_real)), 0))
        phasor_representation = f'{current_magnitude} ∠ {current_phase}°'

        ax.plot(np.real(pole), np.imag(pole), color = 'black', markersize = 12)
        pole_annotations.append(f'Pole: {phasor_representation}')
    # pole_annotations = ['Pole at {:.1f} + {:.1f}j'.format(np.real(p), np.imag(p)) for p in poles]

   # Increase tick label sizes
    ax.tick_params(axis='both', which='major', labelsize=15)

    # Create legend entries for poles
    custom_legend = [Line2D([0], [0], color='black', marker='x', linestyle='None', markersize=10)]
    ax.legend(custom_legend * len(poles), pole_annotations, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

    # Set aspect ratio, grid
    ax.grid(True)

    ax.set_xlim(-1.1 * max(np.abs(poles)), 1.1 * max(np.abs(poles)))

    # Adjust layout to make room for the legend
    plt.subplots_adjust(top=0.85, right=0.70)
    plt.show() # Show the plot on screen

    # Saving the figure
    fig.savefig(f'Figures/Butterworth_Filter_Root_Locus_Am_{Am}.png', dpi=300)

root_locus(R = 10E3, C = 1.6E-9, Am = 1.586) # Underdamped
root_locus(R = 10E3, C = 1.6E-9, Am = 3) # Critically Damped
root_locus(R = 10E3, C = 1.6E-9, Am = 3 + (3- 1.586)) # Overdamped