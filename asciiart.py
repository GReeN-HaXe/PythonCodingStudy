from PIL import Image

# variables
ASCII_CHARS = "@%#*+=-:. "
image = Image.open("ascii-pineapple.jpg")

print("Successfully loaded image:", image.filename)
print("Image size:", image.width, "x", image.height)

pixels = image.load()

width, height = image.size

pixelMatrix = []

for y in range(height):
    row = []
    for x in range(width):
        row.append(pixels[x, y])
    pixelMatrix.append(row)

# Print the pixel matrix
#for row in pixelMatrix:
#    print(row)
#print(pixelMatrix[0][0])  # Print the first pixel as a sample