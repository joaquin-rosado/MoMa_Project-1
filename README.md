# MoMa_Project-1
 
 The Museum of Modern Art published two datasets with all of the artists and artworks that have been part of the museum's exhibition catalogue.
 
 
## Methodology

For this project, I analyzed the Artists dataset, which contained 15,222 artists with basic metadata, such as _name_, _nationality_, _gender_, _birth year_, _death year_, among others.

I used Pandas in Jupyter Notebook, and compared artist's _gender_ and _nationality_ to determine incidence of nationality per gender. First, the  10 nationalities with most incidence were displayed using `value_counts()`. The same function was used to find and compare the amount of male/female artists. 

To find which nationalities were predominant by gender, the `groupby()` function helped order the dataset.

In the _Gender_ column, male and female values were found in upper and lowercase letters. These values were replaced with their initials 'M' and 'F' to reduce confusion. These values, along with _Non-Binary_, were, then, added as separate columns in the dataframe.

Variables by gender were made to divide the results, which were then merged with the `concat` function and exported to csv format.

The final dataset was imported to Datawrapper to create a range plot chart, available in the repository.
