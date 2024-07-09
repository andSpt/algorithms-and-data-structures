def my_hash(s, p, x):
    hash_value = 0
    for char in reversed(s):
        hash_value = (hash_value * x + ord(char)) % p
    return hash_value


def my_rehash(text, pattern, p, x):
    pattern_length = len(pattern)
    text_length = len(text)
    hash_array = [0] * (text_length - pattern_length + 1)
    last_substring = text[text_length - pattern_length:]
    hash_array[text_length - pattern_length] = my_hash(last_substring, p, x)
    y = pow(x, pattern_length, p)
    for i in range(text_length - pattern_length - 1, -1, -1):
        hash_array[i] = (x * hash_array[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % p
    return hash_array


def rabin_karp(pattern, text):
    p = 1000000007
    x = 263
    result = []
    pattern_hash = my_hash(pattern, p, x)
    hash_array = my_rehash(text, pattern, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == hash_array[i] and text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def main():
    pattern = input()
    text = input()
    print(*rabin_karp(pattern, text))


if __name__ == "__main__":
    main()