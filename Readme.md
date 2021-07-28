# NEAREST POINTS

## Assumptions 
- First point in list of tuples in x cordinate
- Second point in the list of tuples in y cordinate
- Uploaded points are grouped batchwise (each api request corresponds to a unique batch)
- Shortest distance accounts also for dirrection hence repetion of some points


## Assumed parts being examined 
- Application/api security (registaration and token generation)
- Data normalizations (Database functionlity)
- Auditable data (Timestamps of data changes)
- Application testability (Unit tests)
- Application documentation (Feature and code documentation)
- Code versioning (Git hub)
- Cloud deployment CI/CD (Heroku or GCP)
- Depandencies management (Requirements.txt)
- Logging and log management
- General application design (12 factor app)



## Tasks
1. Create a Django application. [Done]
2. The application should have an API endpoint that accepts a string of comma separated
points for example “(2,3), (1,1), (5, 4), ...” and calculates the closest points. It then stores them
in a table with the following details: 
-The string of points submitted
-The result of the computation: the closest points pair [Done]
3. Write unit tests to validate your expectations
4. Host the application on Heroku (or a different service of choice that will be publicly
available)
5. Host your code on GitHub and share repository
6. Also share the API of the application and any credentials that might be needed alongside a
summary of how your application works
