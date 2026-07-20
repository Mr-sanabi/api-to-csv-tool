def extract_user_row(user):
    address = user.get("address") or {}
    company = user.get("company") or {}
    result = {
        "id": user.get("id"),
        "name": user.get("name"),
        "username": user.get("username"),
        "email": user.get("email"),
        "city": address.get("city"),
        "company": company.get("name"),
        "website": user.get("website")
    }

    return result

def extract_user_rows(users):
    rows = []
    for user in users:
        row = extract_user_row(user)
        rows.append(row)

    return rows
