from PIL import Image
import scipy.ndimage
import matplotlib.pyplot as plt
import numpy as np

def imread(filename):
    """
        Summary: Reads a iamge file and return an object.
            
        Args: filename.
            
        Returns: An object of an image.
    """
    try:
        global fn
        fn = filename
        img = Image.open(filename)
        return img
    except FileNotFoundError:
        print(f"File: {filename} Not Found.")
        
def imshow(img):
    """
            Summary: displays a iamge file and return an object.
            
            Args: filename.
            
    """
    plt.imshow(img)
    plt.show()
        
def resize(img, s):
    resized_img = img.resize(s)
    return resized_img
    
    
def get_properties(img):
    d = dict()
    global fn
    d['filename'] =fn
    d['format'] = img.format
    d['mode'] = str(img.mode)
    d['dimensions'] = tuple(scipy.ndimage.imread(fn).shape)

    return d

def get_pixels(img):
    return list(img.getdata())

def get_band(img, band):
    prop = get_properties(img)
    if int(prop['dimensions'][2]) > 3:
        img = img.convert('RGB')
    source = img.split()
    R, G, B = 0, 1, 2
    # Assign color intensity bands, zero for red and blue.
    if band.lower() == 'r'  :
        b = source[R].point(lambda i: i * 0.0)
    if band.lower() == 'g'  :
        b = source[G]
    if band.lower() == 'b'  :
        b = source[B].point(lambda i: i * 0.0)
    return np.resize(b, list(img.size)[::-1])

def plot_signature(img):
    prop = get_properties(img)
    if int(prop['dimensions'][2]) > 3:
        img = img.convert('RGB')
    r, g, b = img.split()
    bins = list(range(256))
    plt.plot(bins, r.histogram(), 'r', label="Red")
    plt.plot(bins, g.histogram(), 'g', label="Green")
    plt.plot(bins, b.histogram(), 'b', label="Blue")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.title("Signature of Image")
    plt.grid(True)
    plt.legend()
    plt.show()

def imsave(img, filename):
    img.save(filename)
    
def imrotate(img, degrees):
    return img.rotate(degrees)

def im2bw(img):
    return img.convert('L')
    
