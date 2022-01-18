import os
import sys
from PIL import Image

from generate_image import combine_color, generate_ciphered_image, generate_decrypted_image, generate_secret, separate_color




def load_image(name):
    return Image.open(name)

def main(argv):
    
    input_image_name = str(argv[1])
    message_image = load_image(input_image_name)
    
    color_images = separate_color(message_image.convert("RGB"))
    
    # color_images[0].save("R_image.png")
    # color_images[1].save("G_image.png")
    # color_images[2].save("B_image.png")
    
    # combined_image = combine_color(color_images)
    # combined_image.save("Decrypt_"+input_image_name)
    
    # sys.exit(0)
    
    secret_image = generate_secret(message_image.size)
    secret_image.save("images/secret_"+input_image_name)     
    
    #ciphered_image = generate_ciphered_image(secret_image,message_image)
    
    ciphered_color_images = []
    RGB_msg = ["R","G","B"]
    for i in range(3):
        ciphered_color_images.append(generate_ciphered_image(secret_image,color_images[i]))
        ciphered_color_images[i].save("images/ciphered_"+RGB_msg[i]+"_"+input_image_name)
    
    
    ciphered_image = combine_color(ciphered_color_images)
    ciphered_image.save("images/ciphered_"+input_image_name)
    
    decrypted_images = []
    
    for i in range(3):
        decrypted_images.append(generate_decrypted_image(secret_image,ciphered_color_images[i]))
        decrypted_images[i].save("images/decrypted_"+RGB_msg[i]+"_"+input_image_name)
    #decrypted_image = generate_decrypted_image(secret_image,ciphered_image)
    combined_image = combine_color(decrypted_images)
    
    for x in range(combined_image.size[0]):
        for y in range(combined_image.size[1]):
            color = combined_image.getpixel((x,y))
            combined_image.putpixel((x,y),tuple([255-color[0],255-color[1],255-color[2]]))
    
    combined_image.save("images/Decrypt_"+input_image_name)
    
if __name__ == '__main__':
    main(argv = sys.argv)