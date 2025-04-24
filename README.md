## Abstract
*A max 150-word description of the project question or idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?*

We want to make a recommender which will recommend courses based on the classes a student has taken in the previous semesters (at least 2 semesters are required). We are thinking of excluding the academic core courses, as they will most likely act as noise as every student has to take them. In order to make this recommender, we will gather the data of all the courses which are in the UvA course catalogue. We are also thinking about including a feature in which the user can input their major, which gives more weight to courses from this major. To do this we need to annotate the corpus ourselves, as the major of each UvA course is not explicitly stated.

The reason for us choosing this for our project is due to our own difficulties with creating a study plan when coming into our second year of AUC. As AUC is unique in that you get to create your own study plan, we often found ourselves overwhelmed given the sheer amount of UvA courses available at our fingertips. We think that having a recommender could helps students avoid taking unnecessary courses by showing them courses they did not even know were available. 

## Research questions
We are currently unsure how to structure a research question for this project. 

## Dataset
*List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show you've read the docs and are familiar with some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.*

The dataset will be the UvA course catalogue: https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course

We will create the dataset ourselves by scraping the website for all 3804 courses. The features we will be capturing initially are:
- Course catalogue number
- Course description
- Credits
- Language of Instruction
- College/graduae
- Is part of

After this we hope to manually annotate the corpus by the three AUC majors: Sciences, Humanities, and Social Sciences. 

## A tentative list of milestones for the project
*Add here a sketch of your planning for the coming weeks. Please mention who does what.*

1. Create dataset from UvA Course Catalogue. Done by: Leon.
2. Literature review of relevant sources on recommender systems. Done by: Adrianna and Barbara.
3. Annotate corpus to include majors. Done by: Leon, Adrianna, Barbara.
4. Start working on recommender system. Done by: Currently Unknown.

## Documentation
*This can be added as the project unfolds. You should describe, in particular, what your repo contains and how to reproduce your results.*
