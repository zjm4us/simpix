# simpix

C++ starter code
* simpix_start.cpp
use make to build this example

Usage: simapix_start image1 image2 <output=out.png>

Python starter code
* simpix_start.py

Usage: simapix_start image1 image2 <output=out.png>


-----------------------------------------------------

# Simpix Assignment – PHYS5630

## Description

This project implements a pixel mapping algorithm using simulated annealing to transform one image into another by rearranging its pixels. Each pixel is used exactly once, so the color match cannot be perfect.  

This submission includes both small and large images. Large images meet the PHYS5630 requirement of at least 1920×1080 pixels.

---

## Files Included


Image A and B are from https://en.wikipedia.org/wiki/Impressionism . 
Image C and D are from National Gallary of Arts https://www.nga.gov/artworks . 


| File | Description |
|------|-------------|
| `simpix.py` | Pixel mapping for small images (`imageA.jpg` → `imageB.jpg`) for testing purposes. |
| `large_simpix.py` | Pixel mapping for large images (`large_imageA.jpg` ↔ `large_imageB.jpg`) for final submission. |
| `imageA.jpg`, `imageB.jpg`, frisbe_scott_stadium.png , rotunda_north_facade.png  | Small input images (optional). |
| `large_imageA.jpg`, `large_imageB.jpg`, large_imageC.jpg ,large_imageD.jpg | High-resolution input images. |
| `small_A_to_B.jpg`, frisbee_to_rotunda.jpg | Output for small images. |
| `A_to_B.jpg`, `B_to_A.jpg`, C_to_D.jpg ,D_to_C.jpg  | Output images for large images. |

---

## Requirements

- Python 3.8+  
- Packages: `numpy`, `Pillow`, `numba`  
- Recommended system: 4 cores, 16 GB RAM (Rivanna cluster works well)

---

## How to Run . 

1.  Activate your environment . 

2. Small images (optional test, fast) . 

python simpix.py . 

Outputs:  

imageA_to_imageB.jpg → pixels from imageA.jpg mapped to imageB.jpg . 
frisbee_to_rotunda.jpg → pixels from frisbe_scott_stadium.png mapped to rotunda_north_facade.png . 


Runtimes:  
imageA_to_imageB.jpg: 2.03 seconds . 
frisbee_to_rotunda.jpg: 0.62 seconds . 


3. Large images (final submission) . 
   python large_simpix.py . 
   
Outputs:  


A_to_B.jpg → pixels from large_imageA.jpg mapped to large_imageB.jpg . 
B_to_A.jpg → pixels from large_imageB.jpg mapped to large_imageA.jpg . 
C_to_D.jpg → pixels from large_imageC.jpg mapped to large_imageD.jpg . 
D_to_C.jpg → pixels from large_imageD.jpg mapped to large_imageC.jpg . 

Runtimes:   


A_to_B.jpg: 121.33 seconds . 
B_to_A.jpg: 98.16 seconds .
C_to_D.jpg: 104.62 seconds . 
D_to_C.jpg: 109.23 seconds . 

Method . 

The code uses simulated annealing to iteratively swap pixels in the source image to reduce the color difference with the target image.
Numba is used to accelerate the computation.
Pixel arrays are flattened and stored as float32 for numeric stability.

Results

All outputs are stored in the project folder.
Large image transformations successfully reconstruct the target images at a high-resolution level.
This implementation meets all PHYS5630 assignment requirements.
