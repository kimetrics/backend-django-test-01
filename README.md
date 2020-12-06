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

# Deployment as container

The project can be used within a container.

Run the bash script:

	$ docker build -t backend . -f Dockerfile

Run the following command:

	$ docker run --rm -it  backend
## Challenge Solution by

* **José Nicolielly** - - [jcnil](https://github.com/jcnil/backend-django-test-01)
