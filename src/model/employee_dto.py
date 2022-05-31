import datetime
import mongoengine as me


class Employee(me.Document):
    employee_id = me.StringField(required=True)
    name = me.StringField()
    age = me.IntField()
    sex = me.StringField(max_length=1)
    email = me.StringField()
    date_modified = me.DateTimeField(default=datetime.datetime.utcnow)
    meta = {'collection': 'Employee', 'strict': False}


