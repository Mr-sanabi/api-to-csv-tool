def extract_user_row(user):
    result = {
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "city": user["address"]["city"],
        "company": user["company"]["name"],
        "website": user["website"]
    }

    return result

def extract_user_rows(users):
    rows = []
    for user in users:
        row = extract_user_row(user)
        rows.append(row)

    return rows