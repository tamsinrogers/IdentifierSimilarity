# IdentifierSimilarity

IdentifierSimilarity is an extension of _Namesake: A Checker of Lexical Similarity in Identifier Names_.  In this project, Namesake is used to assess lexical similarity in code and the impact of this similarity on the level of ease developers have debugging code.

Namesake is an open-source tool for assessing confusing naming combinations in Python programs.
Namesake flags confusing identifier naming combinations that are similar in:
* orthography (word form)
* phonology (pronunciation)
* or semantics (meaning)

## 💡 What is Lexical Similarity in Code?
Lexical access describes the retrieval of word shape (orthography), pronunciation (phonology), and meaning (semantics) from memory during reading for comprehension. 


**Orthographic similarity** focuses on the the similarity in word form on the level of letters. Not to be confused by editing distance or Levenshtein's distance, where one letter is replaced by another, orthographic similarity focuses on the similarities between letters shapes.  A good example is the confusion between 'O' and 'C' as individual letters or within words and sentences. Here's a common exmple in code:


<p align="center">
  <img width="400" height="360" src="/documentation/imgs/ortho_example.drawio.png">
</p>


**Phonological similarity** describes two words that share a similar or identical pronunciation, also known as homophones:


<p align="center">
  <img width="400" height="290" src="/documentation/imgs/real_phono.drawio.png">
</p>


**Semantic similarity** describes words that share a meaning (synonyms):


<p align="center">
  <img width="400" height="350" src="/documentation/imgs/semantic.drawio.png">
</p>



## ⚙️ Installing Namesake:
first, to install the requirements:

```sh
pip install -r requirements.txt
```

## 🚀 Running Namesake:
To run Namesake on the file test1.py (with optional similarity thresholds):

```sh
python namesake.py test1.py [orth_threshold] [phon_threshold] [sem_threshold]
```

Threshold values must be between 0 and 1.


## 👀 Example Running Namesake:
<p align="center">
  <img width="800" src="/documentation/imgs/demo-Namesake.png">
</p>

## 📝 Citation:
[Naser Al Madi. 2022. Namesake: A Checker of Lexical Similarity in Identifier
Names. In Proceedings of The 37th IEEE/ACM International Conference on
Automated Software Engineering Workshops (ASEW 2022).](https://www.researchgate.net/publication/363207604_Namesake_A_Checker_of_Lexical_Similarity_in_Identifier_Names)

## ⚖️ License:

 **MIT (Free Software, Hell Yeah!)**
