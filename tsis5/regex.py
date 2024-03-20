#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

s = 'a+b abb abbb abbbb'

reg = re.compile('ab{2,3}')
result = reg.findall(s)
print(result)

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'
import re

s = 'a+b abb abbb abbbb'

reg = re.compile('ab*')
result = reg.findall(s)
print(result)

#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

s = 'abc_def 123_abc abc_def_ghi abc123_def abc'

reg = re.compile('[a-z]+_[a-z]+')
result = reg.findall(s)
print(result)


#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

s = 'Hello World OpenAI PythonProgramming GPT aBc ABCD AbCdEf'

reg = re.compile('[A-Z][a-z]+')
result = reg.findall(s)
print(result)

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

strings = ('abcdb', 'axb', 'ab', 'yyffhb', 'a123b', 'a_b', 'xyzabcdc')

reg = re.compile('a.+b$')
results = []
for s in strings:
    result = reg.findall(s)
    results.extend(result)
print(results)

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

s = 'abcdb axb ab yyffhb a123b a_b xyzabcdc'

reg = re.compile(r'[ ,.]')
result = reg.sub(':', s)
print(result)

#Write a python program to convert snake case string to camel case string
import re

def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0]
    for word in words[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string

snake_case_input = 'hello_world_how_are_you'
camel_case_output = snake_to_camel(snake_case_input)
print(f'Snake Case Input: {snake_case_input}')
print(f'Camel Case Output: {camel_case_output}')

#Write a Python program to split a string at uppercase letters
import re

def split_at_uppercase(string):
    words = re.findall('[A-Z][a-z]*', string)
    return words

input_string = 'SplitThisStringAtUpperCaseLetters'
result = split_at_uppercase(input_string)
print(result)

#Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return modified_string

input_string = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'
result = insert_spaces(input_string)
print(result)

#Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string

camel_case_input = 'convertThisCamelCaseStringToSnakeCase'
snake_case_output = camel_to_snake(camel_case_input)
print(snake_case_output)

