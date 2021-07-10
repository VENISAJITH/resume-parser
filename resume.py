from logging import error
import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import connection
from mysql.connector import cursor
import warnings
import en_core_web_sm
import PyPDF2
import nltk
import os
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.sql.functions import user
nlp=en_core_web_sm.load()
warnings.filterwarnings('ignore')
from pyresparser import ResumeParser
try:
    data = ResumeParser('./resume.pdf').get_extracted_data()
    dic=[]
    dic.append(data)
    d={}
    d=dic
    df=pd.DataFrame(d)
    print(df)
except Error as f:
    print(f)

