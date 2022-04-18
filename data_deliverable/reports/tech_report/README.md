# Tech Report

### Where is the data from? How did you collect your data?

Our project examines the effects of COVID on the music industry. Specifically, it analyzes how COVID impacts certain attributes of songs that make it to the U.S. Billboard’s Top 100 chart. Our data is set within the timeframe of January 28, 2020 to February 28, 2022. From this 25 month period, we chose 5 days in which there was a local maximum of new onset COVID cases, and 5 days in which there was a trough in new COVID cases. The dates are as follows:

- APR 10, 2020: Peak
- JUL 24, 2020: Peak
- SEPT 11, 2020: Trough
- DEC 30, 2020: Trough
- JAN 11, 2021: Peak
- JUNE 22, 2021: Trough
- SEPT 13, 2021: Peak
- OCT 26, 2021: Trough
- NOV 28, 2021: Trough
- JAN 15, 2022: Peak

For each of these days, we scraped Billboard’s Top 100 played songs. This gives us 1,000 records. Songs are left intentionally duplicated in our songs table because a single song may remain on the charts for many weeks. We did not eliminate duplicates because each song corresponds to a unique date/rank pair: there are over 500 distinct songs in the table, and the primary key (rank, month, day, year) provides a method to search unique records.

We collected our data through a multitude of websites. Public data regarding COVID cases in countries across the globe can be found online, and we used Python’s pandas library to clean data from a csv file sourced from ourworldindata.com. The web scraping technique learned in homework 2 was implemented on historical records of Billboard’s Top 100 chart. We scraped Billboard's top songs charts for specific time frames where COVID-19 peaked and was unambiguously affecting the landscape during these periods. Our songs data is obtained from Spotify publicly available repositories and APIs. The spotify API and its related python packages were used to retrieve relevant information. The following libraries were used:

- Spotipy and SpotifyClientCredentials
- json

The spotify API returns data in Json form. Spotify breaks down their audio data into mainly two categories. The first is composed of 11 high dimensional audio data titled Audio Features. The second is a more in depth lower dimensional analysis of the audio titled Audio Analysis.

We supplemented our Spotify dataset with lyrics obtained from Genius.com through a combination of API calls and web scraping.

### Is the source reputable?

All of the sources from which we obtained our data are reputable. For example, Spotify is a widely used app for music streaming across the United States. Billboard has been the premier authority in music rankings for decades. Genius is the foremost source of lyrics on the internet, and allows for crowd-sourced annotations and API interfaces. We obtained our COVID data from a source that provides free, open access datasets used and trusted by paramount companies such as The New York Times, as well as Harvard, Stanford, and other cutting edge universities.

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?

We generated the sample by visually examining the three dates corresponding to the highest and lowest rates of new COVID cases in the past few years. We then extracted the top 100 songs for these periods from Billboard. Our peaks and troughs sampling likely violates the iid assumption because Nov 28, 2021 and Jan 15, 2022 are closer together in time than Jan 11, 2021 and June 22, 2021. Additionally, the first two peaks are closer in magnitude than the second and third. These relationships introduce correlation between the samples that somewhat undermine the statistical tests we intend to conduct. Furthermore, note that our analysis is restricted to the most popular songs at a given moment. This means we overlook songs that don’t make the charts. Notably, the people most affected by Covid are elderly people who do not drive trends in pop music. Instead, pop music reflects the tastes of young people who are the least vulnerable to Covid. Moreover, Billboard’s Hot 100 chart aggregates metrics across sales, airplay, and streaming. During periods of intense Covid, radio stations shut down causing a lag in their uptake of new releases while they aired reruns; record shops closed, forcing consumers to defer their purchases, and people staying at home may not have discovered new music in time to stream it. The upshot of these considerations is that much of the music people were listening to at home or even wanted to be listening to is likely not captured by Billboard.

Choosing the top 100 songs generates a comparatively large sample: many sources (Spotify, radio stations, etc) refer exclusively to the “Top 40” on the charts, perhaps for a given month. By selecting the top 100 for a given moment in time, our metric for music popularity is both broad in scope and high in resolution. On the other hand, we restrict our observations to six moments in time and a single country, which further limits the size and representativeness of our data. Another point of sample bias stems from the fact that Covid waves tended to occur in the Fall, and troughs in the Summer. This means our Covid samples are correlated with seasonal listening patterns. Finally, note that not all periods of Covid are the same. Our data obscures regional variation, and differences in the severity of the distinct variants. A period with three times as many cases as another cannot be said to be “three times worse.” This is especially true because many of the people who were most vulnerable to infection died in the early phases of the pandemic, and thus are no longer present in the latter samples to influence music consumption trends.

### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)

In preparing our data, we discussed extensively the prospects for making causal claims. Ultimately, we concluded that it is methodologically difficult to estimate the treatment effect of Covid on a country because there are no control countries. We looked into countries that have had no Covid cases to use as controls in a difference-in-differences design, but these countries lacked reliable music popularity data. Instead, we resigned to assess the non-Covid counterfactual by looking to periods with low rates of Covid during the past few years. We determined that we can still run tests for statistical significance under this approach and construct our ML component as well.

### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

Throughout our data collection process, we performed an abundance of checks to ensure that our data is collected to our liking. We checked for the cleanliness of our data by inspecting how clean the source data and database outputs are. Specifically, we checked that the numerical values are presented in standardized format, song titles are standardized, and that there are no irrelevant rows/columns in the tables. For example, the original imported COVID data consisted of over 50 columns and 200,000 rows– we cleaned this data by removing rows of countries other than the US and columns of data that was not relevant to our project goals. On the other hand, the data scraped from Billboard’s top 100 had all its values preserved. We cleaned this dataset by stripping the song titles, and standardizing the column with artist names by removing operators that signaled artist features (“&”, “/”, “X”, “+”, etc.). After the operators were removed, songs with multiple artists had each artist individually stored as strings in a list. Ultimately, we chose to store only one of these artists in the database because only one producing artist is needed to identify a unique song. For song titles, artist names, and lyrics, we also performed basic operations such as removing stray commas, quotes, and excess whitespace.

This data is sufficient to complete the project we proposed. We will use the attributes of the songs scraped to conduct hypothesis testing, and use the lyrics of the songs scraped to conduct machine learning analysis.

### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?

So far, we have 1,000 data points in total. For each group we care about (the time periods of COVID peaks and COVID throughs), there are 500 data points in aggregate for each time period.

With our quantity of records we feel confident that we can perform (unpaired) t-tests between the top songs at high- and low- COVID moments from past years. Per the Central Limit Theorem, the distribution of sample means approximates a normal distribution once the sample size exceeds ~30, a threshold that we exceed. We also scraped lyrics for hundreds of songs, which provides us with a rich dataset by which to compare the content of songs in high- and low- COVID periods.

### Are there missing values? Do these occur in fields that are important for your project's goals?

Our data contains a few missing values. Lyrics were not found for all 1000 songs. This discrepancy occurred because some songs do not have lyrics in Genius (especially recent releases), and other songs were only indexed by one out of multiple artists or listed artists inconsistently. However, we believe that the data we have is sufficient for any analyses we may want to run. We are still considering further refinements to our script, and potentially manually collecting lyrics for certain songs.

### Are there duplicates? Do these occur in fields that are important for your project's goals?

Our data also contains a few duplicates. As aforementioned, we obtained a list of Billboard’s top 100 songs for each day in which new COVID cases were a local maximum or minimum. For any two given days, there will likely be a song repeat in the top 100 list. However, we are intentionally keeping these duplicate songs because they still provide information of significance for song data on that particular day.

### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)

Certain points in our dataset are slightly skewed. The distribution of Covid cases over time is negatively skewed, since many cases are concentrated between November 2021 to February 2022, but there is a long tail to the left with cases prior to the Omicron wave. We looked into the days in which there was a local minimum or maximum number of new cases. Interestingly, we found that two of the local peaks occurred at around the same date (mid January) in different years.

### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?

We noticed some data type issues when obtaining the datetime from different sources. Because we collected data from a multitude of websites, the format in which a date or time was presented was not consistent. Thus, we converted datetime types into more accessible formats. For example, in our Billboard table, we separated the day, month, and year into separate columns of type REAL. Another approach we took for the COVID data was to convert the datetime into a STRING, and indexing into certain positions to obtain a certain day, month, or year.

### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?

We had to throw away some collected data. In our lyric analysis, we only considered songs that we could find lyrics for. If there was an instrumental or Spanish-language-only song, we did not use the song. We do not believe this will have a significant impact on the analyses we are able to run, since this represents a small minority of songs in the sample.

### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

One of the big challenges we came across is that we were unable to find a reliable dataset that contains historic information regarding the top 100 songs for any day we select. Billboard and Spotify both update their respective website and playlists daily, and previous data cannot be sourced. We resolved this issue by using a third party website, waybackmachine.com, to view past data. We plan on merging our databases to analyze the characteristics of songs in Billboard’s top 100 rankings. We are hoping to find statistically significant differences between the songs associated with COVID peaks vs troughs. Because we have collected primarily numeric data, e.g. the Spotify metrics, we will deploy t-tests in our analysis (we cannot use z-tests because we do not know the population variance for any metric, e.g. danceability, at a given moment across the Spotify universe). Artist and song are categorical variables because they can recur in different time periods, but the range of these variables is so large as to likely resist analysis by chi-square tests for significance. One exception might be genre, which our data does not currently include, but if we later add this variable, we would analyze its prevalence with chi-square tests.
