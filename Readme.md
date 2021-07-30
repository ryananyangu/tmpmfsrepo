# NEAREST POINTS

## Assumptions 
- First point in list of tuples in x cordinate
- Second point in the list of tuples in y cordinate
- Uploaded points are grouped batchwise (each api request corresponds to a unique batch)
- Shortest distance accounts also for dirrection hence repetion of some points


## Assumed parts being examined 
- Application/api security (registaration and token generation) [Done]
- Data normalizations (Database functionlity) [Done]
- Auditable data (Timestamps of data changes)[Done]
- Application testability (Unit tests)[Done]
- Application documentation (Feature and code documentation)
- Code versioning (Git hub) [Done]
- Cloud deployment CI/CD (Heroku or GCP) [Done]
- Depandencies management (Requirements.txt) [Done]
- Logging and log management [Done]
- General application design (12 factor app)



## Tasks
1. Create a Django application. [Done]
2. The application should have an API endpoint that accepts a string of comma separated
points for example “(2,3), (1,1), (5, 4), ...” and calculates the closest points. It then stores them
in a table with the following details: 
-The string of points submitted [Done]
-The result of the computation: the closest points pair [Done]
3. Write unit tests to validate your expectations
4. Host the application on Heroku (or a different service of choice that will be publicly
available)[Done]
5. Host your code on GitHub and share repository[Done]
6. Also share the API of the application and any credentials that might be needed alongside a
summary of how your application works


```
coverage run --source='.' manage.py test cordinates

Name                                                                                                         Stmts   Miss  Cover
--------------------------------------------------------------------------------------------------------------------------------
cordinates/__init__.py                                                                                           0      0   100%
cordinates/admin.py                                                                                              3      0   100%
cordinates/apps.py                                                                                               4      0   100%
cordinates/migrations/0001_initial.py                                                                            7      0   100%
cordinates/migrations/__init__.py                                                                                0      0   100%
cordinates/models.py                                                                                            15      0   100%
cordinates/tests.py                                                                                             23      0   100%
cordinates/views.py                                                                                             72      1    99%
```
