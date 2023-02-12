import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "Mary gave the child the dog bit a Band-Aid.",
    "Helen is expecting tomorrow to be a bad day.",
    "She told me a little white lie will come back to haunt me first.",
    "The Inuit can fish in their new factory in town.",
    "The cotton clothing is made of grows in Mississippi."
]

## for each sentence in "gardenpathSentences" array/list
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print([(i, i.label_, i.label) for i in nlp_sentence.ents])

## Notes:
## NORP = I wasn't expecting an abbreviation of words
## ORDINAL = I wasn't expecting this word.
