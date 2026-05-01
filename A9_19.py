User = input("Enter a new username: ")
Pass1 = input("Enter a new password: ")
Pass2 = input("Re-enter password: ")
while True:
    if Pass1 != Pass2:
        print("Passwords do not match. Please try again.")
        User = input("Enter a new username: ")
        Pass1 = input("Enter a new password: ")
        Pass2 = input("Re-enter password: ")
    if Pass1 == Pass2:
        print("Success!")
        break
D = {
    User : Pass1
}
print(D)


