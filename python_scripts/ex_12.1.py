
class TallyCounter:

    def __init__(self, color="white"):
        self.counter = 0
        self.max_value = 9999
        self.color = color


    def click(self):
        self.counter = self.counter + 1
        if self.counter >= self.max_value:
            self.counter = 0

    def reset(self):
        self.counter = 0

tally_counter1 = TallyCounter("blue")
tally_counter2 = TallyCounter("red")
print(tally_counter1.counter, tally_counter1.color)
print(tally_counter2.counter, tally_counter2.color)
tally_counter1.click()
tally_counter1.click()
tally_counter1.click()
tally_counter1.click()
tally_counter1.click()
tally_counter1.click()
print(tally_counter1.counter, tally_counter1.color)
print(tally_counter2.counter, tally_counter2.color)