#imprimir en pantalla una imagen
import cv2 as cv

#===========================================================================

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    heigh = int(frame.shape[0]*scale)

    dimensions = (width, heigh)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#===========================================================================
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

#para leer videos, es necesario leer frame por frame...
while True:
    isTrue, frame = capture.read()
    
    #utilizamos la funcion de reescalado previamente definida
    frame_resized = rescaleFrame(frame)

    #cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    #no se que significa esta condición, pero si se pulsa laa tecla d se para el video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()