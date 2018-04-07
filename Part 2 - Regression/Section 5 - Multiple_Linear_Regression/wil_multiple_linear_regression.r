# Multi Linear regression
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

# Fit the model
regressor = lm(formula = Profit ~ .,
  data = data.set.training)

# Explore fits
summary(regressor)


# Predict the Y values
y_pred <- predict(regressor, newdata = data.set.test)

# Plot the data
plt <- plot(x = y_pred, y = data.set.test$Profit)

# Fit the model
regressor = lm(formula = Profit ~ R.D.Spend +
  Administration + Marketing.Spend + State,
  data = data.set.training)

# Explore fits
summary(regressor)

# Fit the model
regressor = lm(formula = Profit ~ R.D.Spend +
  Administration + Marketing.Spend,
  data = data.set.training)

# Explore fits
summary(regressor)

# Fit the model
regressor = lm(formula = Profit ~ R.D.Spend +
  Marketing.Spend, data = data.set.training)

# Explore fits
summary(regressor)


# Fit the model
regressor = lm(formula = Profit ~ R.D.Spend, data = data.set.training)

# Explore fits
summary(regressor)



backwardElimination <- function(x, sl) {
    numVars = length(x)
    for (i in c(1:numVars)){
      regressor = lm(formula = Profit ~ ., data = x)
      maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
      if (maxVar > sl){
        j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
        x = x[, -j]
      }
      numVars = numVars - 1
    }
    return(summary(regressor))
  }

  SL = 0.05
  dataset = data.set[, c(1,2,3,4,5)]
  backwardElimination(data.set.training, SL)
