import random
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from IPython.display import HTML


# Uncomment for reproducible tutorial output.
random.seed(4)

num_qubits = 2
num_steps = 6
one_qubit_gates = ["H", "X", "Y", "Z"]
operations = one_qubit_gates + ["CNOT"]


def random_operation():
    """
    Return either:
        ("H"/"X"/"Y"/"Z", qubit)
    or:
        ("CNOT", control, target)
    """
    operation = random.choice(operations)

    if operation == "CNOT":
        control = random.randrange(num_qubits)
        target = 1 - control  # With 2 qubits, ensure control != target.
        return ("CNOT", control, target)

    qubit = random.randrange(num_qubits)
    return (operation, qubit)


# Pre-sample the entire random circuit.
random_ops = [random_operation() for _ in range(num_steps)]

print("Random circuit operations:")
for step, operation in enumerate(random_ops, start=1):
    print(f"Step {step}: {operation}")


def qubit_y(qubit):
    """
    Map q_0 -> upper wire and q_1 -> lower wire.
    """
    return num_qubits - 1 - qubit


def draw_circuit_frame(frame):
    """
    Draw the circuit containing operations from step 0 through `frame`.
    """
    ax.clear()

    x_max = num_steps + 1


    # Draw operations up to the current frame.
    for step, operation in enumerate(random_ops[:frame + 1], start=1):
        gate = operation[0]

        if gate in one_qubit_gates:
            _, qubit = operation
            y = qubit_y(qubit)

            # Gate box.
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
                step, y, gate,
                ha="center",
                va="center",
                fontsize=14,
                fontweight="bold",
            )

        elif gate == "CNOT":
            _, control, target = operation

            y_control = qubit_y(control)
            y_target = qubit_y(target)

            # Vertical connection between control and target.
            ax.plot(
                [step, step],
                [y_control, y_target],
                color="black",
                linewidth=1.5,
            )

            # Control dot.
            ax.plot(
                step,
                y_control,
                marker="o",
                color="black",
                markersize=8,
            )

            # Target circle.
            target_circle = plt.Circle(
                (step, y_target),
                radius=0.18,
                fill=False,
                edgecolor="black",
                linewidth=1.5,
            )
            ax.add_patch(target_circle)

            # Plus sign inside target.
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
    # Draw quantum wires.
    for qubit in range(num_qubits):
        y = qubit_y(qubit)

        ax.plot([0, x_max], [y, y], color="black", linewidth=1.5)
        ax.text(
            -0.3, y, f"$q_{qubit}$",
            ha="right",
            va="center",
            fontsize=14,
        )

    ax.set_xlim(-0.7, x_max)
    ax.set_ylim(-0.7, num_qubits - 0.3)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_title(
        f"Each episode: Step {frame + 1}/{num_steps}",
        fontsize=15,
    )


fig, ax = plt.subplots(figsize=(12, 3))

animation = FuncAnimation(
    fig,
    draw_circuit_frame,
    frames=num_steps,
    interval=10000,
    repeat=True,
)
animation.save(
    f"random_{num_qubits}qubit_circuit_single.gif",
    writer="pillow",
    fps=2,
)

plt.close(fig)

HTML(animation.to_jshtml())