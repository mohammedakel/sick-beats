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
