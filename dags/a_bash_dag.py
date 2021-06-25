try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from airflow.operators.bash_operator import BashOperator
    from datetime import datetime
    import pandas as pd
    import logging
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))


def first_function_execute():
    logging.info(" ====== first_function_execute ====== ")


with DAG(
        dag_id="a_bash_dag",
        template_searchpath="/opt/airflow/scripts",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },
        catchup=False) as f:

    t1 = BashOperator(
        task_id='my_bash_example',
        # "scripts" folder is under "/usr/local/airflow/dags"
        bash_command="echo 'Hello this is from BASH'")
