import random
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from IPython.display import HTML


# -------------------------
# Configuration
# -------------------------
num_qubits = 2
num_steps = 6
num_seeds = 30

one_qubit_gates = ["H", "X", "Y", "Z"]
operations = one_qubit_gates + ["CNOT"]

fig, ax = plt.subplots(figsize=(10, 3))


# -------------------------
# Random-circuit generation
# -------------------------
def random_operation(rng):
    """
    Return either:
        ("H"/"X"/"Y"/"Z", qubit)
    or:
        ("CNOT", control, target)
    """
    operation = rng.choice(operations)

    if operation == "CNOT":
        control = rng.randrange(num_qubits)
        target = 1 - control  # Two-qubit case: target != control.
        return ("CNOT", control, target)

    qubit = rng.randrange(num_qubits)
    return (operation, qubit)


def make_random_circuit(seed):
    """
    Generate a reproducible random circuit for a single seed.
    """
    rng = random.Random(seed)

    return [
        random_operation(rng)
        for _ in range(num_steps)
    ]


# Pre-generate all 30 circuits.
# This makes each frame deterministic and avoids reseeding global randomness.
circuits = [
    make_random_circuit(seed)
    for seed in range(num_seeds)
]


# -------------------------
# Circuit drawing functions
# -------------------------
def qubit_y(qubit):
    """
    Draw q_0 on the upper wire and q_1 on the lower wire.
    """
    return num_qubits - 1 - qubit


def draw_circuit(operations_for_seed, seed):
    """
    Draw one complete quantum circuit on the shared Matplotlib axes.
    """
    ax.clear()

    x_max = num_steps + 1

    # Draw quantum wires first.
    for qubit in range(num_qubits):
        y = qubit_y(qubit)

        ax.plot([0, x_max], [y, y], color="black", linewidth=1.5)
        ax.text(
            -0.3,
            y,
            f"$q_{qubit}$",
            ha="right",
            va="center",
            fontsize=14,
        )

    # Draw all operations in this seed's circuit.
    for step, operation in enumerate(operations_for_seed, start=1):
        gate = operation[0]

        # One-qubit gate: H, X, Y, or Z.
        if gate in one_qubit_gates:
            _, qubit = operation
            y = qubit_y(qubit)

            box = plt.Rectangle(
                (step - 0.30, y - 0.25),
                width=0.60,
                height=0.50,
                facecolor="lightblue",
                edgecolor="black",
                linewidth=1.5,
            )
            ax.add_patch(box)

            ax.text(
                step,
                y,
                gate,
                ha="center",
                va="center",
                fontsize=14,
                fontweight="bold",
            )

        # CNOT gate.
        elif gate == "CNOT":
            _, control, target = operation

            y_control = qubit_y(control)
            y_target = qubit_y(target)

            # Connector between control and target.
            ax.plot(
                [step, step],
                [y_control, y_target],
                color="black",
                linewidth=1.5,
            )

            # Filled control dot.
            ax.plot(
                step,
                y_control,
                marker="o",
                color="black",
                markersize=8,
            )

            # Circled-plus target.
            target_circle = plt.Circle(
                (step, y_target),
                radius=0.18,
                fill=False,
                edgecolor="black",
                linewidth=1.5,
            )
            ax.add_patch(target_circle)

            ax.plot(
                [step - 0.12, step + 0.12],
                [y_target, y_target],
                color="black",
                linewidth=1.3,
            )
            ax.plot(
                [step, step],
                [y_target - 0.12, y_target + 0.12],
                color="black",
                linewidth=1.3,
            )

    ax.set_xlim(-0.7, x_max)
    ax.set_ylim(-0.7, num_qubits - 0.3)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_title(
        f"Overall training: Episode {seed}",
        fontsize=15,
    )


# -------------------------
# Animation: one frame per seed
# -------------------------
def animate(seed):
    draw_circuit(circuits[seed], seed)


animation = FuncAnimation(
    fig,
    animate,
    frames=range(num_seeds),  # seeds 0, 1, ..., 29
    interval=10000,             # milliseconds per circuit in Jupyter
    repeat=True,
)

animation.save(
    f"random_{num_qubits}qubit_circuit_group.gif",
    writer="pillow",
    fps=2,
)

plt.close(fig)

HTML(animation.to_jshtml())