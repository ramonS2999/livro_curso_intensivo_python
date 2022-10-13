"""Importando os modolos"""
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Criando a classe TestEmployee"""
    def setUp(self):
        self.employee = Employee()                   # instanciando a classe Employee
        self.additional_default = 5000               # Criando atributo do salário padrão
        self.first_name = ['joão', 'maria', 'paulo'] # Criando uma lista com os primeiros nomes
        self.last_name = ['sousa', 'santos', 'lima'] # Criando uma lista com os sobrenomes
        self.annual_salary = [24000, 36000, 48000]   # Criando uma lista com os valores de salário anual
        self.additional = [2000, 3000,  4000]        # Criando uma lista com os valores de para adicionar ao salário
        
    def test_give_default_raise(self):
        """Colocando o valore no atributo que será testado"""
        full_salary = self.employee.annual_salary + self.additional_default

        """Realisando os testes"""
        self.assertEqual(self.employee.first_name, '')            # Testando o primeiro nome padrão
        self.assertEqual(self.employee.last_name, '')             # Testando o sobrenome padrão
        self.assertEqual(self.employee.annual_salary, 0)          # Testando o valor do salario padrão
        self.assertEqual(self.employee.give_raise(), full_salary) # Testando o valor do salario padrão com o valor adicional

    def test_give_custom_raise(self):
        i = 0
        while i < 3:
            """Colocando os valores nos atributos que serão testados"""
            self.employee.first_name = self.first_name[i]                  
            self.employee.last_name = self.last_name[i]                    
            self.employee.annual_salary = self.annual_salary[i]            
            full_salary = self.employee.annual_salary + self.additional[i] 

            """Realisando os testes"""
            self.assertEqual(self.employee.first_name, self.first_name[i])              # Testando o primeiro nome costomizado
            self.assertEqual(self.employee.last_name, self.last_name[i])                # Testando o sobrenome costomizado
            self.assertEqual(self.employee.annual_salary, self.annual_salary[i])        # Testando o valor do salario costomizado
            self.assertEqual(self.employee.give_raise(self.additional[i]), full_salary) # Testando o valor do salario costomizado com o valor adicional

            i += 1

unittest.main()
