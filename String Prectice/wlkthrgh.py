raw_input="  pyhton STRings are EASY to LEARN!"
clear_text=raw_input.strip()
formatted_text=clear_text.title()

word_list=clear_text.split()
total_words=len(word_list)  # this will count word 

print("Formatted Text::", {formatted_text})
print("Total Word Count::", total_words)