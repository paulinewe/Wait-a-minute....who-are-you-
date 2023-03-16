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

Before starting to convert the data, one should organize anstructure the imaging data with at least a folder for each subject. If you have multiple session, the subject folder should have folders for each session. A folder for the NiFTis you will create is also a good idea.
For me the structure in the Data folder looked like this:

```
Data
└───Dicoms
    └───sub-01
    │   └───Anat
            └───SCANS
                └───DICOMS
    │   └───Run01
            └───SCANS
                └───DICOMS
    │   └───Run02
            └───SCANS
                └───DICOMS
    │   └───Run03
            └───SCANS
                └───DICOMS
    │   └───Run04
            └───SCANS
                └───DICOMS
    │   └───Loc
    │   └───Trails
    └───sub-02
└───NiFTi
```

There are a number of converters out there, but I used HeuDiConv and in the following I will explain the neccessary steps my data went through to convert it.

### HeuDiConv
HeuDiConv is a flexible DICOM converter for organizing your brain imaging data into a directory layout depending on your needs as you can simple adapt the heuristic. It provides a fast way of transforming your data as it only uses the relevant DICOMS [^4] and dcm2niix, which converts Dicoms into NiFTi files[^5]. To make life a bit more easy, there are some tutorials out there from which I followed the [walkthrough](https://reproducibility.stanford.edu/bids-tutorial-series-part-2a/) by the Stanford Center for Reproducible Neuroscience.

#### Requirements
* Docker Desktop (https://docs.docker.com/desktop/windows/wsl/)
* Ubuntu 20.04 LTS or any latest version or WSL
* Conda 4.12.0 or latest version

(bring this to life was a hugh mess for me, [see](./Discussion.md#difficulties-and-throwbacks))

#### Process
**1. setting up the environment:**
    After installing everything, you need to enable your WSL in Docker and now you have to pll the latest release of heudiconv.

        ```
        $ docker pull nipy/heudiconv:latest
        ```
**2. getting the dicominfo file:**
    Now you run heudiconv the first time on the first subject to receive the dicominfo file, which is needed to edited the heuristic.py according to the experiment.

        ```
        $ docker run --rm -it -v /mnt/d/Data:/base nipy/heudiconv:latest -d /base/Dicoms/sub-{subject}/*/*/*/* -o /base/NiFTi/ -f convertall -s 01 -c none --overwrite
        ```
    `docker run --rm`: calls docker

    `-v /mnt/d/Data:/base`:  mouths the path to my data and calls it bas

    `nipy/heudiconv:latest`: calls latest heudiconv

    `-d`:  is the path to my Dicom files, with the `/*/*/*/*` defining that they can be found 4 folders deep in the file structure

    `-o`: dfines my output folder

    `-f`: stands for the heuristic file, which will be used later to convert all other files

    `-s 01`: will step in for the place holder in `-d`

    `-c`: converter that is used, here none

    After running this command there is a hidden file in the NiFTi folder, from which you need to move the dicominfo.tsv into the NiFTi folder

    ```
    $ cp /mnt/d/Data/NiFTi/.heudiconv/01/info/dicominfo_ses-01.tsv /mnt/d/Data
    ```
3. ****






# References

[^1]: Gorgolewski, K., Auer, T., Calhoun, V. et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. Sci Data 3, 160044 (2016). https://doi.org/10.1038/sdata.2016.44S

[^2]: https://nifti.nimh.nih.gov/

[^3]: https://bids.neuroimaging.io/benefits.html#benefits

[^4]:Halchenko, Y., Goncalves, M., Velasco, P., Castello, M. V. di O., Ghosh, S., Salo, T., Hanke, M., II, J. T. W., Michael, Dae, Kent, J., Christian, H., Brett, M., Amlien, I., Gorgolewski, C., Lukas, D. C., Markiewicz, C., Tilley, S., Stadler, J., … Wagner, A. (2023). nipy/heudiconv: V0.12.0 (v0.12.0). Zenodo. https://doi.org/10.5281/zenodo.7662350

[^5]: Li, X., Morgan, P. S., Ashburner, J., Smith, J., & Rorden, C. (2016). The first step for neuroimaging data analysis: DICOM to NIfTI conversion. Journal of neuroscience methods, 264, 47–56. https://doi.org/10.1016/j.jneumeth.2016.03.001
