import cv2

# we'll use imread function to read the image. 
# the first parameter is the name of the image file
# second argument is a flag. There are 3 flags: 0, 1, -1
# these flags specifies how to read the image. 1 is represents colored image
# 0 represents grayscale image, and -1 represents image with alpha channel
# we'll give 0 as second parameter to the function because we want to load the picture in grayscale mode
img = cv2.imread("lena.jpg", 0)

# if we give a wrong name than our program will display None
# if we give a correct name then the program will display image matrix
print(f"image: {img}")

# Now we want to display our image. We'll use imshow function
# first parameter is the name of the window that the image will open
# the second argument will be the variable that we store our image's matrix
# However the image will be shown in just a few miliseconds and disappear; therefore, we wouldn't see the image
cv2.imshow("image_lena", img)

# we will use waitKey funtion to prevent the image from disappearing
# the argument of the function will be the miliseconds that we want to keep the image window
# let's give 5000 and the window will wait 5 secs until it closes.
# if we give 0 as an argument then the window won't disappear until we close it manually by pressing the close button of
# the window
# we can also make the window close with a key
key = cv2.waitKey(2000)

# after seeing the window we will use destroyallwindows function to eliminate all the windows that we create
# we can also use destroyWindow to destroy a particular window
# 27 is escape key in ASCII table
if key == 27:
    cv2.destroyAllWindows()
# ord is a built-in function and it returns a character's ASCII value
elif key == ord('s'):
# now we'll write the image to a file with imwrite function 
# the first argument will be the name of the file that we want to write the image on
# the second argument will be the variable that holds an image matrix
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyAllWindows()