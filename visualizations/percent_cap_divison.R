library(ggplot2)
data <- read.csv("/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/training_test_dataset.csv")

ggplot(data, aes(x=PercentCap, y=Salary, group=Cluster)) +
         geom_bar(stat="identity", colour="black", position="dodge", size=0.25, width=0.8, alpha=0.8) +
  scale_fill_manual(values=c("red","blue"))
