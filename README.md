# Analysis of content in Netflix, Amazon Prime, and Disney Plus
In this project, I will compare the content between Netflix, Amazon Prime, and Disney Plus. I will apply ML techniques to predict the type of content that can be expected from these OTT platforms in the coming years. This project is currently work-in-progress.
## Data
**Netflix data**<br>
Shivam Bansal. (2019-12-04). Netflix Movies and TV Shows, Version 5. Retrieved 2022-02-15 from [Netflix Movies and TV Shows](https://www.kaggle.com/shivamb/netflix-shows/metadata)

**Amazon Prime data**<br>
Shivam Bansal. (2021-10-12). Amazon Prime Movies and TV Shows, Version 1. Retrieved 2022-02-15 from [Amazon Prime Movies and TV Shows](https://www.kaggle.com/shivamb/amazon-prime-movies-and-tv-shows/metadata).

**Disney Plus**<br>
Shivam Bansal. (2021-10-02). Disney+ Movies and TV Shows, Version 2. Retrieved 2022-02-15 from [Disney+ Movies and TV Shows](https://www.kaggle.com/shivamb/amazon-prime-movies-and-tv-shows/)

## Introduction and Method
Over the years, Netflix, Prime, and Disney Plus have taken over as entertainment sources in the households of many families. Each of these platforms has its own niche of content. In this project, I will look into the content data such as genre, country of origin, rating, etc of each of the three platforms to look for patterns and trends. The data used is described in the *Data* section. Before beginning with the analysis, the data has to be cleaned.

1. For many of the titles, the country of origin is not available in the data. I have scraped it from the IMDb website corresponding to the title. A single title can have more than one country of origin.
2. There are 30 unique ratings in the dataset which can be reduced to a smaller number. Ratings are according to the [Amazon Prime Maturity Ratings](https://www.primevideo.com/help/ref=atv_hp_nd_cnt?nodeId=GFGQU3WYEG6FSJFJ#:~:text=and%20over%20(12)-,Young%20Adults,(18%2B)). The conversion keys is in [Rating conversion key](https://github.com/sangeethankumar/OTT-Content-Analysis/blob/master/cleaning_criteria/rating_conversion)
3. There are 101 genres which can be reduced to 14.

## Analysis results
1. OTT content is dominated by movies and shows released recently with over 17000 titles with release year after 2000.
2. Prime and Netflix have combined 93% of the OTT content. 
3. Most of the titles have only one country of origin (17185 titles). USA leads as the country of origin with 10008 titles listing USA as one of the countries of origin followed by India, UK, Canada, and France.
4. Drama and Comedy dominate as genres of the contnets

