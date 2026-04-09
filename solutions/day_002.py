def create_user_profile() -> dict:
    username = input()
    age = int(input())
    is_premium = input().strip().lower() == "true"
    dic = {"name":username, "age":age,"premium":is_premium, "points":100}
    print(dic)
    return dic
