import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="frnd"
)

cus = mydb.cursor()

month_num = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        category = request.form.get('category')

        if category:
            query = "SELECT name, dateofbrith, img FROM tblcategory WHERE category = %s"
            cus.execute(query, (category,))
            result = cus.fetchall()
            
            for i in range(len(result)):
                name, dateofbrith, img = result[i]
                month = dateofbrith.month
                month_name = month_num.get(month, "Unknown")
                result[i] = (name, month_name, img)
          
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
