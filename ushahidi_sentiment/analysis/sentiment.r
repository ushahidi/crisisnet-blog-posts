# Sentiment Analysis
# largely based on: http://www.slideshare.net/jeffreybreen/r-by-example-mining-twitter-for
# uses the score.sentiment() found here: https://jeffreybreen.wordpress.com/tag/sentiment-analysis/

# Load ggplot2
library(ggplot2)

# Load the ushahidi report data
text = read.csv("/Users/chrisralbon/Dropbox (Ushahidi)/CrisisNET/comms/blog_posts/crisisnet_blog_posts/ushahidi_sentiment/analysis/ushahidi_world.csv", header=TRUE)

# Create a score.sentiment function (kept original commenting since it is so good)
score.sentiment = function(sentences, pos.words, neg.words, .progress='none')
{
  require(plyr)
  require(stringr)
  
  # we got a vector of sentences. plyr will handle a list
  # or a vector as an "l" for us
  # we want a simple array ("a") of scores back, so we use
  # "l" + "a" + "ply" = "laply":
  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    
    # clean up sentences with R's regex-driven global substitute, gsub():
    sentence = gsub('[[:punct:]]', '', sentence)
    sentence = gsub('[[:cntrl:]]', '', sentence)
    sentence = gsub('\\d+', '', sentence)
    # and convert to lower case:
    sentence = tolower(sentence)
    
    # split into words. str_split is in the stringr package
    word.list = str_split(sentence, '\\s+')
    # sometimes a list() is one level of hierarchy too much
    words = unlist(word.list)
    
    # compare our words to the dictionaries of positive & negative terms
    pos.matches = match(words, pos.words)
    neg.matches = match(words, neg.words)
    
    # match() returns the position of the matched term or NA
    # we just want a TRUE/FALSE:
    pos.matches = !is.na(pos.matches)
    neg.matches = !is.na(neg.matches)
    
    # and conveniently enough, TRUE/FALSE will be treated as 1/0 by sum():
    score = sum(pos.matches) - sum(neg.matches)
    
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}

# Load Hu and Lui 2004's list of positive words
pos.words <- scan("positive-words.txt", what="character", comment.char=";")

# Load Hu and Lui 2004's list of negative words
neg.words <- scan("negative-words.txt", what="character", comment.char=";")

# Create a sentiment score for the data
text.results <- score.sentiment(text$content, pos.words, neg.words)

# Count the number of reports with a positive score
pos_reports = sum(text.results$score < 0); pos_reports

# Count the number of reports with a negative score
neg_reports = sum(text.results$score > 0); neg_reports

# View the number of reports with each score
sum(text.results$score == 10)
sum(text.results$score == 9)
sum(text.results$score == 8)
sum(text.results$score == 7)
sum(text.results$score == 6)
sum(text.results$score == 5)
sum(text.results$score == 4)
sum(text.results$score == 3)
sum(text.results$score == 2)
sum(text.results$score == 1)
sum(text.results$score == -1)
sum(text.results$score == -2)
sum(text.results$score == -3)
sum(text.results$score == -4)
sum(text.results$score == -5)
sum(text.results$score == -6)
sum(text.results$score == -7)
sum(text.results$score == -8)
sum(text.results$score == -9)
sum(text.results$score == -10)

# Remove reports with a zero score (since many are non-english language)
text.results <- subset(text.results, score != 0)

# Remove outliers
text.results <- subset(text.results, score >= -10 & score <= 10)

# View the results
head(text.results)

# Plot the results
ggplot(data=text.results) + # ggplot works on data.frames, always
  geom_bar(mapping=aes(x=score), binwidth=1) + 
  theme_bw() + 
  scale_fill_brewer() + # plain display, nicer colors 
  xlab("Sentiment Score") +
  ylab("Number of Reports")