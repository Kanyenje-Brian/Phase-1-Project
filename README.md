**VANGUARD LTD. AIRCRAFT INSIGHT**

Vanguard, a Business Conglomerate, is interested in expanding its portfolio and has set its scope on purchasing and operating planes for both private and commercial enterprises. However, with no prior experience in the aviation sector, the company needs guidance on which airplanes to invest on as diffrerent airplanes pose different risk factors. In order to provide guidance to the company, intensive research on different airplane data will be done in order to generate insight on which airplanes pose the lowest risks. The insight will be used by the head of the new aviation division in deciding on which airplanes to purchase and operate.


**Objectives**
> Identify the airplane models and manufacturers with the lowest accident rates.
> Determine which airplane engine types are associated with the lowest crash rates.
> Identify the safest airplane operations with the lowest incidence of plane crashes.

DATA UNDERSTANDING
The data to be used in the analysis was gotten from [Kaggle](https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses), a data science platform, which has multiple datasets.

The particular dataset was from the National Transportation Safety Board (NTSB). This dataset is comprised of aviation accidents data from 1962 to 2023 about civil aviation accidents and selected incidents within the United States, its territories and international waters. This makes the data relevant to this study as it includes all the relevant information regarding the accidents (the aircraft type, type of flight, the engine type, and the weather during the incident). All this data will make it possible to fulfill the objectives of the study.

**DATA ANALYSIS**

After data cleaning and preparation, the datasets are now ready for analysis to derive valuable insights. The analysis will be conducted on a piecemeal basis, i.e., objective by objective.

**Objective 1: Identify the airplane makes and models with the lowest accident rates.**
The goal of the first objective is to identify airplane models and manufacturers with the lowest accident rates. Aircraft with the best safety records will be the most advisable for use. This analysis will be conducted by examining which airplane makes and models appear the least in the dataset, as well as assessing the extent of damage sustained in accidents.
 Since there are a lot of models with low accident rates, the data will also be filtered with regard to the Aircraft.damage and Total.Injuries column where only planes with minor aircraft damage and less than 20 injuries will be shown.

 
![download](https://github.com/user-attachments/assets/320c3425-df9a-461a-90c7-d99671c1d822)

Cessna, Piper and Beech aircraft stood out as having most of their models having one crash, had minor damage during the crash and total injuries not exceeding 20.

**Objective 2: Determine which airplane engine types are associated with the lowest crash rates.**

The second objective will be to check which the types of engines of aircraft that were used by planes that had the lowest crashes. This will help in establishing which engine types are the most reliable and not prone to failure.

![download](https://github.com/user-attachments/assets/1f4becdc-d0fb-44e0-8ba5-79ef38ea5822)

The three best engines to use are the Reciprocating, Turbo Fan and Turbo Prop respectively.

**Objective 3: Identify the safest airplane operations with the lowest incidence of plane crashes.**
This objective will aim to uncover the safest airplane operations that put the plane to the lowest risk of an accident. The insight derived from this will help quide Vanguard on choosing which operations to focus on and which to avoid in order to lower the probability of a plane crash.


![download](https://github.com/user-attachments/assets/ce5b7341-371f-4f8b-980b-911cdcab2121)

Most plane that crashed were being operated for private means while planes used for executive/corporate purposes had the least amount of crashes. It would be best to focus on the executive plane operations inorder to minimize chances of a crash.

**Findings and Recommendations**
**Objective 1: Identify the airplane models and manufacturers with the lowest accident rates.**

After analysis, five airplane makes stood out to be the best since they had only one accident recorded. These planes were Aerotrike, Raytheon, Dayton A Babcock, Pereyra and American Autogyro. However, there were a lot of airplane manufacturers with record of one accident accross their fleet so further filtering was done to only remain with planes which sustained minimal damage after the crash and also had less than 20 total injuries. The top three manufacturers that stood out were Cessna, Beech and Piper.

**Objective 2: Determine which airplane engine types are associated with the lowest crash rates.**

The three engine types that were common in airplanes that had only one recorded accident were Reciprocating, Turbo Fan and Turbo Prop engines. It will be advisable if these engines were put into consideration when the planes are being purchased since they have a good track record and seem reliable and not prone to failure. 

**Objective 3: Identify the safest airplane operations with the lowest incidence of plane crashes.**

Planes used in the private enterprise have a higher probability of crashing while planes used in the business and executive/corporate sector have the lowest probability of crashing. This is because many private pilots may have less training, fewer flight hours, and less experience handling emergencies compared to corporate pilots.
