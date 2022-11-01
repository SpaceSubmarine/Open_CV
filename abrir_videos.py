#imprimir en pantalla una imagen
import cv2 as cv

#input = 0 si utilizamos por ejemplo una webcam 
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

#para leer videos, es necesario leer frame por frame...
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    #no se que significa esta condición, pero si se pulsa laa tecla d se para el video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

