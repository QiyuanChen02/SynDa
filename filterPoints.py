import numpy as np
from PIL import Image
from constants import (
    COLOUR_THRESHOLD,
    DISTANCE_THRESHOLD,
)


def filterPoints(data, imageSrc, width, height, type):
    image = Image.open(imageSrc)
    resizedImage = image.resize((round(width), round(height)))
    # Convert the data to a list of [X, Y, Area] points as floats
    parsedData = [[float(point[0]), float(point[1]), float(point[2])] for point in data]

    filteredPoints = []

    for point in parsedData:
        x, y, _ = point
        hasRed = False
        hasGreen = False
        for i in range(-DISTANCE_THRESHOLD, DISTANCE_THRESHOLD):
            for j in range(-DISTANCE_THRESHOLD, DISTANCE_THRESHOLD):
                try:
                    colour = resizedImage.getpixel((round(x) + i, round(y) + j))
                    if (
                        np.linalg.norm([colour[0] - 255, colour[1] - 0, colour[2] - 0])
                        <= COLOUR_THRESHOLD
                    ):
                        hasRed = True
                    if (
                        np.linalg.norm([colour[0] - 0, colour[1] - 255, colour[2] - 0])
                        <= COLOUR_THRESHOLD
                    ):
                        hasGreen = True
                except:
                    pass

        # Check if the point meets the distance criteria for both red and green
        if (type == "red" and hasRed) or (type == "green" and hasGreen):
            filteredPoints.append(point)

    return filteredPoints
