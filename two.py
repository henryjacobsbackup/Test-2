print("Greetings Chieftain")

def fibonnaci(n) :
    if n < 2 : return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)

print(fibonnaci(10))