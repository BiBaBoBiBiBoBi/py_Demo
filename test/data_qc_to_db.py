#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 16:59
# @Author  : Cheney.zhou
# @File    : data_qc
# @Software: PyCharm

file_path = r'data_qc_配置信息.xlsx'
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from urllib import parse

def pocess_db(table_name):
    df = pd.read_excel(file_path, sheet_name=table_name)
    df.columns = [i.strip() for i in df.columns]
    id_list = df['id'].unique()

    if table_name=='data_qc_recordsnew':
        df['qc_result_filename_pattern'] = 'QC_{#DataUpTo#}.xlsx'
        df['arima_result_filename_pattern'] = 'ARM_{#DataUpTo#}.xlsx'

        his_df = pd.read_sql("select id,arima_result_current_file_name,qc_result_current_file_name from "
                             "data_web_qc.data_qc_recordsNew",post_gres_engine)
        df = pd.merge(df,his_df,on=['id'],how='left')


    if not df.empty:
        qc_record_id = ', '.join(list(map(lambda x: "'%s'" % x, id_list)))
        post_gres_engine.execute(f"delete from data_web_qc.{table_name} where id in (%s)" % qc_record_id)
        print(f"delete from data_web_qc.{table_name} where id in (%s)" % qc_record_id)
        df.to_sql(name=table_name, schema='data_web_qc', con=post_gres_engine, chunksize=1000, if_exists='append',index=None)


if __name__ == '__main__':
    post_gres_engine = create_engine('mysql+pymysql://{user_name}:{password}@{server}:{port}/{database}'.format(
        user_name='swa_dev',
        password=parse.quote_plus('swa_dev@123'),
        server='10.0.42.8',
        port=3306,
        database='data_web_qc'
    ),pool_recycle=3600,
        connect_args={'connect_timeout': 60000, 'read_timeout': 60000, 'cursorclass': pymysql.cursors.SSCursor})

    pocess_db('data_qc_recordsnew')
    # pocess_db('data_qc_view_meta_infonew')



