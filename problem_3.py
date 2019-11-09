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
    if(node == None):
        return
    
    char, freq, left, right = node
    left = trim_tree(left)
    right = trim_tree(right)
    
    return char, left, right

def get_char_codes(node, is_reverse=False, current_code="", char_codes=dict()):
    if(node == None):
        return
    
    char, left, right = node
    if(char != None):
        if is_reverse is False:
            char_codes[char] = current_code
            return
        
        char_codes[current_code] = char
        return

    get_char_codes(left, is_reverse, current_code + "0", char_codes)
    get_char_codes(right, is_reverse, current_code + "1", char_codes)
    
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
    char_codes = get_char_codes(tree, True)
    current_code = ""
    decoded_text = ""

    for bit in data:
        current_code += bit
        if(current_code in char_codes):
            char = char_codes[current_code]
            decoded_text += char
            current_code = ""

    return decoded_text

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))