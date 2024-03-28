# Ice Online Store Video Game Sales Analysis
This repository contains the analysis of video game sales data for Ice, an online store that sells video games globally. The goal is to identify patterns that determine the success of video games, enabling the company to spot potential big winners and plan effective advertising campaigns.

# Project Description
Ice Online Store needs to analyze video game sales data to identify patterns determining a game's success. The dataset includes information on user and expert reviews, genres, platforms, and historical sales data dating back to 2016. The dataset also contains the Entertainment Software Rating Board (ESRB) ratings, which evaluate a game's content and assign age ratings.

# Dataset
The dataset contains the following features:

- Name: Name of the game
- Platform: Gaming platform (e.g., Xbox, PlayStation)
- Year_of_Release: Release year of the game
- Genre: Genre of the game
- NA_sales: North American sales in USD million
- EU_sales: European sales in USD million
- JP_sales: Japanese sales in USD million
- Other_sales: Sales in other countries in USD million
- Critic_Score: Critic score (maximum of 100)
- User_Score: User score (maximum of 10)
- Rating: ESRB rating

# Methodology
Step 1: Data Preparation
  - Replace column names and make them lowercase.
  - Convert data to the required types.
  - Handle missing values appropriately.
  - Handle cases where sales are marked as "TBD" (to be determined).

Step 2: Data Analysis
  - Analyze the number of games released in different years.
  - Examine sales variation across different platforms.
  - Identify leading platforms and determine sales trends.
  - Analyze the impact of user and professional reviews on sales.
  - Explore the distribution of games by genre.

Step 3: User Profile Creation
  - Determine top platforms and genres for each region (NA, EU, JP).
  - Investigate the effect of ESRB ratings on sales in individual regions.

Step 4: Hypothesis Testing
  - Test hypotheses regarding average user ratings for Xbox One and PC platforms and for Action and Sports genres.

Step 5: Conclusion
  - Summarize findings and insights from the analysis.

# Dependencies
Make sure you have the following dependencies installed:

Python 3.x
Jupyter Notebook
Pandas
Matplotlib
NumPy
SciPy
