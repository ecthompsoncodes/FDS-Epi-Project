install.packages("tidyverse")

library(tidyverse)


#Read in dataset
setwd("C:/Users/scott/OneDrive/Documents/FDS 510/Dataset")

df = read_csv("data_full.csv")
df = df[, -c(1,2,4:7,9:14,20, 21)]

result <- df %>%
  group_by(county) %>%
  summarise(
    hotspot_prop = round(mean(Hotspot_2), 4)
  )

df1 = df %>%
  distinct(county, .keep_all = TRUE)

result = merge(result, df1, by = 'county')

result1 = result[, -c(4, 5, 17:19)]

result2 = result1[, -c(1, 13, 14, 15)]

intercept_only = lm(hotspot_prop ~ Population.x, result2)

all = lm(hotspot_prop ~ ., result2)

forward_step_model = step(intercept_only, direction = 'forward', scope = formula(all), trace = 0)
summary(forward_step_model)

forward_step_model$anova

forward_step_model$coefficients
