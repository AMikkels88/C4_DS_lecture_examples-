# For install : 
# pip install spacy
# python -m spacy download en_core_web_md

import spacy
from spacy import displacy

# Semantic Similarity
nlp = spacy.load('en_core_web_md')

complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]

print("-------------Complaints similarity---------------")
for token1 in complaints:
    token1 = nlp(token1)
    for token2 in complaints:
        token2 = nlp(token2)
        #print(token1.similarity(token2))


# Lemmatization, stop words, entity recognition
nlp = spacy.load("en_core_web_sm")

doc = nlp("The ABC company is looking at buying the XYZ startup for $1 billion.")

for token in doc:
    print(token.lemma_, token.is_stop)

for token in doc.ents:
    print(token, token.label_)

# stop words removal
text = "The quick brown fox jumps over the lazy dog."

doc = nlp(text)

filtered_text = ' '.join(token.text for token in doc if not token.is_stop)

print(filtered_text)

# Dependecy Parsing

# Noun chunks
doc = nlp("The big brown dog with floppy ears and a wagging tail chased the frisbee in the park on a sunny afternoon.")
for chunk in doc.noun_chunks:
    print(chunk.text)
