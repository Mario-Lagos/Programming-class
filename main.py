'''from Magic_eight_ball import get_eight_ball_responses
question = input ("Ask the Magic Eight Ball a question: ")

try:
    if not question.strip():
        raise ValueError("Question can not be empty")
    answer = get_eight_ball_responses()
    print ("\nMagic Eight Ball Says: {answer}")
except ValueError as error:
    print(f"Input error: {error}")'''

#balance = 500.00
#print ("Welcome to the class bank")

'''while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")    

    option = input("Choose an option: ")    
    match option:
        case "1":
            print(f"Your current balance is: ${balance:.2f}")
        case "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                balance += amount
                print(f"Deposit sucessful.")
                print(f"Your new balance is: ${balance:.2f}")
            except ValueError as error:
                print("Error:",error)

        case "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                if amount > balance:
                    raise ValueError("Insufficient funds.")
                balance -= amount
                print(f"Withdrawal successful.")
                print(f"Your new balance is: ${balance:.2f}")
            except ValueError as error:
                print("Error:", error)
        case "4":
            print("Thank you for using the class bank. Goodbye!")
            break
        case _:
            print("Invalid option. Please try again.")'''

#Tempeture Converter
print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

option = input("Choose an option: ")

try:
    temperature = float(input("Enter the temperature: "))

    match option:
        case "1":
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C = {result:.2f}F") 
        case "2":
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F = {result:.2f}C")
        case "3":
            result = temperature + 273.15
            print(f"{temperature}°C = {result:.2f}K")

except ValueError as error:
    print("Error:", error)
