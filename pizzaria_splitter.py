# Mensagem de boas vindas aparece na tela
print("Welcome to the pizzaria splitter! 🍕🍕🍕")

# Organizando a estrutura do código: Total da conta e taxa de entrega
bill = float(input("What was the total bill? R$ "))
delivery_answer = input("Does the bill have delivery fee (yes/no)? ").strip().lower()

if delivery_answer == "yes":
    delivery_fee = float(input("Enter the delivery fee: R$ "))
else:
    delivery_fee = 0.0

# Organizando a estrutura do código: Gorjetas e números de pessoas que irão pagar a conta
tip = int(input("What percentage tip would you like to give? 10, 12, 15: "))
tip = tip / 100
people = int(input("How many people to split the bill? "))

# --- Cálculos ---
subtotal = bill + delivery_fee
tip_amount = subtotal * tip
total = subtotal + tip_amount
amount_per_person = total / people

# --- Saída (use f-strings) ---
print(f"Subtotal: {subtotal}\nTotal in tips: {tip_amount}\nTotal: {total}\nEach person should pay: {amount_per_person}")

rounded_amount = round(amount_per_person, 2)