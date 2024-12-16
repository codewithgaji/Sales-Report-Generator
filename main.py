"""Project Title:
JSON to Automated Report Generator

Updated Features:
Input: Read a JSON file (e.g., sales_data.json).

Processing:
Parse the JSON data.
Handle missing or malformed data.
Calculate key metrics (e.g., total sales, average sales per category, etc.).

Automation:
Generate a clean, human-readable report summarizing the results.
Save the report as a .txt file. (We’ll scale up to PDF later.)

Optional:
Send the report via email.

2. Set Up the Script:
Use the json module to read and parse the file.
Use Python's built-in functions to process the data.

3. Perform Data Cleaning:
Handle missing fields or incorrect data types with try-except blocks or conditional checks.

4. Perform Data Processing:
Calculate total revenue per category.
Determine the most sold product.
Summarize the total revenue, sales volume, and categories involved.

5. Automate Report Generation:
Write the summary to a .txt file in a formatted style."""



import json
import datetime
import time
import sys

null = 0
sales = {
    "sales": [
        {"product": "Laptop", "category": "Electronics", "price":800, "quantity": 5},
        {"product": "Phone", "category": "Electronics", "price":100, "quantity": 8},
        {"product": "Shoe", "category": "Apparel", "price":50, "quantity": 20},
    ]
}

with open("sales_data.json", "w") as file:
    json.dump(sales, file, indent=4)


with open("sales_data.json", "r") as file:
    data = json.load(file)




"""Ensuring to stop usage of Static print statements"""
"""Simulating a typing effect for the print statements"""
def type_writer(message, delay=0.003):
    for char in message:
        sys.stdout.write(char) # alternatively >> print(char, end="", flush=True) # "end" is used to space each message
        sys.stdout.flush()

        # 'flush=True' is used to ensure the characters appear immediately
        time.sleep(delay)
    return ""# This ensures the function returns a string





def error_handling():
    print("Invalid input! Please enter a valid response\n")



def add_entry():
    """ALlows a user to add a new sales entry"""
    while True:
        try:

            product = input("What product are you purchasing? ")

            cate = input("What category is it? (Electronics/Accessories/Apparel/Wears): ")

            price = int(input("What is the price? "))



            quant = int(input("What quantity are you purchasing? "))
            if quant in [None]:
                quant = 0
                print("Quantity added successfully")

            new_sale = {"product": product, "category": cate, "price": price, "quantity": quant}




            data['sales'].append(new_sale)
            with open("sales_data.json", 'w') as file:
                json.dump(data, file, indent=4)

            print("\nSale added Successfully!\n")
            break
            # This lets the user confirm their sale was added succesfully

        except ValueError: # using parentheses in the exception block won't allow other functions to work properly
            error_handling()
            print("Symbols are not neccessary for your inputs :)\n")
            # No need to add 'add_entry' again, loop(while loop) handles retries!

def view_data():
    """Allows a user to view the data of the sales"""
    try:
        with open('sales_data.json', 'r') as file:
            data = json.load(file)


        for index, entry in enumerate(data['sales']):
            """Enumerate - This iterates through the list of items in the data
                entry - This dynamically accesses the fields of the current list being iterated
                index - keeps the position of the item in the iterable"""
            print(f"Sales {index + 1}")
            print(f"Product: {entry['product']}")
            print(f"Category: {entry['category']}")
            # The splitting of the print statement is so the system can confirm the price and quantity of each product

            # HANDLING MISSING DATA
            try:
                #Handling missing price
                if entry['price'] in [None, null, 0]:
                    print(f"Warning: Price is missing for {entry['product']}")

                    try:
                        entry['price'] = float(input("Enter a price or press Enter to set a defaualt(e.g, 0):") or 0)
                    except ValueError:
                        print("Invalid input. Setting price to 0.")
                        entry['price'] = 0
                    # The 'or 0' is used to place the price at '0' incase the user presses enter.

                #Handling missing quantity
                if entry['quantity'] in [None, null, 0]:
                    print(f"Warning: Quantity is missing for {entry['product']}")
                    try:
                        entry[price] = float(input("Enter a quantity or press Enter to set a defaualt(e.g, 0):") or 0)
                    except ValueError:
                        print("Invalid input. Setting quantity to 0.")
                        entry['quantity'] = 0

                    # The 'or 0' is used to place the price at '0' incase the user presses enter.
            except Exception:
                error_handling()

            print(f"Price: {entry['price']}")
            print(f"Quantity: {entry['quantity']}\n")

        with open('sales_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Data updated successfully! \n")

    except Exception:
        error_handling()



# Calculating Data Revenue by their category

def product_revenue():
    try:
        with open('sales_data.json', 'r') as file:
            data = json.load(file)

        #This initialises a new dictionary to store the revenues for each category
        revenue_per_category = {}

        for entry in data['sales']:
            category = entry['category']
            price = entry.get('price', 0) # This gets the price of the product and defaults it to 0 if price isn't available
            quantity = entry.get('quantity', 0) #This gets the quantity of the product and defaults it to 0 if price isn't available

            # Calculating the revenue for this entry
            revenue = price * quantity

            #Adding to the revenue for the corresponding category
            if category in revenue_per_category:
                """If the category already exists, the current calculated revenue 
                would be added to that category"""
                revenue_per_category[category] += revenue
            else:
                # If not, then we create the category for that revenue
                revenue_per_category[category] = revenue

            #Displaying the results
        print("Revenue per category:")
        for category, revenue in revenue_per_category.items():
            # The '.items()' is used to get both category and its revenue
            print(f"{category}: ${revenue:.2f}\n")
            # The ':.2f' is used to determine the value as a float
            # The '2' is used to let the program know it should be approximated to 2 dp

    except FileNotFoundError:
        print("The sale_data.json file is Missing.")
    except json.JSONDecodeError:
        print("Error reading the JSON file.")


def sales_summarry():
    print("This is the summary of today's sales :) \n")
    try:
        with open("sales_data.json", 'r') as file:
            data = json.load(file)

        sales_vol = 0

        for entry in data['sales']:
            quantity = entry.get('quantity')

            sales_vol += quantity
        print(f"Total Sales is: {sales_vol}")

        total_revenue = 0
        for entry in data['sales']:
            price = entry.get('price', 0)
            quantity = entry.get('quantity')

            revenue = price * quantity

            total_revenue += revenue
            # To avoid showing the iteration on how the values were added, ensure to remove the
            # print func from the looop
        print(f"Total Revenue is: ${total_revenue}")

        cate = set() # Use 'set' to handle duplicate entries
        for item in data['sales']:
            category = item.get('category')
            if category: # This ensures it adds to the set only if category exists
                cate.add(category)
        print("Categories involved:", cate)

    except Exception:
        error_handling()


"""Exporting the sales summary in a readable text format"""
def exp_sales_summary(sales):
    with open('sales_data.json', 'r') as file:
        data = json.load(file)
    file_name = "sales_summary.txt"
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            #The encoding 'utf-8' ensures unicode characters are accepted in the basic text opening
            #Ensure every other thing exists within the 'with' statement if you still want to write into the file
            file.write("🌟 Sales Summary 🌟 \n")
            file.write("==================\n")
        # This is used to iterate through a key-value pair
            for entry in data['sales']:
                product = entry.get('product', 'uknown product') #This is used to adjust to my json file
                price = entry.get('price', 0)
                quantity = entry.get('quantity', 0)
                revenue = price * quantity

                file.write(f"📋 Product: {product}\n")
                file.write(f" Unit sold: {quantity}\n")
                file.write(f" Revenue: ${revenue:.2f}\n")
                file.write("\n")

            file.write("✅ End of Summary \n")

        type_writer(f"📂 Sales summary exported ")

    except Exception as e:
        type_writer(f"❌ Error exporting sales summary : {e}")







def most_sold_product():
    try:
        with open('sales_data.json', 'r') as file:
            data = json.load(file)

        quantity_sold_for_each_product = {}

        for entry in data['sales']:
            product_name = entry['product']
            quantity = entry.get('quantity', 0)
            if quantity in quantity_sold_for_each_product:
                quantity_sold_for_each_product[product_name] += quantity
            else:
                quantity_sold_for_each_product[product_name] = quantity

        # Find the product with the maximum quantity sold
        most_sold_product_name = max(quantity_sold_for_each_product, key=quantity_sold_for_each_product.get)

        most_sold_product_quantity = quantity_sold_for_each_product[most_sold_product_name]
        print("Maximum sold product is:")
        print(f"{most_sold_product_name}: {most_sold_product_quantity}")


    except ValueError:
        error_handling()








def main_menu():
    type_writer("Welcome to Gaji's First Sale Manager Software 😊 \n")
    type_writer("This is a simple prototype of a Sale system where you can\nperfom all sorts of "
          "operation regarding your sales\nLets get you started 😉 \n")
    print("\n") # This is to space the intro from the operations

    while True:  # Optimised code, using the while loop
        type_writer("What would you like to do:"
                    "\n➕ Add a new sale? (press 1)"
                    "\n📋 View Sales record? (press 2)"
                    "\n💰 Calculate Product revenue? (press 3)"
                    "\n🔍 Know the most sold product? (press 4)\n"
                    "✅ Get Sales summary for the day? (press 5)"
                    "\n✅ Export Sales summary (press 6)"
                    )

        try:
            service = int(input("\nEnter here:  "))
            if service == 1:
                add_entry()
            elif service == 2:
                view_data()
            elif service == 3:
                product_revenue()
            elif service == 4:
                most_sold_product()
            elif service == 5:
                sales_summarry()
            elif service == 6:
                exp_sales_summary(sales)

                service = input("Would you like to check something else? (yes/no): \n").lower()
                if service not in ['yes', 'okay', 'yeah']:
                    type_writer("Sales Entry Completed For the Day :) ")
                    break

        except Exception:
            error_handling()

main_menu()
#print(sales['sales'])



