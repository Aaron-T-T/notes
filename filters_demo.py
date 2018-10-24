from PIL import Image

#img = Image.open('beach.jpg')
#img.show()
#
#pixmap = img.load()




#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        r, g, b = pixmap[i,j]
#        r = b
#        g -= r
#        b += g

def purple_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = b
            g -= r
            b += g
    
        
            pixmap[i,j] = (r,g,b)

    img.show()


def blue_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r -= b
            g = r
            b += g
    
        
            pixmap[i,j] = (r,g,b)

    img.show()

def black_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = r+b
            g = r+g
            b = g+b
    
        
            pixmap[i,j] = (r,g,b)

    img.show()

def spray_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = b
            g -= r+i
            b += g
    
        
            pixmap[i,j] = (r,g,b)

    img.show()
    
    
    
    
def pinkpurple_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = b
            g -= r 
            b += g + i
    
        
            pixmap[i,j] = (r,g,b)

    img.show()
    

def white_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = b 
            g = r 
            b = g + j
    
        
            pixmap[i,j] = (r,g,b)

    img.show()

def rainbow_filter(file):
    img = Image.open(file)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = b
            g += r - i
            b = g * 7
    
        
            pixmap[i,j] = (r,g,b)

    img.show()