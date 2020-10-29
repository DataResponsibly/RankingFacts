### Example real datasets:
1. [CSranking_faculty30.csv](dataset/CSranking_faculty30.csv) is a dataset with an additional sensitive attribute 'Department Size' that is a binarized attribute from 'Facult' in the dataset [CS Rankings (CSR)](https://csrankings.org). It is merged with additional attributes from the [NRC assessment dataset](http://www.nap.edu/rdp). 

This dataset has the following attributes:
- Average Count (CSR) computes the geometric mean of the adjusted number of publications in each area by institution.
- Faculty (CSR) is the number of faculty in the department.
- GRE (NRC) is the average GRE scores (2004-2006).
- Department size (CSR) is a binary attribute derived from Faculty. Small department has the number of faculty less or equal than 30.
- Region (NRC) is one of Northeast(NE), Midwest(MW), South Atlantic(SA), South Central(SC), and West(W) regions in the US.
- Pub Count (NRC) is the average number of publications per faculty (2000-2006)
2. [GermanCredit_age25.csv](dataset/GermanCredit_age25.csv) is a dataset with a binarized sensitive attribute 'AgeBinary' according to the threshold 25 from the dataset [German credit dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29). It is originally hosted on UCI’s Machine Learning Repository, contains approximately 1000 observations, with 20 variables. The original dependent variable is whether or not an “individual” has good credit record.
3. [COMPAS_gender.csv](dataset/COMPAS_gender.csv) includes approximately sampled 1000 users' recidivism information from dataset [COMPAS](https://github.com/propublica/compas-analysis). It contains criminal history, jail and prison time, demographics and COMPAS risk scores for defendants from Broward County.
4. [Adult_sample.csv](dataset/adult_sample.csv) includes includes 1000 complete records that are sampled from dataset [Adult](https://archive.ics.uci.edu/ml/datasets/adult) (with 48842 records). The extraction was done by Barry Becker from the 1994 Census database. A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)). Prediction task is to determine whether a person makes over 50K a year.
