import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jonny_Jack01",
    database="online_course"
)

cur = con.cursor()


def add_record(id=None, name=None, gender=None, dob=None, status=None):
    cur.execute("INSERT INTO learner VALUES (%s, %s, %s, %s, %s)",
                (id, name, gender, dob, status,))
    con.commit()


def view_data():
    cur.execute("SELECT * FROM learner")
    rows = cur.fetchall()
    return rows


def delete_record(id):
    cur.execute("DELETE FROM learner WHERE learner_id=%s", (id,))
    con.commit()


def search_data(id=None, name=None, gender=None, dob=None, status=None):
    if id is not None:
        cur.execute("SELECT * FROM learner WHERE learner_id=%s", (id,))
    else:
        cur.execute(
            "SELECT * FROM learner WHERE learner_id=%s AND learner_name=%s AND gender=%s AND date_of_birth=%s AND "
            "employment_status=%s",
            (id, name, gender, dob, status,))
    rows = cur.fetchall()
    return rows


def data_update(id=None, name=None, gender=None, dob=None, status=None):
    cur.execute(
        "UPDATE learner SET learner_id=%s AND learner_name=%s AND gender=%s AND date_of_birth=%s AND "
        "employment_status=%s WHERE learner_id=%s",
        (id, name, gender, dob, status, id,))
    con.commit()
