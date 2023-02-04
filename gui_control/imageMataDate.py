from PIL import Image
from PIL.ExifTags import TAGS
 
# open the image
image = Image.open("a_small_elite_bundle_of_red_rose_on_a_cheerful_cov2.png")
# print(image)
# extracting the exif metadata
exifdata = image.getexif()
# print("5444444444123")
# looping through all the tags present in exifdata
for tagid in exifdata:
     
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)
 
    # passing the tagid to get its respective value
    value = exifdata.get(tagid)
   
    # printing the final result
    print(f"{tagname:25}: {value}")