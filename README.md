# OA_Calculations
Explorations of interrelationships among OA parameters based loosely on
monitoring data from Casco Bay.

In several settings, we have been finding apparent inconsistencies in how data
as observed in Casco Bay get converted behind the scenes to estimates of core
carbonate parameters.

We also have been uncertain about the sensitivity of omega estimates on
accuracy of the core data that undergirds calculation of parameters of the
CO~2~ system.

Here we will have two R Notebooks and some python code:  

1. The first notebook uses selected data from Casco Bay to try to replicate
   FOCB and UNH calculations of OA parameters.  The upshot is that because of
   the way FOCB measures pH, we can not use the r package "seacarb" to calculate
   carbonate chemistry parameters.  WE also can not quite replicate either
   FOCB or UNH values, but if we select the right modeling parameters, we
   can return results for the UNH data that are highly correlated with their
   results, with minimal bias.

2. The second notebook explores sensitivity of Omega estimates based
   on possible variation ("error" ) in each measured parameter.  The results
   show that Omega values are much more sensitive to variation in measurement 
   of pH than to other measured parameters.

3. We also include some python code to recalculate carbonate parameters based
   on the Python package, PyCO2SYS.  This package has more options (and appears
   to be more frequently updated) than the equivalent R package (seacarb).