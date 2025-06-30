import random

orders_served = 0

def make_shawarma(
        customer,                   
        size="large",               
        *extras,                    
        **sauces):            


    global orders_served
    orders_served += 1

    ticket  = f"order #{orders_served} — {customer}\n"
    ticket += f"size: {size}\n"

    if extras:
        ticket += "extras: " + ", ".join(extras) + "\n"


    if sauces:
        # new kind of for
        sauce_lines = [f"{k} ({v})" for k, v in sauces.items()]
        ticket += "souces: " + ", ".join(sauce_lines) + "\n"

    base_price   = {"small": 4, "medium": 6, "large": 8}[size]

    # Lambda tomorrow they will take it
    price_funny  = lambda base, n_extras: base + n_extras * 0.75
    total        = price_funny(base_price, len(extras))

    ticket += f"Total: {total:.2f} LYD\n"
    # use extirnal library
    ticket += random.choice([
    "🍗 Enjoy your meal!",
    "😋 Dig in, champ!",
    "🧄 Don’t forget the gum after that garlic!"
])
    return ticket


print(make_shawarma(
    "Ahmed",
    "medium",
    "potato", "cheese",
    garlic="strong", spicy="medium"
))

print("-" * 40)

print(make_shawarma(
    "moad",
    "large",
    "potato", "cheese",
    garlic="strong", spicy="medium"
))
