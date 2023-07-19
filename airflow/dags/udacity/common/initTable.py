from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class InitTableOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 sql = "",
                 *args, **kwargs):

        super(InitTableOperator, self).__init__(*args, **kwargs)
        # Map params here
        self.redshift_conn_id = redshift_conn_id
        self.sql = sql

    def execute(self, context):
        self.log.info('\n*** InitTableOperator: Loading Table started')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        redshift.run(self.sql)
        self.log.info("*** Table: Complete ***\n")
