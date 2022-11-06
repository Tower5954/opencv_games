import cv2
import csv


cap = cv2.VideoCapture(0)
all_resolutions = {}


with open("resolutions.csv") as csv_file:
    resolutions = csv.reader(csv_file, delimiter="\t")
    for row in resolutions:
        # print(row[1].split('Ã—'))
        width = int(row[1].split('Ã—')[0])
        height = int(row[1].split('Ã—')[1])

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        all_resolutions[str(width) + ' x ' + str(height)] = "supported"

print(all_resolutions)