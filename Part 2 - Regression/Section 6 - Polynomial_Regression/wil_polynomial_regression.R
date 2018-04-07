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
data.set$Level4 <- data.set$Level^4
poly.reg <- lm(formula = Salary ~ ., data = data.set)
summary(poly.reg)

# Visualise the linear model
ggplot() +
  geom_point(aes(x = data.set$Level, y = data.set$Salary), color = 'red') +
  geom_line(aes(x = data.set$Level, y = predict(lin.reg, newdata = data.set) ), color = 'blue') +
  ggtitle('The title') +
  xlab('Level') +
  ylab('Salary')


# Visualise the linear model
x_grid = seq(min(data.set$Level), max(data.set$Level), 0.1)

ggplot() +
  geom_point(aes(x = data.set$Level, y = data.set$Salary), color = 'red') +
  geom_line(aes(x = x_grid, y = predict(poly.reg, newdata = data.frame(Level = x_grid,
                                                                       Level2 = x_grid^2,
                                                                       Level3 = x_grid^3,
                                                                       Level4 = x_grid^4)) ), color = 'blue') +
  ggtitle('The title') +
  xlab('Level') +
  ylab('Salary')


# Predict the value of 6.5 level
lin.pred <- predict(lin.reg,newdata = data.frame(Level = 6.5))

# Use Polynomial model
poly.pred <- predict(poly.reg,newdata = data.frame(Level = 6.5,
                                                   Level2 = 6.5^2,
                                                   Level3 = 6.5^3,
                                                   Level4 = 6.5^4))
