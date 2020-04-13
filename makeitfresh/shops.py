from shopproject import create_app, db, bcrypt
from shopproject.models import User, Shop, Address
import csv
app=create_app()
app.app_context().push()
db.drop_all()
db.session.commit()
db.create_all()
db.session.commit()
with open("csv/users.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    count = 0
    for row in csv_reader:
        if count != 0:
            password = bcrypt.generate_password_hash(row[5])
            user = User(
                user_type=row[0],
                username=row[1],
                email=row[2],
                first_name=row[3],
                last_name=row[4],
                password=password,
            )
            db.session.add(user)
        count +=1

with open("csv/address.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    count = 0
    for row in csv_reader:
        if count != 0:
            address = Address(
                user_id = row[0],
                street_address = row[2],
                district=row[1].lower(),
                pincode=row[3],
            )
            db.session.add(address)
        count +=1

with open("csv/shops.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    count = 0
    for row in csv_reader:
        if count != 0:
            shop = Shop(
                name=row[0],
                propreiter_name=row[1],
                phone_number=row[2],
                address_id=row[3],
                user_id=row[4],
                is_authorised=bool(row[5])
            )
            db.session.add(shop)
        count+=1

db.session.commit()

            


