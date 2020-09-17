from sys_user.models import SysUser
from domain.models import Domain
from contact_form.models import ContactForm
from django.db import models


class FetchRecord:

    def __init__(self, tablename):
        self.filter_string = {}
        self.exclude_string = {}
        self.table_name = tablename
        self.order_by_field = 'id'
        self.start = 0
        self.end = 0

    def table_object(self):
        if self.table_name == "SysUser":
            return SysUser
        if self.table_name == "Domain":
            return Domain
        if self.table_name == 'ContactForm':
            return ContactForm

    def add_query(self, *args):
        if len(args) == 2:
            self.filter_string[args[0]] = args[1]
        else:
            if args[1] == "!=":
                self.exclude_string[args[0]] = args[2]
            if args[1] == "<":
                self.filter_string[args[0]+"__lt"] = args[2]
            if args[1] == ">":
                self.filter_string[args[0]+"__gt"] = args[2]
            if args[1] == "contains":
                self.filter_string[args[0]+"__contains"] = args[2]

    def add_active_query(self):
        self.filter_string["active"] = True
        if self.table_name == "SysUser":
            self.filter_string['is_active'] = True

    def show_query(self):
        print(self.query)

    # def add_active_query(self):
    #     self.filter_string["is_active"] = True

    def add_encoded_query(self):
        pass

    def add_not_null_query(self, field):
        self.exclude_string[field] = ""

    def add_null_query(self, field):
        self.filter_string[field] = ""

    def order_by(self, field):
        self.order_by_field = field

    def order_by_desc(self, field):
        self.order_by_field = "-"+field

    def choose_window(self, start, end):
        self.start = start
        self.end = end

    def set_limit(self, limit):
        self.end = limit

    def get_id(self, sys_id):
        return self.table_object().objects.get(id=sys_id)

    def query(self):
        print(self.filter_string)
        print(self.exclude_string)
        if self.end != 0:
            result = self.table_object().objects.filter(
                **self.filter_string
            ).exclude(
                **self.exclude_string
            ).order_by(
                self.order_by_field
            )[
                self.start:self.end
            ]
        else:
            result = self.table_object().objects.filter(
                **self.filter_string
            ).order_by(
                self.order_by_field
            ).exclude(
                **self.exclude_string
            )
        return result




