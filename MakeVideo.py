import cv2
import os
import numpy as np
# Directory containing image files
image_directory = 'images'

# Output video file path
output_video_path = 'output_video.avi'

# Get the list of image files in the directory
image_files = [img for img in os.listdir(image_directory) if img.endswith(".jpg")]  # Change the extension if your images have a different format

# Sort the image files to ensure they are in the correct order
# Get the first image to retrieve dimensions
first_image = cv2.imread(os.path.join(image_directory, image_files[0]))
height, width, layers = first_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # You can also use other codecs like 'MJPG' or 'DIVX'
video = cv2.VideoWriter(output_video_path, fourcc, 1, (width, height))  # 1 is the frames per second (FPS) of the output video


random_image = first_image
random_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
# Loop through the image files and add them to the video
for image_file in image_files:            
    image_path = os.path.join(image_directory, image_file)
    frame = cv2.imread(image_path)
    frame=cv2.resize(frame,(width,height))
    for k in range(3):
        for i in range(height):
           for j in range(width):
                temp=int(frame[i][j][k])
                bin=int(random_image[i][j][k])
                temp=(temp+bin)%256
 
                frame[i][j][k]=np.uint8(temp)
                    
    video.write(frame)

# Release the VideoWriter and print a success message
video.release()

print(f"Video created successfully at: {output_video_path}")
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
    for k in range(3):
        for i in range(height):
           for j in range(width):
                temp=int(frame[i][j][k])
                bin=int(random_image[i][j][k])
                temp=(temp-bin)%256
 
                frame[i][j][k]=np.uint8(temp) 

    frame = cv2.medianBlur(frame, 3)



    # Process the fra me here (you can display, save, or manipulate the frame as needed)
    # For example, display the frame
 
    cv2.imshow('Video Frame', frame)
    cv2.waitKey()

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()
