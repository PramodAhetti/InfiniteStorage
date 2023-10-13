import cv2
import os
import numpy as np

# Directory containing image files
image_directory = 'images'

# Output video file path
output_video_path = 'output_video.avi'

# Directory to save restored frames
restored_images_directory = 'restored_images'

# Create the restored images directory if it does not exist
os.makedirs(restored_images_directory, exist_ok=True)

# Get the list of image files in the directory
image_files = [img for img in os.listdir(image_directory) if img.endswith(".jpg")]

# Sort the image files to ensure they are in the correct order
# Get the first image to retrieve dimensions
first_image = cv2.imread(os.path.join(image_directory, image_files[0]))
height, width, layers = first_image.shape

# Shuffle columns of the frame (along the width)
random_indices = np.random.permutation(width)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter(output_video_path, fourcc, 1, (width, height))

# Loop through the image files, shuffle columns, add them to the video, and save restored frames
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (width, height))

    # Shuffle columns of the frame (along the width)
    shuffled_frame = frame[:, random_indices]
    video.write(shuffled_frame)



# Release the VideoWriter and print a success message
video.release()
print(f"Video created successfully at: {output_video_path}")
# Open the video file
cap = cv2.VideoCapture(output_video_path)

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
    # Save the original shuffled frame for restoration
    original_shuffled_frame = np.copy(shuffled_frame)

    # Restore the original order of columns for the frame
    restored_frame = np.zeros_like(shuffled_frame)
    for i, index in enumerate(random_indices):
        restored_frame[:, index] = original_shuffled_frame[:, i]

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
