from ultralytics import YOLO

model = YOLO("best (2).pt")

results = model.predict(
    source="fire_test.mp4",
    conf=0.5,
    save=True
)

print("Detection complete!")