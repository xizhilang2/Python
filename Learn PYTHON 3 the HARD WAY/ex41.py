import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "calss %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef _init_(self, ***)":
      "class %%% has-a _init_ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    print(snippet, '\n',class_names)
    other_names = random.sample(WORDS, snippet.count("***"))
    print(other_names)
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        print("result: ", result)

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
        print("results: ",results)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        # 只返回PHRASES的键值，也就是。。。“：”之前的部分
        snippets = list(PHRASES.keys())
        # print(snippets)
        # 打乱snippets内容顺序，其实也就是4个键值重排序
        random.shuffle(snippets)

        for snippet in snippets:
            # 好了，现在根据打乱后的键值取出对应的内容
            phrase = PHRASES[snippet]
            # 这个程序。。。简直就是骗子。。。后续的输入一点用都没有。。。就是不停的再随机展现从字典中抽取
            # 出来的单子加入到写好的展现模板中去。
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
