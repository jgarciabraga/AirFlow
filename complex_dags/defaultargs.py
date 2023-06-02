from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
  'depends_on_past': False,
  'start_date': datetime(2023, 3, 5),
  'email': ['test@test.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(seconds=10)
}

dag = DAG('defaultargs', 
          description="DAG example with default args", 
          default_args = default_args,
          schedule_interval = None,
          start_date = datetime(2023, 1, 1), 
          catchup = False,
          tags = ['processo', 'tag', 'xcom'])

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

task1 >> task2 >> task3