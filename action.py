from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import psycopg2
from pprint import pprint

import datetime

class GetProduct(Action):
    def name(self):
        return "utter_ask_product"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_ask_product")
        return []

class Greet(Action):
    def name(self):
        return "utter_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet")
        return []

class Policy(Action):
    def name(self):
        return "utter_check_policy"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_check_policy")
        return []

class Positive(Action):
    def name(self):
        return "utter_positive"

    def run(self, dispatcher, tracker, domain):
        phone=distaptcher.get_slot("brand")
        dispatcher.utter_message("Yes, we have a {} available".format(phone))
        return []

class FAQ(Action):
    def name(self):
        return "utter_check_faq"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_check_faq")
        return []

class Paymentquery(Action):
    def name(self):
        return "utter_payment_query"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_payment_query")
        return []

class Registrationquery(Action):
    def name(self):
        return "utter_registration_query"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_registration_query")
        return []

class Packagequery(Action):
    def name(self):
        return "utter_package_query"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_package_query")
        return []

class Postquery(Action):
    def name(self):
        return "utter_post_query"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_post_query")
        return []

class Bye(Action):
    def name(self):
        return "utter_bye"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_bye")
        return []

class Confirm(Action):
    def name(self):
        return "utter_confirm"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_confirm")
        return []

class utter_invoice_id(Action):
    def name(self):
        return "utter_invoice_id"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_invoice_id")
        return []

class Getproductprice(Action):
    def name(self):
        return "get_product_price"
    
    def run(self, dispatcher, tracker, domain):        
        try:
            db = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
            db.autocommit = True
            cursor = db.cursor()

        except:
            print('Unable to fetch data')
            
        
        phone=tracker.get_slot('model')
        q="SELECT price FROM phones WHERE model_name = '{}'".format(phone)
        cursor.execute(q)
        results = cursor.fetchall()
        
        if(results!=[]):
            dispatcher.utter_message("The price of {} is ${}".format(phone, results[0][0]))       
            return [SlotSet('price',results[0][0])]

        elif(results==[]):
            dispatcher.utter_message("Sorry we do not have one of those available")
            return []


class Getproductstorage(Action):
    def name(self):
        return "get_product_storage"
    
    def run(self, dispatcher, tracker, domain):        
        try:
            db = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
            db.autocommit = True
            cursor = db.cursor()

        except:
            print('Unable to fetch data')
            
        
        phone=tracker.get_slot('model')
        q="SELECT storage_size FROM phones WHERE model_name = '{}'".format(phone)
        cursor.execute(q)
        results = cursor.fetchall()
        
        if(results!=[]):
            dispatcher.utter_message("The storage capacity of {} is {}".format(phone, results[0][0]))       
            return [SlotSet("ROM", results[0][0])]

        elif(results==[]):
            dispatcher.utter_message("Sorry we do not have one of those available")
            return []

class Getproductcolor(Action):
    def name(self):
        return "get_product_color"

    def run(self, dispatcher, tracker, domain):
        try:
            db = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
            db.autocommit = True
            cursor = db.cursor()

        except:
            print('Unable to fetch data')

        phone=tracker.get_slot('model')
        q="SELECT product_color FROM phones WHERE model_name = '{}'".format(phone)
        cursor.execute(q)
        results = cursor.fetchall()
        if(results!=[]):
            dispatcher.utter_message("The available color is {}".format(results[0][0]))
            return [SlotSet("color", results[0][0])]

        elif(results==[]):
            dispatcher.utter_message("Sorry we do not have one of those available")
            return []

class ConfirmBuy(Action):
    def name(self):
        return "confirm_buy"

    def run(self, dispatcher, tracker, domain):
        try:
            db = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
            db.autocommit = True
            cursor = db.cursor()

        except:
            print('Unable to fetch data')

        phone = tracker.get_slot("model")
        if(phone==""):
            dispatcher.utter_message("Please specify your product")
            return []
        q = "SELECT * FROM phones WHERE model_name = '{}'".format(phone)
        cursor.execute(q)
        results = cursor.fetchall()
        if(results!=[]):
            dispatcher.utter_message("The product is available\nHere is the link: ")
            return []
  
        elif(results==[]):
            dispatcher.utter_message("Sorry we do not have one of those available")
            return []

class Forwardcomplain(Action):
    def name(self):
        return "forward_complain"

    def run(self, dispatcher, tracker, domain):
          
        try:
            db = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
            db.autocommit = True
            cursor = db.cursor()

        except:
            print('Unable to fetch data')

        invoice = tracker.get_slot("invoice_id")
         
        if(invoice==""):
            dispatcher.utter_message("Please give us your invoice_ID")
            return []

        elif(invoice!=""):
            time= str(datetime.datetime.now())[11:19]
            date= str(datetime.datetime.now())[0:10]
                                             #obj   obj   int  
                                             #date  time  inv  
            q = "INSERT INTO complain VALUES('{}', '{}', {})".format(date, time, invoice)
            cursor.execute(q)

            query = "SELECT complain_id FROM complain ORDER BY complain_id DESC LIMIT 1"
            cursor.execute(query)
            complayn = cursor.fetchall()[0][0]
            dispatcher.utter_message("Your complain has been forwarded {} is your complain_id".format(complayn))  
            return [SlotSet("complain_id"), complayn]
