# Data Spec

This is where you will be describing your data spec comprehensively. Please refer to the handout for a couple of examples of good data specs.

You will also need to provide a sample of your data in this directory. Please delete the example `sample.db` and replace it with your own data sample. **_Your sample does not necessarily have to be in the `.db` format; feel free to use `.json`, `.csv`, or any other data format that you are most comfortable with_**.

All our data is stored in four tables: billboard rank, covid data, song attributes, and lyrics.

Table: Billboard Rank
Attribute: rank
Rank is represented by the type REAL, with a default value of 0. The range is 1 to 100 with uniform distribution. This is not an identifier unless paired with other attributes, and the values are not unique since there are songs that will share ranks across different weeks. There are duplicate values, but by using a primary key of (rank, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have a rank. We plan to use this attribute in the analysis to see which songs we should then find the song attributes and song lyrics for, via Spotify API and Genius API, respectively. This feature does not include potentially sensitive information.
Attribute: title
Title is represented by the type VARCHAR, with a default value of ‘’. The range is len(1) to len(30) characters, with most titles being in the range [len(5), len(15)]. This is not an identifier unless paired with other attributes, and the values are not unique since there are songs that will stay on the billboard across multiple weeks. There are duplicate values, but by using a primary key of (title, artist, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have a title. We plan to use this attribute, in conjunction with the artist attribute, to search the Spotify API for song attributes and search the Genius API for song lyrics. This feature does not include potentially sensitive information.
Attribute: artist
Artist is represented by the type VARCHAR, with a default value of ‘’. The range is len(5) to len(30) characters, with most artists being in the range [len(4), len(15)]. This is not an identifier unless paired with other attributes, and the values are not unique since there are artists that will stay on the billboard across multiple weeks and artists that have multiple songs on any given week’s billboard. There are duplicate values, but by using a primary key of (title, artist, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have an artist. We plan to use this attribute, in conjunction with the title attribute, to search the Spotify API for song attributes and search the Genius API for song lyrics. This feature does not include potentially sensitive information.
Attribute: month
Month is represented by the type REAL, with a default value of 0. The range is 1-12 with uniform distribution. This is not an identifier unless paired with other attributes, and the values are not unique since every song on the billboard of a given month will have the same month value. There are duplicate values, but by using a primary key of (rank, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have a month it is shown on the billboard. We will use this attribute to correlate the date of a song’s rank with the date in which Covid cases peaked or declined. Essentially, this attribute will allow us to see what songs are in which time frames when we ultimately do statistical analysis on the song attributes and lyrics. This feature does not include potentially sensitive information.
Attribute: day
Day is represented by the type REAL, with a default value of 0. The range is 1-31 with uniform distribution. This is not an identifier unless paired with other attributes, and the values are not unique since every song on the billboard of a given day will have the same day value. There are duplicate values, but by using a primary key of (rank, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have a day in which it is shown on the billboard. We will use this attribute to correlate the date of a song’s rank with the date in which Covid cases peaked or declined. Essentially, this attribute will allow us to see what songs are in which time frames when we ultimately do statistical analysis on the song attributes and lyrics. This feature does not include potentially sensitive information.
Attribute: year
Year is represented by the type REAL, with a default value of 0. The range is 2020-2022 with a normal distribution. This is not an identifier unless paired with other attributes, and the values are not unique since every song on the billboard on a given year will have the same year value. There are duplicate values, but by using a primary key of (rank, month, day, year), we can see that there are no “duplicate records”. This is a required value since every song on the billboard will have a year in which it is shown on the billboard. We will use this attribute to correlate the date of a song’s rank with the date in which Covid cases peaked or declined. Essentially, this attribute will allow us to see what songs are in which time frames when we ultimately do statistical analysis on the song attributes and lyrics. This feature does not include potentially sensitive information.

Table: Lyrics
Attribute: Title
Same as in billboard table, but distinct
Attribute: Artist
Same as in billboard table, but distinct
Attribute: Lyrics
The lyrics for a song will be represented as a VARCHAR. The default value is the empty string “”, and lyrics can take a wide range of characters, from 0 (instrumentals) to a couple thousand for longer rap songs. We expect a normal distribution where most songs have around 1500 characters, corresponding to a few verses and a repeated chorus. This is not an identifier or unique: artists cover each other’s songs. We will likely not use this to detect duplicates: song title and artist name are sufficient for that purpose. We plan to use this attribute in our analysis to generate estimates of the textual sentiment of top songs. With data for sentiment, as well as measures of mentions of key terms related to Covid, we can estimate differences between the emotional tenor of songs in different periods. Lyrics generally don’t contain private information, but they can include explicit words and harsh language, which deserve sensitivity.

Table: Songs
Attribute: Title
The title of a song is represented as a VARCHAR. The default value is the empty string “”, and can take a wide range of characters. We expect a normal distribution where most titles have around 15 characters. When paired with the artist, this is an identifier. These values are not necessarily unique. This can be used to identify duplicates because a combination of song, artist, and timestamp should be unique. This is a required value because it is an identifier. We plan on using this attribute to create unique identifiers. The title can also be used as a subject of sentiment analysis. This feature does not include potentially sensitive information.
Attribute: Artist
List<String>
red Default: “”
Range: Len = 1 to len = 50
Distribution: > 50% of values in [5, 25]
Identifier: No
Unique: No
Duplicates: Yes: song + artist + timestamp should be unique
Required: Yes
Plan: Yes, can use to create unique identifiers and could also be a subject of sentiment analysis / covid-relatedness
Sensitive: No
Attribute: Year
Representation: REAL
Default: 0
Range: 2000-2022
Distribution: 100% of values in [2017, 2022]
Identifier: No
Unique: No
Duplicates: No
Required: Yes
Plan: Yes, can use to analyze how sentiment shifts every year
Sensitive: No
Attribute: Lyrics
The Genius API will be used to extract song lyrics
All Genius API responses are JSON
The value returned will be an object with key-value pairs of formats and results (in our case, it is either HTML or CSV)
Tracks can take any range of reasonable amount of words
This attribute is not an identifier and values are not necessarily unique
Will be used in analysis to understand how COVID-19 affected lyrical complexity/simplicity as well as prevalent sentiments
Does include any sensitive information as most of the information is publicly available on multiple platforms and formats
Attribute: Popularity
0-to-100 score that ranks how popular an artist is relative to other artists on Spotify
​​Determined by recent stream count, other factors like save rate, the number of playlists, skip rate, and share rate
Duplicate tracks (e.g. the same track from a single and an album) are rated independently
Can be considered a unique identifier  
Attribute: Duration
Representation: TIME
Default: 00:00:00
Range: 00:01:00 to 00:05:00
Distribution: >50% of values in [00:02:30, 00:04:30]
Identifier: No
Unique: No
Duplicates: No
Required: Yes
Plan: can use to determine what length of songs users prefer depending on outside contexts
Sensitive: No
Attribute: liveness  
Detects the presence of an audience in the recording.
Higher liveness values represent an increased probability that the track was performed live.
A value above 0.8 provides strong likelihood that the track is live.
Attribute Loudness:
overall loudness of a track in decibels (dB).
Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks.
Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude).
Values typically range between -60 and 0 dB.
Attribute: Speechiness
Detects the presence of spoken words in a track.
The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value.
Values above 0.66 describe tracks that are probably made entirely of spoken words
Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music.
Values below 0.33 most likely represent music and other non-speech-like tracks.
Attribute: Instrumentalness
Measure whether a track contains no vocals.
Rap or spoken word tracks are clearly ‘vocal’.
The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.
Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
Attribute: Acousticness
Measure from 0.0 to 1.0 of whether the track is acoustic.
1.0 represents high confidence the track is acoustic.
Attribute: Danceability
Describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.
A value of 0.0 is least danceable and 1.0 is most danceable.
Attribute: Energy
Measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
Typically, energetic tracks feel fast, loud, and noisy.
Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
Attribute: tempo
Overall estimated tempo of a track in beats per minute (BPM).
In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
Attribute: valence
Measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

Table: Covid
Attribute: location
Location is represented by the type VARCHAR, with a default value of ‘’. The range is 13 characters with uniform distribution, since we are just collecting data from “United States”. This is not an identifier unless paired with other attributes, and the values are not unique since all the data describe U.S. covid statistics. There are duplicate values, but by using a primary key of (location, date), we can see that there are no “duplicate records”. This is a required value since every statistic has a location. We plan to use this attribute in the analysis to by only getting data regarding U.S. covid cases. This feature does not include potentially sensitive information.
Attribute: Date
Date is represented by the type VARCHAR, with a default value of ‘’. The range is 10 characters with uniform distribution, since all date formats are “xx/xx/xxxx”. This is an identifier, and the values are unique since we are just looking at U.S. data. There are no duplicate values. This is a required value since every statistic has a date. We plan to use this attribute in the analysis to by only getting data regarding U.S. covid cases. We will use this attribute to correlate the date of a song’s rank with the date in which Covid cases peaked or declined. Essentially, this attribute will allow us to see what songs are in which time frames when we ultimately do statistical analysis on the song attributes and lyrics. This feature does not include potentially sensitive information.
Attribute: total cases
Representation: REAL
Default: 0
Range: [0, 1 000 000]
Distribution: Multimodal distribution, a few months generate many of the deaths
Identifier: No
Unique: No
Duplicates: Yes, though duplicates would be suspicious
Required: No
Plan: Yes, look at days in which COVID reaches a local maximum or minimum
Sensitive: No (we will use published datasets)
Attribute: new cases
New cases are represented as type REAL, with a default value of 0. This is not a unique identifier, unless paired with other attributes, and the values are not unique since two days can potentially have the same number of new cases. This value will not be used to detect duplicate records. This is a required value because there is always a number for new recorded cases, even if that number is 0. This feature does not include potentially sensitive information.
Attribute: total deaths
Total deaths are represented as type REAL, with a default value of 0. This is not a unique identifier, unless paired with other attributes, and the values are not unique since two days can potentially have the same number of total deaths. This value will not be used to detect duplicate records. This is a required value because the total number of deaths continues to increase everyday. This feature does not include potentially sensitive information.
Attribute: new deaths
New deaths are represented as type REAL, with a default value of 0. The range is 1 to 1,000,000, with a multimodal distribution since a few months contribute to more covid deaths than others. This is not a unique identifier, unless paired with other attributes, and the values are not unique since two days can potentially have the same number of deaths. This value will not be used to detect duplicate records. This is a required value because a number of deaths can be recorded for everyday, even if that number is 0. We will use this attribute to view and look at the days in which COVID reaches a local maximum or minimum. This feature does not include potentially sensitive information.

Tech Report

Our project examines the effects of COVID on the music industry. Specifically, it analyzes how COVID impacts certain attributes of songs that make it to the U.S. Billboard’s Top 100 chart. Our data is set within the timeframe of January 28, 2020 to February 28, 2022. From this 25 month period, we chose 5 days in which there was a local maximum of new onset COVID cases, and 5 days in which there was a trough in new COVID cases. The dates are as follows:

APR 10, 2020: Peak
JUL 24, 2020: Peak
SEPT 11, 2020: Trough
DEC 30, 2020: Trough
JAN 11, 2021: Peak
JUNE 22, 2021: Trough
SEPT 13, 2021: Peak
OCT 26, 2021: Trough
NOV 28, 2021: Trough
JAN 15, 2022: Peak
For each of these days, we scraped Billboard’s Top 100 played songs. This gives us 1,000 records. Songs are left intentionally duplicated in our songs table because a single song may remain on the charts for many weeks. We did not eliminate duplicates because each song corresponds to a unique date/rank pair: there are over 500 distinct songs in the table, and the primary key (rank, month, day, year) provides a method to search unique records. With our quantity of records we feel confident that we can perform (unpaired) t-tests between the top songs at high- and low- COVID moments from past years. Per the Central Limit Theorem, the distribution of sample means approximates a normal distribution once the sample size exceeds ~30, a threshold that we exceed. We also scraped lyrics for hundreds of songs, which provides us with a rich dataset by which to compare the content of songs in high- and low- COVID periods.

We collected our data through a multitude of websites. Public data regarding COVID cases in countries across the globe can be found online, and we used Python’s pandas library to clean data from a csv file sourced from ourworldindata.com. The web scraping technique learned in homework 2 was implemented on historical records of Billboard’s Top 100 chart. We scraped Billboard's top songs charts for specific time frames where COVID-19 peaked and was unambiguously affecting the landscape during these periods. Our songs data is obtained from Spotify publicly available repositories and APIs. The spotify API and its related python packages were used to retrieve relevant information. The following libraries were used:

Spotipy and SpotifyClientCredentials
json

The spotify API returns data in Json form. Spotify breaks down their audio data into mainly two categories. The first is composed of 11 high dimensional audio data titled Audio Features. The second is a more in depth lower dimensional analysis of the audio titled Audio Analysis.

We supplemented our Spotify dataset with lyrics obtained from Genius.com through a combination of API calls and web scraping. All of the sources from which we obtained our data are reputable. For example, Spotify is a widely used app for music streaming across the United States. Billboard has been the premier authority in music rankings for decades. Genius is the foremost source of lyrics on the internet, and allows for crowd-sourced annotations and API interfaces. We obtained our COVID data from a source that provides free, open access datasets used and trusted by paramount companies such as The New York Times, as well as Harvard, Stanford, and other cutting edge universities.

We generated the sample by visually examining the three dates corresponding to the highest and lowest rates of new COVID cases in the past few years. We then extracted the top 100 songs for these periods from Billboard. Our peaks and troughs sampling likely violates the iid assumption because Nov 28, 2021 and Jan 15, 2022 are closer together in time than Jan 11, 2021 and June 22, 2021. Additionally, the first two peaks are closer in magnitude than the second and third. These relationships introduce correlation between the samples that somewhat undermine the statistical tests we intend to conduct. Furthermore, note that our analysis is restricted to the most popular songs at a given moment. This means we overlook songs that don’t make the charts. Notably, the people most affected by Covid are elderly people who do not drive trends in pop music. Instead, pop music reflects the tastes of young people who are the least vulnerable to Covid. Moreover, Billboard’s Hot 100 chart aggregates metrics across sales, airplay, and streaming. During periods of intense Covid, radio stations shut down causing a lag in their uptake of new releases while they aired reruns; record shops closed, forcing consumers to defer their purchases, and people staying at home may not have discovered new music in time to stream it. The upshot of these considerations is that much of the music people were listening to at home or even wanted to be listening to is likely not captured by Billboard. Choosing the top 100 songs generates a comparatively large sample: many sources (Spotify, radio stations, etc) refer exclusively to the “top 40” on the charts, perhaps for a given month. By selecting the top 100 for a given moment in time, our metric for music popularity is both broad in scope and high in resolution. On the other hand, we restrict our observations to six moments in time and a single country, which further limits the size and representativeness of our data. Another point of sample bias stems from the fact that Covid waves tended to occur in the Fall, and troughs in the Summer. This means our Covid samples are correlated with seasonal listening patterns. Finally, note that not all periods of Covid are the same. Our data obscures regional variation, and differences in the severity of the distinct variants. A period with three times as many cases as another cannot be said to be “three times worse.” This is especially true because many of the people who were most vulnerable to infection died in the early phases of the pandemic, and thus are no longer present in the latter samples to influence music consumption trends.
In preparing our data, we discussed extensively the prospects for making causal claims. Ultimately, we concluded that it is methodologically difficult to estimate the treatment effect of Covid on a country because there are no control countries. We looked into countries that have had no Covid cases to use as controls in a difference-in-differences design, but these countries lacked reliable music popularity data. Instead, we resigned to assess the non-Covid counterfactual by looking to periods with low rates of Covid during the past few years. We determined that we can still run tests for statistical significance under this approach and construct our ML component as well.
Throughout our data collection process, we performed an abundance of checks to ensure that our data is collected to our liking. We checked for the cleanliness of our data by inspecting how clean the source data and database outputs are. Specifically, we checked that the numerical values are presented in standardized format, song titles are standardized, and that there are no irrelevant rows/columns in the tables. For example, the original imported COVID data consisted of over 50 columns and 200,000 rows– we cleaned this data by removing rows of countries other than the US and columns of data that was not relevant to our project goals. On the other hand, the data scraped from Billboard’s top 100 had all its values preserved. We cleaned this dataset by stripping the song titles, and standardizing the column with artist names by removing operators that signaled artist features (“&”, “/”, “X”, “+”, etc.). After the operators were removed, songs with multiple artists had each artist individually stored as strings in a list. Ultimately, we chose to store only one of these artists in the database because only one producing artist is needed to identify a unique song. For song titles, artist names, and lyrics, we also performed basic operations such as removing stray commas, quotes, and excess whitespace.

Our data contains a few missing values. Lyrics were found for 332 out of 427 songs. This discrepancy occurred because some songs do not have lyrics in Genius (especially recent releases), and other songs were only indexed by one out of multiple artists or listed artists inconsistently. However, we believe that the data we have is sufficient for any analyses we may want to run. We are still considering further refinements to our script, and potentially manually collecting lyrics for certain songs. Our data also contains a few duplicates. As aforementioned, we obtained a list of Billboard’s top 100 songs for each day in which new COVID cases were a local maximum or minimum. For any two given days, there will likely be a song repeat in the top 100 list. However, we are intentionally keeping these duplicate songs because they still provide information of significance for song data on that particular day. We had to throw away some collected data– in our lyric analysis, we only considered songs that we could find lyrics for. If there was an instrumental or Spanish-language song, we did not use the song.

Certain points in our dataset are slightly skewed. The distribution of Covid cases over time is negatively skewed, since many cases are concentrated between November 2021 to February 2022, but there is a long tail to the left with cases prior to the Omicron wave. We looked into the days in which there was a local minimum or maximum number of new cases. Interestingly, we found that two of the local peaks occurred at around the same date (mid January) in different years.

We noticed some data type issues when obtaining the datetime from different sources. Because we collected data from a multitude of websites, the format in which a date or time was presented was not consistent. Thus, we converted datetime types into more accessible formats. For example, in our Billboard table, we separated the day, month, and year into separate columns of type REAL. Another approach we took for the COVID data was to convert the datetime into a STRING, and indexing into certain positions to obtain a certain day, month, or year.

One of the big challenges we came across is that we were unable to find a reliable dataset that contains historic information regarding the top 100 songs for any day we select. Billboard and Spotify both update their respective website and playlists daily, and previous data cannot be sourced. We resolved this issue by using a third party website, waybackmachine.com, to view past data. We plan on merging our databases to analyze the characteristics of songs in Billboard’s top 100 rankings. We are hoping to find statistically significant differences between the songs associated with COVID peaks vs troughs. Because we have collected primarily numeric data, e.g. the Spotify metrics, we will deploy t-tests in our analysis (we cannot use z-tests because we do not know the population variance for any metric, e.g. danceability, at a given moment across the Spotify universe). Artist and song are categorical variables because they can recur in different time periods, but the range of these variables is so large as to likely resist analysis by chi-square tests for significance. One exception might be genre, which our data does not currently include, but if we later add this variable, we would analyze its prevalence with chi-square tests.
