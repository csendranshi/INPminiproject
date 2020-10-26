def huffman_encoding(my_string):
    letters = []
    only_letters = []
    for letter in my_string:
        if letter not in letters:
            freq = my_string.count(letter)
            letters.append(freq)
            letters.append(letter)
            only_letters.append(letter)

    nodes = []
    while len(letters) > 0:
        nodes.append(letters[0:2])
        letters = letters[2:]
    nodes.sort()
    huffman_tree = []
    huffman_tree.append(nodes)

    def combine(nodes):
        pos = 0
        newnode = []
        if len(nodes) > 1:
            nodes.sort()
            nodes[pos].append("0")
            nodes[pos + 1].append("1")
            combined_nodel = (nodes[pos][0] + nodes[pos + 1][0])
            combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])
            newnode.append(combined_nodel)
            newnode.append(combined_node2)
            newnodes = []
            newnodes.append(newnode)
            newnodes = newnodes + nodes[2:]
            nodes = newnodes
            huffman_tree.append(nodes)
            combine(nodes)
        return huffman_tree

    newnodes = combine(nodes)
    huffman_tree.sort(reverse=True)

    checklist = []
    for level in huffman_tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)

    letter_binary = []
    if len(only_letters) == 1:
        letter_code = [only_letters[0], "0"]
        letter_binary.append(letter_code * len(my_string))
    else:
        for letter in only_letters:
            lettercode = ""
            for node in checklist:
                if len(node) > 2 and letter in node[1]:
                    lettercode = lettercode + node[2]
            letter_code = [letter, lettercode]
            letter_binary.append(letter_code)

    bitstring = ""
    for character in my_string:
        for item in letter_binary:
            if character in item:
                bitstring = bitstring + item[1]
    # convert the string to an actual binary digit
    binary = (bin(int(bitstring, base=2)))
    # summary of data compression
    uncompressed_file_size = len(my_string) * 7
    compressed_file_size = len(binary) - 2
    print("Your original file-size was", uncompressed_file_size)
    print("This is a saving of ", uncompressed_file_size - compressed_file_size)
    return binary, letter_binary


def HuffmanDecoding(binary, letter_binary):
    bitstring = str(binary[2:])
    uncompressed_string = ""
    code = ""
    print(letter_binary)
    for digit in bitstring:
        code = code + digit
        pos = 0
        for letter in letter_binary:
            print(letter_binary)
            if code == letter[1]:
                uncompressed_string = uncompressed_string + letter_binary[pos][0]
                code = ""
            pos += 1
    return uncompressed_string
