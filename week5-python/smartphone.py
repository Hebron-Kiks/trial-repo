# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged. Battery: {self.battery} mAh")
    
    def info(self):
        print(f"Smartphone Info: {self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh")


# Derived class (Inheritance)
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)  # inherit base attributes
        self.android_version = android_version
    
    # Polymorphism: override info() method
    def info(self):
        print(f"Android Phone: {self.brand} {self.model}, Storage: {self.storage}GB, "
              f"Battery: {self.battery}mAh, Android {self.android_version}")
    
    # Extra method unique to AndroidPhone
    def install_app(self, app_name):
        print(f"{self.brand} {self.model} is installing {app_name}...")


# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 128, 3200)
phone1.info()
phone1.call("123-456-7890")
phone1.charge(200)

print("------")

phone2 = AndroidPhone("Samsung", "Galaxy S23", 256, 4000, "13")
phone2.info()
phone2.call("987-654-3210")
phone2.install_app("WhatsApp")
