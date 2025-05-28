## Abstract

We made an AUC recommender which takes 8 courses as an input (first year) and outputs 5 recommendations for the next semester. The recommender is memory-based using content-based filtering. As for the input we excluded the Academic Core and Other Majors requirenmentrs, focusing on accurate recommendations within one's major. We obtained the dataset for out project by web scraping the UvA Course Catalogue, which contains descriptions for all available courses at UvA and AUC.

The reason for us choosing this for our project is due to our own difficulties with creating a study plan when coming into our second year of AUC. As AUC is unique in that you get to create your own study plan, we often found ourselves overwhelmed given the sheer amount of UvA courses available at our fingertips. Having a recommender could help students avoid taking unnecessary courses by showing them courses they did not even know were available. 

## Research questions/Thesis
The recommender will output the courses accurately 80% of the times, which translates to minimun 4 out of 5 correctly recommended.

## Dataset

The dataset will be the UvA course catalogue: https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course.

We created the dataset ourselves by scraping the website for all 3812 courses. After removing the courses not tought in English the final dataset contains 3345. The features we captured: 
- Course catalogue number
- Course description
- Credits
- Language of Instruction
- College/graduae
- Is part of

We preprocessed the course descriptions and used two models - TF-IDF Vectorisation and SentBERT Transformer - to produce the recommendations. 

## A tentative list of milestones for the project

1. Create the dataset from UvA Course Catalogue. Done by: Leon.
2. Literature review of relevant sources on recommender systems and evaluation metrics. Done by: Adrianna and Barbara.
3. Annotate corpus to include majors. Done by: Leon, Adrianna, Barbara.
4. Create a Recommender system. Done by: Barbara, Adrianna, Leon
5. Test the models: Done by: Barbara and Leon.
6. Evaluate the models: Done by: Adrianna and Leon.
7. Write the report : The contributions are listed in the report. 

## Documentation
*This can be added as the project unfolds. You should describe, in particular, what your repo contains and how to reproduce your results.*
