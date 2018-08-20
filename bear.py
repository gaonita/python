class Bear:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "🐻 <-(Hello, my name is " + self.name + ")"

    def set_name(self, name):
        self.name = name


bamse = Bear('bamse')
#baloo = Bear('baloo')

print(bamse)
bamse.set_name('baloo')
print(bamse)
#print(baloo)
