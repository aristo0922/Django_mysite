# Django_mysite

## migration

```terminal
# user model에 대한 migration을 만든다
jang-alyeong-ui-MacBook-Pro:mysite aristo$ python3 manage.py makemigrations
Migrations for 'account':
  account/migrations/0001_initial.py
    - Create model user
    
# 앞서 만든 migration을 db 와 연동한다
jang-alyeong-ui-MacBook-Pro:mysite aristo$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, sessions
Running migrations:
  Applying account.0001_initial... OK
  Applying contenttypes.0001_initial... OK

```
