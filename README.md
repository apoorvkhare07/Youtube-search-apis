# Youtube-search-apis

An Api and dashboard to give data about latest videos of a particular search query.
  
### Prerequisites
Install Django2.0, Python3.6, restframework, django_crontab.

### Deployment steps

* Clone the Repository
* Install Django cursor pagination library
  * `pip install django-cursor-pagination`
* Run Migrations
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* Start the Cronjob
  * `python manage.py crontab add`: This starts a cronjob which fetches data from Youtube every hour and stores in the database.
* Start the server
  * `python manage.py runserver`

#### Dashboard
* Go to `localhost:8000/search`, this will open the dashboard with pagination. This shows 12 videos on a page sorted on the basis of publish time.

#### Api Endpoint
* `localhost:8000/search/api`, this returns Json response of the first 10 videos. The response contains 2 boolean flags `has_next_page` and `has_previous_page` telling whether the page has next or previous page and 2 values `last_cursor` and `first_cursor` of the corresponding page data.
* The requests takes an optional parameter `after` or `before`. Where after takes the `last_cursor` and gives the next page whereas before takes the `first_cursor` and gives previous page data. 

`localhost:8000/search/api?after/before=` 
