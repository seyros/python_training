# -*- coding: utf-8 -*-
__author__ = 'ivanov'


from model.contact import Contact


def test_add_contact(app):
    contact = Contact(firstname="Аркадий", middlename="Семенович", lastname="Паровозов", nickname="parovoz",
                      title="Dr.", company="Sputnik", address="Moscow, Rumyantsevo district",
                      homephone="322223322", mobilephone="79991112233", workphone="84951999999",
                      fax="fax111222333", email="email1@gmail.com", email2="email2@gmail.com",
                      email3="email3@gmail.com", homepage="https://www.parovoziki.con",
                      address2="Moscow, Altufievo district", secondaryphone="84992223344",
                      notes="Один очень уважаемый человек")
    app.contact.create(contact)