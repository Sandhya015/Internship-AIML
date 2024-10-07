class Laptop:
    def __init__(self,brand:str,ram:int):
        if ram > 0:
            self.brand =brand
            self.ram = ram
        else:
            raise ValueError("RAM must be a positive integer")

    def upgrade_ram(self,additional_ram:int):
        if additional_ram > 0:
            self.ram += additional_ram
            print(f"RAM upgraded to {self.ram}GB")

        else:
            print("Error:Additional RAM must be positive integer")

laptop = Laptop("Dell",8)
laptop.upgrade_ram(4)
laptop.upgrade_ram(-2)