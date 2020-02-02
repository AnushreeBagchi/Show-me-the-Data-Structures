def get_freq(string):
    letters = []
    only_letters = []
    for char in string:
        if char not in letters:
            freq = string.count(char)
            letters.append(freq)
            letters.append(char)
            only_letters.append(char)
    return letters, only_letters

def get_leaf_nodes(letters):
    nodes = list()
    huffman_tree = list()
    while len(letters)> 1:
        nodes.append(letters[0:2])
        letters = letters[2:]
    nodes.sort()
    huffman_tree.append(nodes) 
    return huffman_tree, nodes

def get_huffman_tree(nodes, huffman_tree):
    new_node = []
    if len(nodes)> 1:
        nodes.sort() # to get the 2 nodes with lowest frequency
        nodes[0].append(0) #appending 0 for the left branch 
        nodes[1].append(1) #and 1 for right branch
        new_node.append(nodes[0][0]+ nodes[1][0])
        new_node.append(nodes[0][1]+ nodes[1][1])
        nodes = nodes[2:]
        nodes.append(new_node)
        nodes.sort()
        huffman_tree.append(nodes)
        get_huffman_tree(nodes, huffman_tree)
    return huffman_tree, nodes

def get_codes(huffman_tree, level, letter):
    checklist = [] # for flattening the tree
    for level in huffman_tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)
    code = ""
    for node in checklist:
        if letter in node[1]:
            if node[1] == letter:
                code += str(node[2])
                return code
            else:
                if len(node)>2:
                    code += str(node[2])
    return code


def huffman_tree_encoding(string):
    letters , only_letters = get_freq(string)
    huffman_tree, nodes = get_leaf_nodes(letters)
    huffman_tree, new_nodes = get_huffman_tree(nodes, huffman_tree)
    huffman_tree.sort(reverse = True)
    codes = ""
    codes_dict = dict()
    for letter in only_letters:
        code = get_codes(huffman_tree, 0, letter)
        codes_dict[letter] = code
    for char in string:
        codes += codes_dict[char]
    return codes, codes_dict

def huffman_tree_decoding(encoded_string, code_dict):
    decoded = ""
    code = ""
    for digit in encoded_string:
        code += digit
        for letter in code_dict:
            if code == code_dict[letter]:
                code = ""
                decoded += letter
    return decoded

def test1():
    input_string = "The bird is the word"
    encodes_codes, codes_dict = huffman_tree_encoding(input_string)
    print("Codes for each charaters in sentence = {}".format(codes_dict))

    decoded_string = huffman_tree_decoding(encodes_codes, codes_dict)
    print("Encoded string = {}".format(encodes_codes))
    print("Decoded string: {}".format(decoded_string))

    print("Pass" if decoded_string == input_string else "Fail")
    print("Pass" if encodes_codes == "1110000100011011101010100111111001001111101010001000110101101101001111" else "Fail")
test1()

def test2():
    input_string = "She sells sea shells"
    encodes_codes, codes_dict = huffman_tree_encoding(input_string)
    print("Codes for each charaters in sentence = {}".format(codes_dict))

    decoded_string = huffman_tree_decoding(encodes_codes, codes_dict)
    print("Encoded string = {}".format(encodes_codes))
    print("Decoded string: {}".format(decoded_string))

    print("Pass" if decoded_string == input_string else "Fail")
    print("Pass" if encodes_codes == "11100111100110100001011011010001110111010111100010110" else "Fail")
test2()

def test3(): # edge case when input string is not provided
    input_string  = ""
    encodes_codes, codes_dict = huffman_tree_encoding(input_string)
    decoded_string = huffman_tree_decoding(encodes_codes, codes_dict)

    print("Pass" if decoded_string == input_string else "Fail")
    print("Pass" if encodes_codes == "" else "Fail")
test3()


