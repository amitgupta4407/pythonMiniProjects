from PIL import Image 
import os

# path= r""
src = r"D:\up-scaled_img\day4"
des_path = r"D:\stickers\cats"

def mj_split(des_path,img_path,img_name):
    img = Image.open(img_path)
    width, height = img.size
    center_x = width // 2
    center_y = height // 2
    # Crop the image into 4 quadrants
    top_left = img.crop((0, 0, center_x, center_y))
    top_right = img.crop((center_x, 0, width, center_y))
    bottom_left = img.crop((0, center_y, center_x, height))
    bottom_right = img.crop((center_x, center_y, width, height))
    # Save the cropped images
    top_left.save(des_path+"\\"+img_name+"(2).png")
    top_right.save(des_path+"\\"+img_name+"(1).png")
    bottom_left.save(des_path+"\\"+img_name+"(3).png")
    bottom_right.save(des_path+"\\"+img_name+"(4).png")
# mj_split(r"C:\Users\ek440\Desktop\code\gui_control\a_small_elite_bundle_of_red_rose_on_a_cheerful_cov2.png")

def batch_process(src_folder):
    for filename in os.listdir(src_folder):
        print(filename[10:-40])
        if filename.endswith((".png", ".jpg", ".jpeg")):
            mj_split(des_path,src_folder+"\\"+filename,filename[10:-40])
            # exit()
batch_process(src)