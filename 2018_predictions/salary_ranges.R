library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)
library(scales)

dollar <- dollar_format()

salaryRange <- function(cluster) {
  if (cluster == 1) {
    return("< $800,000")
  } else if (cluster == 2) {
    return("$800,000 - $1,499,999")
  } else if (cluster == 3) {
    return("$1,500,000 - $2,999,999")
  } else if (cluster == 4) {
    return("$3,000,000 - $4,999,999")
  } else if (cluster == 5) {
    return("$5,000,000 - $7,999,999")
  } else if (cluster == 6) {
    return("$8,000,000 - $9,999,999")
  } else if (cluster == 7) {
    return("$10,000,000 - $12,499,999")
  } else if (cluster == 8) {
    return("$12,500,000 - $14,999,999")
  } else if (cluster == 9) {
    return("$15,000,000 - $17,999,999")
  } else {
    return(">= $18,000,000")
  }
}

percentRange <- function(cluster, cap = 101000000) {
  if (cluster == 1) {
    return(paste("< ", dollar(.02 * cap), sep = ""))
  } else if (cluster == 2) {
    return(salaryString(.02, .04, cap))
  } else if (cluster == 3) {
    return(salaryString(.04, .07, cap))
  } else if (cluster == 4) {
    return(salaryString(.07, .1, cap))
  } else if (cluster == 5) {
    return(salaryString(.1, .13, cap))
  } else if (cluster == 6) {
    return(salaryString(.13, .16, cap))
  } else if (cluster == 7) {
    return(salaryString(.16, .19, cap))
  } else {
    return(paste("> ", dollar(.19 * cap), sep = ""))
  }
}

salaryString <- function(min, max, cap) {
  minSal <- dollar(min * cap)
  maxSal <- dollar(max * cap)
  return(paste(minSal, " - ", maxSal, sep = ""))
}

results <- read.csv("/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_predictions.csv", stringsAsFactors = FALSE)
currentSalaries <- read.csv("/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_source/fixed_2018.csv", stringsAsFactors = FALSE)

current <- currentSalaries %>% select(name_x, average)

final <- results %>% mutate (Salary = sapply(salary, percentRange))%>%
  inner_join(current, by = c(name_x = "name_x"))%>%
  select(name_x, Cluster = salary, `Predicted Salary` = Salary,
         `Current Salary` = average)%>%
  mutate (`Current Salary` = sapply(`Current Salary`, dollar))

write.csv(final, "/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_predicted_salary_detailed.csv")
