import sys, math, re, ast

model_file = open("nbmodel.txt", "r")
model_data = model_file.read().split("\n")
class1_probabilities = ast.literal_eval(model_data[1])
class2_probabilities = ast.literal_eval(model_data[3])
count = ast.literal_eval(model_data[5])
unique_words = ast.literal_eval(model_data[7])
unique_words = set(unique_words)
unique_words_count = len(unique_words)

pos_word_count = count["pos_word_count"]
neg_word_count = count["neg_word_count"]
true_word_count = count["true_word_count"]
fake_word_count = count["fake_word_count"]
true_count = count["true_count"]
pos_count = count["pos_count"]
line_count = count["line_count"]

testing_file_path = sys.argv[1]
# testing_file_path = "dev-text.txt" #"test_debug.txt" #
test_file = open(testing_file_path, "r")
test_data = test_file.read().split("\n")

output_data = list()


def process_each_line(identifier, sentence):
    sentence = sentence.split()
    true_probability = math.log(float(true_count) / line_count)
    fake_probability = math.log(float(line_count - true_count) / line_count)
    pos_probability = math.log(float(pos_count) / line_count)
    neg_probability = math.log(float(line_count - pos_count) / line_count)

    for word in sentence:
        if word not in unique_words:
            continue
        if (word, 'True') in class1_probabilities:
            true_probability += math.log(class1_probabilities[(word, 'True')])
        else:
            print word
            probability = 1 / float(true_word_count + unique_words_count)
            true_probability += math.log(probability)

        if (word, 'Fake') in class1_probabilities:
            fake_probability += math.log(class1_probabilities[(word, 'Fake')])
        else:
            probability = 1 / float(fake_word_count + unique_words_count)
            fake_probability += math.log(probability)

        if (word, 'Pos') in class2_probabilities:
            pos_probability += math.log(class2_probabilities[(word, 'Pos')])
        else:
            probability = 1 / float(pos_word_count + unique_words_count)
            pos_probability += math.log(probability)

        if (word, 'Neg') in class2_probabilities:
            neg_probability += math.log(class2_probabilities[(word, 'Neg')])
        else:
            probability = 1 / float(neg_word_count + unique_words_count)
            neg_probability += math.log(probability)
    # print true_probability, fake_probability, pos_probability, neg_probability
    class1 = "True" if true_probability >= fake_probability else "Fake"
    class2 = "Pos" if pos_probability >= neg_probability else "Neg"
    return identifier + " " + class1 + " " + class2


def parse_test_file():
    for line in test_data:
        parts = line.split(" ", 1)
        if len(parts) < 2:
            continue
        identifier = parts[0]
        sentence = re.sub(r'[^\w\s]', ' ', parts[1]).lower()
        output_data.append(process_each_line(identifier, sentence))


parse_test_file()
model_file.close()
output_file = open("nboutput.txt", "w")
for line in output_data:
    output_file.write(line + "\n")
output_file.close()


