from django.db import connection
from django.db.utils import OperationalError
from django.test import TestCase, Client

from hello_world.models import TableFirst, TableSecond


class HelloWorldTests(TestCase):
    def setUp(self) -> None:
        table_first = TableFirst.objects.create(field_first='Lorem Ipsum')
        second_texts = (
            """Lorem Ipsum is simply dummy text of the printing and typesetting industry.""",
            """Contrary to popular belief, Lorem Ipsum is not simply random text.""",
            """There are many variations of passages of Lorem Ipsum available""",
        )
        for second_text in second_texts:
            TableSecond.objects.create(
                field_second=second_text,
                table_first=table_first
            )

    def test_db_connection(self):
        try:
            cursor = connection.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True
        self.assertEqual(connected, True)

    def test_hello_world(self):
        cursor = connection.cursor()
        cursor.execute("""SELECT `field_first` FROM `hello_world_tablefirst` LIMIT 1""")
        field_first = cursor.fetchone()
        # Normalize data fields first
        field_first = field_first[0]

        cursor.execute("""SELECT `field_second` FROM `hello_world_tablesecond` WHERE `table_first_id` = 1""")
        fields_second = cursor.fetchall()
        # Normalize data fields second
        fields_second = [i[0] for i in fields_second]

        client = Client()
        response = client.get('/hello-world/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Simple project')
        self.assertEqual(response.context['field_first'], field_first)
        self.assertEqual(response.context['fields_second'], fields_second)
