# install.packages("httr")
library(httr)

# Find the most recent R questions on stackoverflow
r <- GET(
  "http://dev.crisis.net",
  path = "questions",
  query = list(
    site = "stackoverflow.com",
    tagged = "r"
  )
)

# Check the request succeeded
stop_for_status(r)

# Automatically parse the json output
questions <- content(r)
questions$items[[1]]$title
#> [1] "Remove NAs from data frame without deleting entire rows/columns"

