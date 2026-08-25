input_str='''Hello! "Now's &"'''
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*'''
str=input(str)

cleaned_str = ""
for char in input_str:
    if char not in punctuation:
        cleaned_str += char
print(f"String of the input_str", {input_str})
print(f"String after removing the punctuation", {cleaned_str})