import cv2

def find_any_face(): 
    faceCascade = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml" )

    def identify_faces( image ):
        faces = faceCascade.detectMultiScale( image, 2 )
        return image if len(faces) else []

    cap = cv2.VideoCapture( cv2.CAP_ANY )

    while True:
        ret, frame = cap.read( )
        if ret == True:
            img = identify_faces( cv2.flip( frame, 1 ) )
            if len( img ):
                break

    cap.release( )
    return img