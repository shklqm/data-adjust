# Data-adjust


### Install & run

First install requirements

    pip install -r requirements.txt

Next run migrations

    python manage.py makemigrations api
    python manage.py migrate

Then load fixture data

    python manage.py loaddata records_data

Finally runserver

    python manage.py runserver



### Sample test cases

1. Impressions and clicks api
    http://localhost:8000/api/range/?group_by=channel&group_by=country&date_to=2017-06-01&order_by=clicks&order_type=desc

2. Installs api
    http://localhost:8000/api/installs/?month=5&year=2017&group_by=date&order_by=date&order_type=asc

3. Revenue api
    http://localhost:8000/api/revenue/?date=2017-06-01&group_by=os&order_by=revenue&order_type=desc

4. Metric api
    http://localhost:8000/api/metric/?country=CA&group_by=channel&order_by=cpi&order_type=desc
