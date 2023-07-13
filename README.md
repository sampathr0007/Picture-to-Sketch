# Picture-to-Sketch
In this project I developed a model which converts any picture to the pencil sketch irrespective of the lighting factor(the image must be slightly visible).

Project Report: Picture to Pencil Sketch Conversion using OpenCV and Image Manipulation Techniques

Introduction:
The purpose of this project is to develop a software application that can convert any given picture into a pencil sketch using OpenCV (Open Source Computer Vision Library) and apply various image manipulation techniques such as color manipulation, blurring, and Photoshop effects. The project leverages the knowledge of image processing algorithms, color theory, and image editing techniques to achieve the desired output.

Methodology:
The project implementation involves the following steps:

a. Image Loading: The user selects an image file, and the software application loads the image using the OpenCV library.

b. Color to Gray Conversion: The loaded image is converted from color to grayscale, as a pencil sketch is typically represented in shades of gray.

c. Image Blurring: To create a smoother and more artistic effect, the grayscale image is blurred using various blurring algorithms available in OpenCV, such as Gaussian blur or bilateral filter.

d. Inverting Image: The blurred image is inverted to obtain a negative image, which enhances the pencil sketch-like appearance.

e. Pencil Sketch Effect: The negative image is then blended with the original grayscale image using appropriate blending techniques to create a pencil sketch effect. This step involves adjusting the contrast and intensity of the image to achieve the desired output.

f. Photoshop Effects: To add further artistic effects, Photoshop-like techniques such as applying filters, adjusting brightness/contrast, or adding texture can be implemented to enhance the pencil sketch output.

Implementation Details:
The project is implemented using the following technologies and tools:
a. Programming Language: Python
b. OpenCV Library: Used for image loading, manipulation, and processing.
c. Image Blurring Algorithms: Gaussian blur, bilateral filter, etc.
d. Image Editing Techniques: Contrast adjustment, blending, Photoshop effects.
e. Development Environment: Python IDE (Integrated Development Environment) such as PyCharm or Jupyter Notebook.

Results and Evaluation:
The performance of the picture to pencil sketch conversion can be evaluated based on the quality of the output sketches. The software application can be tested using various types of images, including different lighting conditions, complex backgrounds, and different color schemes. The output pencil sketches should retain the main features of the original image while displaying a hand-drawn appearance.
The evaluation can also include user feedback on the usability and effectiveness of the software application, taking into consideration factors such as ease of use, speed of conversion, and overall user satisfaction.

Conclusion:
The project successfully implements a software application that converts any given picture into a pencil sketch using OpenCV and various image manipulation techniques. By leveraging knowledge of colors, blurring, and Photoshop effects, the project achieves a realistic pencil sketch-like output. The application has potential applications in the fields of art, design, and image editing.
