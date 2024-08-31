# Takes the data in the 2 csv files and returns a list of points with the format [X, Y, Area]
def fetchPoints(fileName):
    wantedData = ["AreaShape_Center_X", "AreaShape_Center_Y", "AreaShape_Area"]
    wantedIndices = []
    points = []
    wantedPoints = []
    try:
        with open(fileName) as f:
            for line in f:
                points.append(line.split(","))
    except FileNotFoundError:
        raise Exception(f"The file {fileName} was not found. The file is either missing or labelled incorrectly.")

    for data in wantedData:
        if data not in points[0]:
            raise Exception("wantedData array invalid.")
        else:
            wantedIndices.append(points[0].index(data))

    for point in points[1:]:
        wantedPoints.append([float(point[i]) for i in wantedIndices])
    return wantedPoints
