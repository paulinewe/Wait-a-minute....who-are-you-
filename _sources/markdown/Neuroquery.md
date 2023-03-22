# Neuroquery

Due to the problems mentions in the other chapters, I was not able to set up a machine learing approach. Nevertheless, I want to present some result to answer validate the results of the study my project is based on. So to answer where person identity informations are processed and stored, I used a metaanylsis tool called [Neuroquery](https://neuroquery.org/about).

## Metaanlysis with Neuroquery

Out there are many neuroscientific papers and each year they get more and more, so finding an answer to a specific question is quiet difficult to do manually. To find a way through the jungle of neuroscientific papers and make collecting and aggregating them faster, easier and automated, Dockès et al. [^1] developed Neuroquery.
What it does, is prediciting neural correlates of neuroscience concepts related to behavior, diseases, or anatomy. 
The predictive frameswork allows to generate brain maps by generalizing from excessively studied terms to less extensively studied terms, that are not accessible to traditional meta-analyses. Neuroquery works in a 'dynamic, contextually-informed way that allows for mutual interactions' (p.4). As a result high-quality brain maps are created for infrequently studied concepts. The maps predict spatial distributions of findings from which one can form regions of interest or interpret results of less studied terms. Yet it has to be noted, that the tool does not work with voxel-based null hypthesis. That being said, it is less suited to tell whether an area is activated during a study or not.

NeuroQuery is an accurate model of the literature' and approximates well results of actual experimental data collection. It works by modeling the semantic relations underling the vocabulary of neuroscience and makes use of techniques from natural language processing. It makes better use of available information and recovers biologically plausible brain maps. Due to the semantic model, Neuroquery is not so sensitive to variations in terminology and it captures semantic similarities, which helps find related concepts and explore their associations with brain activity. Neuroquery also supports researcher with exploration of the domain knowledge across sub-fields, generation new hypotheses, construction of regions of interest or putting results into perspektive. 

NeuroQuery is easily usable [online](https://neuroquery.org/query?text=music+listening) and the data and source code can be freely available. 

## Meta-analysis for the project




[^1]: Jérôme Dockès, Russell A Poldrack, Romain Primet, Hande Gözükan, Tal Yarkoni, Fabian Suchanek, Bertrand Thirion, Gaël Varoquaux (2020) NeuroQuery, comprehensive meta-analysis of human brain mapping eLife 9:e53385
https://doi.org/10.7554/eLife.53385
