library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

stats <- c("Adv", "PerGame")

fixYear <- function(year) {
  for (stat in stats) {
    tableName <- paste("2018_predictions/2018_source/",
                       stat, year,".csv", sep = "")
    table <- read.csv(tableName)
    fixName<- mutate(table,
                     fix = gsub(
                       '[^A-Za-z]+', '',
                       gsub('[.]','',
                            tolower(
                              gsub('\\\\.*', '', Player)))))
    movedPlayers <- fixName %>%
      filter(Tm == "TOT")
    temp <- fixName %>% group_by(Player) %>%
      filter(max(row_number()) == 1) %>% ungroup()
    final <- rbind(temp, movedPlayers)

    printName <- paste(
      "2018_predictions/2018_source/", stat,"_", year, "wrangled.csv", sep = "")


    write.csv(final, file = printName, append = FALSE, sep = ",")
  }
}

fixYear("2018")


