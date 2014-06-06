Ushahidi Reports Sentiment Analysis
====================

This folder contains the code used to construct a sentiment analysis of ~4000 English language reports sent into Ushahidi.

To replicate the results:

1. Run ushahidi_world_visual_140514.ipynb, which pulls the data from CrisisNET, completes the data munging, and spits out a csv.
2. Run sentiement.r, which takes the data in the csv, runs the sentiment analysis and creates the ggplot visual

The data comes from [Crisis.net](http://crisis.net).
