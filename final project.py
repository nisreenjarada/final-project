class Client:
    def __int__(self , id , age , id_no , phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id
        return self.id
    def s_full_name(self , full_name):
        return self.full_name
    def s_age(self , age):
        return self.age
    def s_id_no(self , id_no):
        return self.id_no
    def s_phone_number(self , phone_number):
        return self.phone_number

class Librarian(Client):
    def __int__(self,id,full_ name,age,id_no,phone_number,salary = 0.0):
    super() __int__(id,full_name,age,id_no,phone_number)
    self.salary = salary
    def s_salary(self):
        return self.salary

p = librarian(random,randint(1,1000) input('your name :') 19 , 48 ,3322332)
print(p.id , p.full_name)


class Book:
    def __int__(self,id,title,description,author,status):
        self.id = id
        self.title = title
        self.description = description
        self.author
        self.status

    def s_id(self,id):
        return self.id
    def s_title(self,title):
        return self.title
    def s_descrption(self,description):
        return self.description
    def s_author(self,author):
        return self.author
    def s_status(self,status):
        if self.status:
            return 'Active'
        else:
            return 'Inactive'



class Borrowing_order:
    def __int__(self,id,start_date,and_data,book_id,cliend_id,status):
        self.id = id
        self.start_data = start_data
        self.end_data = end_data
        self.book_id = book_id
        self.cliend_id = cliend_id
        self.status = status
    def s_id(self,id):
        return self.id
    def s_start_data(self,start_data):
        return self.start_data
    def s_end_data(self,end_data):
        return self.end_data
    def s_book_id(self,book_id):
        return self.book_id
    def s_cliend_id(self,cliend_id):
        return self.cliend_id
    def s_status(self,status):
        return self.status


user = []
books = []
borrowed_order = []
total_borrowed_books = 0
total_available_books = 0
total_borrowed_orders = 0

user.append(Client(random.randint(1,100000),str(input("Client name :"))) , int(input("Client Age:")) , '1',



