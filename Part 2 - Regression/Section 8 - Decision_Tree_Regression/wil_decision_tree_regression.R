# Regression Template

# Importing the dataset
dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]

# Fitting the Regression Model to the dataset
library(rpart)
regressor <- rpart(formula = Salary ~ ., 
                   data = dataset,
                   control = rpart.control(minsplit = 1)
                   )

# Predict the y value
y.pred <- predict(regressor,
                  newdata = data.frame(Level = 6.5)
                  )

# Library
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Decision Tree Model)') +
  xlab('Level') +
  ylab('Salary')

# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Decision Tree Model)') +
  xlab('Level') +
  ylab('Salary')
