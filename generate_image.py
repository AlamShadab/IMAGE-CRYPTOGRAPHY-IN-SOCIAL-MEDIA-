import random
from PIL import Image


def separate_color(image):
    w,h = image.size
    color_images = [Image.new(mode="L",size=image.size) for i in range(3)]
    
    for x in range(w):
        for y in range(h):
            color = image.getpixel((x,y))
            for i in range(3):
                color_images[i].putpixel((x,y),color[i])
    
    return color_images

def generate_secret(size, secret_image=None):
    width, height = size
    new_secret_image = Image.new(mode="L",size=(width*2,height*2))
    
    if secret_image:
        old_width,old_height  = secret_image.size
    else:
        old_width,old_height = (-1,-1)
    
    
    for x in range(0,2*width,2):
        for   y in range(0,2*height,2):
            if(x < old_width and y < old_height):
                color = secret_image.getpixel((x,y))
            else:
                color = random.randint(0,256)
            new_secret_image.putpixel((x,y),color)
            new_secret_image.putpixel((x+1,y),255-color)
            new_secret_image.putpixel((x,y+1),255-color)
            new_secret_image.putpixel((x+1,y+1),color)
    
    return new_secret_image



def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode="L",size=(width*2,height*2))
    
    for x in range(0,2*width,2):
        for y in range(0,2*height,2):
            secret = secret_image.getpixel((x,y))
            message = prepared_image.getpixel((x/2,y/2))
            color = secret ^ message
            ciphered_image.putpixel((x,y),255-color)
            ciphered_image.putpixel((x+1,y),color)
            ciphered_image.putpixel((x,y+1),color)
            ciphered_image.putpixel((x+1,y+1),255-color)
    
    return ciphered_image


def generate_decrypted_image(infile1,infile2):
    outfile = Image.new('L', infile1.size)
    for x in range(infile1.size[0]):
        for y in range(infile1.size[1]):
            outfile.putpixel((x,y),(infile1.getpixel((x,y))^infile2.getpixel((x,y))))
    return outfile


def combine_color(images):
    
    image = Image.new(mode="RGB",size=images[0].size)
    w,h = images[0].size
    for x in range(w):
        for y in range(h):
            r = images[0].getpixel((x,y))
            g = images[1].getpixel((x,y))
            b = images[2].getpixel((x,y))
            
            color = tuple([r,g,b])
            image.putpixel((x,y),color)
    
    return image