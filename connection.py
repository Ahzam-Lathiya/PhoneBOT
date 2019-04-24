import datetime
import psycopg2
from pprint import pprint

try:
    connection = psycopg2.connect(user = "neckai",
                                  password = "912NS@#!",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
    connection.autocommit = True
    cursor = connection.cursor()
except:
    pprint("Cannot connect to DataBase")
        
def giveprice():
    x=input("Enter model name:")
    view_command = "SELECT price FROM phones WHERE model_name = '{}'".format(x)
    cursor.execute(view_command)
    price_view=cursor.fetchall()
  
    if(price_view==[]):return "Product not found"
    elif(price_view!=[]):return price_view[0][0]  

def giverom():
    x=input("Enter model name:")
    view_command = "SELECT storage_size FROM phones WHERE model_name = '{}'".format(x)
    cursor.execute(view_command)
    rom_view=cursor.fetchall()
  
    if(rom_view==[]):return "Product not found"
    elif(rom_view!=[]):return rom_view[0][0]

def givecolor():
    x=input("Enter model name:")
    view_command = "SELECT product_color FROM phones WHERE model_name = '{}'".format(x)
    cursor.execute(view_command)
    color_view=cursor.fetchall()
    if(color_view==[]):return "Product not found"
    elif(color_view!=[]):return color_view[0][0]  
    
def givemodels():
    x=input("Enter brand name:")
    view_command = "SELECT model_name FROM phones WHERE brand_name = '{}'".format(x)
    cursor.execute(view_command)
    model_view = cursor.fetchall()
    if(model_view==[]):return "Product not found" 
    elif(model_view!=[]):
        for i in model_view:
            print(i[0])
         
def forwardcomplain():
    q = "SELECT complain_id FROM complain ORDER BY complain_id DESC LIMIT 1"
    cursor.execute(q)
    complayn = cursor.fetchall()
    invoice = input("Enter Invoice ID:")
    
    time= str(datetime.datetime.now())[11:19]
    date= str(datetime.datetime.now())[0:10]
    complain_command = "INSERT INTO complain VALUES({}, '{}', 55, 2, '{}', '{}')".format(complayn[0][0]+1, invoice, 
    date, time)
    cursor.execute(complain_command)
    print("Complain has been forwarded")


def showcomplain():
    view_command = "SELECT complain_id FROM complain ORDER BY complain_id DESC LIMIT 1"
    cursor.execute(view_command)
    complain_view = cursor.fetchall()
    print(complain_view[0][0])
    next_id = complain_view[0][0] + 1
    print("next complain is:{}".format(next_id))
    print(type(next_id))	

def givelastinvoice():
    q = "SELECT invoice_no FROM invoice ORDER BY invoice_no DESC LIMIT 1"
    cursor.execute(q)
    give_invoice = cursor.fetchall()
    return give_invoice[0][0]

def givelastuser():
    q = "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1"
    cursor.execute(q)
    give_user = cursor.fetchall()
    return give_user[0][0]

def givelastphone():
    q = "SELECT product_id FROM phones ORDER BY product_id DESC LIMIT 1"
    cursor.execute(q)
    give_phone = cursor.fetchall()
    return give_phone[0][0] 

def givelastaddress():
    q = "SELECT address_id FROM delivery ORDER BY address_id DESC LIMIT 1"
    cursor.execute(q)
    give_address = cursor.fetchall()
    return give_address[0][0] 

def givelastcomplain():
    q = "SELECT complain_id FROM complain ORDER BY complain_id DESC LIMIT 1"
    cursor.execute(q)
    give_complain = cursor.fetchall()
    if(give_complain!=[]): return give_complain[0][0] + 1
    else: return 1

def insertcomplain():
    add_command = "INSERT INTO complain VALUES('2019/5/4' ,'15:00:31' ,12 )"
    cursor.execute(add_command)

    q = "SELECT complain_id FROM complain ORDER BY complain_id DESC LIMIT 1"
    cursor.execute(q)
    give_complain = cursor.fetchall()[0][0]
    print("{} is your new complain no.".format(give_complain))

print(insertcomplain())
