from flask import Flask, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)

# ----------------------------------------------------
# LOGGING CONFIG
# ----------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

# ----------------------------------------------------
# DB CONNECTION
# ----------------------------------------------------
def get_db():
    logging.debug("Attempting DB connection...")
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="V@ishnav1",
            database="company"
        )
        logging.debug("DB connection successful.")
        return db
    except Exception as e:
        logging.error(f"DB connection failed: {e}")
        raise

# ----------------------------------------------------
# GET EMPLOYEES
# ----------------------------------------------------
@app.route("/departments", methods=["GET"])
def get_employees():
    logging.debug("GET /departments called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing SELECT query")
        cursor.execute("SELECT * FROM departments")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500

# ----------------------------------------------------
# POST EMPLOYEE
# ----------------------------------------------------
@app.route("/departments", methods=["POST"])
def add_employee():
    logging.debug("POST /departments called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "INSERT INTO departments (dept_id,dept_name,emp_id) VALUES (%s,%s,%s)"
        logging.debug(f"Executing INSERT: {sql}")

        cursor.execute(sql, (data["dept_id"],data["dept_name"], data["emp_id"]))
        db.commit()
        db.close()

        logging.debug("POST completed")
        return "POST EXECUTED"
    except Exception as e:
        logging.error(f"Error in POST: {e}")
        return "POST ERROR", 500

# ----------------------------------------------------
# PUT EMPLOYEE
# ----------------------------------------------------
@app.route("/departments/<int:id>", methods=["PUT"])
def update_employee(emp_id):
    logging.debug(f"PUT /departments/{emp_id} called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "UPDATE departments SET dept_id=%s, dept_name=%s WHERE emp_id=%s"
        logging.debug(f"Executing UPDATE: {sql}")

        cursor.execute(sql, (data["dept_id"], data["dept_name"], data["emp_id"]))
        db.commit()
        db.close()

        logging.debug("PUT completed")
        return "PUT EXECUTED"
    except Exception as e:
        logging.error(f"Error in PUT: {e}")
        return "PUT ERROR", 500

# ----------------------------------------------------
# DELETE EMPLOYEE
# ----------------------------------------------------
@app.route("/departments/<int:id>", methods=["DELETE"])
def delete_employee(emp_id):
    logging.debug(f"DELETE /departments/{emp_id} called")
    try:
        db = get_db()
        cursor = db.cursor()

        sql = "DELETE FROM employees WHERE id=%s"
        logging.debug(f"Executing DELETE: {sql}")

        cursor.execute(sql, (emp_id,))
        db.commit()
        db.close()

        logging.debug("DELETE completed")
        return "DELETE EXECUTED"
    except Exception as e:
        logging.error(f"Error in DELETE: {e}")
        return "DELETE ERROR", 500

# ----------------------------------------------------
# RUN
# ----------------------------------------------------
if __name__ == "__main__":
    logging.debug("Starting Flask server...")
    app.run(debug=True)
