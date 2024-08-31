import pandas as pd
import os


def outputExcel(
    filteredPostSynapseData,
    closestNeighbours,
    closestNeighbourDistance,
    synapses,
    isValidSynapse,
    outputPath,
):
    df = pd.DataFrame(
        {
            "Object Syt1 (POST)": filteredPostSynapseData,
            "Closest Neighbour": closestNeighbours,
            "Closest Neighbour Distance": closestNeighbourDistance,
            "Synapse": synapses,
            "Is Synapse": isValidSynapse,
        },
    )

    folderPath = os.path.dirname(outputPath)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    df.to_excel(outputPath, index=False)
