import matplotlib.pyplot as plt
import numpy as np

def plot_phasors(phasors: list[dict], title: str):
    fig = plt.figure(figsize=(18, 15))  # Size for better visibility
    ax = fig.add_subplot(111)
    ax.set_title(title, fontsize=20)  # Title font size

    plot_size = 1

    filename = f'{title.replace(" ", "_")}_'
    for phasor in phasors:
        real_part, imag_part = round(phasor['real'], 2), round(phasor['imag'], 2)
        complex_representation = f"{real_part} + {imag_part}j"

        magnitude = round(np.sqrt(real_part**2 + imag_part**2), 2)
        if real_part != 0 and imag_part != 0:
            phasor_angle = round(np.degrees(np.arctan(imag_part / real_part)), 3)
        else:
            phasor_angle = 0
        phasor_representation = f"{magnitude} ∠ {round(phasor_angle, 1)}°"

        # Draw Phasor
        ax.quiver(
            0, 0, real_part, imag_part, angles='xy', scale_units='xy', scale=1,
            color=phasor['color'], label=f'{phasor['name']}: {phasor_representation} = {complex_representation}',
            linewidth=2
        )

        if magnitude > plot_size:
            plot_size = magnitude
        filename += f'''{phasor_representation.replace(' ', '_')}__'''


    # Draw horizontal and vertical lines representing axes
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Update axis labels to Sigma and jω
    ax.set_xlabel('Real Axis (σ)', fontsize=15)
    ax.set_ylabel('Imaginary Axis (jω)', fontsize=15)

    # Set axis limits
    ax.set_xlim(-1.1 * plot_size, 1.1 * plot_size)
    ax.set_ylim(-1.1 * plot_size, 1.1 * plot_size)

    # Increase tick label sizes
    ax.tick_params(axis='both', which='major', labelsize=15)

    # Place the legend outside of the axes
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

    # Set aspect ratio, grid
    ax.set_aspect('equal', 'box')
    ax.grid(True)

    fig.savefig(f'../Figures/{filename.rstrip('__')}.png')  # Save the figure as a PNG file

    plt.show()

# Set the limits for the plot; adjust these values as necessary.

plot_phasors(
    phasors = [
        {'name': 'V1', 'real': 15.04 * np.cos(0*np.pi/180.0), 'imag': 0, 'color': 'blue'},
        {'name': 'V2', 'real': 26.88 * np.cos(-267.7*np.pi/180.0), 'imag': 26.88 * np.sin(-267.7*np.pi/180.0), 'color': 'orange'},
        {'name': 'V3', 'real': 34.68 * np.cos(-61.2*np.pi/180.0), 'imag': 34.68 * np.sin(-61.2*np.pi/180.0), 'color': 'green'}
    ],
    title = 'Series RLC Circuit (Phasor Diagram)'
)