

print("Hello World")

myname = "Roopesh"

print(f"Hello {myname}! How are you?")

def hello_name(somename):
    print(f"Hello {somename}! This is a function.")


def repeat_hello(someone, n_times):
    for i in range(n_times):
        print(f"Hello there {someone}! This is print statement number: {i+1}")


if __name__ == "__main__":
    hello_name("Class")
    hello_name("King")
    hello_name("Folks")

    repeat_hello(someone= "Siddarth the idiot", n_times=50)

