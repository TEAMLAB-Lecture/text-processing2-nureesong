#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    digit_string = ''
    if input_string:
        string = input_string[:]
        for char in string:
            if char.isdigit():
                digit_string = digit_string + ' ' + words[int(char)]
                # print(digit_string)
        digit_string = digit_string.lstrip()
    
    return digit_string


def to_camel_case(underscore_str):
    string = underscore_str[:]
    string = string.strip('_')
    
    if string == '':
        camelcase_str = ''  # filtering '___' and ''
    else:
        if string.count('_') == 0:  # already Camel case
            camelcase_str = underscore_str[:]
        else:
            string_list = string.split('_')  # remove underscores in the middle
            camelcase_str = ''
            for word in string_list:
                if word:
                    camelcase_str = camelcase_str + word[0].upper() + word[1:].lower()
            camelcase_str = camelcase_str[0].lower() + camelcase_str[1:]
    
    return camelcase_str
