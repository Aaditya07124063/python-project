import sys
import subprocess
import random

# Ensure required modules are installed
required_modules = ["opencv-python", "mediapipe", "pyautogui"]
for module in required_modules:
    try:
        __import__(module.replace("-", "_"))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

# Generate 100 random colors
colors = {f"Color {i+1}": tuple(random.randint(0, 255) for _ in range(3)) for i in range(100)}
selected_color = list(colors.keys())[0]

color_positions = {}  # Store color positions on the screen
scroll_offset = 0  # Scroll offset for color selection
scroll_threshold = 0.05  # Adjust scroll sensitivity

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror image
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Display available colors as small square boxes on the right side
    y_offset = 50
    x_offset = w - 30  # Keep colors aligned on the right side
    color_positions.clear()
    visible_colors = list(colors.items())[scroll_offset:scroll_offset+10]  # Show 10 colors at a time
    for i, (color_name, color_value) in enumerate(visible_colors):
        box_x, box_y = x_offset, y_offset + i * 30
        cv2.rectangle(frame, (box_x - 20, box_y), (box_x, box_y + 20), color_value, -1)
        color_positions[color_name] = (box_x - 10, box_y + 10)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get finger tip positions
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            middle_y = int(middle_tip.y * h)

            # Check if finger is tapping on a color option
            for color_name, (color_x, color_y) in color_positions.items():
                if abs(index_x - color_x) < 10 and abs(index_y - color_y) < 10:
                    selected_color = color_name
                    break

            # Scroll gestures (Two Fingers Move Up or Down)
            if abs(index_y - middle_y) < 20 and abs(ring_tip.y - pinky_tip.y) < 0.05:  # Ensure two fingers close together
                if index_tip.y < middle_tip.y - scroll_threshold:
                    scroll_offset = max(0, scroll_offset - 1)  # Scroll up
                elif index_tip.y > middle_tip.y + scroll_threshold:
                    scroll_offset = min(len(colors) - 10, scroll_offset + 1)  # Scroll down

    # Apply selected color as overlay to entire frame
    overlay = frame.copy()
    overlay[:, :] = colors[selected_color]
    cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)

    # Display selected color text
    cv2.putText(frame, f"Color: {selected_color}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Hand Gesture Color Selector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
// try.
//v2.0