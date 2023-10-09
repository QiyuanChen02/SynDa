# Defines the number of pixels in each block of the density grid.
# The higher the number, the larger the squares will be, which may be useful for images with sparse points
gridsize = 30

# Both threshold below used to filter out the pre-synaptic and post-synaptic points which don't show up in the initial image
# Defines how far away a colour should be (in distance to the exact RGB colouring) before it's no longer counted as red or green
colourThreshold = 150
# Defines the distance we must find a red and green pixel in the image for the point to be counted as a synapse
distanceThreshold = 2

# Both thresholds below used to filter out the synapse if the pre-synaptic and post-synaptic points are too far away or too close to each other
prePostDistanceLowerThreshold = -4
prePostDistanceUpperThreshold = 8
