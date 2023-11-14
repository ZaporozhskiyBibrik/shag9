from random import choice
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 10
        self.days = 0
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 2
        self.progress -= 0.1
        self.money -= 2
    def to_work(self):
      if self.money > 10:
         print("I will work at night job")
         self.gladness -= 1
         self.money += 20
         self.progress += 10
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 1:
            print("Passed externally…")
            self.alive = False
        elif self.money >0:
          print("I will go to work at night job")
          self.money += 10
          self.gladness -= -2
          self.progress += 5
    def __iter__(self):
        return self
    def __next__(self):
        if not self.alive or self.days >= 365 or self.money == 0:
            raise StopIteration
        self.days += 1
        day = " Day " + str(self.days) + " of " + self.name + " life "
        print(f"{day:=^50}")
        actions = [self.to_study, self.to_sleep, self.to_chill]
        action = choice(actions)
        action()
        self.end_of_day()
        self.is_alive()
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")
nick = Student(name="Nick")
for day in nick:
    pass
