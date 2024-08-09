def huffman_decode(code_table, encoded_string):
    decoded_string = ''
    current_code = ''
    for bit in encoded_string:
        current_code += bit
        if current_code in code_table:
            decoded_string += code_table[current_code]
            current_code = ''
    return decoded_string

def main():
    quantity_chars_into_string, size_encode_string = map(int, input().split())
    code_table = {}
    for _ in range(quantity_chars_into_string):
        letter, code = input().split(': ')
        code_table[code] = letter
    encoded_string = input()
    decoded_string = huffman_decode(code_table, encoded_string)
    print(decoded_string)

if __name__ == '__main__':
    main()
