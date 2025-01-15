import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from gpiozero import LED, Buzzer
from signal import pause
import numpy as np

# LED ve Buzzer tanımları
led_severe = LED(18)
buzzer_severe = Buzzer(23)
led_moderate = LED(24)
buzzer_moderate = Buzzer(25)

# YOLO modeli yükle
model = YOLO("best.pt")

# Picamera2'yi başlat
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

try:
    while True:
        # Kameradan görüntü al
        frame = picam2.capture_array()

        # YOLO tahminlerini yap
        results = model.predict(source=frame, show=False, conf=0.5)

        # Tahmin sonuçlarını işle
        labels = [result['name'] for result in results[0].boxes.data]

        # Severe durumunu kontrol et
        if "severe" in labels:
            led_severe.on()
            buzzer_severe.beep(on_time=3, off_time=0, n=1)
        else:
            led_severe.off()

        # Moderate durumunu kontrol et
        if "moderate" in labels:
            led_moderate.on()
            buzzer_moderate.beep(on_time=3, off_time=0, n=1)
        else:
            led_moderate.off()

        # Tahmin sonuçlarını görüntüle
        annotated_frame = results[0].plot()

        # OpenCV ile görüntüleme
        annotated_frame_bgr = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("YOLO Tahmin", annotated_frame_bgr)

        # 'q' tuşuna basıldığında çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    picam2.stop()
    cv2.destroyAllWindows()
