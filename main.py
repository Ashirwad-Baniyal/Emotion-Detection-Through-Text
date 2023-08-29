# clearing the file
# 1.create a text file and read data from it
# 2.convert to lowercase
# 3.Remove punctuation.
import re
import emoji
import string
from collections import Counter
import matplotlib.pyplot as plt

def extract_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64f"  # emoticons
        u"\U0001F300-\U0001F5ff"  # symbols & pictographs
        u"\U0001F680-\U0001F6ff"  # transport & map symbols
        u"\U0001f1e0-\U0001f1ff"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.findall(text)


text = open("reviews.txt",encoding="utf-8").read()
emojis = extract_emoji(text)
print(emojis)

emoji_list = emojis
emoji_descriptions = []

for emoji_code in emoji_list:
    emoji_descriptions.append(emoji.demojize(emoji_code))

#print(emoji_descriptions)

emoji_list = emoji_descriptions
emojiToText = []

for emoji in emoji_list:
    emojiToText.append(emoji.replace(':','').replace('_',' '))

print(emojiToText)

text = open("reviews.txt", encoding="utf-8").read()

lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

with open('textfile.txt', 'r') as f:
    text = f.read()
    stop_words = text.split()


# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

final_words=final_words+emojiToText
#  If word is present -> Add the emotion to emotion_list
#  Finally count each emotion in the emotion list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
count = Counter(emotion_list)
print(count)

# Plotting emotions on the graph
fig, ax1 = plt.subplots()
print(fig,ax1)
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig('emotionGraph.png')
plt.show()

