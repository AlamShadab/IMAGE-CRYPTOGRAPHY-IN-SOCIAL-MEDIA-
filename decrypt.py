import os
from PIL import Image
import sys

infile1 = Image.open('ciphered.png')
infile2 = Image.open('secret.png')

outfile = Image.new('1', infile1.size)
for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        outfile.putpixel((x,y),max(infile1.getpixel((x,y)), infile2.getpixel((x,y))))
outfile.save('Decrypted.png')



for secret in range(10):
    for original in range(10):
        ciphered = secret^original
        decrypt = secret^ciphered
        
        print("original=",original," secret=",secret," ciphered=",ciphered," decrypt=",decrypt)
        
