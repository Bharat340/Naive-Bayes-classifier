import sys, time, string, re

start_time = time.time()
# training_filepath = sys.argv[1]
training_filepath = "train-labeled.txt" #"train_debug.txt"
training_file = open(training_filepath, "r")
training_data = training_file.read()
# stop_words = ["all", "just", "don't", "being", "over", "both", "through", "yourselves", "its", "before", "o", "don", "hadn", "herself", "ll", "had", "should", "to", "only", "won", "under", "ours", "has", "should've", "haven't", "do", "them", "his", "very", "you've", "they", "not", "during", "now", "him", "nor", "wasn't", "d", "did", "didn", "this", "she", "each", "further", "won't", "where", "mustn't", "isn't", "few", "because", "you'd", "doing", "some", "hasn", "hasn't", "are", "our", "ourselves", "out", "what", "for", "needn't", "below", "re", "does", "shouldn't", "above", "between", "mustn", "t", "be", "we", "who", "mightn't", "doesn't", "were", "here", "shouldn", "hers", "aren't", "by", "on", "about", "couldn", "of", "wouldn't", "against", "s", "isn", "or", "own", "into", "yourself", "down", "hadn't", "mightn", "couldn't", "wasn", "your", "you're", "from", "her", "their", "aren", "it's", "there", "been", "whom", "too", "wouldn", "themselves", "weren", "was", "until", "more", "himself", "that", "didn't", "but", "that'll", "with", "than", "those", "he", "me", "myself", "ma", "weren't", "these", "up", "will", "while", "ain", "can", "theirs", "my", "and", "ve", "then", "is", "am", "it", "doesn", "an", "as", "itself", "at", "have", "in", "any", "if", "again", "no", "when", "same", "how", "other", "which", "you", "shan't", "shan", "needn", "haven", "after", "most", "such", "why", "a", "off", "i", "m", "yours", "you'll", "so", "y", "she's", "the", "having", "once"]
stop_words = ['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep\tkeeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure\tt', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', "we'll", 'went', 'were', 'werent', "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero']
stop_words = set(stop_words)
class1_probabilities = dict()
class2_probabilities = dict()
unique_words = set()
line_count, true_count, pos_count = 0, 0, 0
true_word_count, fake_word_count, pos_word_count, neg_word_count = 0, 0, 0, 0


def parse_input_file():
    global line_count, true_count, pos_count
    global true_word_count, fake_word_count, pos_word_count, neg_word_count
    for line in training_data.split("\n"):
        parts = line.split(" ", 3)
        if len(parts) < 4:
            continue
        line_count += 1
        class1 = parts[1]
        class2 = parts[2]
        sentence = parts[3].strip()
        sentence = re.sub(r'[^\w\s]', ' ', sentence).lower()
        sentence = sentence.split()
        sentence = [w for w in sentence if not w in stop_words]
        length = len(sentence)
        if "Pos" == class2:
            pos_count += 1
            pos_word_count += length
        else:
            neg_word_count += length
        if "True" == class1:
            true_count += 1
            true_word_count += length
        else:
            fake_word_count += length
        # sentence = sentence.translate(None, string.punctuation).lower()
        for word in sentence:
            unique_words.add(word)
            if (word, class1) in class1_probabilities:
                class1_probabilities[(word, class1)] += 1
            else:
                class1_probabilities[(word, class1)] = 1
            if (word, class2) in class2_probabilities:
                class2_probabilities[(word, class2)] += 1
            else:
                class2_probabilities[(word, class2)] = 1


def calculate_probabilities():
    global true_word_count, fake_word_count, pos_word_count, neg_word_count
    unique_words_count = len(unique_words)
    for key, value in class1_probabilities.iteritems():
        if "True" == key[1]:
            denominator = true_word_count + unique_words_count
        else:
            denominator = fake_word_count + unique_words_count
        class1_probabilities[key] = (value + 1) / float(denominator)

    for key, value in class2_probabilities.iteritems():
        if "Pos" == key[1]:
            denominator = pos_word_count + unique_words_count
        else:
            denominator = neg_word_count + unique_words_count
        class2_probabilities[key] = (value + 1) / float(denominator)


parse_input_file()
calculate_probabilities()
unique_words = list(unique_words)
training_file.close()

count = dict()
count["pos_word_count"] = pos_word_count
count["neg_word_count"] = neg_word_count
count["true_word_count"] = true_word_count
count["fake_word_count"] = fake_word_count
count["true_count"] = true_count
count["pos_count"] = pos_count
count["line_count"] = line_count

print len(unique_words), len(class1_probabilities), len(class2_probabilities), count

output_file = open("nbmodel.txt", "w")
output_file.write("Class1 probabilities\n")
output_file.write(repr(class1_probabilities) + "\n")
output_file.write("Class2 probabilities\n")
output_file.write(repr(class2_probabilities) + "\n")
output_file.write("Counts\n")
output_file.write(repr(count) + "\n")
output_file.write("Unique words\n")
output_file.write(repr(unique_words))
output_file.close()
