class Employee():
    """Criando a classe Employee"""
    def __init__ (self, first_name='', last_name='', annual_salary=0 ):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, additional=5000):
        self.annual_salary += additional
        return self.annual_salary
