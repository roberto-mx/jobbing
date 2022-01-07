# Routes 
## Catalogs
- ```GET /countries```
- ```GET /countries/{id}```
- ```GET /states```
- ```GET /states/{id}```
- ```GET /states/filter?country={id}```
- ```GET /municipalities```
- ```GET /municipalities/{id}```
- ```GET /municipalities/filter?state={id}```
- ```GET /colonies```
- ```GET /colonies/{id}```
- ```GET /colonies/filter?municipality={id}```
- ```GET /colonies/filter?zipcode={zip}```
- ```GET /zipcodes```
- ```GET /zipcodes/{id}```
- ```GET /skills```
- ```GET /skills/{id}```
- ```GET /status```
- ```GET /status/{id}```

## Authentication
- ```POST /login```
- ```POST /logout```

## Users
- ```GET /users```
- ```GET /users/{id}```
- ```GET /users/filter?rol={id}```
- ```GET /users/filter?skill={id}```
- ```GET /userus/filter?status={id}```
- ```GET /users/{id}/address```
- ```PUT /users/{id}```
- ```PUT /users/{id}/address```
- ```POST /users```
- ```POST /users/{id}/address```
- ```DELETE /users/{id}```
- ```DELETE /users/{id}/address```

## Media
- ```GET /media```
- ```GET /media/{id}```
- ```PUT /media/{id}```
- ```POST /media```
- ```DELETE /media/{id}```