from flask import Flask, request
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect(
    dbname="zaherDB",
    user="super_zaher",
    password="user123",
    host="localhost",
    port="5432",
)


cur = conn.cursor()

users = [{"name": "", "phone": "", "email": "", "password": ""}]

proudcts = [{"name": "", "price": "", "item_count": 0, "owner_id": 0}]


@app.get("/users")
def get_all_user():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    return {"users": users}


# @app.get("/proudcts")
# def get_all_products():
#     cur.execute("SELECT * FROM proudcts")
#     proudcts = cur.fetchall()


@app.get("/delete/<int:id>")
def delete_user(id):
    cur.execute(f"delete from users where user_id = {id}")
    conn.commit()
    return {"users": users}


# @app.get("/delete/<init:id>")
# def delete_proudct(id):
#     cur.execute(f"DELETE FROM proudcts where id_product = {id}")
#     conn.commit()
#     return{"proudcts" : proudcts}


@app.post("/add")
def creat_new_user():
    request_data = request.get_json()
    new_user = {
        "name": request_data["name"],
        "phone": request_data["phone"],
        "email": request_data["email"],
        "password": request_data["password"],
    }
    cur.execute(
        "INSERT INTO users (name, email,password,phone) VALUES (%s,%s,%s,%s)",
        [
            new_user.get("name"),
            new_user.get("email"),
            new_user.get("password"),
            new_user.get("phone"),
        ],
    )  #
    conn.commit()
    cur.execute("SELECT * FROM users ")
    users = cur.fetchall()
    return {"users": users}


# @app.post("/add")
# def add_new_product():
#     request_data =request.json()
#     new_product = {"name":request_data["name"], "price":request_data["price"],"item_count":request_data["item_count"],"owner_id":request_data["owner_id"] }
#     cur.execute("INSERT INTO proudcts (name, price,item_count,owner_id) VALUES (%s,%s,%s)",[new_product.get("name"),new_product.get("price"),new_product.get("item_count"),new_product.get("owner_id")])
#     conn.commit()
#     cur.execute("select * from products")
#     proudcts = cur.fetchall()
#     return {"users" : users}

# # @app.post("/proudct/<string:name>/item")
# # def create_product(name):
# #     request_data = request.get_json()
# #     for prouduct in proudcts:
# #         if prouduct["name"] == name :
# #             New_item = {"name":request_data["name"],"price":request_data["price"]}
# #             prouduct["items"].append(New_item)
# #             return New_item , 201
# #     return{"message": "store not found"}, 404


# # @app.get("/store/<string:name>")

# # def Get_One_store(name):


# #     for store in stores:
# #         if store["name"] == name :
# #             return store

# #     return{"message" :"this store not found"} , 404


# # @app.get("/store/<string:name>/item")
# # def Get_All_items_in_one_store(name):

#     for store in stores:
#         if store["name"] == name :
#             return {'items':store["items"]}
#     return{"message" :"this store not found"} , 404


if __name__ == "__main__":
    app.run(debug=True, port=9000)
