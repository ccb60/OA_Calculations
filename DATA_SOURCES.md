# Data Notes

All data derived from CBEP_OA and FOCB_OA repository data files. See those
repositories for additional detail.

Data was selected only for summer and fall of 2016, then columns were 
reordered so order was similar between the two files.

Note that the two files use different pH scales.  FOCB used the NBS pH scale,
while data from UNH uses the Total pH scale.

One representative on-line source had the following to say:
> Potentiometric measurements of pH are inherently less precise than
  spectrophotometric measurements. Moreover, the relationship between the NBS
  Scale and the Total Scale is not exact and depends on characteristics of the
  electrode employed.

In the core [FOCB_OA analysis](https://github.com/ccb60/FOCB_OA), we recalculate
pH on the Total scale using python and PyCO2SYS to get around this problem.

