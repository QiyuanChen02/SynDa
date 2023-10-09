import numpy as np
from PIL import Image


def filterPoints(
    data, imageSrc, width, height, type, colourThreshold, distanceThreshold
):
    image = Image.open(imageSrc)
    resizedImage = image.resize((round(width), round(height)))
    # Convert the data to a list of [X, Y, Area] points as floats
    parsedData = [[float(point[0]), float(point[1]), float(point[2])] for point in data]

    filteredPoints = []

    for point in parsedData:
        x, y, _ = point
        hasRed = False
        hasGreen = False
        for i in range(-distanceThreshold, distanceThreshold):
            for j in range(-distanceThreshold, distanceThreshold):
                try:
                    colour = resizedImage.getpixel((round(x) + i, round(y) + j))
                    if (
                        np.linalg.norm([colour[0] - 255, colour[1] - 0, colour[2] - 0])
                        <= colourThreshold
                    ):
                        hasRed = True
                    if (
                        np.linalg.norm([colour[0] - 0, colour[1] - 255, colour[2] - 0])
                        <= colourThreshold
                    ):
                        hasGreen = True
                except:
                    pass

        # Check if the point meets the distance criteria for both red and green
        if (type == "red" and hasRed) or (type == "green" and hasGreen):
            filteredPoints.append(point)

    return filteredPoints
