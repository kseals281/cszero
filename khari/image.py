image = [[w, w, w, w, w],
         [w, b, w, b, w],
         [w, w, g, w, w],
         [w, b, w, b, w],
         [w, w, w, w, w]]
         
def removeRed(image):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            newRow.append(0, pixel[1], pixel[2])
            #255 - pixel[0], 255 - pixel[1], 255- pixel[2] inversion
        newImage.append(newRow)
    return newImage
