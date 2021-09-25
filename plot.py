import matplotlib.pyplot as plt
import numpy as np
import time

def create_random_skill(n):
    np.random.seed(42)
    grades = np.random.normal(40000, 20000, size=(n))
    grades = list(map(int, grades))
    return grades

def display():
    with open('output1.txt', 'r') as skills:
        skill = skills.read()
        skill = skill[4:-1].lstrip().rstrip()
        skill = list(map(float, skill.split(',')))
        
    mu, sigma = 40000, 20000
    s = np.array(skill)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                   np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
             linewidth=2, color='r')
    #plt.plot(y,x)
    plt.show()
    #print(s)

t = 0
while t<10:
    display()
    time.sleep(1)
    t+=1
    
