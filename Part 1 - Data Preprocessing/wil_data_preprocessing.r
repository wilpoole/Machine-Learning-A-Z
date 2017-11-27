# Data preprocessing
#

# PAckages
library(caTools)


# Variables
data.directory <- "data"
data.file <- "data.csv"


# Functions


# Data import
data.set <- read.csv(file.path(data.directory, data.file))

# Correcting the missing data
data.set$Age <- ifelse(is.na(data.set$Age),
  ave(data.set$Age, FUN = function(x) mean(x, na.rm = TRUE)),
  data.set$Age
  )

data.set$Salary <- ifelse(is.na(data.set$Salary),
  ave(data.set$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
  data.set$Salary
  )

# Converting categorical data to numerical values
data.set$Country <- factor(
  data.set$Country,
  levels = unique(data.set$Country),
  labels = seq(1, length(unique(data.set$Country)))
  )

data.set$Purchased <- factor(
  data.set$Purchased,
  levels = unique(data.set$Purchased),
  labels = seq(0, length(unique(data.set$Purchased))-1)
  )

# Splitting the data into test and training data_set_dependent_test
set.seed(0)
split <- sample.split(data.set$Purchased, SplitRatio = 0.8)

data.set.training <- subset(data.set, split == TRUE)
data.set.test <- subset(data.set, split == FALSE)

# Scaling the dataset
data.set.training[ , 2:3] <- scale(data.set.training[ , 2:3])
data.set.test[ , 2:3] <- scale(data.set.test[ , 2:3])
