import matplotlib.pyplot as plt
import numpy as np

def plot_phasors(phasors: list[dict], title: str):
    fig = plt.figure(figsize = (12, 12))  # Square Aspect Ratio
    ax = fig.add_subplot(111)
    ax.set_title(title, fontsize = 20, pad = 30)  # Title with Padding

    filename = f'{title.replace(" ", "_")}_'
    magnitudes = []

    for phasor in phasors:
        real_part, imag_part = round(phasor['real'], 2), round(phasor['imag'], 2)
        complex_representation = f"{real_part} + {imag_part}j"

        magnitude = round(np.sqrt(real_part**2 + imag_part**2), 2)
        magnitudes.append(magnitude)

        if real_part != 0 and imag_part != 0:
            phasor_angle = round(np.degrees(np.arctan(imag_part / real_part)), 3)
        else:
            phasor_angle = 0
        phasor_representation = f"{magnitude} ∠ {round(phasor_angle, 1)}°"

        # Draw Phasor
        ax.quiver(
            0, 0, real_part, imag_part, angles='xy', scale_units='xy', scale=1,
            color=phasor['color'], label=f'{phasor["name"]}: {phasor_representation} = {complex_representation}',
            linewidth=2
        )

        filename += f'''{phasor_representation.replace(' ', '_')}__'''

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    ax.set_xlabel('Real Axis (σ)', fontsize=15)
    ax.set_ylabel('Imaginary Axis (jω)', fontsize=15)

    max_real = max(abs(phasor['real']) for phasor in phasors)
    max_imag = max(abs(phasor['imag']) for phasor in phasors)

    if abs(max_real) < 1:
        ax.set_xlim(-1, 1)
        ax.set_xticks(np.linspace(round(-1), round(1), 11))
    else:
        ax.set_xlim(-1.2 * max_real, 1.2 * max_real)
        ax.set_xticks(np.linspace(round(-1.2 * max_real), round(1.2 * max_real), 11))

    if abs(max_imag) < 1:
        ax.set_ylim(-1, 1)
        ax.set_yticks(np.linspace(round(-1), round(1), 11))
    else:
        ax.set_ylim(-1.2 * max_imag, 1.2 * max_imag)
        ax.set_yticks(np.linspace(round(-1.2 * max_imag), round(1.2 * max_imag), 11))

    ax.tick_params(axis='both', which='minor', labelsize=15)

    ax.legend(
        loc = 'lower center', bbox_to_anchor = (0.5, 1.15),  # Position Above Plot with Padding
        ncol = 2, framealpha = 0.9,  # 2 Columns, Transparent Background
        fontsize = 12,
    )

    ax.grid(True)
    fig.subplots_adjust(bottom = 0.7)

    fig.tight_layout(rect = [0, 0, 1, 0.9]) # Make Space for Title
    fig.savefig(f'Figures/{filename.replace("\n","").replace(":","_").rstrip("__")}.png')
    plt.show()

plot_phasors(
    phasors=[
        {
            'name': 'V1', 'color': 'blue',
            'real': 10 * np.cos(-3.4*np.pi/180.0),
            'imag': 10 * np.sin(-3.4*np.pi/180.0),
        },
        {
            'name': 'V2', 'color': 'green',
            'real': 10.15 * np.cos(-243.2*np.pi/180.0),
            'imag': 10.15 * np.sin(-243.2*np.pi/180.0)
        },
        {
            'name': 'V3', 'color': 'orange',
            'real': 10.09 * np.cos(-122.7*np.pi/180.0),
            'imag': 10.09 * np.sin(-122.7*np.pi/180.0)
        },
    ],
    title='Three-Phase RL Balanced Load (Voltage Phasor Diagram)'
)

plot_phasors(
    phasors=[
        {
            'name': 'I1', 'color': 'blue',
            'real': 0.3 * np.cos(-50.8*np.pi/180.0),
            'imag': 0.3 * np.sin(-50.8*np.pi/180.0),
        },
        {
            'name': 'I2', 'color': 'green',
            'real': 0.26 * np.cos(63*np.pi/180.0),
            'imag': 0.26 * np.sin(63*np.pi/180.0)
        },
        {
            'name': 'I3', 'color': 'orange',
            'real': 0.27* np.cos(-174.9*np.pi/180.0),
            'imag': 0.27* np.sin(-174.9*np.pi/180.0)
        },
    ],
    title='Three-Phase RL Balanced Load (Current Phasor Diagram)'
)
