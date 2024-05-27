import cv2

input = cv2.VideoCapture(0)
height = int(input.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(input.get(cv2.CAP_PROP_FRAME_WIDTH))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('IqraSaher.avi', fourcc, 30, (height, width), isColor=True)

while input.isOpened():
    # get validity boolean and current frame
    ret, frame = input.read()

    # if valid tag is false, loop back to start
    if not ret:
        break
    else:
        out.write(frame)

input.release()
out.release()