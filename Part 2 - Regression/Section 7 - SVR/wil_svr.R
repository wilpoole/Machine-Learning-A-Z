# Polynomial regression
library(caTools)
library(ggplot2)
library(e1071)

# Variables
data.directory <- "."
data.file <- "Position_Salaries.csv"

# Load the data
data.set <- read.csv(file.path(data.directory, data.file))
data.set <- data.set[2:3]
head(data.set)

# Define the regressor, make sure to mention for regression template
regressor <- svm(formula = Salary ~ .,
  data = data.set,
  type = "eps-regression")

#
pred <- predict(regressor,newdata = data.frame(Level = 6.5))
print(pred)

# Visualising the SVR results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = data.set$Level, y = data.set$Salary),
             colour = 'red') +
  geom_line(aes(x = data.set$Level, y = predict(regressor, newdata = data.set)),
            colour = 'blue') +
  ggtitle('Truth or Bluff (SVR)') +
  xlab('Level') +
  ylab('Salary')

# Visualising the SVR results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(data.set$Level), max(data.set$Level), 0.1)
ggplot() +
  geom_point(aes(x = data.set$Level, y = data.set$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (SVR)') +
  xlab('Level') +
  ylab('Salary')
  
