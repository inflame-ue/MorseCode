# imports
from morse_dict import morse_code_dict


# function block
def text_to_morse_code(text: str) -> str:
    """
    Converts any text into morse code
    :param text: 26 latin letters(lower of upper, doesn't matter), arabic numbers and some symbols - in a string format
    :return: converted to morse code text
    """
    # convert string to list
    list_of_characters = list(text)

    # convert each character to its correlated character in morse code
    morse_code = [morse_code_dict[char.upper()] for char in list_of_characters]

    # return the result
    return "".join(morse_code)


# run config
if __name__ == "__main__":
    # take user input
    user_input = input("Input data for conversion into morse code:\n")

    # get the morse code
    print(f"Here's you morse code: \n{text_to_morse_code(text=user_input)}")
