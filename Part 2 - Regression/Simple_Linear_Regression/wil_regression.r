# Simple Linear regression

library(caTools)
library(ggplot2)


# Variables
data.directory <- "."
data.file <- "Salary_Data.csv"

# Load the data
data.set <- read.csv(file.path(data.directory, data.file))

# Split the data into training and test
set.seed(0)
split <- sample.split(data.set$YearsExperience , SplitRatio = 0.8)

data.set.training <- subset(data.set, split == TRUE)
data.set.test <- subset(data.set, split == FALSE)


# Fit the model

regressor = lm(formula = Salary ~ YearsExperience,
  data = data.set.training
)

summary(regressor)


data.set.predict = predict(regressor, newdata = data.set.test)


ggplot() +
  geom_point(aes(
    x = data.set.training$YearsExperience, y = data.set.training$Salary
  ), color = "red") +
  geom_line(aes(
    x = data.set.training$YearsExperience, y = predict(regressor, newdata = data.set.training)
  ), color = "blue") +
  ggtitle("Salary vs Experience") +
  xlab("Years Experience (Yrs)") +
  ylab("Salary ($)")
