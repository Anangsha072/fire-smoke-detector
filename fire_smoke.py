from ultralytics import YOLO
import cvzone
import cv2

# Load model
model = YOLO("best (2).pt")

# Open video
cap = cv2.VideoCapture("269443751-chimney-pipe-steam-new-york-or.mp4")

# Confidence threshold
CONF_THRESHOLD = 0.30

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    # Run detection
    results = model(frame, conf=0.25)

    # Process detections
    for box in results[0].boxes:

        confidence = float(box.conf[0])

        # Ignore low confidence detections
        if confidence < CONF_THRESHOLD:
            continue

        cls = int(box.cls[0])

        # Get class name directly from model
        label = model.names[cls]

        print(f"{label}: {confidence:.2f}")

        # Bounding box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Colors
        if label.lower() == "fire":
            color = (0, 0, 255)      # Red
        else:
            color = (255, 0, 0)      # Blue

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

        # Display label and confidence
        cvzone.putTextRect(
            frame,
            f"{label.capitalize()} {confidence*100:.1f}%",
            (x1, max(y1 - 10, 20)),
            scale=1,
            thickness=2
        )

    cv2.imshow("Fire and Smoke Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()