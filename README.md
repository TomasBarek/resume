# Some of my codes for presentation

## Goal of the repository

Purpose of this repository is to get used to work with git and to _show-off my codes for a job interview as I have no professional background._

---

## Personal goals with this repository

At the moment of creating this repository is to learn along the job coding and find a job within IT in some junior position to become a senior developer in one or more of the following tools:

- Python
- C++
- SQL
- HTML/CSS/JS
- PHP

---

## Python codes

Most of the codes will be from my [100 days bootcamp (Angela Yu)](https://www.udemy.com/course/100-days-of-code/) journey with some modification over time that come up to my mind and hope that also my own projects - these will start with "\_".

Will be followed by Data science & machine learning bootcamp and web development bootcamp.

---

## HTML, CSS, JS, PHP codes

These I am learning via [learn2code (Roman Hraška)](https://skillmea.sk/)

There are 3 webpages I am about to do, starting on 2023:

1. Cafeteria that will me used mostly as eShop
2. Local bowling league - collecting data, filtering, evaluation, event registrations, accounts with forum
3. Appointment page for local masseur
   Once that any of the pages are running live, there will be an update with URLs.

---

## Job related info

NOTE: also available for work as **self-employment**

```
from random import randint

work_experience = 0
skill = "unknown"
salary = randint(1000, 1500)
work = False

# Evaluate input
given_chance = int(input("Type 1 to hire, 0 to miss the opportunity: "))
if given_chance == 1:
    print(f"Hypothetical offer: {salary} $")
while not work:
    if given_chance == 0:
        print("Thank you for viewing my README anyway. Have a nice day.")
        break
    elif given_chance == 1 and work_experience < 2:
        print(f"Thank you for opportunity. {2 - work_experience} year/s to see the fruits.")
        work_experience += 1
    else:
        skill = "obtained"
        print(f"Let's discuss {skill} knowledge and outcome over {work_experience} years.")
        work = True
```
