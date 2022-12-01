library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

wrangleSet <- function(year) {
  salName <- "2018_predictions/2018_source/2018_free_agents_list.csv"
  statName <- "2018_predictions/2018_source/2018_standardized.csv"
  
  sal <- read.csv(salName, stringsAsFactors = FALSE)
  stat <-read.csv(statName, stringsAsFactors = FALSE)
  
  salary <- sal %>% select(name)
  data <- stat %>% inner_join(sal, c("fix" = "name"))
  
  final <- data %>% select(Player, Pos, Age, Tm, name = fix, DRB, TOV, PPG = PS.G, VORP)
  
  
  return(final)
}

final <- wrangleSet("2018")
head(final)

write.csv(final, "/Users/annamartirosyan/PycharmProjects/NBA_salaries/2018_predictions/2018_final_detailed.csv")