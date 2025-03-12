import random

class Parent:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self._determine_alleles()
    
    def _determine_alleles(self):
        # Mapping golongan darah ke alel
        match self.blood_type:
            case 'A': return ['A', 'O']
            case 'B': return ['B', 'O']
            case 'AB': return ['A', 'B']
            case 'O': return ['O', 'O']
            case _: raise ValueError("Golongan darah tidak valid")
    
    def get_allele(self):
        return random.choice(self.alleles)

class Father(Parent):
    pass

class Mother(Parent):
    pass

class Child:
    def __init__(self, father, mother):
        self.blood_type = self._determine_blood_type(father, mother)
    
    def _determine_blood_type(self, father, mother):
        # Ambil satu alel dari masing-masing orang tua
        alleles = sorted([
            father.get_allele(),
            mother.get_allele()
        ])
        
        # Tentukan golongan darah
        match alleles:
            case ['A', 'A'] | ['A', 'O']: return 'A'
            case ['B', 'B'] | ['B', 'O']: return 'B'
            case ['A', 'B']: return 'AB'
            case ['O', 'O']: return 'O'
            case _: return 'Unknown'  

# Contoh penggunaan
father = Father('A')
mother = Mother('B')
child = Child(father, mother)
print(f"Golongan darah anak: {child.blood_type}")
