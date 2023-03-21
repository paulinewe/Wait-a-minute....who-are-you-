# Preprocessing and Qualitiy Control

Capacity and time limits stopped me from doing preprocessing, as my laptop already was working on its limits during the conversion and after that I had to move a way from Frankfurt so I also was not able to do it in the Lab. Nevertheless I will describe, what I would have done to preprocess my data on a local machine. To do so, I want to introduce you to [fMRIprep](https://fmriprep.org/en/stable/) and [MRIQC](https://mriqc.readthedocs.io/en/latest/). 

## Qualitiy Control with MRIQC

Visual inspection of fMRI is error-prone and unpractical the more images are part of a data set, therefore is an automated tool developed for robust and accurate qualitiy assessment. It extractes image quality metrics from structural and functional MRI data. Using this tool helps to filter and descide on the further usage or exclusion of participants images.

### Principles

The developement of the tool is based on the following principles [^1]:

1. **Modularity and integrability**

    The workflow of MRIQC integrates sub-workflows that based on third party software toolboxes such as FSL, ANTs and AFNI.

2. **Minimal Preprocessing**

    The workflow should be as minimal as possible to estimate the image qualitiy metrics from original data or minimally processed data.

3. **Interoperability and standards**

    MRIQC follows the BIDS stanardization.

4. **Reliability and robustness**

    The tool is reqularly checked for its robustness against data variablity as well as its reliability.

### Requirements

* [Docker Desktop](https://docs.docker.com/desktop/windows/wsl/)
* Ubuntu 20.04 LTS or any latest version or WSL
* data set in BIDS format

### Running MRIQC with Docker

*following the [documentation of MRIQC](https://mriqc.readthedocs.io/en/latest/running.html) and [BIRC Computing Guide](https://bircibrain.github.io/computingguide/docs/fmri-preprocessing/mriqc.html)*

1. **Setting up the environment**

    As in the [conversion](./BIDS-Conversion.md/#dicom-conversion) Docker comes in handy for the qulaitiy control of the brain images. Therefore is is necessary to pull the corresponding container.

    ```
    docker run -it nipreps/mriqc:latest --version
    ```
    You will need to have your 'BIDS-data' in a seperate folder and a one for the output.

2. **Quality Control for Subjects**

    Now the analysis for all `subjects` can be done with the following command:

    ```
    docker run -it --rm -v /mnt/d/Data/Nifti:/data:ro -v /mnt/d/Data/QC:/out nipreps/mriqc:latest /data /out participant
    ```
    If you want to analysis particular subjects, you can specify with `--participant_label`.

3. **Quality Control on Group-Level**

    After running MRIQC for all subjects, the group level report can be generated.

    ```
    docker run -it --rm -v /mnt/d/Data/Nifti:/data:ro -v /mnt/d/Data/QC:/out nipreps/mriqc:latest /data /out group
    ```
The process of MRIQC can be fully customized, [see](https://mriqc.readthedocs.io/en/latest/running.html)

4. **Outputs**

     *Individual reports*: MRIQC generates individual reports with mosaic views of a number of cutting planes and additional information. Based on that you can visualize those images flagged as low-quality by the classifier and sort them out.
    
    *Group report*: shows a scatter plot for each of the image qulaitiy measures from which it is  easy to identify outliers for each metric. The plots are interactive and by clicking on a sample the corresponding individual report appears.

## Preprocessing with fMRIprep

To preprocess task-based or resting-state functional fMRI is fMRIprep a robust open-source application, providing piplines to preprocess the relevant data. 

### Principles
It has three core strengths of fMRIprep [^2] [^3]:

1. **Robustness**

    The pipeline adapts according to the input data without great loss in quality of outputs, meaning the results are as good as possible independently of scanner, scanning parameters or additional correction scans.

2. **Ease of Use**

    fMRIprep is based on BIDS standard, which results in minimal input from the user and allows an automated process.

3. **“Glass box” philosophy**

    Eventhough the process is automated, it provides the user with visual reports on each subject with all details on on the processing steps, allowing to understand the method and supports deciding on which subjects should be kept for group level analysis. Additionally there is extensive [documentation](https://fmriprep.org/en/stable/) avialable.

### Requirements

* [Docker Desktop](https://docs.docker.com/desktop/windows/wsl/)
* Ubuntu 20.04 LTS or any latest version or WSL
* data set in BIDS format

### Running fMRIprep with Docker

*following the tutorial from [Lukas Snoek](https://lukas-snoek.com/NI-edu/fMRI-introduction/week_4/fmriprep.html) and [BIRC Computing Guide](https://bircibrain.github.io/computingguide/docs/fmri-preprocessing/fmriprep.html)*

1. **Setting up the enviroment**

    Again, it is possible to install fMRIprep via Docker by installing the container. Installing fMRIprep to Docker can simplely be done with the following command:

    ```
    pip install fmriprep-docker
    ```
    In order to run surface processing features the [FreeSurfer license](https://surfer.nmr.mgh.harvard.edu/fswiki/License) needs to be downloaded. Just put it in a code folder (use the one from the conversion) inside your Nifti folder.

2. **Preprocessing**

    To start preprocessing the data, use the following command. Provide the BIDS-folder that should be preprocessed, an output folder and add the license.
    
    ```
    fmriprep-docker /mnt/d/Data/Nifti /mnt/d/Data/prepro --fs-license-file /mnt/d/Data/Nifti/code/license.txt
    ```
    As nothing further is specified, fMRIprep will preprocess everthing in the Nifti folder. For running only specific participants or task, flags cn be added (e.g.`--participant 01 --task localizer`). You can also instruct fMRIprep to ignore things with `--ignore xyz`.

    **Performance**
    Next to what and what not to process, fMRIpreps performance can be adapted depending on the machine your are running it and to parallelize the preprocessing. With `--nthreads` and `--omp-nthreads` parameters, you can decide on how many threads of your computer are used for fMRIprep. Also the RAM that is used can be specified with `--mem_mb` parameters, which is necessary if you parallelize a lot.

    **Output spaces**
    Witn the --output-spaces flag you can tell Fmriprep to what spaces you want your preprocessed data registered, like registering your functional data to the participant’s T1 scan (that is called registration). In addition, you can also specify a standard template, like the MNI template for spatial normalization.

    <details>
    <summary>Registration and Normalization </summary>
    <p> The human brain is in general quit similiar between people, but  there are still differences in siza and shape and to perform group-level analysis it is necessary to ensure that the voxels in brain A represent the same structure in brain B. Therefore the brain images need to be normalized and registered. For normalization, firstly the anatomical brain image is matched to a template with standard dimensions and coordinates. The transformations can then be applied to the functional scan, so that anatomical nd functional are aligned, which is called registration.
    
    https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/Preprocessing/Registration_Normalization.html#normalization-smoothing-and-statistical-power
    </p>
    </details>

    All other possiblities can be found [here](https://fmriprep.org/en/stable/usage.html).

3. **Outputs**

    For output fMRIprep provides a directory for each subject with the figures from the preprocessing stages, the preprocessed anatomical and functional files and a summary and all figures in a HTML-file.


## References

[^1]: Esteban O, Birman D, Schaer M, Koyejo OO, Poldrack RA, Gorgolewski KJ; MRIQC: Advancing the Automatic Prediction of Image Quality in MRI from Unseen Sites; PLOS ONE 12(9):e0184661; doi:10.1371/journal.pone.0184661.

[^2]:Esteban, O., Markiewicz, C.J., Blair, R.W. et al. fMRIPrep: a robust preprocessing pipeline for functional MRI. Nat Methods 16, 111–116 (2019). https://doi.org/10.1038/s41592-018-0235-4

[^3]:Esteban, O., Ciric, R., Finc, K. et al. Analysis of task-based functional MRI data preprocessed with fMRIPrep. Nat Protoc 15, 2186–2202 (2020). https://doi.org/10.1038/s41596-020-0327-3


