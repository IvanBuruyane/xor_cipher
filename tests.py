import pytest
from xor_cipher import *


class TestsXOREncryption:

    def test_xor_encrypt_function_works_properly(self) -> None:
        original_text = "Hit me baby one more time"
        key = "join"
        expected_encrypted_text = [34, 6, 29, 78, 7, 10, 73, 12, 11, 13, 16, 78, 5, 1, 12, 78, 7, 0, 27, 11, 74, 27, 0,
                                   3, 15]
        actual_encrypted_text = xor_encrypt(original_text, key)
        type_of_actual_encrypted_text = type(actual_encrypted_text)
        assert type_of_actual_encrypted_text is list, f"xor_encrypt function returned {type_of_actual_encrypted_text}," \
                                                      f"expected: list"
        assert actual_encrypted_text == expected_encrypted_text, f"xor_encrypt function returned: " \
                                                                 f"{actual_encrypted_text}, expected: " \
                                                                 f"{expected_encrypted_text}"

    def test_xor_decrypt_function_works_properly(self) -> None:
        encrypted_text = [44, 26, 4, 31, 73, 82, 48, 67, 17, 29, 8, 69, 27, 13, 67, 20, 19, 13, 12, 28, 87, 77, 91]
        key = "cutlery"
        expected_decrypted_text = "Oops, I did it again..."
        actual_decrypted_text = xor_decrypt(encrypted_text, key)
        type_of_actual_decrypted_text = type(actual_decrypted_text)
        assert type_of_actual_decrypted_text == str, f"xor_decrypt function returned {type_of_actual_decrypted_text}," \
                                                     f"expected: str"
        assert actual_decrypted_text == expected_decrypted_text, f"xor_decrypt function returned: " \
                                                                 f"{actual_decrypted_text}, expected: " \
                                                                 f"{expected_decrypted_text}"

    def test_xor_decrypt_from_xor_encrypt_works_properly(self) -> None:
        original_text = "just_random_text"
        key = "key"
        actual_result = xor_decrypt(xor_encrypt(original_text, key), key)
        assert actual_result == original_text, f"xor_decrypt returned: {actual_result}, expected: {original_text}"

    @pytest.mark.parametrize("text", [
        "It's October the third.",
        "I never imagined we’d end up like this.",
        "I can't hear you. I don't mean you. Nice to meet you. See you tomorrow.",
        "I felt that I should help her.",
        "Alex was supposed to be sterile, but they had been wrong about that.",
        "He had been taking care of her for nearly a year now.",
        "Why are you disappointed in me?",
        "Just then the man with the star came and stood before the Wizard.",
        "As they continued toward the house, he cleared his throat.",
        "Yet they honestly think there is no choice left.",
        "About this time I found out the use of a key.",
        "It is a little speech that I have written for him.",
        "After that other people brought water from a brook and sprinkled the earth.",
        "Let's go do the chores one last time before we leave.",
        "They had two adopted children already.",
        "I just got word that my father had a heart attack.",
        "She objected at first, but finally submitted.",
        "I am not saying we live in a utopia.",
        "That's what I say.",
        "He was the best loved of all our poets.",
        "There were sparks between them from the start.",
        "As always, he had been there when she needed him.",
        "Don't forget your manners.",
        "You would have said that was crazy.",
        "If there is not a new man, how can the new clothes be made to fit?",
        "I guess he's going to use it in his business.",
        "Suppose we each sing a song in turn.",
        "Speaking of which , where is Alex?",
        "Nature is hard to be overcome, but she must be overcome.",
        "He knew how to work with his hands."
    ])
    def test_is_there_common_english_words_positive(self, text) -> None:
        is_there_words = is_there_common_english_words(text)
        assert is_there_words, f"is_there_common_english_words function returned: {is_there_words} for the text:" \
                               f"{text}. Expected {not is_there_words}"

    def test_is_there_common_english_words_negative(self) -> None:
        text = "fjkafak 324234 )*)&$&# jkdk put it please lololo привет\n"
        is_there_words = is_there_common_english_words(text)
        assert not is_there_words, f"is_there_common_english_words function returned: {is_there_words} for the text:" \
                               f"{text}. Expected {not is_there_words}"

    def test_guess_key_function_works_properly(self) -> None:
        with open("cipher.txt", "r") as file:
            cipher_string = file.read()
            cipher_list = list(map(int, cipher_string.split(",")))
        possible_keys = guess_key(cipher_list, 3)
        assert len(possible_keys) == 1, f"guess_key function returned more than one key"
        with open("decrypted_cipher.txt", "r") as result_file:
            results = result_file.readlines()
        actual_key, actual_decrypted_text = possible_keys[0]
        expected_key, expected_decrypted_text = results
        expected_key = expected_key.strip("\n")
        assert actual_key == expected_key, f"guess_key function returned: '{actual_key}' key, expected: " \
                                           f"'{expected_key}' key"
        assert actual_decrypted_text == expected_decrypted_text, f"guess_key function returned following decrypted " \
                                                                 f"text:\n'{actual_decrypted_text}'\nExpected:\n" \
                                                                 f"'{expected_decrypted_text}'"


