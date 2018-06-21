# -*- coding: utf-8 -*-
from django.db import connection


class Hobby:

    def __init__(self):
        self.cursor = connection.cursor()

    def select_hobby_list(self, condition):
        sql = """
            SELECT GUITAR_ID,IMG,TITLE,DESCR FROM HOBBY_GUITAR 
        """
        if condition != "":
            sql += """
                    WHERE LOCATE(%s,TITLE)
            """
            self.cursor.execute(sql, (condition,))
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
