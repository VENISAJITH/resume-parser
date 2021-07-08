import warnings
warnings.filterwarnings('ignore')
import en_core_web_sm
nlp=en_core_web_sm.load()
import PyPDF2
import os
import nltk
from pyresparser import ResumeParser
dic=[]
data=ResumeParser('resume.pdf').get_extracted_data()
data
dic.append(data)
dic
import pandas as pd
d={}
d=dic
df=pd.DataFrame(d)
df
