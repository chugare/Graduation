# coding:utf-8
import sys
import settings
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
from gensim.models import Word2Vec
class PreOperation:

    basepath = settings.basepath
    filename_source = settings.filename_sourcef
    filename_seg = settings.filename_seg
    filename_vec = settings.filename_vec
    # 合并所有评论文件
    _model = None
    def gather_data(self,flist):
        df = open(self.basepath+'gathered_file.txt', 'wb')
        for offsetpath in flist:
            try:
                f = open(self.basepath+offsetpath,'r')
            except IOError:
                continue
            for line in f:
                df.write(line)
    # 分词
    def segment(self):
        fin = open(self.basepath + self.filename_source, 'r')
        fout = open(self.basepath + self.filename_seg, 'wb')
        for line in fin:
            fout.write(' '.join(jieba.cut(line,cut_all=False)))

        fout.close()
        fin.close()
    # 生成向量--
    # 1打开模型文件，并输入给公共变量
    def open_model(self,filename):
        self._model = Word2Vec.load(filename)

    def generate_vec(self,f):
    # 输入：打开的文件
        if self._model is None:
            print 'Have not initial model,use open_model(filename) first'
        article = None

        for line in f:
            if article is None:
                article = str(line)
                continue
            wl = jieba.cut(line)

    flist = []
    for i in range(0, 203):
        flist.append(str(i)+'.txt')
    gather_data(flist)
    segment()
