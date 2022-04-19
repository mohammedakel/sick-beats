# Tech Report

### A defined hypothesis or prediction task, with clearly stated metrics for success.

Hypothesis 1: There is a significant difference in mean danceability rating for songs during COVID peaks and songs during COVID troughs. Success is finding that there is a significant (p-value < 0.05) difference).

Hypothesis 2: There is a significant difference in mean energy rating for songs during COVID peaks and songs during COVID troughs. Success is finding that there is a significant (p-value < 0.05) difference).

Hypothesis 3: There is a significant difference in mean valence rating for songs during COVID peaks and songs during COVID troughs. Success is finding that there is a significant (p-value < 0.05) difference).

Machine Learning 1: K-Means clustering of songs based on musical attributes. Success is identifying distinct clusters that visually separate the songs along meaningful dimensions (loudness, tempo, etc).

Machine Learning 2: We used the NLP sentiment analysis tool in the Flair library to determine the positive or negative sentiment of the lyrics in songs at Covid peaks and troughs. The tool returned a "Positive" or "Negative" label along with a confidence metric between [0, 1]. We recorded the confidence value in our data table, interpreting it as the expected value of an indicator random variable. Success is finding statistically significant differences in sentiment by peak vs trough.

Machine Learning 3: We ran a logistic regression of positive/negative sentiment on other attributes like date and peak vs trough. We scaled and demeaned the data by way of preprocessing and applied K-Fold validation. The library we employed uses an l2 regularizer by default to penalize complexity in the model. Success is a high average accuracy rating.

### Why did you use this statistical test or ML algorithm?

For the three hypotheses, we decided to use a two-sample t-test because we are testing the unknown population means for two groups.

K-means clustering presented an appealing first approach because, as an unsupervised algorithm, it provided immediate, easily-visualized insight into our data without the need for labeled observations. Additionally, because we had encountered these methods in the previous assignment, we felt confident in our ability to use them well.

For sentiment analysis, Flair's tool has been trained on many corpuses of data, and of the options we considered, Flair's sacraficed runtime for improved accuracy, which we valued for our purposes.

We used logistic regression because we aimed to provide a binary classification of lyrical sentiment as a function of numeric data. Indeed, classifying the positivity vs negativity of the lyrics based on some probability threshold was consonant with our understanding of Flair's sentiment score as the expectation of an indicator variable. 

### Which other tests did you consider or evaluate?

Other statistical tests were not as relevant to showing a difference in population means. First, since we separated the time periods into that of COVID peaks and that of COVID troughs, we had essentially two populations, so it wouldn't make sense to do a paired t-test. We also wouldn't use a Chi-squared test of independence because we are not testing categorical variables, but rather continuous, numerical values.

### How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

For the statistical tests, we used the threshold of p-value < 0.05 to measure success or failure. We chose this value due to conventional standards of significance levels.

When evaluating the model, ...

### What is your interpretation of the results? Do accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

Hypothesis 1: The p-value of the two-sample t-test was 0.531. Since the p-value is above our chosen signficance level of 0.05, we cannot reject the null hypothesis, and cannot conclude that there is a significant difference in mean danceability rating for songs during COVID peaks and songs during COVID troughs.

Hypothesis 2: The p-value of the two-sample t-test was 0.043. Since the p-value is below our chosen significance level of 0.05, we can reject the null hypothesis, and can conclude that there was a significant difference in mean energy rating for songs during COVID peaks and songs during COVID troughs.

Hypothesis 3: The p-value of the two-sample t-test was 0.835. Since the p-value is above our chosen significance level of 0.05, we cannot reject the null hypothesis, and cannot conclude that there is a significant difference in mean valence rating for songs during COVID peaks and songs during COVID troughs.

Machine Learning 1: ...

It makes sense that the mean energy rating would be different during COVID peaks and throughts--people may not feel like listening to upbeat music during times of COVID peaks, for instance. However, it is weird that difference in energy values would be statistically different, but not the differences in danceability or valence. It seems that, intuitively, all three should somewhat be related to each other. For instance, more energetic songs are usually more danceable. However, we are confident in the way we conducted the two-sample t-test so there must have been some other factor that affects danceability and valence but not energy.

### For your visualization, why did you pick this graph? What alternative ways might you communicate the result? Were there any challenges visualizing the results, if so, what where they? Will your visualization require text to provide context or is it standalone (either is fine, but it's recognize which type your visualization is)?

We picked ...

### Full results + graphs (at least 1 stats/ml test and at least 1 visualization). You should push your visualizations to the /analysis_deliverable/visualizations folder in your repo. Depending on your model/test/project we would ideally like you to show us your full process so we can evaluate how you conducted the test!

### If you did a statistics test, are there any confounding trends or variables you might be observing?

A confounding variable might be the fact that music taste is subject to pop culture shocks (i.e. something might go viral on social media and as a result cause a song to be trending). This is pretty much outside of the scope so there was no way to control for that in the statistics test.

### If you did a machine learning model, why did you choose this machine learning technique? Does your data have any sensitive/protected attributes that could affect your machine learning model?

You can also attach photos from your repo
