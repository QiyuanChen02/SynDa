import matplotlib.pyplot as plt  # pip install matplotlib
import mplcursors  # pip install mplcursors


# Show the interactive visualization
def interactiveVisualisation(data, imageDensity):
    # Create the x and y arrays for the scatter plot
    x = []
    y = []
    colours = []
    for coordinate in data:
        x.append(float(coordinate[0]))
        y.append(float(coordinate[1]))
        colours.append((1, 0.65, 0, 0.6))

    # Create the scatter plot with the image of the density grid as the background
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, s=2, color=colours)
    ax.imshow(imageDensity)
    ax.invert_yaxis()

    # Adds interactivity to the scatter plot, allowing the user to see information about the exact point when clicking on it.
    # This information includes the x and y coordinates of the point, the exact id of both the pre and post synaptic neurons which make up the point.
    mplcursors.cursor(scatter).connect(
        "add",
        lambda sel: sel.annotation.set_text(
            f"({sel.target[0]:.2f}, {sel.target[1]:.2f})"
        ),
    )

    # Shows the interactive visualization
    plt.show()
