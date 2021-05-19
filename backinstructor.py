import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jonny_Jack01",
    database="online_course"
)

cur = con.cursor()


def add_record(insid=None, uniid=None, name=None, gender=None, dob=None, major=None):
    cur.execute("INSERT INTO instructor VALUES (%s, %s, %s, %s, %s, %s)",
                (insid, uniid, name, gender, dob, major,))
    con.commit()


def view_data():
    cur.execute("SELECT * FROM instructor")
    rows = cur.fetchall()
    return rows


def delete_record(id):
    cur.execute("DELETE FROM instructor WHERE instructor_id=%s", (id,))
    con.commit()


def search_data(insid=None, uniid=None, name=None, gender=None, dob=None, major=None):
    if insid is not None:
        cur.execute("SELECT * FROM instructor WHERE instructor_id=%s", (insid,))
    else:
        cur.execute(
            "SELECT * FROM instructor WHERE instructor_id=%s AND uni_id=%s AND instructor_name=%s AND gender=%s AND "
            "date_of_birth=%s AND major=%s",
            (insid, uniid, name, gender, dob, major,))
    rows = cur.fetchall()
    return rows


def data_update(insid=None, uniid=None, name=None, gender=None, dob=None, major=None):
    cur.execute(
        "UPDATE instructor SET instructor_id=%s AND uni_id=%s AND instructor_name=%s AND gender=%s AND "
        "date_of_birth=%s AND major=%s WHERE instructor_id=%s",
        (insid, uniid, name, gender, dob, major,))
    con.commit()
