How to call some endpoints with authentication

# Login
Call login:
```
wget --post-file=login --header=Content-Type:application/json http://localhost:5000/login
```

the file login should content something like (TODO: just to send username and password):

```
{
  "email": "admin@admin.com",
  "imageProfile": "0",
  "password": "admin",
  "username": "admin"
}
```

# Call user
```
wget -d --header="x-access-token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI1ODE4ZmVhOC01OGE0LTRlYTctOWNiNC1lMGRmNDk1YTc0M2QiLCJleHAiOjE2MjQ4NTA4NjN9.U3XSP7VmMQMzs-dHNY_6WtO1EyWijjFptU_LwxCWRig" http://localhost:5000/user/5818fea8-58a4-4ea7-9cb4-e0df495a743d
```