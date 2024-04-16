def decode_file(filepath):

    wordmap = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            count, word = line.split(' ', 1)
            count = int(count)
            wordmap.update({count: word})

    return wordmap


file_path = 'encoded_file.txt'
word_map = decode_file(file_path)
#print(word_map)
row = 1
last_num = 1
print("Decoded file is....")
while word_map.get(last_num) is not None:
    print(str(last_num) + " : " + word_map[last_num])
    row = row + 1
    last_num = last_num + row

