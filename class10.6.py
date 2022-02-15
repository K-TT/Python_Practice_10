Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Activity 6.1
>>> import re
>>> import nltk
>>> tokens=re.split(' ',"I am testing re.split for class 10")
>>> print(tokens)
['I', 'am', 'testing', 're.split', 'for', 'class', '10']
>>> tagged=nltk.pos_tag(tokens)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tagged=nltk.pos_tag(tokens)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/__init__.py", line 165, in pos_tag
    tagger = _get_tagger(lang)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/__init__.py", line 107, in _get_tagger
    tagger = PerceptronTagger()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/perceptron.py", line 167, in __init__
    find("taggers/averaged_perceptron_tagger/" + PICKLE)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93maveraged_perceptron_tagger[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('averaged_perceptron_tagger')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtaggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickle[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

>>> nltk.download('averaged_perceptron_tagger')
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/kateryna/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
True
>>> tagged=nltk.pos_tag(tokens)
>>> print(tagged)
[('I', 'PRP'), ('am', 'VBP'), ('testing', 'VBG'), ('re.split', 'NN'), ('for', 'IN'), ('class', 'NN'), ('10', 'CD')]
>>> #Activity 6.2
>>> entities = nltk.chunk.ne_chunk(tagged)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    entities = nltk.chunk.ne_chunk(tagged)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/chunk/__init__.py", line 183, in ne_chunk
    chunker = load(chunker_pickle)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 750, in load
    opened_resource = _open(resource_url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 876, in _open
    return find(path_, path + [""]).open()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mmaxent_ne_chunker[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('maxent_ne_chunker')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mchunkers/maxent_ne_chunker/PY3/english_ace_multiclass.pickle[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************

>>> nltk.download('maxent_ne_chunker')
[nltk_data] Downloading package maxent_ne_chunker to
[nltk_data]     /Users/kateryna/nltk_data...
[nltk_data]   Unzipping chunkers/maxent_ne_chunker.zip.
True
>>> entities = nltk.chunk.ne_chunk(tagged)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('words')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/words.zip/words/[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    entities = nltk.chunk.ne_chunk(tagged)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/chunk/__init__.py", line 184, in ne_chunk
    return chunker.parse(tagged_tokens)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/chunk/named_entity.py", line 127, in parse
    tagged = self._tagger.tag(tokens)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/sequential.py", line 61, in tag
    tags.append(self.tag_one(tokens, i, tags))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/sequential.py", line 81, in tag_one
    tag = tagger.choose_tag(tokens, index, history)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/sequential.py", line 647, in choose_tag
    featureset = self.feature_detector(tokens, index, history)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tag/sequential.py", line 694, in feature_detector
    return self._feature_detector(tokens, index, history)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/chunk/named_entity.py", line 101, in _feature_detector
    "en-wordlist": (word in self._english_wordlist()),
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/chunk/named_entity.py", line 52, in _english_wordlist
    self._en_wordlist = set(words.words("en-basic"))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 121, in __getattr__
    self.__load()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 86, in __load
    raise e
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('words')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/words[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

>>> nltk.download('words')
[nltk_data] Downloading package words to /Users/kateryna/nltk_data...
[nltk_data]   Unzipping corpora/words.zip.
True
>>> entities = nltk.chunk.ne_chunk(tagged)
>>> print(entities)
(S I/PRP am/VBP testing/VBG re.split/NN for/IN class/NN 10/CD)
 #Activity 6.3                                       
>>> from nltk.corpus import treebank
>>> t = treebank.parsed_sents('wsj_0001.mrg')[0]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mtreebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/treebank.zip/treebank/combined/[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t = treebank.parsed_sents('wsj_0001.mrg')[0]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 121, in __getattr__
    self.__load()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 86, in __load
    raise e
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mtreebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/treebank/combined[0m

  Searched in:
    - '/Users/kateryna/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

>>> nltk.download('treebank')
[nltk_data] Downloading package treebank to
[nltk_data]     /Users/kateryna/nltk_data...
[nltk_data]   Unzipping corpora/treebank.zip.
True
>>> t = treebank.parsed_sents('wsj_0001.mrg')[0]
>>> t.draw()
>>> 
