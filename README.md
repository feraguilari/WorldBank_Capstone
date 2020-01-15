# Predicting Risk of Default using Worldwide Governance Indicators (WGI)
## Motivation
I had the oportunity to attend a hackathon organized by The World Bank with the aim to explore new ways of extracting valuable insight from their data that would contribute towards their mission. The World Bank's mission is "to achieve the twin goals of ending extreme poverty and building shared prosperity".  

The World Bank like any other banking institution has limited resources, and the efficient allocation of this resources is crucial to achieve the bank's goals. With various country competing for financing options to improve their countries, how do we choose go gets the resources they need?  

In this project, I look into country governance indicators and how they impact the country's risk of default as rated by independet sovereign debt credit agency's. The main question to be answered is, how does government indicators impact risk of defaut?
## Non-Technical Presentation
Click on the following image to be redirected to the presentation hosted on youtube.

[![Presentation Image](http://img.youtube.com/vi/ny-iaCbJucM/0.jpg)](http://www.youtube.com/watch?v=ny-iaCbJucM "Project Non-Technical Presentation")
## Process Overview
![Process Overview Mindmap](/img/WGI-process.png)
## Data Sources
### The World Bank's DataBank

Aggregate and individual governance indicators for six dimensions of governance: Voice and Accountability; Political Stability and Absence of Violence/Terrorism; Government Effectiveness; Regulatory Quality; Rule of Law; Control of Corruption.
Access the database by following [this link.](https://databank.worldbank.org/source/worldwide-governance-indicators)

### Countryeconomy.com
A sovereign credit rating is the credit rating of a sovereign entity, such as a national government. The sovereign credit rating indicates the risk level of the investing environment of a country and is used by investors when looking to invest in particular jurisdictions, and also takes into account political risk.[Wikipedia](https://en.wikipedia.org/wiki/Credit_rating)
Go to the website following [this link.](https://countryeconomy.com/ratings)

## Data Insights
### Worldwide Governance Indicators Through Time
![header](img/WGI_WorldwideAverages.png "Worldwide governance indicator averages per year")

The World Bank developed The Worldwide Governance Indicators in 1996, this is when the highest values for most indicators with average values close to 0, except for 'RL.EST' and 'VA.EST', Rule of Law and Voice and Accountability respectively, which started with the lowest observed values. They converge around year 2004 and shortly after that, they all together decrease drastically around year 2006. In more recent years, from 2016 onwards, the indicators show reduced volatility and more stable average values.
### Worldwide Governance Indicators Controlled by Investment Grade Category
![header](img/WGIvsGrade.png "Indicators boxplots controlled by investment grade category")

When controlling and ordering the Worldwide Governance Indicators for invetment grade category according to level of risk, we can notice a decreasing trend for all indicator values. This could mean that there is an association between level of risk and indicator values, where the lower the risk the higher the values for all governance indicators. Governance indicators and risk are inversely related.
### Regional Distribution of Investment Grade Categories
![header](img/RegionalGrades.png "Investment grade categories distributed by region")

There are ony 3 regions with prime rating grades, North America, Europe and Central Asia, and East Asia Pacific. Sub-Saharan Africa has the most highly sepculative rating grades of all regions. South Asia is mostly awardaded lower medium grades downward. Additinally, Latin America and the Caribbean is the region with the most extremely speculative grades received.

## The Model
I trained 3 non parametric classification models, K-NearestNeighbors, RandomForest, GradientBoosting. I chose non-parametric models because the worldwide governance indicators are non-normally distributed. I want to keep the explainability of the models simple, hence I opted not to transform the data to make it more normal. I developed a pipeline to tune the hyper-parameters for the three models with a 5-fold cross-validation GridSearch, optimizing for precision. Precision is a relevant metric in this project beacuse it answers the following question: What proportion of the predicted investment grade classes are correctly predicted? The World Bank relies on this precision because it has to offer competitive loan terms for all levels of risk. The results are shown in the following table:

| model            | accuracy | precision | recall | f1     |
|------------------|----------|-----------|--------|--------|
| knn              | 65.69%   | 51.45%    | 52.28% | 51.49% |
| GradientBoosting | 66.91%   | 49.97%    | 50.25% | 49.98% |
| RandomForest     | 54.41%   | 42.37%    | 41.42% | 41.32% |



## Conclusion and Recommendations
I have developed a KNearestNeighbors Classification model that has 51% precision and 65% accuracy scores. The metrics are significant given that there are 8 different classes and the most popular one only had about 25% incidence.


This model does not substitute for due dilligence or more complete current models. This model could be thouhgt as a feature engineering tool to be used during preprocessing to develop a new feature, in this case the rating grade, and use it to increase the more robust model's performance.


