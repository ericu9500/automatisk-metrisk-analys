# automatisk-metrisk-analys
Repository for a metrical project within the fall-semester "Pandora" seminary series on machine learning and Ancient Greek at Uppsala university.[^1]



I've put together a number of small tools related to the Levenshtein distance between metrical lines in the corpus. Trivially, ```levenshtein_exe.py``` can be used to just find the metric lines most Levenshtein-similar to a given line. There are innumerable usecases for this metric, e.g. tracking rhythmic intertextuality, confirming rhythmic genre conventions etc. If you ```chmod +x``` and run e.g.

```
levenshtein_exe.py "u-u-u-u-u-u-"
```
it will output the ten Levenshtein-closest lines in the corpus. 




[^1]: In the below I will take for granted the file structure of the ```master``` branch of the present repository, i.e. all mentions of scripts will be relative this folder structure. Specifically, all scripts will tacitly draw upon the corpus of txt-files in the folder [hypotactic_txts_greek](hypotactic_txts_greek) if unless otherwise stated. 
