from sys_user.models import SysUser
from django.db import models


class FetchRecord:

    def __init__(self, tablename):
        self.filter_string = {}
        self.exclude_string = {}
        self.tablename = tablename

    i = 12345

    def table_object(self):
        if self.tablename == "SysUser":
            return SysUser

    # def lprint(self):
    #     query = self.table_object().objects.get(id=1)
    #     print(query)

    def add_query(self, field, value):
        self.filter_string[field] = value

    def show_query(self):
        print(self.query)

    def add_active_query(self):
        self.filter_string["active"] = True

    def add_encoded_query(self):
        pass

    def add_not_null_query(self, field):
        self.exclude_string[field] = ""
        pass

    def add_null_query(self, field):
        self.filter_string[field] = ""

    def choose_window(self):
        pass

    def set_limit(self):
        pass

    def query(self):
        print(self.filter_string)
        print(self.exclude_string)
        a = self.table_object().objects.filter(**self.filter_string).exclude(**self.exclude_string)
        print(a)




