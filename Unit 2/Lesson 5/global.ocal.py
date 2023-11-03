global_book = "Science Encyclopedia" #global_book is declared OUTSIDE of all functions. IT EXISTS THROUGHOUT EVERY PROGRAM

def section_book():
    local_book = "Chemistry Handbook"
    print(f"In the section: We have the {global_book} and the {local_book}")

section_book()

print(f"In the library we stil have {global_book}")

print(f"We do not have: {local_book}")

myBook = myBook+"hello"
print(myBook)
print(section_book())


x = -1
if x>0:
    inside_if = "This was created in the 'if' block"
    print(inside_if)
else:
    inside_if = "The variable is empty"

#local scope doesn't include anything except fo functions so this is still visibile
print(inside_if)

def section_book():
    local_book = "Chemistry Handbook" + global_book
    