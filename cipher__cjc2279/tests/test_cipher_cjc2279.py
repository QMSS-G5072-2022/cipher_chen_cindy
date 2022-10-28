from cipher_cjc2279 import __version__
from cipher_cjc2279 import cipher_cjc2279

def test_version():
    assert __version__ == 0.1.0


# def cipher(text, shift, encrypt=True):
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     new_text = ''

#     assert type(shift) == int, "shift cannot be a string input"

#     for c in text:
#         index = alphabet.find(c)
#         if index == -1:
#             new_text += c
#         else:
#             new_index = index + shift if encrypt == True else index - shift
#             new_index %= len(alphabet)
#             new_text += alphabet[new_index:new_index+1]
#     return new_text

# def test_cipher_function():
#     assert cipher("wallaby", 26) == "WALLABY", "cipher() function doesn't work correctly"