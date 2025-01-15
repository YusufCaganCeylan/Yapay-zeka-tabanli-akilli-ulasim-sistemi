from ultralytics import YOLO
#modeli yükleme
model = YOLO('best.pt')
#Video üzerinden tahmin yapma
results = model.predict(source='kaza.mp4', conf=0.25, save=True)


