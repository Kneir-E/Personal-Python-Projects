import random

if __name__ == '__main__':
    char_ref = ['`', '$', '#', '+', '!', '<', ')', '^', '@', '*', ';', '>', '%', '[', ']', '~', '|', '\\', '&', ':', '(', '?', "'", '.', '/', '=', '_', ',', '-', '"',  '7', '1', '6',  '5', '3', '0', '9', '2', '4', '8', '\n', ' ', 'm', 'a', 'd', 'e', 'l', 'y', 'p', 'k', 'o', 't', 'h', 'i', 'n', 'g', 'w', 'X', 'D', 'u', 'f', 'b', 'R', 'c', 'r', 's', 'H', 'G', 'F', 'x', 'W', 'I', 'N', 'Y', 'T', 'E', 'O', 'A', 'M', 'S', 'L', 'P', 'B', 'U', 'v', 'V', 'K', 'j', 'J', 'z', 'q', 'C', 'Z', 'Q'] 
    color_list = []
    for char in char_ref:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        data = (r, g, b)
        color_list.append(data)

    print(color_list)