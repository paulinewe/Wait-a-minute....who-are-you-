# Neuroquery

Due to the problems mentions in the other chapters, I was not able to set up a machine learing approach. Nevertheless, I want to present some result to answer validate the results of the study my project is based on. So to answer where person identity informations are processed and stored, I used a metaanylsis tool called [Neuroquery](https://neuroquery.org/about).

## Meta-analysis with Neuroquery

Out there are many neuroscientific papers and each year they get more and more, so finding an answer to a specific question is quiet difficult to do manually. To find a way through the jungle of neuroscientific papers and make collecting and aggregating them faster, easier and automated, Dockès et al. [^1] developed Neuroquery.
What it does, is prediciting neural correlates of neuroscience concepts related to behavior, diseases, or anatomy. 
The predictive frameswork allows to generate brain maps by generalizing from excessively studied terms to less extensively studied terms, that are not accessible to traditional meta-analyses. Neuroquery works in a 'dynamic, contextually-informed way that allows for mutual interactions' (p.4). As a result high-quality brain maps are created for infrequently studied concepts. The maps predict spatial distributions of findings from which one can form regions of interest or interpret results of less studied terms. Yet it has to be noted, that the tool does not work with voxel-based null hypthesis. That being said, it is less suited to tell whether an area is activated during a study or not.

NeuroQuery is an accurate model of the literature' and approximates well results of actual experimental data collection. It works by modeling the semantic relations underling the vocabulary of neuroscience and makes use of techniques from natural language processing. It makes better use of available information and recovers biologically plausible brain maps. Due to the semantic model, Neuroquery is not so sensitive to variations in terminology and it captures semantic similarities, which helps find related concepts and explore their associations with brain activity. Neuroquery also supports researcher with exploration of the domain knowledge across sub-fields, generation new hypotheses, construction of regions of interest or putting results into perspektive. 

NeuroQuery is easily usable [online](https://neuroquery.org/query?text=music+listening) and the data and source code can be freely available. 

## Meta-analysis for the project

So to start with Neuroquery, I need to decicde on what terms I want to enter into the tool. For that we need to look back at the orginal paper. So what they wanted to look at ID-specific processing in the fusiform face area and occipital face area, using ambient images of celebrities and by generating and violating expectations about person ID, they tested if prediction error responses manifest in the neuroimaging signal. The study shows image-independent ID-specific adaptation effects in the FFA for famous familiar faces and in combination with the results of the OFA, the authors suggest that the ID representations in occipito-temporal regions are not yet completely clarified [^2]. 

> Baed on the paper and related, I expect that we will get a brain map that predicts high activation in FFA and OFA.

Based on that I decided on the following terms:
* face perception
* identity
* familiarity
* face recognition
* face
* preddiction error

![neuroquery](./images/neuroquery.png)

After entering the terms in Neuroquery, I got this table, the [brain map](/content/code/Brainmap.ipynb) with the predicted brain areas and a list of related papers.

Let's have a look at the table first.

### List of terms

Neuroquery builds a list of the term in your query, meaning the words recognized in the entered text and termns in expansion, so terms that are related to the entered ones. The table provides measures for similarity to the query and the weight in the brain map. Similarity to the query means the similarity of a term to terms in the query. It is modulated by how many times these terms are mentioned in the query and the measure is based on the co-occurrences of the terms in the literature[^3]. Face, face recognition, prediction error and face perception stand-out in terms of similiarity.
The weight in the brain map describes how much each term contributes to the [brain map](/content/code/Brainmap.ipynb). We see that the term face conributes mainly to the brain map, which is not a suprise as it captures everything regarding faces[^3]. Small contributions come from 'face recognition' and the related terms in the expansion from which the term 'ffa' contributes most.

### Evaluation of the literature 

The tool list the most relevant publications related to the query, but keep in mind that it is based on the articles it is trained on. (14,000 full-text publications and 400,000 peak activations).

Some of the literature captures more general the brain regions related to face recognition[^5][^7] [^9] [^10] [^13] [^18] [^21] and familiarity[^4][^6] [^8] [^12] and do not match the focus of the paper by Rostalski et al. 

There are some studies, that report similar activations as Rostalski et al. but using different approaches. There are studies [^11] using the repetion-priming paradigm. The authors conclude that the FFA showed only marginal effects of face familiarity and no reliable generalization across different face images. Rostalski et al. found, that FFA discriminates between identities independently of images, but like Pourtois et al., say that a fully image-invariant representation is probably not present in the FFA. Other studies using the fMRI-adaption paradigm and repetion-priming paragdim [^14] [^15] [^16] [^17] [^19] [^20] [^22] [^23] also found adaptation to facial identity and face-identity change effects in the FFA and the OFA, but not image-invariant adapation. Similar findings reported Rostalksi et al. between the adaption condition and the violation condition. The OFA was activated by conscious and non-conscious changes to face identity. 

To sum it up, the most studies provided by Neuroquery point in the same direction as the results of the paper by Rostalski et al. It has to be noted, that the eight papers are excluded, as they did not matched the relevant topics and concept this project is about.

![literaturelist](/content/markdown/images/litneuro.png)

# References

[^1]: Jérôme Dockès, Russell A Poldrack, Romain Primet, Hande Gözükan, Tal Yarkoni, Fabian Suchanek, Bertrand Thirion, Gaël Varoquaux (2020) NeuroQuery, comprehensive meta-analysis of human brain mapping eLife 9:e53385
https://doi.org/10.7554/eLife.53385

[^2]: Rostalski, S.-M., Robinson, J. E., Ambrus, G. G., Johnston, P., & Kovács, G. (2022). Person identity-specific adaptation effects in the ventral occipito-temporal cortex. European Journal of Neuroscience, 55( 5), 1232– 1243. https://doi.org/10.1111/ejn.15604 

[^3]: https://neuroquery.org/about

[^4]: Gobbini, M. I., & Haxby, J. V. (2006). Neural response to the visual familiarity of faces. Brain research bulletin, 71(1-3), 76–82. https://doi.org/10.1016/j.brainresbull.2006.08.003

[^5]: Zhen, Z., Fang, H., & Liu, J. (2013). The hierarchical brain network for face recognition. PloS one, 8(3), e59886. https://doi.org/10.1371/journal.pone.0059886

[^6]: Platek, S. M., & Kemp, S. M. (2009). Is family special to the brain? An event-related fMRI study of familiar, familial, and self-face recognition. Neuropsychologia, 47(3), 849–858. https://doi.org/10.1016/j.neuropsychologia.2008.12.027

[^7]: Huang, L., Song, Y., Li, J., Zhen, Z., Yang, Z., & Liu, J. (2014). Individual differences in cortical face selectivity predict behavioral performance in face recognition. Frontiers in human neuroscience, 8, 483. https://doi.org/10.3389/fnhum.2014.00483

[^8]: Olivares, E. I., Saavedra, C., Trujillo-Barreto, N. J., & Iglesias, J. (2013). Long-term information and distributed neural activation are relevant for the "internal features advantage" in face processing: electrophysiological and source reconstruction evidence. Cortex; a journal devoted to the study of the nervous system and behavior, 49(10), 2735–2747. https://doi.org/10.1016/j.cortex.2013.08.001

[^9]: Kurth, S., Moyse, E., Bahri, M. A., Salmon, E., & Bastin, C. (2015). Recognition of personally familiar faces and functional connectivity in Alzheimer's disease. Cortex; a journal devoted to the study of the nervous system and behavior, 67, 59–73. https://doi.org/10.1016/j.cortex.2015.03.013

[^10]: Ding, X. P., Fu, G., & Lee, K. (2014). Neural correlates of own- and other-race face recognition in children: a functional near-infrared spectroscopy study. NeuroImage, 85 Pt 1(0 1), 335–344. https://doi.org/10.1016/j.neuroimage.2013.07.051

[^11]: Pourtois, G., Schwartz, S., Seghier, M. L., Lazeyras, F., & Vuilleumier, P. (2005). View-independent coding of face identity in frontal and temporal cortices is modulated by familiarity: an event-related fMRI study. NeuroImage, 24(4), 1214–1224. https://doi.org/10.1016/j.neuroimage.2004.10.038

[^12]: Weibert, K., & Andrews, T. J. (2015). Activity in the right fusiform face area predicts the behavioural advantage for the perception of familiar faces. Neuropsychologia, 75, 588–596. https://doi.org/10.1016/j.neuropsychologia.2015.07.015

[^13]: Kumfor, F., Hutchings, R., Irish, M., Hodges, J. R., Rhodes, G., Palermo, R., & Piguet, O. (2015). Do I know you? Examining face and object memory in frontotemporal dementia. Neuropsychologia, 71, 101–111. https://doi.org/10.1016/j.neuropsychologia.2015.03.020

[^14]: Large, M. E., Cavina-Pratesi, C., Vilis, T., & Culham, J. C. (2008). The neural correlates of change detection in the face perception network. Neuropsychologia, 46(8), 2169–2176. https://doi.org/10.1016/j.neuropsychologia.2008.02.027

[^15]: Weibert, K., Harris, R. J., Mitchell, A., Byrne, H., Young, A. W., & Andrews, T. J. (2016). An image-invariant neural response to familiar faces in the human medial temporal lobe. Cortex; a journal devoted to the study of the nervous system and behavior, 84, 34–42. https://doi.org/10.1016/j.cortex.2016.08.014

[^16]: Mur, M., Ruff, D. A., Bodurka, J., Bandettini, P. A., & Kriegeskorte, N. (2010). Face-identity change activation outside the face system: "release from adaptation" may not always indicate neuronal selectivity. Cerebral cortex (New York, N.Y. : 1991), 20(9), 2027–2042. https://doi.org/10.1093/cercor/bhp272

[^17]: Dricot, L., Sorger, B., Schiltz, C., Goebel, R., & Rossion, B. (2008). The roles of "face" and "non-face" areas during individual face perception: evidence by fMRI adaptation in a brain-damaged prosopagnosic patient. NeuroImage, 40(1), 318–332. https://doi.org/10.1016/j.neuroimage.2007.11.012

[^18]: Nestor, A., Vettel, J. M., & Tarr, M. J. (2008). Task-specific codes for face recognition: how they shape the neural representation of features for detection and individuation. PloS one, 3(12), e3978. https://doi.org/10.1371/journal.pone.0003978

[^19]: Lai, J., Pancaroglu, R., Oruc, I., Barton, J. J., & Davies-Thompson, J. (2014). Neuroanatomic correlates of the feature-salience hierarchy in face processing: an fMRI -adaptation study. Neuropsychologia, 53, 274–283. https://doi.org/10.1016/j.neuropsychologia.2013.10.016

[^20]: Andrews, T. J., & Ewbank, M. P. (2004). Distinct representations for facial identity and changeable aspects of faces in the human temporal lobe. NeuroImage, 23(3), 905–913. https://doi.org/10.1016/j.neuroimage.2004.07.060

[^21]: Zhang, H., Tian, J., Liu, J., Li, J., & Lee, K. (2009). Intrinsically organized network for face perception during the resting state. Neuroscience letters, 454(1), 1–5. https://doi.org/10.1016/j.neulet.2009.02.054

[^22]: Axelrod, V., & Yovel, G. (2015). Successful decoding of famous faces in the fusiform face area. PloS one, 10(2), e0117126. https://doi.org/10.1371/journal.pone.0117126

[^23]: Eger, E., Schweinberger, S. R., Dolan, R. J., & Henson, R. N. (2005). Familiarity enhances invariance of face representations in human ventral visual cortex: fMRI evidence. NeuroImage, 26(4), 1128–1139. https://doi.org/10.1016/j.neuroimage.2005.03.010