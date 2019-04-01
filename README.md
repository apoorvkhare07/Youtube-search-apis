# Youtube-search-apis

An Api and dashboard to give data about latest videos of a particular search query.
  
### Prerequisites
Install Django2.0, Python3.6, restframework, django_crontab.

### Deployment steps

* Clone the Repository
* Run Migrations
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* Start the Cronjob
  * `python manage.py add crontab add`: This starts a cronjob which fetches data from Youtube every hour and stores in the database.
* Start the server
  * `python manage.py runserver`

#### Dashboard
* Go to `localhost:8000/search`, this will open the dashboard with pagination. This shows 12 videos on a page sorted on the basis of publish time.

#### Api Endpoint
* `localhost:8000/search/api`, this returns Json response of the first 12 videos and with a `nextPageId` value.
* The requests takes an optional parameter `pageId`. Which sends the video's data of the next page. `localhost:8000/search/api?pageId=` 
