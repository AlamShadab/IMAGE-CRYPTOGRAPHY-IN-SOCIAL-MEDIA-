import argparse

def get_options():
    parser = argparse.ArgumentParser(description='Visual cipher image generator.')
    
    parser.add_argument('--message','-m',required=True,metavar="MESSAGE_IMAGE_FILE_PATH",help='message image')
    
    parser.add_argument('--secret','-s',metavar="SELECT_IMAGE_FILE_PATH", default="secret.png",help='secret image to be generated')
    parser.add_argument('--ciphered','-c',metavar="SELECT_IMAGE_FILE_PATH", default="ciphered.png",help='ciphered image to be generated')
    
    parser.add_argument('--resize','-r',metavar="WIDTH,HEIGHT",help="resize message image (defaults to message image size). If width or height is larger than that of the secret image, the secret image will be enlarged")
    
    parser.add_argument('--prepared_message','-p', metavar="PREPARED_MESSAGE_IMAGE_FILE_PATH", help='If present, the prepared message image is saved to this path')    
    
    parser.add_argument('--display', '-d', action='store_true')
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()
    if args.resize:
        try:
            width, height = [int(i.strip()) for i in args.resize.strip().split(",")]
            args.resize = (width, height)
        except:
            parser.error("Invalid format for resize option.")
        else:
            if width <= 0:
                parser.error("Resize width should be > 0.")
            if height <= 0:
                parser.error("Resize height should be > 0.")

    return args
    
    