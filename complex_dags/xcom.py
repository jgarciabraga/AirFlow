from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
  'depends_on_past': False,
  'start_date': datetime(2023, 3, 5),
  'email': ['test@test.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'tags': ['processo', 'tag', 'pipeline'],
  'retry_delay': timedelta(seconds=10),
}

dag = DAG('xcom', 
          description="DAG example with xcom", 
          default_args = default_args,
          schedule_interval=None,
          start_date=datetime(2023, 1, 1), 
          catchup=False)

def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1', value = 10200)

task1 = PythonOperator(task_id="tsk1", python_callable=task_write, dag=dag)

def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f'Valor informado {valor}')

task2 = PythonOperator(task_id="tsk2", python_callable=task_read, dag=dag)

task1 >> task2
