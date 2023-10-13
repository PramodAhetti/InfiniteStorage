import cv2
import os
import numpy as np



cap = cv2.VideoCapture('output_video.avi')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Loop through the video frames and display restored frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not successfully read, break the loop
    if not ret:
        break
    restored_frame = np.zeros_like(shuffled_frame)
    for i, index in enumerate(random_indices):
        restored_frame[:, index] = shuffled_frame[:, i]
    
    # Save the restored frame to the restored images directory
    restored_image_path = os.path.join(restored_images_directory, f'restored_{image_file}')
    cv2.imwrite(restored_image_path, restored_frame)
    # Display the frame here (you can save or further process the frame if needed)
    cv2.imshow('Restored Video Frame', frame)

    # Wait for a key event and check if the 'q' key was pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()

print(f"Restored frames saved in: {restored_images_directory}")
