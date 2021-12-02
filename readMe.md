
## Signup
Method POST 
routes
localhost:3000/user/signup

```shell
"name": "Abacd",
"email": "abcd@example.com",
"password": "abc123",
"role": "admin"
```

## Login
Method POST 
routes
localhost:3000/user/login

```shell
"email": "abcd@example.com",
"password": "abc123"
```

## Admin Routes
method GET
routes
localhost:3000/auth/admin
{User must be login and the role should be admin}

## Employee Routes
method GET
routes
localhost:3000/auth/emp
{User must be login}