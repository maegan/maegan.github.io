# CSIS110, HW2, fall 2018, sample code and template

# We're giving you this to help you get started.  Get this
# program to run, THEN change the picture to one of your choosing
# and complete the rest of the program as required. You don't have to
# use "negative" or "mirrorHorizontal", they're just here as 
# examples.  Make sure your program fulfills the assignment
# requirements, and have fun!!

# Program creates a collage of 2 copies of the "bigben.jpg" picture, 
# the original plus one with the negative.  It then mirrors the whole 
# collage, without losing any of the original 2 versions.
# To run this program:  load into JES, run "setMediaPath()" from command 
# area to set the media path to the folder containing "bigben.jpg", then 
# type "createCollage()"

# Transforms "picture" into its negative (code from from book, Program 41)
def negative(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen (pixel)
    b = getBlue(pixel)
    nucolor = makeColor(255-r, 255-g, 255-b)
    setColor (pixel, nucolor)

# Mirrors an image horizontally (from book, Program 67)
def mirrorHorizontal(source):
  mirrorpoint = int(getHeight(source)/2)
  for yOffset in range(0,mirrorpoint):
    for x in range(1,getWidth(source)):
      pbottom = getPixel(source,x,yOffset+mirrorpoint)
      ptop = getPixel(source,x,mirrorpoint-yOffset)
      setColor(pbottom,getColor(ptop))

# Create a collage of 2 versions of "bigben.jpg", then mirror 
# horizontally.  
def createCollage():



  # Find original picture and copy into empty canvas
  #  (you will use a different picture)
  orig = makePicture (getMediaPath( "bigben.jpg"))
  
  # Create empty canvas, 2x width and 2x height of original
  #  (note that you'll use different numbers here to make a different sized canvas)
  canvas = makeEmptyPicture (getWidth(orig)*2, getHeight(orig)*2)
  
  copyInto (orig, canvas, 0, 0)
  
  # negative original (you don't have to use "negative", but you can)         
  negative (orig)
  copyInto (orig, canvas, getWidth(orig), 0)
  
  # other manipulations and copying go here, after you get our
  #   program working ....
    
  # mirror across horiz. axis
  #  (you don't have to use horizontal mirroring, but you can)
  mirrorHorizontal (canvas)

  # wrap up
  show (canvas)
  
               
createCollage()               