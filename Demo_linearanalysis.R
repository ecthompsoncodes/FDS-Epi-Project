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

result = result[, -c(4, 5, 17:19)]

result2 = result[, -c(1, 13, 14, 15)]

p = lm(hotspot_prop ~ ., result2)

step_model = step(p)
summary(step_model)

step_model$anova
