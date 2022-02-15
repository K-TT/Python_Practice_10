s = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
def word_freq(text):
   """ No use of NLTK yet
       Function to create a dictionary of word frequencies of the text
       - key is the word
       - value is the frequency (count) of the word in the text
    """
   dFreq={}
   for word in text.split():
        if word in dFreq:
            dFreq[word] += 1
        else:
            dFreq[word]=1
   return dFreq

if __name__ == "__main__":
    import pprint
    pprint.pprint(word_freq(s))
