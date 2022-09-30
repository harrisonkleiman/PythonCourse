# Assignment 1:

import sys
import os
import re

# directory_containing_files = "/Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:

# 1. Create a dictionary to store the words and their counts

word_count = {}

# 2. Loop through the files in the directory

for file in os.listdir(directory_containing_files):

# 3. Open each file

    with open(os.path.join(directory_containing_files, file), "r") as f:
# 4. Read the contents of the file

        contents = f.read()
# 5. Split the contents of the file into a list of words

        words = contents.split()
#6. Lopp through the words in the list

        for word in words:
            
# 7. Check if the word is in the dictionary

            if word in word_count:
# 8. If the word is in the dictionary, increment the count

                word_count[word] += 1
# 9. If the word is not in the dictionary, add it to the dictionary with a count of 1
    
            else:
                word_count[word] = 1
# 10. Print the dictionary

print(word_count)


# 11. Run the program from the command line

# 12. Test the program with the following command:

# python3 assignment_01.py /Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files hello Peter computer















































#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)