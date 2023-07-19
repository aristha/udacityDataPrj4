import datetime
import os
from airflow import DAG
from udacity.common.CreateTbale import SqlInsert
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from udacity.common.initTable import InitTableOperator
dag = DAG('tablecreation_dag',
          description='Drop and Create tables in Redshift using airflow',
          schedule_interval=None, #'0 * * * *'
          start_date=datetime.datetime(2023, 7, 18, 0, 0, 0, 0)
        )

CREATE_artists_tables_task = InitTableOperator(
    task_id="CREATE_artists",
    
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_artists
)
CREATE_songplays_tables_task = InitTableOperator(
    task_id="CREATE_songplays",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_songplays
)
CREATE_songs_tables_task = InitTableOperator(
    task_id="CREATE_songs",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_songs
)
CREATE_staging_events_tables_task = InitTableOperator(
    task_id="CREATE_staging_events",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_staging_events
)
CREATE_staging_songs_tables_task = InitTableOperator(
    task_id="CREATE_staging_songs",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_staging_songs
)

CREATE_time_tables_task = InitTableOperator(
    task_id="CREATE_time",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_time
)
CREATE_users_tables_task = InitTableOperator(
    task_id="CREATE_users",
    dag=dag,
    redshift_conn_id="redshift",
    sql=SqlInsert.CREATE_users
)
