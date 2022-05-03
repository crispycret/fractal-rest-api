import os, sys, json
import hashlib
import pymysql

from . import queries

# Try using GOOGLE_APPLICATION_CREDENTIALS environment variable instead of manually passing the file for security reasons.

class SETTINGS(object):
    '''
    The AWS_RDS requires a setting.json file with the following structure to connect to a database.
{
    "host": "",
    "port": 3306,
    "user": "",
    "password": "",
    "db_name": ""
}
    '''
    SETTINGS_PATH = os.path.join(os.path.curdir, 'components/db/settings.json')
    data = json.loads(open(SETTINGS_PATH, 'r').read())


    
class AWS_RDS (object):
    conn = None
    cursor = None

    host = SETTINGS.data['host']
    port = SETTINGS.data['port']
    user = SETTINGS.data['user']
    password = SETTINGS.data['password']
    db_name = SETTINGS.data['db_name']

    @staticmethod
    def connect():
        AWS_RDS.conn = pymysql.connect(
            host=AWS_RDS.host,
            port=AWS_RDS.port,
            user=AWS_RDS.user,
            password=AWS_RDS.password,
            db=AWS_RDS.db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        AWS_RDS.cursor = AWS_RDS.conn.cursor()
    
    @staticmethod
    def generate_columns_values(data):
        columns, values = ['','']
        size = len(data.keys())
        for i, item in enumerate(data.items()):
            if (i < size-1):
                columns += ', ' + item[0]
                values += ', ' + item[1]
        return [columns, values]

    @staticmethod
    def generate_where_constraint(data):
        size = len(data.keys())
        where_constraint = ''
        for i, item in enumerate(data.items()):

            where_constraint += item[0] + '='
            if type(item[1]) is not str: where_constraint += str(item[1])
            else: where_constraint += '"' + item[1] + '"'

            if (i < size-1):
                where_constraint += ' AND '
        return where_constraint


    @staticmethod
    def IsConnected():
        return bool(AWS_RDS.cursor)


    @staticmethod
    def ForceConnect():
        if not AWS_RDS.cursor:
            AWS_RDS.connect()
            if not AWS_RDS.cursor: return False
        return True

    @staticmethod
    def status_report(query):
        status = []
        status.append(AWS_RDS.cursor.execute(query))
        status.append(AWS_RDS.conn.commit())
        return status






    @staticmethod
    def create_user(data):
        """ Save a user to the database. """
        if not AWS_RDS.IsConnected(): return
        columns, values = AWS_RDS.generate_columns_values(data)
        query = queries.insert_user(columns, values)
        
        return AWS_RDS.status_report(query)[0]

    

    @staticmethod
    def select_user_id(username):
        if not AWS_RDS.IsConnected(): return
        query = queries.select_user_id(username)
        AWS_RDS.cursor.execute(query)
        return AWS_RDS.cursor.fetchone()


    @staticmethod
    def verify_user_password(data):
        if not AWS_RDS.IsConnected(): return
        username = data['username']
        secret = data['secret']
        query = queries.select_user(username, secret)
        AWS_RDS.cursor.execute(query)
        return AWS_RDS.cursor.fetchone()





    @staticmethod
    def create_fractal_type(data):
        if not AWS_RDS.IsConnected(): return
        columns, values = AWS_RDS.generate_columns_values(data)
        query = queries.insert_fractal_type(columns, values)
        return AWS_RDS.status_report(query)[0]
    
    @staticmethod
    def load_fractal_type(data):
        if not AWS_RDS.IsConnected(): return
        where_constraint = AWS_RDS.generate_where_constraint(data)
        query = queries.select_fractal_type(where_constraint)
        AWS_RDS.cursor.execute(query)
        return AWS_RDS.cursor.fetchall()
    




    @staticmethod
    def create_fractal_project(data):
        if not AWS_RDS.IsConnected(): return
        columns, values = AWS_RDS.generate_columns_values(data)
        query = queries.insert_fractal_project(columns, values)
        return AWS_RDS.status_report(query)[0]


    @staticmethod
    def load_fractal_project (data):
        """ Return users fractal projects as json object """
        if not AWS_RDS.IsConnected(): return
        where_constraint = AWS_RDS.generate_where_constraint(data)
        query = queries.select_fractal_project(where_constraint)
        AWS_RDS.cursor.execute(query)
        return AWS_RDS.cursor.fetchall()

    



    @staticmethod
    def create_mandelbrot(data):
        """ data is in json format. """
        # data = {
        #     "username": "", 
        #     "fractal_type": "", 
        #     "project_name": "", 
        #     "max_iteration": "", 
        #     "bounds": "", 
        #     "zoom": "", 
        #     "pos_x": "", 
        #     "pos_y": ""
        # }

        if not AWS_RDS.IsConnected(): return
        columns, values = AWS_RDS.generate_columns_values(data)
        query = queries.insert_mandelbrot(columns, values)            
        return AWS_RDS.status_report(query)[0]

 

    @staticmethod
    def update_mandelbrot(data):
        """ data is in json format. """             
        if not AWS_RDS.cursor: 
            AWS_RDS.connect()
            if not AWS_RDS.cursor: return

        primary_key_constraint = 'username="' + data['username'] + '"' +\
             ' AND ' + 'fractal_type="' + data['fractal_type'] + + '"' +\
             ' AND ' + 'project_name="' + data['project_name'] + '"'

        params = ''
        for i, column, value in enumerate(data.items()):
            params += column + '=' + value
            if (i < len(data)-1):
                parmas += ' AND '

        query = f'''
        UPDATE Mandelbrot 
        SET {params}
        WHERE {primary_key_constraint};
        '''

        return AWS_RDS.status_report(query)[0]

        
    @staticmethod
    def load_mandelbrot(data):
        if not AWS_RDS.IsConnected(): return
        where_constraint = AWS_RDS.generate_where_constraint(data)
        query = queries.select_mandelbrot(where_constraint)   
        AWS_RDS.cursor.execute(query)
        return AWS_RDS.cursor.fetchone()


if __name__ == '__main__':
    f = open('new.json', 'r')
    data = json.loads(f.read())

    AWS_RDS.connect()
    AWS_RDS.save_mandelbrot(data)

    # with open("db_dataset.json", 'r') as f:
    #     contents = json.load(f)
    #
    #     FirebaseDB.open_connection()
    #     FirebaseDB.set(contents)








