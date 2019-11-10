import sys

def get_char_freq(data):
    res = {} 
    for char in data: 
        res[char] = res.get(char, 0) + 1
    return res

def get_min_idx(char_list):
    idx, _ = min(enumerate(char_list), key=lambda tup: tup[1][1])
    return idx

def trim_tree(node):
    if node == None:
        return
    
    char, freq, left, right = node
    left = trim_tree(left)
    right = trim_tree(right)
    
    return char, left, right

def get_char_codes(node, is_reverse=False, current_code=""):
    char_codes = dict()

    if node is None:
        return char_codes
    else:
        char, left, right = node
        if char is not None:
            current_code = "0" if len(current_code) == 0 else current_code
            if is_reverse is False:
                char_codes[char] = current_code
            else:
                char_codes[current_code] = char
            
            return char_codes

        char_codes.update(get_char_codes(left, is_reverse, current_code + "0"))
        char_codes.update(get_char_codes(right, is_reverse, current_code + "1"))

    return char_codes

def get_encoded_text(text, char_codes):
    encoded_text = ""
    for char in text:
        encoded_text += char_codes[char]
    return encoded_text

def huffman_encoding(data):
    # Find the frequency
    # Order the frequency
    # Add up the lowest frequency
    if not data or not isinstance(data, str):
        return 'Invalid data!', None

    char_freq = get_char_freq(data)
    char_list = [(char, freq, None, None) for char, freq in char_freq.items()]
    char_list.sort(key=lambda tup: tup[1])
    
    while len(char_list) > 1:
        n1 = char_list.pop(get_min_idx(char_list))
        n2 = char_list.pop(get_min_idx(char_list))
        c1, f1, l1, r1 = n1
        c2, f2, l2, r2 = n2
        node = (None, f1+f2, n1, n2)
        char_list.append(node)
        
    root = char_list.pop()
    tree = trim_tree(root)
    char_codes = get_char_codes(tree)
    encoded_text = get_encoded_text(data, char_codes)

    return encoded_text, tree

def huffman_decoding(data, tree):
    if data is None or len(data) == 0:
        return None

    char_codes = get_char_codes(tree, True)
    current_code = ""
    decoded_text = ""

    for bit in data:
        current_code += bit
        if current_code in char_codes:
            char = char_codes[current_code]
            decoded_text += char
            current_code = ""

    return decoded_text

# Test case 1

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))

# Expected: 0110111011111100111000001010110000100011010011110111111010101011001010
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

# Expected: The bird is the word
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 2

encoded_data, tree = huffman_encoding(None)

# Expected: None because there's no input in the first place
print ("The content of the encoded data is: {}\n".format(encoded_data))

encoded_data, tree = huffman_encoding("S")
# Expected: 0 because it's only a single text and it cannot do the halving
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

# Expected: S
print ("The content of the encoded data is: {}\n".format(decoded_data))

encoded_data, tree = huffman_encoding("aaaaa")
# Expected: 00000 because it's only a single text and it cannot do the halving and it's just a repitition of the codes
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

# Expected: aaaaa
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 3

a_massive_input = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

print ("The size of the data is: {}\n".format(sys.getsizeof(a_massive_input)))
print ("The content of the data is: {}\n".format(a_massive_input))

encoded_data, tree = huffman_encoding(a_massive_input)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
# Expected: 11010101001111011000011011110110011001011010010000110111101111010111101001110110100101101101001111111001001000011010110110011111111000001101010011100111001111010111111100010010001110010111011011110001100011110001011101110101100010010111110010011100101000101000011001100011110001011101110111100010010010001010110011011100111011000111111010101001111011000011011110110011001011010010000110111101001010110101110010010000001000111110001001000111011110001001001000101011001101110011110011001101011110101100010110001001001011101110010111100100100001101011011001111111100000110101001110011100011010000001101111110100111100010111100011111000100100011101100001001100100100110000001100000101010011011111101001010010001000111010110001110100010000010001000001111010011000111001011101101111000110000011011111110000110011001000111010111110111001011011010110000100111111001111010111111100100111001010001110101100010010111101010111111011010101101001001101100001001011101111100111110000111110110101010010000001110101111110010011100101000111101000101000101111011101101000100011100100100110011001000011000111101100111100111010010101101011110100100011011110100001111101000000100101111000001111001110011100010110100111111110101101111101000000111101111000100011000100011011011100010101001101111001001010001100111010110110101000111111100010010001111011000001010010111101111000110000111110001011000010111111001101100111000011110111111111001001110010100010100001100110001111000101110100110111111011000011010101011110000111100010111011100010101010000100011000111010110110101101001111110100010001011110100101011000101110000100100110001111011001111001111101001010110101110010100110010101000101100101110110111101000010010111011110001111100010010001110110000100110010011011001010001100000101011111010010111110001001111110001001000111110110001011000001011010000111001111010111111101010100011001101101011010000110011110100100100000011001010111101111001110001100010101111000011110001011101111101010100111101100001101111011001100101101001000011011110010101011010101001011011100001010100110111101011000100101110110100111101100011111011000101111000100011001011010011111111010010111110001001111100100001010001000110000110010111100101010000010011011001111010010010111100010111011110100011110101111001101001010111011000111101100111001000000111011001010110110100100100010101110110010110010110111000001100001101010010000001101111101111000101111101100100010010011110001011101111101000000110111010011100111000101011100111101011111110101010011110110000110111101100110010110100100001101011000111101100111100111011110101110101111101100011100010111011100010101100010100100110110011110100100100010010111110101101011011111100111110001001010111001110101111110110000101100100001101111111010010111101101011011100100100011110010011110101100110110101101111110000010010111001001100111111110001001000111110110000101100100101001001101100001111011110011100011000001000110011100111101011111010111100101010110111000011111010010100100010001111011000110011001000011110001011101110101110011101111100101011110110010110011100110100011000110001111011001011101001000111001010011011110001100111001111010111110100010100111100010111011111010101001111011000011011110110011001011010010000110111101111010111110001001010111001110111110011101001010110101110101111011010011110110000110010000011110110110010001011000010101010111100000111101101101010110110111100100111101011001101101110010010100011000111001110001110011110101111110110000110011000001101110101001101111010110101110011001010010100111010000100101111100001111101000101001111000101110111100110011001100000001110001100000100011001110100100011011000100110111110111100111000110000010001100111010010001101100010011001100110111101101010100100001111000101110111011111001111011000110011001000111101100111001000000111110110000101100100101001001101100001111001100001100010111010110011110100100101100011110110000110101100010011111110010000101000100011000011001011110010101000001001101100111101001001011110001011101110010101011011110010000101101110000101011101011000100101111101001000001001111001010101101110000111000100100111110000111101110101111000001111010011110100010100001111101010100111101100001101111011001100101101001000011011110101101011111000100100001111101111110010000110101101010100010110110011101101001110010000101101111100000110101001110010011011110101100010010111010111110100000101110111011110100111111010110011110111111001100110110001111011000011011110111001011010010000110110011001111110100101111011010110111010001000101111001111010000001101111101101010110001001111111101001000001001111101001111100000101011110101100011110110101101110111100011111000100100001111101111101111000110101101011000101111100111011000111110011000100101110110111001101000101011111010000001101110100111001110001010111010010101110100000011100011010000011101101101000000100101110011110100000011011111110001001000111100111000010111011101010011011111010001101101000110001110110100010101110010011001111110101101111101111011110010000100011001001101111101000110110100011000111011010001010111001110001110010101000110110010100111010000111100110001101111000110101000000010111111000001001011101001010000110100110100011011111010110001001011111000100100011110110011100100000011010100010110001
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

# Expected: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Expected: True
print ("Is it the same? {}\n".format(a_massive_input == decoded_data))

# Test case 4

encoded_data, tree = huffman_encoding(123)
# Expected: Invalid data! because it's expecting a string
print ("The content of the encoded data is: {}\n".format(encoded_data))