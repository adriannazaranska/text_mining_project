## Abstract

We made an AUC recommender which takes 8 courses as an input (first year) and outputs 5 recommendations for the next semester. The recommender is memory-based using content-based filtering. As for the input we excluded the Academic Core and Other Majors requirenmentrs, focusing on accurate recommendations within one's major. We obtained the dataset for out project by web scraping the UvA Course Catalogue, which contains descriptions for all available courses at UvA and AUC.

The reason for us choosing this for our project is due to our own difficulties with creating a study plan when coming into our second year of AUC. As AUC is unique in that you get to create your own study plan, we often found ourselves overwhelmed given the sheer amount of UvA courses available at our fingertips. Having a recommender could help students avoid taking unnecessary courses by showing them courses they did not even know were available. 

## Research Question
How can different text mining approaches and embedding techniques be optimized to maximize both precision and diversity in an AUC course recommender system?

## Dataset

The dataset will be the UvA course catalogue: https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course.

We created the dataset ourselves by scraping the website for all 3812 courses. After removing the courses not tought in English the final dataset contained 3345. The features we captured: 
- Course catalogue number
- Course description
- Credits
- Language of Instruction
- College/graduae
- Is part of

We preprocessed the course descriptions and used two models - TF-IDF Vectorisation and SentBERT Transformer - to produce the recommendations. The only features we used for the models were the course description, is part of, and college/graduate. The other could be used in the future for more used-decided filtering. 

## A tentative list of milestones for the project

1. Create the dataset from UvA Course Catalogue. Done by: Leon.
2. Literature review of relevant sources on recommender systems and evaluation metrics. Done by: Adrianna and Barbara.
3. Annotate corpus to include majors. Done by: Leon, Adrianna, Barbara.
4. Create a Recommender system. Done by: Barbara, Adrianna, Leon
5. Test the models: Done by: Barbara and Leon.
6. Evaluate the models: Done by: Adrianna and Leon.
7. Write the report : The contributions are listed in the report. 

## Documentation

This repository contains the following folders/files:

- datasets: folder containing datasets which we will be using within the jupyter notebooks.
- datasets/recommender_dataset.csv: contains the information scraped from the UvA course catalogue website for 2024-2025. More accurate description can be found above in 'Dataset'.
- datasets/test_set.txt: contains handmade groups of courses for certain majors/tracks, used to evaluate the performance of the recommender.
- datasets/uva_course_links.txt: preliminary dataset containing the links to all courses, used to extract detailed info which is stored in recommender_dataset.csv. These links are scraped from the UvA course catalgoue.
- auc_course_recommender.ipynb: main jupyter notebook containing most of the code for the project.
- auc_course_recommender_report.pdf: report of our findings.
- presentation.pdf: presentation used in class to introduce our project to the class.
- uva_course_webscraper.ipynb: this is a jupyter notebook used to scrape the data from the UvA course catalogue.

To recreate results:
- Use the same dataset as obtained in uva_course_webscraper.ipynb
- Preprocess the dataset in the same way as in auc_course_recommender.ipynb
- Use the same models in the same way as in auc_course_recommender.ipynb
