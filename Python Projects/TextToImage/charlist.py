
if __name__ == '__main__':
    input_file_path = r'inputfile.txt'

    with open(input_file_path, 'rt') as in_file:
        data = in_file.read(-1)
        in_file.close()

    list = []
    for char in data:
        if(not (char in list)):
            list.append(char)
    
    print(list)
    print(len(list))