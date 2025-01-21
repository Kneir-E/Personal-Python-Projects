
def extract_content(input_file_path, output_file_path):
    with open (input_file_path, 'rt') as in_file, open(output_file_path, 'at') as out_file:
        lines = in_file.readlines()
        lines = lines[::-1]
        for line in lines:
            line = line.lstrip(' ')
            if line.startswith('"content": '): 
                out_file.write(line[len('"content": "'):(len(line)-3)] + '\n')
        in_file.close()
        out_file.close()

if __name__ == '__main__':
    output_file_path = r'OutputFilePath'

    input_file_path = r'InputFilePath'
    extract_content(input_file_path, output_file_path)

    print('done')

