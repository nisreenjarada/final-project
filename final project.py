class Client:
    def __int__(self , id , age , id_no , phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

    def s_id(self,id):
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