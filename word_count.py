machine_learning_count_length = open ("Machine_Learning.txt", "r")

text= machine_learning_count_length.read()

words= text.split()

print(len(words))

machine_learning_count_length.close()