import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            random_draw = []
            for _ in range(number):
                random_int = random.randint(0, len(self.contents)-1)
                random_draw.append(self.contents.pop(random_int))
            return random_draw



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_matched = 0
    contents = []
    contents = sorted(contents)
    
    for key, value in expected_balls.items():
        for _ in range(value):
            contents.append(key)

    for _ in range(num_experiments):
        draw = sorted(hat.draw(num_balls_drawn))
        copied_draw = copy.deepcopy(draw)
        matched_contents = []
        for i in range(len(contents)):
            if contents[i] in copied_draw:
                matched_contents.append(copied_draw.pop(copied_draw.index(contents[i])))

        if sorted(matched_contents) == sorted(contents):
            num_matched += 1
    return num_matched / num_experiments

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)