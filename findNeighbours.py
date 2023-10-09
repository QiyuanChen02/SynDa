import math


# Finds the closest neighbour of each post synaptic neuron
def findNeighbours(pre, post):
    closestNeighbours = []
    closestNeighbourDistance = []
    for postSynapse in post:
        minDistance = [math.inf, math.inf]  # [distance, index]
        for j, preSynapse in enumerate(pre):
            distance = math.sqrt(
                ((postSynapse[0] - preSynapse[0]) ** 2)
                + ((postSynapse[1] - preSynapse[1]) ** 2)
            )
            if distance < minDistance[0]:
                minDistance = [distance, j]
        closestNeighbours.append(minDistance[1])
        closestNeighbourDistance.append(minDistance[0])
    return closestNeighbours, closestNeighbourDistance


# Finds the post synaptic neurons which are closest to each pre synaptic neuron
def isClosestNeighbour(closestNeighbours, closestNeighbourDistance, index):
    minDistance = math.inf

    for i in range(len(closestNeighbours)):
        if (
            closestNeighbours[i] == closestNeighbours[index]
            and closestNeighbourDistance[i] < minDistance
        ):
            minDistance = closestNeighbourDistance[i]

    return closestNeighbourDistance[index] == minDistance
