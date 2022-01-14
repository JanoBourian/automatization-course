import unittest 

class PruebaExperimental(unittest.TestCase):
    
    def pruebaIgual(self, a, b):
        self.assertEqual(a, b)
    
    def runTest(self):
        self.pruebaIgual(2, 2)
        self.pruebaIgual(2, 5)
        self.pruebaIgual("hola", "mundo")
        self.pruebaIgual(3, 3)
        
print(PruebaExperimental().run())
resultado = PruebaExperimental().run()
print(dir(resultado))
print(resultado.failures)
print(resultado.errors)