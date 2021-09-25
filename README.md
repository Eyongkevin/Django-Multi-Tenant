# Multi-Tenant Application in Django
Here, we build an application in Django that serve multi-tenant purposes. 


# About Branch
This branch is an application of shared app-server with isolated database.

## Setup
- Clone and download code from this repo
- Create postgres databases. Check `DATABASES` in the setting.py file to know which databases to create.
- Do a migrate(check commands below)
- Create super users for each database(check commands below)
- Configure your subdomains so that `<xxx>.polls.local` hits your development machine by modifying
    - `/etc/host` for mac and linux
    - `C:\Windows\System32\Drivers\etc\hosts` for windows

    Add
    ```
    127.0.0.1 thor.polls.local 
    127.0.0.1 potter.polls.local
    ```
- Run server(check commands below)
- Access each tenant via its url
    `thor.pools.local:8000/admin` or `potter.pools.local:8000/admin`
# Commands
Here are commands that we can run for this multi-tenant application.

**NB**: Database available are `thor` and `potter`
## migrate
`python manage.py migrate --database=<db-name>`

Without the database argument, it will default to the `default` database


## makemigrations
`python manage.py makemigrations <app-name>`

This will perform the makemigration for all database.

## create super user
```
python manage.py createsuperuser_tenant
        --user=?
        --password=?
        --email=?
        --database=?
```