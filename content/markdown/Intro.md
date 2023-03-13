# Introduction 
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](http://www.peerherholz.github.io/MSc05_template_repository/)
[![GitHub size](https://img.shields.io/github/repo-size/PeerHerholz/MSc05_template_repository)](https://github.com/repronim/OHBMEducation-2022/archive/master.zip)
[![GitHub issues](https://img.shields.io/github/issues/PeerHerholz/MSc05_template_repository?style=plastic)](https://github.com/PeerHerholz/MSc05_template_repository/issues)
[![GitHub PR](https://img.shields.io/github/issues-pr/PeerHerholz/MSc05_template_repository)](https://github.com/PeerHerholz/MSc05_template_repository/pulls)
[![License](https://img.shields.io/github/license/PeerHerholz/MSc05_template_repository)](https://github.com/PeerHerholz/MSc05_template_repository)

So before we dive in to what about what my project is all about, here are some information on the context of the project and the background of this site. 

## The Course 'Cognitive and Computational Neuroscience' 

Psychology students in there masters degree at [University of Frankfurt](https://www.uni-frankfurt.de/de?locale=de) take part in research internships as a part of there curriculum. As a student majoring in Cognitive Neuroscience, one could choose the course ['Cognitve and Computational Neuroscience: an introduction to machine/deep learning and neuro-data-science'](https://peerherholz.github.io/Cog_Com_Neuro_ML_DL/index.html). The goal of the course is to provide an understanding for research processes and practical tools to make research more sufficent, but also more transparent and enable replicability. All this is taught while introducing people to neuroscience and artificial intelligence. To get the most out of it, students are working on self-chosen experiements in which they apply their knowldege from the course. The course is/was taught and the projects were primarly supervised by [Michael Ernst](https://github.com/M-earnest) and [Peer Herholz](https://github.com/PeerHerholz).


## Whoru

Whoru...is short for 'Whor are you' and that is kind of the theme for my project work.
 
 <iframe src="https://giphy.com/embed/agmheddabICHK" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/my-post-agmheddabICHK">via GIPHY</a></p>

I am quite interested in face recognition and initailly wanted to add an fMRI assessment based on my bachelor thesis on [pattern separation](https://www.youtube.com/watch?v=P_G7HCNG-bI) of familiar and unfamiliar faces in cooperation with [Prof. Dr. Gyula Kovács from the University of Jena](http://cogsci.uni-jena.de/team/team-subpage-kovacs/). Unfortunately, for time, capacitiy  and practical reasons I had to cancel that idea (one of the difficulties I encountered, [see here](./Discussion.md#difficulties-and-throwbacks)).

Prof. Kovács was so kind to give access to another data set, from a different study on face recognition and that is the one I worked on during the course. It took a bit of organisational and bureaucratic work to get the data set...

... and that guys, is the story on how I finally got a data set!

<iframe src="https://giphy.com/embed/POlPO0U0KuwDu" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/bg-POlPO0U0KuwDu">via GIPHY</a></p>

### Background and Research Question
#### Face Recognition
Everyday we encounter many many different faces, which our brain has to process. Recognising and identifying faces is important to navigate through social situation. But how does it work?

Kovács [^1], for example, proposed that, it starts by getting familiar with an unfamiliar face on a purely visual level due to repeated visual exposure. At this stage we cannot retrieve any  information other than that we already have seen the person, but visual features and simple concepts (e.g. old/young, male/female) are encoded. Later we might gain contextual and associative information about the person, like the moments we met but also episodic informations and biographical semantic information about the person forms. The more knowledge we gather, the more detailed becomes the representation of the person in the brain thus it reaches a stages in which identification of a now well-known person becomes easier. Nevertheless the process of forming such a robust ID representation is still a mystery.
In face recognition task we can see that recognition for familiar faces is better than unfamiliar [^2]. Thus, is seems reasonable to assume, that they are not equally processed.

#### Relevant Brain Regions
There are some brain region responding mainly to faces. The central region for ID-specific information processing seems to be the fusiform face area (FFA), eventhough other regions are also involved to the process [^3][^4].Tsantani et al. [^5] showed also that the occipital face area (OFA) contains ID-specific information. But still the literature is not sure on how the representations in the face areas look like.

#### Research Question
The data used for this analysis comes from the paper "Person identity-specific adaptation effects in the ventral occipito-temporal cortex" [^4].  They aimed to investigate ID-specific processing in the fusiform and OFAs by using ambient images of celebrities and adopting the logic of the Johnston et al.[^6] onto a fMRI experiment. In their experiment participants underwent trials containing eight different images of a famous person, images of eight different famous persons or seven different images of a particular famous person followed by an identity change to violate potential expectation effects about person identity.

They showed, that the difference of highly variable, ambient images of the same versus different identities was only significant for the FFA. For the OFA they showed significantly lower activation for conditions where expectations are violated compared with alternating identities.

> Aim of Whoru: To get to a more detailed understanding of the differences between the conditions and the brain regions with a classification problem.




## References

[^1]:Gyula Kovács; Getting to Know Someone: Familiarity, Person Recognition, and Identification in the Human Brain. J Cogn Neurosci 2020; 32 (12): 2205–2225. doi: https://doi.org/10.1162/jocn_a_01627

[^2]:Bruce, V., Henderson, Z., Newman, C., & Burton, A. M. (2001). Matching identities of familiar and unfamiliar faces caught on CCTV images. Journal of Experimental Psychology: Applied, 7(3), 207–218. https://doi.org/10.1037/1076-898X.7.3.207

[^3]:Duchaine, B., & Yovel, G. (2015). A revised neural framework for face processing. Annual Review of Vision Science, 1, 393–416. https://doi.org/10.1146/annurev-vision-082114-035518

[^4]:Rostalski, S.-M., Robinson, J. E., Ambrus, G. G., Johnston, P., & Kovács, G. (2022). Person identity-specific adaptation effects in the ventral occipito-temporal cortex. European Journal of Neuroscience, 55( 5), 1232– 1243. https://doi.org/10.1111/ejn.15604 

[^5]:Tsantani, M., Kriegeskorte, N., Storrs, K., Williams, A. L., McGettigan, C., & Garrido, L. (2021). FFA and OFA encode distinct types of face identity information. The Journal of Neuroscience, 41, JN-RM-1449-20. https://doi.org/10.1523/jneurosci.1449-20.2020

[^6]:Johnston, P., Overell, A., Kaufman, J., Robinson, J., & Young, A. W. (2016). Expectations about person identity modulate the face-sensitive N170. Cortex, 85, 54–64. https://doi.org/10.1016/j.cortex.2016.10.002