import cv2
import mediapipe as mp
import math
import numpy as np

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inisialisasi MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(0)

def count_raised_fingers(landmarks):
    fingers = [
        landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x,
        landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y,
        landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y,
        landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y,
        landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
    ]
    return fingers.count(True)

def calculate_distance(point1, point2, frame_width, frame_height):
    dx = (point1.x - point2.x) * frame_width
    dy = (point1.y - point2.y) * frame_height
    distance_pixels = math.sqrt(dx**2 + dy**2)
    distance_cm = distance_pixels * 0.026
    return distance_cm

def draw_star(frame, center, size, color, thickness):
    points = []
    for i in range(5):
        angle = i * 2 * math.pi / 5 - math.pi / 2
        x = int(center[0] + size * math.cos(angle))
        y = int(center[1] + size * math.sin(angle))
        points.append((x, y))
    for i in range(5):
        cv2.line(frame, points[i], points[(i + 2) % 5], color, thickness)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    total_fingers = 0
    right_hand_distance = None
    left_hand_distance = None
    
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            total_fingers += count_raised_fingers(hand_landmarks)
            
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            center_x = int((index_finger_tip.x + thumb_tip.x) / 2 * frame.shape[1])
            center_y = int((index_finger_tip.y + thumb_tip.y) / 2 * frame.shape[0])
            distance_cm = calculate_distance(index_finger_tip, thumb_tip, frame.shape[1], frame.shape[0])
            size = int(distance_cm * 10)  
            
            draw_star(frame, (center_x, center_y), size, (0, 165, 255), 2)  # Orange color
            
            if handedness.classification[0].label == 'Right':
                right_hand_distance = distance_cm
            else:
                left_hand_distance = distance_cm
    
    if right_hand_distance is not None:
        cv2.putText(frame, f"Right: {right_hand_distance:.2f} cm", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    if left_hand_distance is not None:
        cv2.putText(frame, f"Left: {left_hand_distance:.2f} cm", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.putText(frame, f"Total Fingers: {total_fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Hand Detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()