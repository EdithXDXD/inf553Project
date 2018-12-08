# inf553Project. Results files:

-- UPDATED LINK --
https://drive.google.com/drive/folders/1mbLbGB0pBRtLR-gwN1rEO4x29oLVsZmX

| File Name                                      | Type   | Description                                                                    |
|------------------------------------------------|--------|--------------------------------------------------------------------------------|
| processed data                                 | folder | all the preprocessed data from the original yelp dataset.                      |
| wordcloud                                      | folder | visualization of user similarity profile                                       |
| yelp_user_potential_restaurants_sample_all.txt | TXT    | Candidate set for restaurant recommendation                                    |
| user_based_prediction_result                   | folder | user-based predicted score and test sets                                       |
| restaurant_based_prediction_result             | folder | restaurant-based predicted score                                               |
| sentiment_analysis_score_for_user.txt          | TXT    | Sentiment Analysis for User Profile                                            |
| **final_prediction_test_file.txt**                 | TXT    | final prediction test dataset                                                  |
| **final_prediction_output.txt**                    | TXT    | final predicted scores (we processed the recommendation decision in notebook)  |


# inf553Project. Individual Contributions
**Ruyin Shao:** <br>
1. Implement programs to generate sets of similar users by KNN  <br> 
2. Transform the Euclidian distances into similariti measures Build the word cloud of user profiles based on these results <br> 
3. Conduct final review, modification of our paper and make the presentation slides

**Di Huang:**  <br>
1. Implement the part of sentiment analysis based on review text  <br> 
2. Build user profiles and item profile <br> 
3. Calculate the personalized score between user and restaurant based on cosine similarity and use that for prediction  <br> 
4. Implement linear regression to set weights. Write the model part(Section 3) of our paper

**Kai Wang:**  <br>
1. Implement the functions of user-based collaborative filtering based on the user similarity values extracted from KNN results and use that for rating prediction and recommendation. <br> 
2. Write the result and conclusion part (Section 4) of our paper.

**Xuezheng Tao:**  <br>
1. Implement the programs of item-based collaborative filtering based on cosine similarity between restaurants and use that for rating prediction and recommendation  <br>
2. Write the abstract and introduction, dataset part (Section 1 and 2) of our paper.
