
from ISO8583 import *
from ISOErrors import *
import traceback
import binascii
import os

def MyAHex(str):
    return binascii.a2b_hex(str.replace(' ',''))

def MyHexA(str):
    return binascii.b2a_hex(str)

print("3333")
print(binascii.b2a_hex("3333".encode("utf-8")))

os.system(['clear','cls'][os.name == 'nt'])

# get new object
p = ISO8583()
#some string describing the transation type
transation = "200"
print ('Setting transation type to %s' % transation)
p.setTransationType(transation)
# Is the same that:
#p.setMTI(transation)

#Some tests and 
print ('Setting bits')

p.setBit(2, "5477666265921222")
p.setBit(3,"000000")
p.setBit(4,14959)
p.setBit(11,555556)
p.setBit(22,"0220")
p.setBit(25,"00")
p.setBit(35,"5477666265921222d25085060000012600000")
p.setBit(41,"33333333")
p.setBit(42,"222222222222222")
p.setBit(49,156)
p.setBit(53,"1000000000000000")
p.setBit(60,"2200001")
p.setBit(64,"3133394343433842")

#show hex bitmap
print ('Bitmap in HEX')
p.showBitmap()

#Show bits
print ('Bits with values')
p.showIsoBits()

# Show raw ASCII ISO
print ('The package is -> ')
p.showRawIso()
