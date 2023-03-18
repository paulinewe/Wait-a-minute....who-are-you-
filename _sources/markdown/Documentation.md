# Documentation

##  Evaluation of Data Set

As mentioned in the [Intro](./Intro.md) I recieved my data from Prof. Dr. Gyula Kovács at University of Jena. I was provided with access to there server to download the dataset.
Unfourtunately the raw data is not available freely, that's why I am can only present what is legally possible and therefore reproducing is limited. Nevertheless, extraced fMRI data and code from the originial study by Rostalski et al. (2022) is available at OSF (https://osf.io/m3pwt/). 

The data set consists of functional magnetic resonance imaging (fMRI) scans from a face recognition task for 30 participants. For scanning a three Tesla MR Scanner (Siemens Prisma fit) was used. Functional data was obtained using an Echo Planar Imaging (EPI) Sequence (35 slices; TR = 2000 ms; TE = 30 ms; flip angle = 90°; 64*64 matrices; in-plane resolution: 3 × 3 mm2; slice thickness: 3 mm).  and magnetisation-prepared rapid gradient-echo sequence (MP-RAGE; TR = 2300 ms; TE = 3,03, 1 mm isotropic voxel size) was used to acquire high-resolution T1-weighted sagittal images for structual 3D images. For all images they used a 20-channel head coil. 

The data did not come in BIDS standard. So in order to make working more easily, effectively and understandable for others I had to [convert](./BIDS-Conversion.md) it, which was quite time consuming. Due to data not being published online, all work needed to be done locally, which makes the small sample size an advantages, as some things could be done on a ordinary laptop but on the other hand this puts limits on what can be done in terms of machine-learning-because of the sample size, but also the possbilities with my own laptop. So the project is more or less reduced to getting to know the workflows and programms to prepare the data, whether than setting up an algorithm. If you want to analyze it with an algorithm it is more suited to use an already trained one, than use it as a base to train an algorithm. For that it would need a huge amount more subjects.

Nevertheless, the data is useful and the experimental paradigm interesting plus with more subjects it probably provides a lot of information on face recognition areas to unravel.

## Version control

To keep on track with everything which has be done, it is important to ensure some form of version control. It is also important to have a backup and GitHub is one practical tool to use for version control. GitHub is a webbased hosting service. On Github you create a local folder structure in a respository in which you can push the changes made in the local files or you can pull respositories from other onto your local machine to work on them. Github also allows to add different branches, so that you changes not all happen on your master branch and later you merge branches together. Next to all the version controll, it is a platform where you can easily work with others on a project and get help. That not being enough, hosting this website is also possible through Github.

[.... my github respository](https://github.com/paulinewe/Whoru).

## Literature

Organizing literature and citing can be done by using a reference management software. The one I used ist Zotero Libary, which is a free and open-source software. Due to its browser add-on, adding ressources to your library is done in secounds as it automatically extracts metadata, but you can also upload e.g. BibTex formats.

[....what I read](https://www.zotero.org/groups/4721790/whoareu)

## Open Lab Notebook

When you push things to GitHUb you should add a commit message, idicating what changes took place. For a more detailes description on what was done, it is recommended to write an open lab notebook. In this notebook you can document, what you did, what your goals are, what problems appeared, update monthly/weekly/daily etc... endless possiblities.

I decided to provide monthly updates. They contained what ruff summary of the month before, updates for every week of the month, problems and task for the following month.

[....what I did when](https://github.com/paulinewe/Whoru/tree/main/open_lab_notebook/pages)

# Computational Environment

To be able to run a code of someody else, you need the computational environment in which the code was created. This consits of all modules etc. that where used. 

[....the environment](https://github.com/paulinewe/Whoru/tree/main/content/code)

>Disclaimer: as the data is not freely available, reproducing my steps is not possible :/

## OSF

OSF is an open-source online platform to register and manage projects. Here you can also document your progress, share projects and you ressources. It is a place where all the above mentioned programmes can be integrated and so the latest updates automatically are documented in the OSF project.

[.... overview on my OSF project](https://osf.io/aenpr/?view_only=026c7375139f4cceb16d0242692d7092)

