import pandas as pd


def outputExcel(
    filteredPostSynapseData,
    closestNeighbours,
    closestNeighbourDistance,
    synapses,
    isValidSynapse,
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
    df.to_excel("output/pointData.xlsx", index=False)
