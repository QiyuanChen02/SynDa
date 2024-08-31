from helpers.constants import (
    INPUT_FOLDER_NAME,
    OUTPUT_FOLDER_NAME,
    PRE_SYNAPSE_FILE_NAME,
    POST_SYNAPSE_FILE_NAME,
    IMAGE_FILE_NAME,
    DENSITY_IMAGE_FILE_NAME,
    SYNAPSE_IMAGE_FILE_NAME,
    SYNAPSE_DATA_FILE_NAME,
)

# Returns a list of important paths for the input and output files
def fetchPaths(folderName):
    paths = (
        f"{INPUT_FOLDER_NAME}/{folderName}/{PRE_SYNAPSE_FILE_NAME}",
        f"{INPUT_FOLDER_NAME}/{folderName}/{POST_SYNAPSE_FILE_NAME}",
        f"{INPUT_FOLDER_NAME}/{folderName}/{IMAGE_FILE_NAME}",
        f"{OUTPUT_FOLDER_NAME}/{folderName}/{DENSITY_IMAGE_FILE_NAME}",
        f"{OUTPUT_FOLDER_NAME}/{folderName}/{SYNAPSE_IMAGE_FILE_NAME}",
        f"{OUTPUT_FOLDER_NAME}/{folderName}/{SYNAPSE_DATA_FILE_NAME}",
    )
    return paths
