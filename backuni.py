import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jonny_Jack01",
    database="online_course"
)

cur = con.cursor()


def add_record(id=None, name=None, website=None, description=None):
    cur.execute("INSERT INTO university VALUES (%s, %s, %s, %s)",
                (id, name, website, description,))
    con.commit()


def view_data():
    cur.execute("SELECT * FROM university")
    rows = cur.fetchall()
    return rows


def delete_record(id):
    cur.execute("DELETE FROM university WHERE uni_id=%s", (id,))
    con.commit()


def search_data(id=None, name=None, website=None, description=None):
    if id is not None:
        cur.execute("SELECT * FROM university WHERE uni_id=%s", (id,))
    else:
        cur.execute(
            "SELECT * FROM university WHERE uni_id=%s AND uni_name=%s AND website=%s AND uni_description=%s",
            (id, name, website, description,))
    rows = cur.fetchall()
    return rows


def data_update(id=None, name=None, website=None, description=None):
    cur.execute(
        "UPDATE university SET uni_id=%s AND uni_id=%s AND website=%s AND uni_description=%s WHERE uni_id=%s",
        (id, name, website, description, id,))
    con.commit()
