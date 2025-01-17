import matplotlib.pyplot as plt
import numpy as np

def plot_poles(poles, real_lim, imag_lim):
    fig = plt.figure(figsize=(18, 15))  # Size for better visibility
    ax = fig.add_subplot(111)
    ax.set_title('Butterworth Filter: Poles', fontsize=20)  # Title font size

    # Calculate radius and phasor angle for both poles
    radius = int(np.ceil(np.sqrt(poles[0][0]**2 + poles[0][1]**2)))

    filename = f'Butterworth_Filter_Plot_Radius_{radius}_Poles_'''
    for pole in poles:
        current_real, current_imag = pole
        complex_representation = f"{current_real} + {current_imag}j"
        if current_real != 0 and current_imag != 0:
            phasor_angle = np.degrees(np.arctan(current_imag / current_real))
        else:
            phasor_angle = 0
        phasor_representation = f"{radius} ∠ {round(phasor_angle, 1)}°"

        ax.plot(
            [0, current_real], [0, current_imag], 'k-',  # Changed color code to 'k-' for black
            label=f'Pole: {phasor_representation} = {complex_representation}',
            linewidth=2, marker='o', markersize=8, markerfacecolor='black', markeredgecolor='black',
        )
        filename += f'''{phasor_representation.replace(' ', '_')}__'''

    # Draw phasor circle
    phasor_circle = plt.Circle((0, 0), radius, color='black', fill=False, linewidth=1.5, linestyle='dashed')
    ax.add_artist(phasor_circle)

    # Draw horizontal and vertical lines representing axes
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Update axis labels to Sigma and jω
    ax.set_xlabel('Real Axis (σ)', fontsize=15)
    ax.set_ylabel('Imaginary Axis (jω)', fontsize=15)

    # Set axis limits
    ax.set_xlim(-1.1 * radius, 1.1 * radius)
    ax.set_ylim(-1.1 * radius, 1.1 * radius)

    # Increase tick label sizes
    ax.tick_params(axis='both', which='major', labelsize=15)

    # Place the legend outside of the axes
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

    # Set aspect ratio, grid
    ax.set_aspect('equal', 'box')
    ax.grid(True)

    fig.savefig(f'Figures/{filename.rstrip('__')}.png')  # Save the figure as a PNG file

    plt.show()

# Set the limits for the plot; adjust these values as necessary.

# Original poles
plot_poles(
    poles = [(-7071, 7071), (-7071, -7071)],
    real_lim = -8000, imag_lim = 8000
)

# Oscillatory poles
plot_poles(
    poles = [(0, 10E3), (0, -10E3)],
    real_lim = -8000, imag_lim = 8000
)