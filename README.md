# Point of sale test

Write a very basic Django project that uses Django Rest Framework to provide a RESTful API for a point of sale that let's you track the inventory of products and the orders done.

Use the provided project boilerplate and add the code needed to pass all the *unit tests* provided in both `modules.inventory.tests` and `modules.orders.tests`.

Use at least the models provided in both `modules.inventory.models` and `modules.orders.models`, but feel free to add any extra model if needed. You are only allowed to use `django-rest-framework` and no other library.

The API must use **JSON** format and should provide the following endpoints and functionalities:

### `/api/products/`

* List all existing products
* Create a new product
* Retrieve an existing product
* Update an existing product

Note that **deleting a product is not allowed**.

A product must allow you to save:

* The description of the product
* The unit price of the product in cents
* The available stock of the product

### `/api/orders/`

* List all existing orders
* Create a new order
* Retrieve an existing order

Note that **updating or deleting a product is not allowed**.

A order must allow you to save/calculate:

* The list of items that were purchased
* The quantity of each item
* The total amount earned by the order in cents

Note that when a order is created, the corresponding products' stock must be updated.

## Instructions

### For code
1. Fork this repository
2. Get a local copy of your fork
3. Create a new branch
4. Install the requirements with `pip install -r requirements.txt`
5. Run your tests with `python src/manage.py test src`
6. Commit your work when the command above reports an OK result
7. Push your work to your fork
8. Send a pull request from your fork's branch to this repo

### For deployment
1. Complete the `Dockerfile` to assemble an image.
2. Configure with `Gunicorn` and connect with a web server or reverse proxy that you prefer.
3. Deploy it in the cloud infrastructure that you prefer (Ask for an instance if you don't have).
4. Create a basic document with the steps to deploy.



## Run development Docker environment

To run development environment using docker and docker-compose,
you only need to run:

    $ docker-compose up --build

The docker-compose.yml file define an architecture that uses
a Nginx services as reverse proxy for the app, a PostgreSQL service
for the database and a django service that run the application.

- The djago service is built with the main *Dockerfile* in the project root path, and all the configurations
  files are stored in *deploy/app/*, like gunicorn, supervisor, entrypoint and wait-for-it.


- The nginx service is built with the *Dockerfile* inside of *deploy/nginx/*, and store the nginx configuration
template for the application. The differences between template file and configuration file is that a
template file can use environment variables and a configuration file can't. The nginx image (>1.19)
reads the template files inside the folder */etc/nginx/templates/* and replace the environment variables,
after the replacement the config files are moved into */etc/nginx/conf.d/* removing the *.template* extension from the
template file. An input-outpu explame is showing below:
  

    Input:   /etc/nginx/templates/mysite.conf.template
    Output:  /etc/nginx/conf.d/mysite.conf

Feel free to change the nginx and application configuration files to adapt to you needs.

To theploy the application using heroku see [DEPLOY.md](DEPLOY.md)


## Challenge Querys

### Query 1:

```sql
SELECT e.estado, t.*, e.nielsen AS aera FROM tienda AS t
INNER JOIN estado AS e
ON e.id = t.estado_id
WHERE venta = (
	SELECT max(venta) 
	FROM tienda
)
```

### Query 2:
```sql
SELECT e.estado, count(e.estado) AS ventas, SUM(t.venta) AS total, MAX(t.venta) as venta_mayor
FROM tienda AS t
INNER JOIN estado AS e
ON e.id = t.estado_id
GROUP BY e.estado
ORDER BY total DESC
```


### Query 3
```sql
SELECT DISTINCT ON (e.estado) e.estado, t.*
FROM public.tienda as t
INNER JOIN estado as e
on e.id = t.estado_id
order by e.estado DESC
```