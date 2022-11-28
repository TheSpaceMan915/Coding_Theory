import struct


# opening the file to read in binary format
file_path = '../files/circles.bmp'
file_bmp = open(file_path, 'rb')

# reading bytes
# unpacking a tuple of bytes (3,2,5,30,2) using struct module
# converting objects of bytes to strings using % operator
print('Type:', file_bmp.read(2))
print('Size: %s' % struct.unpack('I', file_bmp.read(4)))
print('Reserve 1: %s' % struct.unpack('H', file_bmp.read(2)))
print('Reserve 2: %s' % struct.unpack('H', file_bmp.read(2)))
print('Offset: %s' % struct.unpack('I', file_bmp.read(4)))

print('DIB The size of the header: %s' % struct.unpack('I', file_bmp.read(4)))
print('Width: %s' % struct.unpack('I', file_bmp.read(4)))
print('Height: %s' % struct.unpack('I', file_bmp.read(4)))
print('The number of colour planes: %s' % struct.unpack('H', file_bmp.read(2)))
print('Bit/pixel: %s' % struct.unpack('H', file_bmp.read(2)))
print('Compression method: %s' % struct.unpack('I', file_bmp.read(4)))
print('Image size: %s' % struct.unpack('I', file_bmp.read(4)))
print('Horizontal resolution: %s' % struct.unpack('I', file_bmp.read(4)))
print('Vertical resolution: %s' % struct.unpack('I', file_bmp.read(4)))
print('The number of colours: %s' % struct.unpack('I', file_bmp.read(4)))
print('The number of important colours: %s' % struct.unpack('I', file_bmp.read(4)))

file_bmp.close()