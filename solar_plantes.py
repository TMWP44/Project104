import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Define font and scale for putText
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2
color = (255, 255, 255)

# Add text for each planet
cv2.putText(img, "Sun", (20, 300), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Mercury", (75, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Venus", (200, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Earth", (300, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Mars", (400, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (550, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Saturn", (800, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Uranus", (950, 50), font, scale, color, thickness, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1100, 50), font, scale, color, thickness, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close the displayed image window
cv2.destroyAllWindows()
