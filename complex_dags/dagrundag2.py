from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG('dag_run_dag_2', description="DAG RUN DAG 2", schedule_interval=None,
          start_date=datetime(2023, 1, 1), catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)


task1 >> task2

