import pymysql

class Crud:

    def __init__(self):
        self.con = pymysql.connect(host='localhost',user='root',password='punitha',
db='Inventory'
        )
        print("Welcome to my shop")

    def add(self, id, name, category, price, quantity):
        q ="insert into product(id,name,category,price,quantity)values({0}, '{1}', '{2}', {3}, {4})".format(id,name,category,price,quantity)
        

        cur = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        cur.close()

        print("Added Successfully")

    def view(self):
        q = "SELECT * FROM product"

        cur = self.con.cursor()
        cur.execute(q)

        data = cur.fetchall()

        for row in data:
            print(row)

        cur.close()

        print("View Successful")

    def edit(self, id, price):
        q = "UPDATE product SET price=%s WHERE id=%s"

        cur = self.con.cursor()
        cur.execute(q, (price, id))
        self.con.commit()
        cur.close()

        print("Update Successful")

    def delete(self, id):
        q = "DELETE FROM product WHERE id=%s"

        cur = self.con.cursor()
        cur.execute(q, (id,))
        self.con.commit()
        cur.close()

        print("Delete Successful")
import db as pro

obj = pro.Crud()

while True:
    try:
        print("\n1.Add\n2.View\n3.Update\n4.delete\n5.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            i = int(input("Enter ID: "))
            n = input("Enter Name: ")
            c = input("Enter Category: ")
            p = int(input("Enter Price: "))
            q = int(input("Enter Quantity: "))

            obj.add(i, n, c, p, q)

        elif ch == 2:
            obj.view()

        elif ch == 3:
            print("\nProduct update shop")

            i = int(input("Enter ID: "))
            p = int(input("Enter Price: "))

            obj.edit(i, p)

        elif ch == 4:
            print("\nProduct delete shop")

            i = int(input("Enter ID: "))

            obj.delete(i)

        elif ch == 5:
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)



