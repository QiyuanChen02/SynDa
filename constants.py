# File locations to obtain the data for the pre and post synaptic neurons, and the initial image of the synapses, so we can filter out the pre and post synaptic neurons which don't show up in the image
# All three files are required for the program to run
HOMER_SYNAPSE_PATH = "input/Homer for Q 1.csv"
SYT_SYNAPSE_PATH = "input/Syt for Q 2.csv"
INPUT_IMAGE_PATH = "input/synapses.png"

# File locations to save the density image output and generated excel file output showing the calculations for the synapses
DENSITY_IMAGE_OUTPUT_PATH = "output/densityImage.png"
EXCEL_OUTPUT_PATH = "output/synapseData.xlsx"

# Defines the number of pixels in each block of the density grid.
# The higher the number, the larger the squares will be, which may be useful for images with sparse points
GRIDSIZE = 100

# Colour of displayed points on the png image and the interactive visualization in RGB format
POINTS_COLOUR = (255, 255, 0)
# Colour of the brightest grid in the density map in RGB format
DENSITY_COLOUR = (175, 175, 250)

# Both threshold below used to filter out the pre-synaptic and post-synaptic points which don't show up in the initial image
# Defines how far away a colour should be (in distance to the exact RGB colouring) before it's no longer counted as red or green
COLOUR_THRESHOLD = 150
# Defines the distance we must find a red and green pixel in the image for the point to be counted as a synapse
DISTANCE_THRESHOLD = 2

# Both thresholds below used to filter out the synapse if the pre-synaptic and post-synaptic points are too far away or too close to each other
PRE_POST_DIST_LOWER_THRESHOLD = -4
PRE_POST_DIST_UPPER_THRESHOLD = 8
