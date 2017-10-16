# -*- coding: utf-8 -*-
__author__ = 'ivanov'

from sys import maxsize


class Contact:

#     def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.homephone = homephone
#         self.mobilephone = mobilephone
#         self.workphone = workphone
# #        self.secondaryphone = secondaryphone
#         self.id = id

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None,
                 address2=None, secondaryphone=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
