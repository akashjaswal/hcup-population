# Project Working directory
setwd("~/Desktop/Projects/hcup-data/")

#Installing required packages
install.packages("ggplot2")
install.packages("data.table")
install.packages("plm")
library(plm)
library(ggplot2)
library(data.table)
library(scales)

# Loading Hospitalization data 

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1990_CORE.rdat")
h_90 <- data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1991_CORE.rdat")
h_91 <- data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1992_CORE.rdat")
h_92  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1993_CORE.rdat")
h_93  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1994_CORE.rdat")
h_94  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1995_CORE.rdat")
h_95  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1996_CORE.rdat")
h_96  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1997_CORE.rdat")
h_97  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1998_CORE.rdat")
h_98  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_1999_CORE.rdat")
h_99  <-  data.frame(temp)
  
load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2000_CORE.rdat")
h_00  <-  data.frame(temp)
  
load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2001_CORE.rdat")
h_01  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2002_CORE.rdat")
h_02  <-  data.frame(temp)
  
load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2003_CORE.rdat")
h_03  <- data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2004_CORE.rdat")
h_04  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2005_CORE.rdat")
h_05  <-  data.frame(temp)
  
load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2006_CORE.rdat")
h_06  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2007_CORE.rdat")
h_07  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2008_CORE.rdat")
h_08  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2009_CORE.rdat")
h_09  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2010_CORE.rdat")
h_10  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2011_CORE.rdat")
h_11  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2012_CORE.rdat")
h_12  <-  data.frame(temp)

load("~/Desktop/Projects/hcup-data/HospData/WA_SIDC_2013_CORE.rdat")
h_13  <-  data.frame(temp)

load("~/.RData")
load("~/Desktop/Projects/hcup-data/all_hdata.RData")

write.csv(h_04, file = "Hosp_04.csv")
write.csv(h_05, file = "Hosp_05.csv")
write.csv(h_06, file = "Hosp_06.csv")
write.csv(h_07, file = "Hosp_07.csv")
write.csv(h_08, file = "Hosp_08.csv")
write.csv(h_09, file = "Hosp_09.csv")
write.csv(h_10, file = "Hosp_10.csv")
write.csv(h_11, file = "Hosp_11.csv")
write.csv(h_12, file = 'Hosp_12.csv')
write.csv(h_13, file = "Hosp_13.csv")

WA_population <- read.csv("WA_population_data.csv")
WA_population <- data.frame(WA_population)
View(WA_population)
by(WA_population$Population, WA_population$Year, sum)

# WA_population$Year <- as.factor(WA_population$Year)
# WA_population$AgeGroup <- as.factor(WA_population$AgeGroup)
cols <- c('Population','Year','AgeGroup')
pop1 <-  subset(WA_population)[cols]

pop_agg <- aggregate(pop1, by=list(year=WA_population$Year, County=WA_population$AgeGroup), FUN=sum)
pop_agg <- pop_agg[c('year','AgeGroup','Population')]

qplot(factor(year), data=pop_agg, geom="bar", fill=factor(AgeGroup))

color_p <- c('#4183D7','#1F3A93', '#00B16A','#1E824C','#F4D03F','#F9690E','#D91E18') 
d <- ggplot(pop_agg, aes(x = year, y = Population, fill = AgeGroup)) + 
  geom_bar(stat = "identity", alpha = 0.7) + scale_y_continuous(name="Population", labels = comma) + theme_bw() 
d + scale_fill_gradientn(colours = color_p, space = "Lab",
                          guide = "colourbar") + ggtitle("WA State population trends by age group per year")

WA_population$Year <- as.numeric(WA_population$Year)
WA_population <- as.numeric(WA_population$Gender)
gender_data <- aggregate(WA_population, by=list(WA_population['Year'],WA_population['Gender']), FUN=sum)

vaccine_data <- read.csv("WA_state_vaccine_data.csv")

setwd("~/Desktop/Projects/hcup-data/Extracted_hospcsv/")

h_04 <- read.csv("Hosp_04.csv")
h_05 <- read.csv("Hosp_05.csv")
h_06 <- read.csv("Hosp_06.csv")
h_07 <- read.csv("Hosp_07.csv")
h_08 <- read.csv("Hosp_08.csv")
h_09 <- read.csv("Hosp_09.csv")
h_10 <- read.csv("Hosp_10.csv")
h_11 <- read.csv("Hosp_11.csv")
h_12 <- read.csv("Hosp_12.csv")
h_13 <- read.csv("Hosp_13.csv")

cols = c("age","female","ayear","amonth","pstco2","zip")
hf_04 <- h_04[cols]
hf_05 <- h_05[cols]
hf_06 <- h_06[cols]
hf_07 <- h_07[cols]
hf_08 <- h_08[cols]
hf_09 <- h_09[cols]
hf_10 <- h_10[cols]
hf_11 <- h_11[cols]
hf_12 <- h_12[cols]
hf_13 <- h_13[cols]

write.csv(hf_04, file = "Hosp_04.csv")
write.csv(hf_05, file = "Hosp_05.csv")
write.csv(hf_06, file = "Hosp_06.csv")
write.csv(hf_07, file = "Hosp_07.csv")
write.csv(hf_08, file = "Hosp_08.csv")
write.csv(hf_09, file = "Hosp_09.csv")
write.csv(hf_10, file = "Hosp_10.csv")
write.csv(hf_11, file = "Hosp_11.csv")
write.csv(hf_12, file = 'Hosp_12.csv')
write.csv(hf_13, file = "Hosp_13.csv")

filter_data <- function(h_data) {
  for(i in 1:nrow(h_data)) {
  if (h_data[i,]['age'] >=0 & h_data[i,]['age'] <= 4) {
    h_data[i,]['AgeGroup'] <- 1
  }
  if (h_data[i,]['age'] >= 5 & h_data[i,]['age'] <= 9) {
    h_data[i,]['AgeGroup'] <- 2
  }
  if (h_data[i,]['age'] >= 10 & h_data[i,]['age'] <= 14) {
    h_data[i,]['AgeGroup'] <- 3
  }
  if (h_data[i,]['age'] >= 15 & h_data[i,]['age'] <= 19) {
    h_data[i,]['AgeGroup'] <- 4
  }
  if (h_data[i,]['age'] >= 20 & h_data[i,]['age'] <= 24) {
    h_data[i,]['AgeGroup'] <- 5
  }
  if (h_data[i,]['age'] >= 25 & h_data[i,]['age'] <= 29) {
    h_data[i,]['AgeGroup'] <- 6
  }
  if (h_data[i,]['age'] >= 30 & h_data[i,]['age'] <= 34) {
    h_data[i,]['AgeGroup'] <- 7
  }
  if (h_data[i,]['age'] >= 35 & h_data[i,]['age'] <= 39) {
    h_data[i,]['AgeGroup'] <- 8
  }
  if (h_data[i,]['age'] >= 40 & h_data[i,]['age'] <= 44) {
    h_data[i,]['AgeGroup'] <- 9
  }
  if (h_data[i,]['age'] >= 45 & h_data[i,]['age'] <= 49) {
    h_data[i,]['AgeGroup'] <- 10
  }
  if (h_data[i,]['age'] >= 50 & h_data[i,]['age'] <= 54) {
    h_data[i,]['AgeGroup'] <- 11
  }
  if (h_data[i,]['age'] >= 55 & h_data[i,]['age'] <= 59) {
    h_data[i,]['AgeGroup'] <- 12
  }
  if (h_data[i,]['age'] >= 60 & h_data[i,]['age'] <= 64) {
    h_data[i,]['AgeGroup'] <- 13
  }
  if (h_data[i,]['age'] >= 65 & h_data[i,]['age'] <= 69) {
    h_data[i,]['AgeGroup'] <- 14
  }
  if (h_data[i,]['age'] >= 70 & h_data[i,]['age'] <= 74) {
    h_data[i,]['AgeGroup'] <- 15
  }
  if (h_data[i,]['age'] >= 75 & h_data[i,]['age'] <= 79) {
    h_data[i,]['AgeGroup'] <- 16
  }
  if (h_data[i,]['age'] >= 80 & h_data[i,]['age'] <= 84) {
    h_data[i,]['AgeGroup'] <- 17
  }
  if (h_data[i,]['age'] >= 85) {
    h_data[i,]['AgeGroup'] <- 18
  }
  }
  return(h_data)
}

filter_data1 <- function(h_data) {
    if (h_data['age'] >=0 & h_data['age'] <= 4) {
      h_data['AgeGroup'] <- 1
    }
    if (h_data['age'] >= 5 & h_data['age'] <= 9) {
      h_data['AgeGroup'] <- 2
    }
    if (h_data['age'] >= 10 & h_data['age'] <= 14) {
      h_data['AgeGroup'] <- 3
    }
    if (h_data['age'] >= 15 & h_data['age'] <= 19) {
      h_data['AgeGroup'] <- 4
    }
    if (h_data['age'] >= 20 & h_data['age'] <= 24) {
      h_data['AgeGroup'] <- 5
    }
    if (h_data['age'] >= 25 & h_data['age'] <= 29) {
      h_data['AgeGroup'] <- 6
    }
    if (h_data['age'] >= 30 & h_data['age'] <= 34) {
      h_data['AgeGroup'] <- 7
    }
    if (h_data['age'] >= 35 & h_data['age'] <= 39) {
      h_data['AgeGroup'] <- 8
    }
    if (h_data['age'] >= 40 & h_data['age'] <= 44) {
      h_data['AgeGroup'] <- 9
    }
    if (h_data['age'] >= 45 & h_data['age'] <= 49) {
      h_data['AgeGroup'] <- 10
    }
    if (h_data['age'] >= 50 & h_data['age'] <= 54) {
      h_data['AgeGroup'] <- 11
    }
    if (h_data['age'] >= 55 & h_data['age'] <= 59) {
      h_data['AgeGroup'] <- 12
    }
    if (h_data['age'] >= 60 & h_data['age'] <= 64) {
      h_data['AgeGroup'] <- 13
    }
    if (h_data['age'] >= 65 & h_data['age'] <= 69) {
      h_data['AgeGroup'] <- 14
    }
    if (h_data['age'] >= 70 & h_data['age'] <= 74) {
      h_data['AgeGroup'] <- 15
    }
    if (h_data['age'] >= 75 & h_data['age'] <= 79) {
      h_data['AgeGroup'] <- 16
    }
    if (h_data['age'] >= 80 & h_data['age'] <= 84) {
      h_data['AgeGroup'] <- 17
    }
    if (h_data['age'] >= 85) {
      h_data['AgeGroup'] <- 18
    }
  return(h_data)
}

hff_04 <- filter_data(hf_04)
hf_04[1,]['age']

setwd("~/Desktop/Projects/hcup-data/")
paneldata = read.csv("Master_Data_Final.csv")
View(paneldata)

library(lattice)
xyplot(Patients_Ratio ~ year | factor(County), data=paneldata, pch=19, type=c("p","g"), main="Patients Ratio (Normalized by Monthly Population)")
xyplot(All_Vaccinated_Ratio ~ year | factor(County), data=paneldata, pch=19, type=c("p","g"), main="All Vaccinations Ratio (Normalized by Monthly Population)")
xyplot(All_4313314_Ratio ~ year | factor(County), data=paneldata, pch=19, type=c("p","g"), main="All 4313314 Series Ratio (Normalized by Monthly Population)")
xyplot(All_Vaccinated_Ratio + All_4313314_Ratio + Patients_Ratio ~ year | factor(County), data=paneldata, pch=19, type=c("p","g"), main="Vaccination Ratios And Hospitalization Patients Ratio by Year (Normalized by Monthly Population)",auto.key=TRUE, alpha=0.2)

reg0 <- plm(Patients_Ratio ~ All_Vaccinated_Ratio, data = paneldata, index = c("County", "Timeline"), model = "within", effect = "time")
print(reg0)
reg1 <- plm(Patients_Ratio ~ All_Vaccinated_Ratio * factor(County), data = paneldata, index = c("County", "Timeline"), model = "within", effect = "time")
x <- fixef(reg1)
print(x)
print(reg1)

reg2 <- plm(Patients_Ratio ~ All_4313314_Ratio * County, data = paneldata, index = c("County", "Timeline"), model = "within", effect = "twoway")
print(reg2)


pop_agg1 <- aggregate(pop1, by=list(year=WA_population$Year, County=WA_population$County), FUN=sum)
pop_agg1 <- pop_agg1[c('year','County','Population')]
xyplot(Population ~ year | factor(County), data=pop_agg1, pch=19, type=c("p","g"), main="Population Trends by County")
