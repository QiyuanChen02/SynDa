import math
from helpers.findNeighbours import isClosestNeighbour
from helpers.constants import (
    PRE_POST_DIST_LOWER_THRESHOLD,
    PRE_POST_DIST_UPPER_THRESHOLD,
)


def getSynapse(pre, post, closestNeighbours, closestNeighbourDistance):
    synapses = []
    for i, postSynapse in enumerate(post):
        preSynapse = pre[closestNeighbours[i]]
        radiusPre = (preSynapse[2] / math.pi) ** 0.5
        radiusPost = (postSynapse[2] / math.pi) ** 0.5
        synpase = [
            (
                (
                    (radiusPost + 0.5 * closestNeighbourDistance[i])
                    / (radiusPre + radiusPost + closestNeighbourDistance[i])
                )
                * (preSynapse[0] - postSynapse[0])
            )
            + postSynapse[0],
            (
                (
                    (radiusPost + 0.5 * closestNeighbourDistance[i])
                    / (radiusPre + radiusPost + closestNeighbourDistance[i])
                )
                * (preSynapse[1] - postSynapse[1])
            )
            + postSynapse[1],
        ]
        synapses.append(synpase)
    return synapses


def validateSynapses(
    synapses,
    closestNeighbours,
    closestNeighbourDistance,
    preSynapseData,
    postSynapseData,
):
    distanceMinusRadius = []
    for i in range(len(closestNeighbourDistance)):
        distanceMinusRadius.append(
            closestNeighbourDistance[i]
            - (preSynapseData[closestNeighbours[i]][2] / math.pi) ** 0.5
            - (postSynapseData[i][2] / math.pi) ** 0.5
        )

    isValidSynapse = []
    for i in range(len(synapses)):
        isValidSynapse.append(
            isClosestNeighbour(closestNeighbours, closestNeighbourDistance, i)
            and PRE_POST_DIST_LOWER_THRESHOLD
            < distanceMinusRadius[i]
            < PRE_POST_DIST_UPPER_THRESHOLD
        )

    validSynapses = []
    for i in range(len(synapses)):
        if isValidSynapse[i]:
            validSynapses.append(synapses[i])

    return isValidSynapse, validSynapses
