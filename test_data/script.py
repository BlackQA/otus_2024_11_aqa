import csv
import json


def read_books(csv_file_path):
    books = []
    with open(csv_file_path, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = {
                "title": row.get("Title"),
                "author": row.get("Author"),
                "pages": int(row.get("Pages", 0)),
                "genre": row.get("Genre"),
            }
            books.append(row)
    return books


def read_users(json_file_path):
    with open(json_file_path, mode="r") as jsonfile:
        users = json.load(jsonfile)
    return users


def distribute_books(books, users):
    num_books = len(books)
    num_users = len(users)
    base_amount = num_books // num_users
    remainder = num_books % num_users

    distributed_books = []
    start = 0
    for i in range(num_users):
        end = start + base_amount + (1 if i < remainder else 0)
        distributed_books.append(books[start:end])
        start = end
    return distributed_books


def create_result_json(users, distributed_books):
    result = []
    for user, books in zip(users, distributed_books):
        user_data = {
            "name": user.get("name"),
            "gender": user.get("gender"),
            "address": user.get("address"),
            "age": user.get("age"),
            "books": [],
        }
        for book in books:
            book_data = {
                "title": book.get("Title"),
                "author": book.get("Author"),
                "pages": book.get("Pages"),
                "genre": book.get("Genre"),
            }
            user_data["books"].append(book_data)
        result.append(user_data)
    return result


def main():
    books = read_books("books.csv")
    users = read_users("users.json")
    distributed_books = distribute_books(books, users)
    result = create_result_json(users, distributed_books)
    with open("result.json", mode="w") as jsonfile:
        json.dump(result, jsonfile, ensure_ascii=False, indent=4)
    print("result.json создан успешно.")


if __name__ == "__main__":
    main()
