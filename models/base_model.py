#!/usr/bin/python3
'''
Defines the 'BaseModel' class

Atributtes:

    id = a id generated by the 'uuid.uuid4()' function
    update_at = last save hour
    created_at = created date

Methods:

    save: Save the last changes and update the 'update_at' value
    to_dict: Return a dict with all the attributes and add one more:
                '__class__': store the class name


    string representation: [<class name>] (<self.id>) <self.__dict__>
'''

import models
import datetime
import uuid


class BaseModel:
    '''
Parent class to assing id and avoid any redundancy in the code

Atributtes:

    id = a id generated by the 'uuid.uuid4()' function
    update_at = last save hour
    created_at = created date

Methods:

    save: Save the last changes and update the 'update_at' value
    to_dict: Return a dict with all the attributes and add one more:
                '__class__': store the class name

'''

    def __init__(self, *args, **kargs):
        '''
Initialize the class with the default values or the kargs ones
'''

        if kargs is None or len(kargs) < 1:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.datetime.now()
            self.created_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kargs.items():
                if key == '__class__':
                    continue
                elif key in {'updated_at', 'created_at'}:
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        '''
Return the info of the object in a string

String representation: [<class name>] (<self.id>) <self.__dict__>        
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
Update the object and actualize the 'updated_at' date.

The date in the object will be 'datetime.datetime' type
'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
Return a dictionary with all the object information,
the dates change to str type

Add a new argumment called '__class__' with the class name
'''
        a = {}
        for key, arg in self.__dict__.items():
            if key in {'updated_at', 'created_at'}:
                a.update({key: arg.isoformat()})
            else:
                a.update({key: arg})
        a.update({'__class__': self.__class__.__name__})
        return a
