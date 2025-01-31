import re


recpt_re = re.compile(f'[a-z A-Z 0-9]+@[a-z A-Z 0-9]+\.[a-z A-Z]+')

def add_recipient(email: str, lst: str):
    with open(f"{lst}.txt", "a+") as f:
        f.seek(0)
        if email in [l.strip() for l in f.readlines()]:
            print(f"[ERROR] {email} already in list.")
        else:
            f.write(email + "\n")
            print(f"Added {email} to {lst}.")
        f.close()

def get_choice(choices, prompt):
    choices = [c.lower() for c in choices]
    return get_valid_input(prompt, lambda c: c.lower() in choices)

def get_valid_input(prompt, f):
    choice = input(prompt)
    while not f(choice):
        choice = input(f"Invalid input {choice}. Please enter again: ")
    return choice

email = get_valid_input("Enter email: ", lambda e: recpt_re.match(e))
if get_choice(["y", "n"], "Add to all? [Y|n] ").lower() == "y":
    add_recipient(email, "all")
if get_choice(["y", "n"], "Add to beta testers? [Y|n] ").lower() == "y":
    add_recipient(email, "beta")
if get_choice(["y", "n"], "Add to admins? [Y|n] ").lower() == "y":
    add_recipient(email, "admins")
