import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jonny_Jack01",
    database="online_course"
)

cur = con.cursor()


def add_record(id, name, topic, syllabus, price, description):
    cur.execute("INSERT INTO course VALUES (%s, %s, %s, %s, %s, %s)",
                (id, name, topic, syllabus, price, description,))
    con.commit()


def view_data():
    cur.execute("SELECT * FROM course")
    rows = cur.fetchall()
    return rows


def delete_record(id):
    cur.execute("DELETE FROM course WHERE course_id=%s", (id,))
    con.commit()


def search_data(id, name, topic, syllabus, price, description):
    if id is not None:
        cur.execute("SELECT * FROM course WHERE course_id=%s", (id,))
    else:
        cur.execute(
            "SELECT * FROM course WHERE course_id=%s AND course_name=%s AND topic=%s AND syllabus=%s AND "
            "price=%s AND course_description=%s",
            (id, name, topic, syllabus, price, description,))
    rows = cur.fetchall()
    return rows


def data_update(id, name, topic, syllabus, price, description):
    cur.execute(
        "UPDATE course SET course_id=%s AND course_name=%s AND topic=%s AND syllabus=%s AND "
        "price=%s AND course_description=%s WHERE course_id=%s",
        (id, name, topic, syllabus, price, description, id,))
    con.commit()
