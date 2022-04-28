# Fractal Rest API


This API was built for the [`Fractal Engine`](https://github.com/crispycret/fractal-webapp) to handle the generation of fractals and to act as an interface with the database.
Credentials are hidden.

## Setup

### Clone the repo
```
git clone https://github.com/crispycret/fractal-rest-api.git
cd fractal-rest-api
```

### Create and activate virtual environmnet
```
python -m venv venv
source venv/bin/activate
```

### Install dependendices
```
pip install -r requirements.txt
```

### Credentials
If you would like to use this program you need to create the following file at the following path: 

`fractal-rest-api/components/db/settings.json`

Inside the `settings.json` file you need to put your credentials for your mysql server.

### settings.json Structure
```
{
    "host": "",
    "port": 3306,
    "user": "",
    "password": "",
    "db_name": ""
}
```


## Start
You should now be ready to start the program.
```
flask run
```




# Example queries to the API

