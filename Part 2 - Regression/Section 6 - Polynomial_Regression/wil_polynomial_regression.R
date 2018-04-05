# Polynomial regression
library(caTools)
library(ggplot2)


# Variables
data.directory <- "."
data.file <- "Position_Salaries.csv"

# Load the data
data.set <- read.csv(file.path(data.directory, data.file))
data.set <- data.set[2:3]
head(data.set)

# Fitting linear model first
lin.reg <- lm(data = data.set, formula = Salary ~ .)

# Poly regression
data.set$Level2 <- data.set$Level^2
data.set$Level3 <- data.set$Level^3
poly.reg <- lm(formula = Salary ~ ., data = data.set)
summary(poly.reg)

# Visualise the linear model
ggplot() +
  geom_point(aes(x = data.set$Level, y = data.set$Salary),color = 'red') +
  geom_line(aes(x = data.set$Level, y = predict(lin.reg, newdata = data.set$Level)), color = 'blue') +
  ggtitle('The title') +
  xlab('Level') +
  ylab('Salary')
