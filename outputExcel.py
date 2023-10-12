import pandas as pd
from constants import EXCEL_OUTPUT_PATH


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
    df.to_excel(EXCEL_OUTPUT_PATH, index=False)
