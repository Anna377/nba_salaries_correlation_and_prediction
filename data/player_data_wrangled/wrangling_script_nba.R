library(DataComputing)
library(tidyr)
library(printr)
library(dplyr)

stats <- c("Adv","PerGame","Totals")
years <- c("2022")
fixYear <- function(year) {
  for (stat in stats) {
    tableName <- paste("data/player_data/players",
                       year, "/",stat,"_", year,".csv", sep = "")
    # Unwrangled Player Salary table location
    table <- read.csv(tableName)
    fixName<- mutate(table,
                     fix = gsub('[^A-Za-z]+', '', gsub('[.]','', tolower(gsub('\\\\.*', '', Player)))))
    movedPlayers <- fixName %>%
      filter(Tm == "TOT")
    temp <- fixName %>% group_by(Player) %>%
      filter(max(row_number()) == 1) %>% ungroup()
    final <- rbind(temp, movedPlayers)

    printName <- paste(
      "data/player_data_wrangled/players",
      year, "/",stat,"_",year,"wrangled.csv", sep = "")
    dir.create(paste("data/player_data_wrangled/players",
      year, "/", sep = ""), showWarnings = FALSE)
    # Writes new wrangled tables in separate directory
    write.csv(final, file = printName, append = FALSE, sep = ",")
  }
}

for (year in years) {
  fixYear(year)
}