# BIDS-Conversion

My data set consists of Dicoms, which are not arragend according to the 'Brain Imaging Data Structure' (BIDS). But why is this not [practical](./BIDS-Conversion.md#brain-imaging-data-structure) and how can one [convert](./BIDS-Conversion.md#dicom-conversion) the data structure into the BIDS format?

This is something I will explain in the following. Let's begin with BIDS and the advantages of organising data like that.

## Brain Imaging Data Structure

BIDS is a standard developed to get to a consensus on how to organize, describe and collect neuroimaging data. BIDS is based on NiFTi files, which should be converted from source dat e.g. DICOM. BIDS follows a specific way on naming and structuring files as you can see in the image below.[^1] Next to the NiFTi files, which stores the brain imaging data [^2], JSON files containing the respective metadata and TSV files with demographics etc. 

![BIDS_CON](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fsdata.2016.44/MediaObjects/41597_2016_Article_BFsdata201644_Fig1_HTML.jpg?as=webp)
*taken from Gorgolewski, K., Auer, T., Calhoun, V. et al. (2016), p.3*

### Advantages
 
Using a common standard for the description and organization has the follwoing advantages[^3] :

* easily understandable data structure, so that veryone at any time can work with the data
* reduces error due to misunderstandings
* optimizing reproducability and efficiency, as standardization allows automated analysis workflows
* validation tools make finding missings easier
* speeds up sharing data on online databases as they can understand and export data in BIDS format


## DICOM Conversion

Before starting to convert the data, one should organize anstructure the imaging data with at least a folder for each subject. If you have multiple session, the subject folder should have folders for each session. 
For me the structure in the DICOMs folder looked like this:

<img src="./content/static/Structure.jpg">

There are a number of converters out there, but I used HeuDiConv and in the following I will explain the neccessary steps my data went through to convert it.

### HeuDiConv


# References

[^1]: Gorgolewski, K., Auer, T., Calhoun, V. et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. Sci Data 3, 160044 (2016). https://doi.org/10.1038/sdata.2016.44S

[^2]: https://nifti.nimh.nih.gov/

[^3]: https://bids.neuroimaging.io/benefits.html#benefits