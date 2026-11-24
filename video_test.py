import cv2
import sys
video_pfad = sys.argv[1] if len(sys.argv) > 1 else "verkehr.webm"
video = cv2.VideoCapture(video_pfad)

if not video.isOpened():
    print("Video konnte nicht geöffnet werden.")

else:
    anzahl_bilder = 0

    while True:
        erfolg, bild = video.read()

        if not erfolg:
            break

        anzahl_bilder = anzahl_bilder + 1

        cv2.imshow("AI-TrafficFlow", bild)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    print("Gelesene Bilder:", anzahl_bilder)

video.release()
cv2.destroyAllWindows()