# Timestamp-Extractor
This Documentation is related to the timestamp_extraction.py

### Classes and Functions
This Python file contains 1 class, 5 private functions and 3 public functions

Class name : tse

Public functions 

Function 1 : extraction_datetime
Function 2 : extraction_dmy
Function 3 : extraction_time

### Requirements 
    1)opencv-python
    2)numpy

### Imports 
    1)os
    2)sys
    3)cv2
    4)numpy
    5)skimage

### How to Use
Import the class into your required file
```
=> from timestamp_extraction import tse
```

Create an object of the class tse with arguments of image (required) and path of the control images (default : ./control_images)
```    
=> img1 = tse(image, path)
```

If you want the entire timestamp, use extraction_datetime()
This returns date, month, year, hour, minute, second in this order
```    
=> date, month, year, hour, minute, second = img1.extraction_datetime()
```

If you want just the date, month and year, use extraction_dmy()
This returns date, month, year in this order
```    
=> date, month, year = img1.extraction_datetime()
```

If you want the just the hour, minute and second, use extraction_time()
This returns hour, minute, second in this order
```    
=> hour, minute, second = img1.extraction_time()
```