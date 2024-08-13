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
  <img width="429" alt="Screenshot 2024-08-13 at 10 11 37 AM" src="https://github.com/user-attachments/assets/344edd80-9f80-4b0f-b8de-4bb1b7a26f59">
</p>


**Phonological similarity** describes two words that share a similar or identical pronunciation, also known as homophones:


<p align="center">
  <img width="423" alt="Screenshot 2024-08-13 at 10 12 00 AM" src="https://github.com/user-attachments/assets/18f02dfd-9ecb-47b7-a8c2-0343d444dcb4">
</p>


**Semantic similarity** describes words that share a meaning (synonyms):


<p align="center">
  <img width="425" alt="Screenshot 2024-08-13 at 10 12 16 AM" src="https://github.com/user-attachments/assets/3ff87042-7c66-47d5-a058-d8870384fc0b">
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
  <img width="820" alt="Screenshot 2024-08-13 at 10 12 31 AM" src="https://github.com/user-attachments/assets/3984e73c-5182-48c4-919c-4a87261a3005">
</p>

## 📝 Citation:
[Naser Al Madi. 2022. Namesake: A Checker of Lexical Similarity in Identifier
Names. In Proceedings of The 37th IEEE/ACM International Conference on
Automated Software Engineering Workshops (ASEW 2022).](https://www.researchgate.net/publication/363207604_Namesake_A_Checker_of_Lexical_Similarity_in_Identifier_Names)

## ⚖️ License:

 **MIT (Free Software, Hell Yeah!)**
