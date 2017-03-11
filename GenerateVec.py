# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn.decomposition import PCA

import settings
from gensim.models import Word2Vec

filename_vec = 'Word60.model'
#vecfilename = settings.basepath+settings.filename_vec
model =  Word2Vec.load(filename_vec)

def trans_sentence2matrix(sentence):
