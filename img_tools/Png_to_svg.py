# !pip install aspose-words 
# py 3.10.9

import aspose.words as aw

#  Create document object
doc = aw.Document()

# Create a document builder object
builder = aw.DocumentBuilder(doc)

# Load and insert PNG image
shape = builder.insert_image(r"C:\Users\ek440\Desktop\code\gui_control\person_transp_bckgrnd.png")

# Specify image save format as SVG
saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)

# Save image as SVG
shape.get_shape_renderer().save(r"D:\stickers\cats_transparent\logo_out.svg", saveOptions)