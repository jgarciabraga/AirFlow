from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG('second_trigger_dag', description="Second DAG with trigger rule", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="exit 1")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(
        task_id="tsk3", bash_command="sleep 5", trigger_rule="one_failed")

    [task1, task2] >> task3
