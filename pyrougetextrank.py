import os
import numpy as np
from pythonrouge import pythonrouge

path2model = 'path to model summary'
path2gold = 'path to reference summaries'
files = os.listdir(path2model)
final_mean = []
for i in files:
    gold_summ = os.listdir(path2gold+'/' + i.split('.txt')[0])
    with open(path2model + '/' + i,'r') as fmodel:
        textmodel = fmodel.read()
        fmodel.close()
    score = []
    for j in gold_summ:
        with open(path2gold + '/' + i.split('.txt')[0] + '/' + j,'r') as fgold:
            textgold = fgold.read()
            fmodel.close()
        score.append(pythonrouge.pythonrouge(textmodel, textgold)['ROUGE-1'])
    final_mean.append(np.max(score))
    print np.max(score)

print np.mean(final_mean)
print np.std(final_mean)
