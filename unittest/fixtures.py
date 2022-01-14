import unittest   

class PruebaFixture(unittest.TestCase):

    def pruebaIgual(self, a, b):
        print('Preparando pruebas')
        self.assertEqual(a, b)
    
    def setUp(self):
        self.a = 2
        self.b = 3
    
    def tearDown(self):
        print("Terminaron las pruebas.")
    
    def runTest(self):
        self.pruebaIgual(2, self.a)
        self.pruebaIgual(2, self.b)
        self.pruebaIgual('Hola, ', 'Mundo')
        
print(PruebaFixture().run())