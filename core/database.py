import psycopg2


class Database:
    def __init__(self, host, user, password, port, dbname):
        self.con = psycopg2.connect(host=host, user=user, password=password, port=port, dbname=dbname)
        self.cur = self.con.cursor()

        self.con.autocommit = True

    def get_users(self) -> dict:
        data = {}
        self.cur.execute("SELECT * FROM worker;")
        for line in self.cur.fetchall():
            data[line[0]] = {'id': line[0], 'fio': line[1],  'post': line[5], 'remarks': line[8]}
        return data

    def add_user(self, fio, post):
        self.cur.execute('INSERT INTO worker(fio, post) values (%s, %s)', (fio, post))

    def add_remark(self, user_id):
        self.cur.execute(f"UPDATE worker SET remarks = remarks + 1 WHERE id = %s", (user_id, ))

    def get_statements(self):
        data = []
        self.cur.execute("SELECT * FROM statements;")
        for line in self.cur.fetchall():
            data.append({'id': line[0], 'employee_id': line[1], 'type': line[2]})
        return data

    def add_statements(self, user_id, statement_type):
        self.cur.execute('INSERT INTO statements(employee_id, type) values (%s, %s)', (user_id, statement_type))
