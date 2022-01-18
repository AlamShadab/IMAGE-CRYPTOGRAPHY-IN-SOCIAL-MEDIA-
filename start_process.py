from __future__ import division,print_function,unicode_literals

import os
import sys
from PIL import Image

import logging
from argument_func import get_options

from generate_image import generate_decrypted_image, generate_secret,generate_ciphered_image

__version__ = "0.1"



def load_image(name):
    return Image.open(name)

def prepare_message_image(image,size):
    if size != image.size:
        image= image.resize(size,Image.ANTIALIAS)
    return image.convert("1")


def start_process():
    logging.basicConfig()
    
    args = get_options()
    if args.verbose > 2:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.verbose > 1:
        logging.getLogger().setLevel(logging.INFO)
    elif args.verbose > 0:
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.ERROR)
    
    logging.info("Cipher image generator version %s"% __version__)
    
    try:
        logging.debug("Loading message image '%s'" %(args.message))
        message_image = load_image(args.message)
    except IOError as e:
        logging.fatal("Fatal error: I/O error while loading message image '%s' (%s)" %(args.message, str(e)))
        sys.exit(1)
    
    
    if args.resize is None:
        size = message_image.size
    else:
        size = args.resize
        
    width, height = size
    
    if os.path.isfile(args.secret):
        try:
            logging.debug("Loading secret image '%s'" %(args.secret))
            secret_image = load_image(args.secret)
            
            secret_width, secret_height = secret_image.size
            
            if( secret_width < width or secret_height < height):
                logging.info("Enlarging secret image to fit message size")
                secret_image = generate_secret(size, secret_image=secret_image)
                save_secret = True
        except IOError as e:
            logging.fatal("I/O error while loading secret image '%s' (%s)" % (args.secret,str(e)))
            sys.exit(2)
            
    else:
        logging.info("Generating secret image '%s'" % (args.secret))
        secret_image = generate_secret(size)
        save_secret = True
    
    prepared_image = prepare_message_image(message_image, size)
    ciphered_image = generate_ciphered_image(secret_image, message_image)
    
    if save_secret:
        logging.debug("Saving secret image '%s'" % (args.secret))
        try:
            secret_image.save(args.secret)
        except IOError as e:
            logging.error("I/O error while saving secret image '%s' (%s)" % (args.secret),str(e))
    
    if args.prepared_message:
        logging.debug("Saving prepared message image '%s'" % (args.prepared_message))
        try:
            prepared_image.save(args.prepared_message)
        except IOError as e:
            logging.error("I/O error while saving prepared message image '%s' (%s)" % (args.prepared_message, str(e)))
    
    
    try:
        ciphered_image.save(args.ciphered)
    except IOError as e:
        logging.fatal("I/O error while ciphered image '%s' (%s)" % (args.ciphered, str(e)))
        sys.exit(3)
    
    infile1 = Image.open(args.ciphered)
    infile2 = Image.open(args.secret)
    
    decrypted_image = generate_decrypted_image(infile1,infile2)
    
    try:
        decrypted_image.save("decrypted_"+args.message)
    except IOError as e:
        logging.fatal("I/O error while Decrypted image '%s' (%s)" % (args.ciphered, str(e)))
        sys.exit(3)
        
        
    # if args.display:
    #     prepared_image.show()
    #     secret_image.show()
    #     ciphered_image.show()
    
    
if __name__ == '__main__':
    start_process()
    