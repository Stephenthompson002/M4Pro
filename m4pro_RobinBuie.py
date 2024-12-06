import csv

# Define the book inventory
book_inventory = {
    "William Shakespeare": [
        {"book": "Hamlet", "year": 1601, "price": 14.52, "quantity": 43},
        {"book": "Macbeth", "year": 1606, "price": 13.45, "quantity": 50},
        {"book": "Othello", "year": 1604, "price": 15.30, "quantity": 37},
        {"book": "Romeo and Juliet", "year": 1597, "price": 12.99, "quantity": 60}
    ],
    "Charles Dickens": [
        {"book": "A Tale of Two Cities", "year": 1859, "price": 9.56, "quantity": 75},
        {"book": "Great Expectations", "year": 1861, "price": 12.50, "quantity": 60},
        {"book": "Oliver Twist", "year": 1837, "price": 9.75, "quantity": 50},
        {"book": "David Copperfield", "year": 1850, "price": 11.25, "quantity": 40}
    ],
    "James Joyce": [
        {"book": "Ulysses", "year": 1922, "price": 19.99, "quantity": 30},
        {"book": "A Portrait of the Artist as a Young Man", "year": 1916, "price": 13.20, "quantity": 25},
        {"book": "Dubliners", "year": 1914, "price": 12.00, "quantity": 35},
        {"book": "Finnegans Wake", "year": 1939, "price": 16.50, "quantity": 20}
    ],
    "Ernest Hemingway": [
        {"book": "The Old Man and the Sea", "year": 1952, "price": 10.35, "quantity": 80},
        {"book": "A Farewell to Arms", "year": 1929, "price": 14.75, "quantity": 45},
        {"book": "For Whom the Bell Tolls", "year": 1940, "price": 13.50, "quantity": 50},
        {"book": "The Sun Also Rises", "year": 1926, "price": 12.99, "quantity": 55}
    ],
    "J.K. Rowling": [
        {"book": "Harry Potter And the Sorcerer's Stone", "year": 1997, "price": 16.62, "quantity": 100},
        {"book": "Harry Potter And the Chamber of Secrets", "year": 1998, "price": 22.99, "quantity": 90},
        {"book": "Harry Potter And the Prisoner of Azkaban", "year": 1999, "price": 23.99, "quantity": 85},
        {"book": "Harry Potter And the Goblet of Fire", "year": 2000, "price": 25.99, "quantity": 80}
    ]
}

# Function to display the main menu of the program
def display_menu():
    print("\n-----------Menu------------")
    print("1) Display Book Inventory and Calculate Total")
    print("2) Lookup by Author and Get Total")
    print("3) Lookup by Book Name and Get Total")
    print("4) Lookup By Price Range")
    print("5) Exit ")
    print("----------------------")

# Function to write the book inventory to text and CSV files
def write_inventory_to_file(text_filename, csv_filename, books, total):
    # Write to text file
    with open(text_filename, 'w') as text_file:
        # Print column headers for the inventory list
        text_file.write(f"{'Author':<20} {'Book':<30} {'Year':<6} {'Price':<10} {'Quantity':<10}\n")
        text_file.write("----------------------------------------------------------------------\n")
        for author, book_list in books.items():
            for book in book_list:
                # Format each book's details and write to the file
                text_file.write(f"{author:<20} {book['book']:<30} {book['year']:<6} ${book['price']:<10.2f} {book['quantity']:<10}\n")
        text_file.write(f"\nOverall Total Inventory Value: ${total:.2f}\n")

    # Write to CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Author", "Book", "Year", "Price", "Quantity"])
        for author, book_list in books.items():
            for book in book_list:
                # Write each book's data to CSV file
                writer.writerow([author, book["book"], book["year"], f"${book['price']:.2f}", book["quantity"]])
        writer.writerow(["Overall Total", "", "", f"${total:.2f}"])

# Function to display all books and calculate the total value
def display_inventory():
    # Calculate the total value of all books in the inventory
    total_inventory_value = sum(book["price"] * book["quantity"] for books in book_inventory.values() for book in books)
    # Write the inventory details to text and CSV files
    write_inventory_to_file("book_inventory.txt", "book_inven_CSV.csv", book_inventory, total_inventory_value)
    print("Inventory written to 'book_inventory.txt' and 'book_inven_CSV.csv'.")

# Function to search books by author name (partial/full name allowed)
def search_by_author():
    # Get the author search term from the user (convert to lowercase for case-insensitive comparison)
    author_name_input = input("Enter author's name (partial or full): ").strip().lower()

    # Initialize a list to store books found for the author
    found_books = []
    total_author_value = 0

    # Loop through the book inventory and match author names
    for author, books in book_inventory.items():
        if author_name_input in author.lower():
            # If the author matches, add the books to the result list
            for book in books:
                total = book["price"] * book["quantity"]
                found_books.append((author, book["book"], book["year"], book["price"], book["quantity"], total))
                total_author_value += total

    # If books are found, write them to files
    if found_books:
        # Generate filenames for text and CSV files
        file_name_base = author_name_input.lower() + "_books"
        text_file_name = file_name_base + ".txt"
        csv_file_name = file_name_base + "_CSV.csv"

        # Write to the text file
        with open(text_file_name, "w") as text_file:
            text_file.write(f"\n{'Author':<30} {'Book':<50} {'Year':<6} {'Price':<8} {'Quantity':<8} {'Total':<10}\n")
            text_file.write("-" * 120 + "\n")
            for author, book, year, price, quantity, total in found_books:
                text_file.write(f"{author:<30} {book:<50} {year:<6} ${price:<8.2f} {quantity:<8} ${total:<10.2f}\n")
            text_file.write("-" * 120 + "\n")
            text_file.write(f"\nOverall Total Value: ${total_author_value:.2f}\n")

        # Write to the CSV file
        with open(csv_file_name, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Author', 'Book', 'Year', 'Price', 'Quantity', 'Total'])
            for author, book, year, price, quantity, total in found_books:
                writer.writerow([author, book, year, f"${price:.2f}", quantity, f"${total:.2f}"])
            writer.writerow(['', '', '', '', 'Overall Total', f"${total_author_value:.2f}"])

        # Print the books found for the author
        print(f"\nBooks by author '{author_name_input}':")
        print(f"{'Author':<30} {'Book':<50} {'Year':<6} {'Price':<8} {'Quantity':<8} {'Total':<10}")
        print("-" * 120)
        for author, book, year, price, quantity, total in found_books:
            print(f"{author:<30} {book:<50} {year:<6} ${price:<8.2f} {quantity:<8} ${total:<10.2f}")
        print("-" * 120)
        print(f"\nOverall Total Value: ${total_author_value:.2f}")
    else:
        print(f"No books found for author containing '{author_name_input}'.")

# Function to search for books by name (partial/full name allowed)
def search_by_book_name():
    # Get the book search term from the user
    book_name_input = input("Enter book name (partial or full): ").strip().lower()

    # Initialize a list to store books matching the search term
    found_books = []

    # Loop through the book inventory and match book titles
    for author, books in book_inventory.items():
        for book in books:
            if book_name_input in book["book"].lower():
                found_books.append((author, book["book"], book["year"], book["price"], book["quantity"]))

    # If books are found, display them
    if found_books:
        print(f"\nBooks matching '{book_name_input}':")
        print(f"{'Author':<30} {'Book':<50} {'Year':<6} {'Price':<8} {'Quantity':<8}")
        print("-" * 120)
        for author, book, year, price, quantity in found_books:
            print(f"{author:<30} {book:<50} {year:<6} ${price:<8.2f} {quantity:<8}")
        print("-" * 120)
    else:
        print(f"No books found containing '{book_name_input}' in their title.")

# Function to search for books within a price range
def search_by_price_range():
    try:
        # Get the price range from the user
        start_range = float(input("Enter Start range: "))
        end_range = float(input("Enter last number in lookup range: "))

        # Initialize a list to hold books in the specified price range
        found_books = []

        # Loop through the book inventory and find books in the price range
        for author, books in book_inventory.items():
            for book in books:
                if start_range <= book["price"] <= end_range:
                    found_books.append((author, book["book"], book["year"], book["price"], book["quantity"]))

        if found_books:
            # Generate the filename based on the price range
            file_name = f"books_{int(start_range)}_{int(end_range)}"

            # Write to the text file
            with open(f"{file_name}.txt", "w") as text_file:
                text_file.write(f"{'Author':<30} {'Book':<50} {'Year':<6} {'Price':<8} {'Quantity':<8}\n")
                text_file.write("-" * 120 + "\n")
                total_value = 0
                for author, book, year, price, quantity in found_books:
                    total_value += price * quantity
                    text_file.write(f"{author:<30} {book:<50} {year:<6} ${price:<8.2f} {quantity:<8}\n")
                text_file.write("-" * 120 + "\n")
                text_file.write(f"Overall Total Value: ${total_value:.2f}\n")

            # Write to the CSV file
            with open(f"{file_name}.csv", "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Author', 'Book', 'Year', 'Price', 'Quantity', 'Total Value'])
                total_value = 0
                for author, book, year, price, quantity in found_books:
                    total_value += price * quantity
                    writer.writerow([author, book, year, f"${price:.2f}", quantity, f"${price * quantity:.2f}"])
                writer.writerow(['', '', '', '', 'Overall Total', f"${total_value:.2f}"])

            print(f"Files written to {file_name}.txt and {file_name}.csv")

        else:
            print("No books found in the entered price range.")
    except ValueError:
        print("Invalid input. Please enter numeric values for price range.")

# Main function that drives the program's menu
def main():
    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter Choice: ")
        if choice == "1":
            display_inventory()
        elif choice == "2":
            search_by_author()
        elif choice == "3":
            search_by_book_name()
        elif choice == "4":
            search_by_price_range()
        elif choice == "5":
            print("The program will stop now.")
            break  # Exit the loop and stop the program
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()  # Call the main function to run the program
