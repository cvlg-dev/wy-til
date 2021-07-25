import pymssql
import time
import re

import kss

from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp

# -*- coding:utf-8 -*-

import pandas as pd
import pymssql
from tqdm import tqdm

class MssqlExecutor:
    '''
    Mssql instance which receives database information from config_data.
    '''
    def __init__(self) -> None:

        self.username = ''
        self.password = ''

        self.server = ''
        self.dbname = ''
        self.conn = pymssql.connect(self.server, self.username, self.password, self.dbname)

    def query_from_db(self, sql_query: str) -> pd.DataFrame:
        '''
        Query from Mssql database

        Parameters
        ----------
        sql_query : str
            MS SQL query statement

        Returns
        -------
        query_output : pd.DataFrame
            Tabular dataset as a result of query, in pandas datafrmae format.

        '''
        # query to MSSQL DB
        query_output = pd.read_sql(sql_query, self.conn)
        return query_output


    def insert_row_to_db(self, dbname, tbname, row: tuple):
        cur = self.conn.cursor()

        if 'nan' in str(row):
            row = str(row).replace('nan', 'NULL')
        if 'None' in str(row):
            row = str(row).replace('None', 'NULL')
        query = "INSERT INTO [{}].[dbo].[{}] VALUES {};".format(dbname, tbname, str(row))

        cur.execute(query)
        self.conn.commit()


    def insert_df_to_db(self, dbname, tbname, dataframe, progress_bar = True):
        data = [tuple(x) for x in dataframe.values]
        if progress_bar:
            iterator = tqdm(data)
        else:
            iterator = data

        for i in iterator:
            cur = self.conn.cursor()
            # If including NULL value in dataframe
            if 'nan' in str(i):
                i = str(i).replace('nan', 'NULL')
            if 'None' in str(i):
                i = str(i).replace('None', 'NULL')
            query = "INSERT INTO [{}].[dbo].[{}] VALUES {};".format(dbname, tbname, str(i))

            cur.execute(query)
            self.conn.commit()

    def execute_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()



def extract_sentences(text):
    return kss.split_sentences(text)


def get_key_sentences(tup):
    sentence_list = []
    print(tup[0])
    if tup[1]['str_content'] is not None:
	    for s in extract_sentences(tup[1]['str_content']):
	        try:
	            re.search(r'|'.join([a for a in tup[1]['alias_matched'].split(', ')]), s).group()
	        except AttributeError:
	            pass
	        else:
	            sentence_list.append(s)
    return ' '.join(sentence_list)




if __name__ == "__main__":
	db_handler = MssqlExecutor()
	df = db_handler.query_from_db("select * from ana_ra_news_alias_matched")



	st_time = time.time()

	final_result = []
	with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
	    print("Max worker count is {}".format(mp.cpu_count()))

	    procs = []
	    for row in df.iterrows():
	        procs.append(executor.submit(get_key_sentences, row))
	    
	    for p in as_completed(procs):
	        final_result.append(p.result()) 	


	ed_time = time.time()
	print("Duration: {}".format(ed_time - st_time))	        
	print(len(final_result))
	print(final_result[0])
	print("################")
	print(final_result[1])
	print("################")
	print(final_result[2])
	print("################")
	print(final_result[3])
	print("################")
	print(final_result[4])