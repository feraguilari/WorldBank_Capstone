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
### Worldwide Governance Indicators Controlled by Investment Grade Category
[logo]:..img/WGIvsGrade.png "Logo Title Text 2"
![alt text](../img/WGIvsGrade.png "Logo Title Text 1")

## Conclusion and Recommendations
I have developed a KNearestNeighbors Classification model that has 51% precision and 65% accuracy scores. the metrics are significant given that there are 8 different classes and the most popular one only had about 25% incidence.


This model does not substitute for due dilligence or more complete current models. This model could be thouhgt as a feature engineering tool to be used during preprocessing to develop a new feature, in this case the rating grade, and use it to increase the more robust model's performance.

