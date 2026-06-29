class VisaCard:
    def __init__(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number
    def display_details(self):
        print(self.holder_name)
        print(self.card_number)
    def compute_reward(self, purchase_type, amount):
        reward = amount * 0.01
        return reward
class HpVisaCard(VisaCard):
    def compute_reward(self, purchase_type, amount):
        reward = super().compute_reward(purchase_type, amount)
        if purchase_type == "Fuel":
            reward += 10
        return reward
card_type = input("enter cardtype").strip()
holder_name = input("enter holdername").strip()
card_number = input("ener cardnumber").strip()
amount = float(input("enter amount"))
purchase_type = input("enter purchase type").strip()
if card_type == "VISA":
    card = VisaCard(holder_name, card_number)
elif card_type == "HPVISA":
    card = HpVisaCard(holder_name, card_number)
else:
    print("InvalidChoice")
    exit()
card.display_details()
print(f"{card.compute_reward(purchase_type, amount):.2f}")

