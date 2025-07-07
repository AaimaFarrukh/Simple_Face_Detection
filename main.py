#Importing Modulues
import cv2


#Drawing Boundry for Face Detection
def draw_boundry(img,classifier, scaleFactor,minNeighbors, color,text):
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords=[]
    for(x, y, w, h) in features:
        cv2.rectangle(img, (w,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA) 
        coords= [x, y, w, h]
    return coords
#Detecting the Face
def detect(img, faceCascade, eyesCascade):
    color= {"blue":(255,0,0), "red":"0,0,255", "green":(0,255,0)}
    coords= draw_boundry(img, faceCascade, 1.1, 10, color['blue'], "Face")
    
    if len(coords)==4:
        roi_img= img[coords[1]: coords[1]+ coords[3], coords[0]: coords[0]+ coords[2]]
        coords= draw_boundry(img, eyesCascade, 1.05, 15, color['green'], "Eyes")
    return img

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyesCascade= cv2.CascadeClassifier("haarcascade_eye.xml")

video_capture= cv2.VideoCapture(0)

while True:
    _, img= video_capture.read()
    img= detect(img, faceCascade, eyesCascade)
    cv2.imshow("face detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
