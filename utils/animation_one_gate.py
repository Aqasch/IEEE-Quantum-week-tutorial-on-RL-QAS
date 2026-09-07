import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------
random.seed(4)  # Remove for a different random sequence each run.

one_qubit_gates = ["H", "X", "Y", "Z"]
gate_types = one_qubit_gates + ["CNOT"]

# Number of individual random samples in one loop.
num_samples = 12

# Frames for which each sampled gate remains visible.
frames_per_gate = 6

# Gate sequence is pre-sampled so the GIF renders deterministically.
sampled_gates = [random.choice(gate_types) for _ in range(num_samples)]

print("Randomly sampled gates:")
print(" → ".join(sampled_gates))


# ------------------------------------------------------------
# Gate drawing functions
# ------------------------------------------------------------
def draw_single_gate(ax, gate, alpha, scale):
    """Draw a single one-qubit gate as a box."""
    width = 1.35 * scale
    height = 1.15 * scale

    gate_box = plt.Rectangle(
        (-width / 2, -height / 2),
        width=width,
        height=height,
        facecolor="#9DD9F3",
        edgecolor="#1A1A1A",
        linewidth=2.5,
        alpha=alpha,
    )
    ax.add_patch(gate_box)

    ax.text(
        0,
        0,
        gate,
        ha="center",
        va="center",
        fontsize=38 * scale,
        fontweight="bold",
        color="#111111",
        alpha=alpha,
    )


def draw_cnot_symbol(ax, alpha, scale):
    """
    Draw only a CNOT icon, without circuit wires:
    a control dot, vertical connection, and target-plus circle.
    """
    y_control = 0.65 * scale
    y_target = -0.65 * scale

    # Connection line.
    ax.plot(
        [0, 0],
        [y_control, y_target],
        color="#111111",
        linewidth=2.8 * scale,
        alpha=alpha,
    )

    # Control dot.
    ax.plot(
        0,
        y_control,
        marker="o",
        color="#111111",
        markersize=12 * scale,
        alpha=alpha,
    )

    # Target circle.
    radius = 0.30 * scale
    target = plt.Circle(
        (0, y_target),
        radius=radius,
        fill=False,
        edgecolor="#111111",
        linewidth=2.8 * scale,
        alpha=alpha,
    )
    ax.add_patch(target)

    # Target plus sign.
    plus_radius = 0.19 * scale

    ax.plot(
        [-plus_radius, plus_radius],
        [y_target, y_target],
        color="#111111",
        linewidth=2.2 * scale,
        alpha=alpha,
    )
    ax.plot(
        [0, 0],
        [y_target - plus_radius, y_target + plus_radius],
        color="#111111",
        linewidth=2.2 * scale,
        alpha=alpha,
    )

    # Label makes the operation unambiguous.
    ax.text(
        0.62,
        0.05,
        "",
        ha="left",
        va="center",
        fontsize=24 * scale,
        fontweight="bold",
        color="#111111",
        alpha=alpha,
    )


# ------------------------------------------------------------
# Animation update
# ------------------------------------------------------------
def draw_frame(frame):
    """
    Display exactly one randomly sampled gate.

    Every `frames_per_gate` frames, the current gate is replaced
    by the next randomly sampled gate.
    """
    ax.clear()

    gate_index = frame // frames_per_gate
    local_frame = frame % frames_per_gate
    gate = sampled_gates[gate_index]

    # Smooth fade-in for a newly sampled gate.
    fade_frames = 5
    alpha = min(1.0, (local_frame + 1) / fade_frames)

    # Small pop-in effect.
    scale = 0.75 + 0.25 * min(1.0, (local_frame + 1) / fade_frames)

    if gate in one_qubit_gates:
        draw_single_gate(ax, gate, alpha, scale)
    else:
        draw_cnot_symbol(ax, alpha, scale)

    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")

    # ax.set_title(
    #     f"Randomly sampled gate {gate_index + 1}/{num_samples}",
    #     fontsize=16,
    #     pad=16,
    # )


# ------------------------------------------------------------
# Build, save, and display the GIF
# ------------------------------------------------------------
total_frames = num_samples * frames_per_gate

fig, ax = plt.subplots(figsize=(5, 4))

animation = FuncAnimation(
    fig,
    draw_frame,
    frames=total_frames,
    interval=90,
    repeat=True,
)

animation.save(
    "random_quantum_gate_sampling.gif",
    writer="pillow",
    fps=11,
)

plt.close(fig)

display(HTML(animation.to_jshtml()))