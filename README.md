# Title: Ideas for Project

## Abstract
*A max 150-word description of the project question or idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?*

We came up with four ideas for the project, which explore the text in very different directions.

The first option analyses a dataset containing information about executed inmates and their last statements, which we would like to focus on. We are interested in detecting sentiment and emotional patterns in these final statements to explore expressions of regret. For further analysis, we also thought about including the amount of years between the verdict and execution and country to see how they could possibly correlate.

The second option is analyzing non-contextual English jokes (plain jokes, which are linguistically made to be funny) to find out what makes it good and funny. We wanted to explore whether there are any general patterns that allow identifying something as funny, but also analyse the emotional tones and forms. We thought about building a classifier which would, based on our findings, identify jokes within a larger dataset.

We had two ideas for the dataset that has the Wikibooks:

The first idea is to look at three languages: one that constructs words by concatenating them e.g. German or Dutch, one would be English, and the last one would be a language with is not that similar to the other ones e.g French or Spanish (they are in another family of languages than German and English). The goal of our project would be then to compare the translation for the first language into English and the third language into English. We would look at how the difference in word formation would influence the translation of those languages into English.

The second idea is to take languages which are written in another alphabet than English, such as Russian, Japanese or Hebrew, and analyze does and how the alphabet influences the quality of the translation.

## Research questions
*A list of research questions you would like to address during the project. *

1. What are the dominant emotional tones expressed in the final statements, and can they be useful in detecting regret?

2. Are there any structural, linguistic and emotional features that allow to define jokes as funny, and detect them in larger datasets?

3. How do word formation patterns in different languages influence the way they are translated into English?

4. How do different alphabets influence the quality of translation?

## Dataset
*List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show you've read the docs and are familiar with some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.*

Death Row:  https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html

200k Plaintext English Jokes: https://github.com/taivop/joke-dataset

Wikibooks in 12 Languages: https://www.kaggle.com/datasets/dhruvildave/wikibooks-dataset

## A tentative list of milestones for the project
*Add here a sketch of your planning for the coming weeks. Please mention who does what.*

## Documentation
*This can be added as the project unfolds. You should describe, in particular, what your repo contains and how to reproduce your results.*