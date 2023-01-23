# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# names = ["Alex", "De", "Souza", "Dave"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# import pandas as pd

# student_dict = {
#     "student" : ["Angela", "James", "Lily"],
#     "score" : [56, 76, 98]
# }

# student_df = pd.DataFrame(student_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(key)

# for (index, row) in student_df.iterrows():
#     print(index)
#     print(row.student)
#     print(row.score)

import pandas as pd

df = pd.read_csv("/home/beast/100Days/NATO_alphabet/nato_phonetic_alphabet.csv")
print(df)    

# {new_index : new_value for (index, row) in dataframe.iterrows()}
nato_dict = {row.letter : row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    name = input('What is your name?\n')
    try:
        nato_vername = [nato_dict[letter] for letter in name.upper().strip()]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(nato_vername)

generate_phonetic()