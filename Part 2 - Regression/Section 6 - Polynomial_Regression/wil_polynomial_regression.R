# Polynomial regression
library(caTools)
library(ggplot2)


# Variables
data.directory <- "."
data.file <- "50_Startups.csv"

# Load the data
data.set <- read.csv(file.path(data.directory, data.file))
head(data.set)

# Encoding categorical data
data.set$State <- factor(data.set$State,
  levels = unique(data.set$State),
  labels = seq(1, length(unique(data.set$State)), 1)
)

# Split the data into training and test
set.seed(0)
split <- sample.split(data.set$R.D.Spend , SplitRatio = 0.8)
data.set.training <- subset(data.set, split == TRUE)
data.set.test <- subset(data.set, split == FALSE)
head(data.set.training)
