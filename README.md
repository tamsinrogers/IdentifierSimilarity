# IdentifierSimilarity

IdentifierSimilarity is an extension of _Namesake: A Checker of Lexical Similarity in Identifier Names_.  In this project, Namesake is used to "score" identifiers for similarity against each other in order to further assess lexical similarity in code and the impact of this similarity on the level of ease developers have debugging code in a survey setting.

Namesake is an open-source tool for assessing confusing naming combinations in Python programs.
Namesake flags confusing identifier naming combinations that are similar in:
* orthography (word form)
* phonology (pronunciation)
* or semantics (meaning)


## 💡 What is Lexical Similarity in Code?
Lexical access describes the retrieval of word shape (orthography), pronunciation (phonology), and meaning (semantics) from memory during reading for comprehension. 


**Orthographic similarity** focuses on the the similarity in word form on the level of letters. Not to be confused by editing distance or Levenshtein's distance, where one letter is replaced by another, orthographic similarity focuses on the similarities between letters shapes.  A good example is the confusion between 'O' and 'C' as individual letters or within words and sentences. Here's a common example in code:

<p align="center">
  <img width="429" alt="Screenshot 2024-08-13 at 10 11 37 AM" src="https://github.com/user-attachments/assets/344edd80-9f80-4b0f-b8de-4bb1b7a26f59">
</p>

Survery participants were presented either code snippet A (left), which contains the orthographically dissimilar identifiers "l" and "u" or code snippet B (right), which contains the orthographically similar identifiers "x" and "y".

<p align="center">
<img width="300" alt="Screenshot 2024-08-13 at 10 17 01 AM" src="https://github.com/user-attachments/assets/fe164b0e-4402-4af0-985b-c1b2d0a9e3de">
<img width="300" alt="Screenshot 2024-08-13 at 10 18 43 AM" src="https://github.com/user-attachments/assets/a61710f5-ef77-4d81-a0c5-f733b01996c7">
</p>

**Phonological similarity** describes two words that share a similar or identical pronunciation, also known as homophones:


<p align="center">
  <img width="423" alt="Screenshot 2024-08-13 at 10 12 00 AM" src="https://github.com/user-attachments/assets/18f02dfd-9ecb-47b7-a8c2-0343d444dcb4">
</p>

Survery participants were presented either code snippet A (left), which contains the phonologically dissimilar identifiers "pt" and "err" or code snippet B (right), which contains the phonologically similar identifiers "pare" and "pair".

<p align="center">
<img width="300" alt="Screenshot 2024-08-13 at 10 19 22 AM" src="https://github.com/user-attachments/assets/e4a1c697-f70d-4a8e-a75f-23e77f96ad54">
<img width="325" alt="Screenshot 2024-08-13 at 10 19 51 AM" src="https://github.com/user-attachments/assets/6a0a0cad-cf9a-478d-8762-7a7e96e3296f">
</p>


**Semantic similarity** describes words that share a meaning (synonyms):


<p align="center">
  <img width="425" alt="Screenshot 2024-08-13 at 10 12 16 AM" src="https://github.com/user-attachments/assets/3ff87042-7c66-47d5-a058-d8870384fc0b">
</p>

Survery participants were presented either code snippet A (left), which contains the semantically dissimilar identifiers "element" and "var" or code snippet B (right), which contains the semantically similar identifiers "short_string" and "little_string".

<p align="center">
<img width="300" alt="Screenshot 2024-08-13 at 10 22 47 AM" src="https://github.com/user-attachments/assets/08c192a1-25f7-4514-8182-bf357c9aeef8">
<img width="300" alt="Screenshot 2024-08-13 at 10 23 05 AM" src="https://github.com/user-attachments/assets/863cefcb-b40f-44f2-bc09-b5677cfe1ae5">
</p>

* Note that there are 4 different potential code snippet versions of each similarity genre available to be presented to any given participant in the survey.

## ❓ How are Identifiers Scored for Similarity?
Identifier pairs are awarded a score 0-100 based on how similar they are in an orthographic (look), phonological (sound), or semantic (meaning), basis.

An example of scoring for phonological similarity, using the International Phonetic Alphabet (IPA) to find the most similar IPA of out-of-vocabulary and IPA of in-vocabulary words.
<p align="center">
<img width="611" alt="Screenshot 2024-08-13 at 10 36 32 AM" src="https://github.com/user-attachments/assets/8a91df61-bae9-4577-ba96-ed46f5f582f2">
</p>

This below output is an example of a Namesake warning that two identifiers within a code snippet are similar.  
<p align="center">
<img width="300" alt="Screenshot 2024-08-13 at 10 36 10 AM" src="https://github.com/user-attachments/assets/8c53a7e0-a0d4-43c8-b547-f15e37747f9a">
</p>

  ## 📊 Results
Using buggy code snippets containing commonly-confused identifiers, we assessed the debugging ability of programmers as follows:

<p align="center">
<img width="500" alt="Screenshot 2024-08-13 at 10 16 19 AM" src="https://github.com/user-attachments/assets/76dbae27-7394-4209-9865-e1810d1a2fc7">
<img width="500" alt="Screenshot 2024-08-13 at 10 16 40 AM" src="https://github.com/user-attachments/assets/5687146c-aaf8-43b1-b86c-8eda8a59d650">
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
