import os
from densityAnalyser import analyseImageDensity
from showSynapse import analyseImageSynapse
from helpers.constants import INPUT_FOLDER_NAME, OUTPUT_FOLDER_NAME

def main():

    # Performs the density and synapse analysis on all the folders in the input directory
    print("Performing analysis on all folders in the input directory...\n")
    for item in os.listdir(INPUT_FOLDER_NAME):
        item_path = os.path.join(INPUT_FOLDER_NAME, item)
        if os.path.isdir(item_path):
            print(f"Started analysis of {item}")
            analyseImageDensity(item, visualise=False)
            analyseImageSynapse(item, visualise=False)
            print(f"Analysis of {item} complete!\n")
    print(f"Analysis complete! The results can be found in the {OUTPUT_FOLDER_NAME} directory.")

if __name__ == "__main__":
    main()
