import sys, os, json




def insert_user (columns, values):
    return f'INSERT INTO User ({columns}) VALUES ({values});'

def update_user (set, where):
    return f'UPDATE User SET {set} WHERE {where};'

def select_user_id (username):
    return f'SELECT id FROM User WHERE username="{username}";'

def verify_user_password (username, secret):
    return f'SELECT id FROM User WHERE username="{username}" AND secret="{secret}";'
    



def insert_fractal_type (columns, values):
    return f'INSERT INTO FractalType ({columns}) VALUES ({values});'

def update_fractal_type(set, where):
    return f'UPDATE FractalType SET {set} WHERE {where};'

def select_fractal_type(where):
    if where == None:
        return f'SELECT * FROM FractalType WHERE {where};'
    return  f'SELECT * FROM FractalType;'

def select_all_fractal_types():
    return  f'SELECT * FROM FractalType;'



def insert_fractal_project(columns, values):
    return f'INSERT INTO FractalProject ({columns}) VALUES ({values});'

def update_fractal_project(set, where):
    return f'UPDATE FractalProject SET {set} WHERE {where};'

def select_fractal_project(where):
    return f'SELECT * FROM FractalProject WHERE {where};'

def select_all_public_fractal_projects(where):
    return f'SELECT * FROM FractalProject WHERE public=TRUE;'
    
def select_all_fractal_projects_(where):
    return f'SELECT * FROM FractalProject WHERE public=TRUE;'


def insert_mandelbrot(columns, values):
    return 'INSERT INTO Mandelbrot ({columns}) VALUES ({values});'

def update_mandelbrot(set, where):
    return 'UPDATE Mandelbrot SET {set} WHERE {where};'

def select_mandelbrot(where):
    return 'SELECT * FROM Mandelbrot WHERE {where};'


