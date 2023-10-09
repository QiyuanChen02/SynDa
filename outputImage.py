from PIL import Image  # pip install pillow
import math


def getColourMap(gridDensity):
    # Define a color map for the synapses
    colorMapSynapses = [
        (0, 0, 0),
        (255, 165, 0),
    ]

    # Define a color map for the density grid.
    # Note that the maximum number of synapses in a square is used to determine the color of the squares, by dividing the number of synapses in a square by the maximum number of synapses and then converting it into an RGB tuple
    maximumGridValue = max(map(max, gridDensity))
    colorMapDensity = list(
        map(
            lambda x: (x, x, x),
            [
                math.floor(255 * (i / maximumGridValue))
                for i in range(maximumGridValue + 1)
            ],
        )
    )

    return colorMapSynapses, colorMapDensity


def gridToImage(array, colorMap, scalingFactor):
    # Determine the dimensions of the array
    height = len(array)
    width = len(array[0])

    # Scale up the dimensions (e.g scalingFactor 10 means 10x10 blocks for each array element)
    scaledHeight = height * scalingFactor
    scaledWidth = width * scalingFactor

    image = Image.new("RGB", (scaledWidth, scaledHeight))

    for y in range(height):
        for x in range(width):
            value = array[y][x]
            color = colorMap[value]

            blockX = x * scalingFactor
            blockY = y * scalingFactor

            # Secondary loop to set the pixels of the block, with the scaling factor being the size of the block
            for i in range(scalingFactor):
                for j in range(scalingFactor):
                    image.putpixel((blockX + i, blockY + j), color)

    return image


# This function overlays two images on top of each other, using the blend function of the PIL library.
def overlayImages(image1, image2, alpha=0.5):
    if image1.size != image2.size:
        raise ValueError("Both images must have the same dimensions.")

    # Create a new blank image with the same dimensions as the input images
    overlayedImage = Image.new("RGBA", image1.size)

    # Blend the two images together
    overlayedImage = Image.blend(image1.convert("RGBA"), image2.convert("RGBA"), alpha)
    return overlayedImage


def createOutputImage(gridDensity, gridSynapses, scalingFactor):
    colorMapSynapses, colorMapDensity = getColourMap(gridDensity)
    imageSynapse = gridToImage(gridSynapses, colorMapSynapses, 1)
    imageDensity = gridToImage(gridDensity, colorMapDensity, scalingFactor)
    combinedImage = overlayImages(imageSynapse, imageDensity)
    combinedImage.save("output/densityImage.png")
    return imageDensity, imageSynapse, combinedImage
