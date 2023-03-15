from rembg import remove
#py 3.10.9
import os
# input_path = r"D:\stickers\cats\2.5d_cat_pastel_color_white_background_vector_color_a_(1).png"
# output_path = r"D:\stickers\cats_transparent\2.5d_cat_pastel_color_white_background_vector_color_a_(1).png"

# with open(input_path, 'rb') as i:
#     with open(output_path, 'wb') as o:
#         input = i.read()
#         output = remove(input)
#         o.write(output)

src_path = r"D:\stickers\cats_2.2_up"
des_path = r"D:\stickers\cat_2.2_up_rmbg"
for filename in os.listdir(src_path):

    with open(src_path+"\\"+filename, 'rb') as i:
        new_name = filename[12:-40]+".png"
        with open(des_path+"\\"+new_name, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    print(filename[12:-40]+".png")
    # exit()
print("********************************************")