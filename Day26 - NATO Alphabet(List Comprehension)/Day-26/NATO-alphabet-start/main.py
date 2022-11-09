student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Creating a dictionary using dictionary comprehension from csv:
# keys are the letters and values are code words
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


# Function creates a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    # using exception for key errors in case user doesn't enter a valid word
    try:
        new_list = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        # if word not valid, function called again so user enters another word
        generate_phonetic()
    else:
        print(new_list)

# once line read will call function definition just above
generate_phonetic()