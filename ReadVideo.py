import cv2

# Path to the video file
video_path = 'output_video.avi'  # Replace this with the actual path to your video file

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not successfully read, break the loop
    if not ret:
        break

    # Process the frame here (you can display, save, or manipulate the frame as needed)
    # For example, display the frame
    cv2.imshow('Video Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()
