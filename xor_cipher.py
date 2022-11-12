import re
from itertools import permutations


def xor_encrypt(text: str, key: str) -> list:
    """Encrypt given text with given key using XOR cipher. Return list of ASCII codes of encrypted symbols"""
    # It is not specified in the task, but I assume that both text and key must be not empty strings
    if type(text) is not str or type(key) is not str or not text or not key:
        raise TypeError("Text and key must be non empty strings")
    text_length = len(text)
    key_length = len(key)
    output = []
    for i in range(text_length):
        output.append(ord(text[i]) ^ ord(key[i % key_length]))
    return output


def xor_decrypt(encrypted_text: list, key: str) -> str:
    """Decrypt given text with given key using XOR cipher. Return string that contains decrypted text"""
    # It is not specified in the task, but I assume that encrypted_text must be not empty list,
    # key must be not empty string
    if type(encrypted_text) is not list or not encrypted_text:
        raise TypeError("Encrypted text must be non empty list")
    if type(key) is not str or not key:
        raise TypeError("Key must be non empty string")
    text_length = len(encrypted_text)
    key_length = len(key)
    output_list = []
    for i in range(text_length):
        output_list.append(encrypted_text[i] ^ ord(key[i % key_length]))
    return "".join(list(map(chr, output_list)))


def guess_key(encrypted_text: list, key_size: int) -> list:
    """
    Try to decode given encrypted list of ASCII codes, assuming that key has certain length and original text
    is a usual English text. Return list of tuples, each tuple include key and text, decrypted with this key
    """
    allowed_text_codes = [i for i in range(32, 127)]  # it is my assumption, not really clear from the task
    allowed_key_codes = [i for i in range(97, 123)]
    # It is my assumption that the key includes only unique symbols
    possible_keys = permutations(allowed_key_codes, key_size)
    output = []
    for encrypted_key in possible_keys:
        decrypted_codes = []
        is_text_readable = True
        # The loop below is used to decode detect any forbidden symbol in the decrypted text as soon as possible
        # and instantly move to the next variant of the key
        for i in range(len(encrypted_text)):
            decrypted_symbol_code = encrypted_text[i] ^ encrypted_key[i % key_size]
            if decrypted_symbol_code not in allowed_text_codes:
                is_text_readable = False
                break
            decrypted_codes.append(decrypted_symbol_code)
        if not is_text_readable:
            continue
        text = "".join(list(map(chr, decrypted_codes)))
        key = "".join(list(map(chr, encrypted_key)))
        if is_there_common_english_words(text):
            output.append((key, text))
    return output


def is_there_common_english_words(text: str) -> bool:
    """
    Check is text includes common at least on of the 30 most common English words, consists of more than 2 letters.
    Return True if text includes at least one word, otherwise False
    """
    common_english_words = ["the", "end", "you", "that", "was", "for", "are", "with", "his", "they", "this", "have",
                            "from", "one", "had", "word", "but", "not", "what", "all", "were", "when", "your", "said",
                            "there", "use", "each", "which", "she", "how"]
    for word in common_english_words:
        if re.findall(f" {word} ", text):
            return True
    return False
