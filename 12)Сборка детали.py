from functools import reduce
automaton = []

while True:
    d = input()
    if not d:
        break
    automaton.append(d)

automaton = [a.split(' ') for a in automaton]
automaton_details = {auto.pop(0): auto[1:] for auto in automaton[1:] if len(auto[1:]) > 0}
atoms = [a for a in automaton if len(a) == 1]
atoms = reduce(lambda x, y: x + y, atoms) if atoms else []

is_constructable = 1


def parse_automaton(details):
    global is_constructable
    if isinstance(details, list):
        for detail in details:
            parse_automaton(detail)
    elif isinstance(details, str) and (details in atoms):
        is_constructable = 1
    elif isinstance(details, str) and (details in automaton_details):
        parse_automaton(automaton_details[details])
    else:
        is_constructable = 0

parse_automaton(automaton[0][1:])
print ('YES') if is_constructable else ('NO')
