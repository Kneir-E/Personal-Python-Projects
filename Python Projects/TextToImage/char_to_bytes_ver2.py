
from PIL import Image

def calcHeightWidth(length):
    total_pixels=length
    
    aspect_ratio_width = 16
    aspect_ratio_height = 9

    # Calculate width and height
    width = int((total_pixels * aspect_ratio_width / (aspect_ratio_width + aspect_ratio_height)) ** 0.5)
    height = int(total_pixels / width)

    return width, height



def charToRGBA(data):
    char_ref = ['`', '$', '#', '+', '!', '<', ')', '^', '@', '*', ';', '>', '%', '[', ']', '~', '|', '\\', '&', ':', '(', '?', "'", '.', '/', '=', '_', ',', '-', '"',  '7', '1', '6',  '5', '3', '0', '9', '2', '4', '8', '\n', ' ', 'm', 'a', 'd', 'e', 'l', 'y', 'p', 'k', 'o', 't', 'h', 'i', 'n', 'g', 'w', 'X', 'D', 'u', 'f', 'b', 'R', 'c', 'r', 's', 'H', 'G', 'F', 'x', 'W', 'I', 'N', 'Y', 'T', 'E', 'O', 'A', 'M', 'S', 'L', 'P', 'B', 'U', 'v', 'V', 'K', 'j', 'J', 'z', 'q', 'C', 'Z', 'Q',
                 '{', '}'] 
    color_list = [(173, 197, 103), (144, 204, 228), (184, 139, 33), (232, 220, 74), (119, 114, 70), (140, 97, 155), (104, 113, 222), (143, 128, 251), (192, 59, 60), (92, 178, 232), (201, 133, 190), (20, 5, 51), (26, 27, 22), 
                    (41, 163, 242), (78, 89, 93), (245, 233, 23), (150, 149, 34), (59, 122, 199), (136, 195, 220), (132, 31, 168), (206, 178, 141), (189, 193, 30), (163, 39, 229), (58, 170, 251), (73, 100, 90), (95, 137, 62),
                    (117, 213, 25), (169, 247, 80), (68, 49, 68), (119, 131, 248), (157, 157, 33), (191, 1, 38), (56, 228, 144), (215, 93, 17), (8, 190, 153), (57, 123, 30), (140, 75, 240), (137, 197, 102), (38, 194, 23), 
                    (10, 180, 33), (69, 188, 186), (176, 18, 181), (6, 67, 110), (127, 18, 173), (96, 136, 48), (246, 203, 12), (197, 133, 198), (76, 151, 107), (21, 125, 60), (118, 223, 114), (217, 29, 4), (0, 153, 5), 
                    (40, 74, 242), (101, 66, 142), (68, 202, 158), (162, 199, 183), (166, 216, 111), (208, 106, 20), (59, 40, 93), (96, 211, 78), (220, 137, 5), (163, 164, 4), (123, 119, 147), (162, 47, 127), (237, 130, 75), 
                    (248, 54, 118), (156, 77, 222), (125, 114, 80), (65, 4, 1), (200, 32, 179), (143, 103, 170), (93, 80, 5), (128, 172, 253), (110, 33, 13), (93, 39, 85), (36, 226, 157), (21, 226, 9), (2, 166, 93), (245, 119, 15),
                    (51, 64, 204), (191, 83, 178), (31, 126, 32), (106, 130, 21), (15, 22, 173), (108, 251, 174), (247, 161, 219), (77, 193, 237), (37, 80, 234), (41, 101, 222), (31, 214, 96), (44, 221, 25), (89, 128, 105), 
                    (30, 32, 113), (105, 153, 33), (31, 175, 21), (221, 285, 73)]
    rgba_arr = []
    for char in data:
        rgba_arr.append( color_list[char_ref.index(char)] )

    return rgba_arr



if __name__ == '__main__':
    input_file_path = r'INPUTFILE_URL'

    with open(input_file_path, 'rt') as in_file:        #Load all the characters in the file
        data = in_file.read(-1)
        in_file.close()

    height, width = calcHeightWidth(len(data))          #Calculate the height and width to get as close as possible to 16:9

    rgba_arr = charToRGBA(data)                         #create RGBA data

    image = Image.new("RGB", (width, height+1))

    for i, pixel in enumerate(rgba_arr):
        x = i % width
        y = i // width
        image.putpixel((x, y), pixel)

    # Save the image as a PNG file
    image.save(r"OUTPUTFILE_URL")