import json
import csv


with open('user.json', 'r') as user_file:
    users = json.load(user_file)


with open('books.csv', 'r') as books_file:
    books_reader = csv.DictReader(books_file)
    books = [{"title": row['Title'], "author": row['Author'], "pages": int(row['Pages']), "genre": row['Genre']} for row in books_reader]


num_users = len(users)
num_books = len(books)

book_index = 0
result_users = []
for i, user in enumerate(users):
    books_count = num_books // num_users
    if i < num_books % num_users:
        books_count += 1

    user_books = books[book_index:book_index+books_count]

    formatted_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user_books
    }
    result_users.append(formatted_user)

    book_index += books_count


for user in result_users:
    print(f"{user['name']} получил(а) {len(user['books'])} книг.")
    
    
with open('result.json', 'w') as result_file:
    json.dump(result_users, result_file, ensure_ascii=False, indent=4)

print('result.json успешно создан.')