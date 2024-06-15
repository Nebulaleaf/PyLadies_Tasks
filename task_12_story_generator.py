'''
For this use module random and create following lists: when, who, name, residence, went, happened.
Fill these lists with various options according to the topic and then print in the end your story😁 

Here is an example of mine:
"On a rainy afternoon, a clumsy dragon named Lady Whiskers that lived in a floating island,
went to the a chocolate factory and invented a new dance move."
'''

import random

when = [
    "On a Monday morning", "On a Friday afternoon", "During a late-night coding session",
    "On a coffee-fueled morning", "On a deadline day", "On a bug-fixing night",
    "During a code review session", "On a team meeting day", "During a hackathon",
    "On a deployment day", "During a sprint planning session", "On a lazy Sunday"
]

who = [
    "a Python hacker", "a caffeine-addicted coder", "a debugging wizard",
    "a sleep-deprived developer", "a code-review ninja", "a front-end magician",
    "a back-end guru", "a full-stack hero", "a keyboard warrior",
    "an open-source enthusiast", "a startup hustler", "a cybersecurity expert"
]

name = [
    "Debugging Dan", "Scripted Sally", "Code-Master Carl",
    "Looping Larry", "Algorithm Amy", "Syntax Sam",
    "Exception Eric", "Binary Ben", "Function Fiona",
    "Variable Vanessa", "Networked Nick", "Compile Chloe"
]

residence = [
    "that lived in a messy codebase", "that lived in a forgotten GitHub repo",
    "that lived in a hidden stack of documentation", "that lived in a labyrinth of legacy code",
    "that lived in a mysterious server room", "that lived in a virtual machine",
    "that lived in a containerized environment", "that lived in a cloud infrastructure",
    "that lived in a terminal window", "that lived in a debug console",
    "that lived in a CI/CD pipeline", "that lived in a code review queue"
]

went = [
    "to a tech conference", "to a code retreat", "to a debugging session",
    "to a virtual stand-up meeting", "to a hackathon", "to a coffee shop",
    "to a developer's meetup", "to a code jam", "to a programming contest",
    "to a tech talk", "to a sprint demo", "to a pair programming session"
]

happened = [
    "and found a missing semicolon", "and refactored the entire codebase",
    "and fixed an elusive bug", "and wrote an epic README",
    "and automated their job", "and discovered a hidden feature",
    "and impressed everyone with their Git skills", "and created a viral meme",
    "and optimized a slow function", "and implemented a dark mode",
    "and built a new feature overnight", "and solved a production issue"
]

story = f"{random.choice(when)}, {random.choice(who)} named {random.choice(name)} {random.choice(residence)}, went {random.choice(went)} {random.choice(happened)}."
print(story)
