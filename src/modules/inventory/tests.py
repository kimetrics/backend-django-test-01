from django.test import Client, TestCase

from .models import Product


class ProductTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def create_coke(self):
        return Product.objects.create(
            description='Coca-Cola',
            unit_price='500.01',
            stock=10
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), [])

        coke = self.create_coke()
        expected = [
            {
                'id': coke.id,
                'description': 'Coca-Cola',
                'unit_price': '500.01',
                'stock': 10,
            }
        ]
        response = self.client.get('/api/products/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), expected)

    def test_create_product(self):
        self.assertEquals(Product.objects.count(), 0)

        body = {
            'description': 'Coca-Cola',
            'unit_price': '500.01',
            'stock': 10,
        }
        response = self.client.post('/api/products/create/', body, 'application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Product.objects.count(), 1)

        product = Product.objects.get()
        expected = {
            'id': product.id,
            'description': 'Coca-Cola',
            'unit_price': '500.01',
            'stock': 10,
        }
        self.assertEquals(response.json(), expected)

    def test_get_product(self):
        coke = self.create_coke()
        expected = {
            'id': coke.id,
            'description': 'Coca-Cola',
            'unit_price': '500.01',
            'stock': 10,
        }
        response = self.client.get(f'/api/products/retrieve/{coke.id}/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), expected)

    def test_get_product_after_edition(self):
        coke = self.create_coke()
        expected = {
            'id': coke.id,
            'description': 'Coca-Cola',
            'unit_price': '500.01',
            'stock': 10,
        }
        response = self.client.get(f'/api/products/retrieve/{coke.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

        coke.description = "Coca-Cola 500ml"
        coke.unit_price = '800.01'
        coke.save()

        expected = {
            'id': coke.id,
            'description': 'Coca-Cola 500ml',
            'unit_price': '800.01',
            'stock': 10,
        }
        response = self.client.get(f'/api/products/retrieve/{coke.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_update_product(self):
        coke = self.create_coke()
        response = self.client.get(f'/api/products/retrieve/{coke.id}/')
        self.assertEqual(response.status_code, 200)

        # Test HTTP PUT
        body = {
            'description': 'Coca-Cola 500ml',
            'unit_price': '800.01',
            'stock': 5,
        }
        expected = {
            'id': coke.id,
            'description': 'Coca-Cola 500ml',
            'unit_price': '800.01',
            'stock': 5,
        }
        response = self.client.put(
            f'/api/products/update/{coke.id}/',
            body,
            'application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

        # Test HTTP PATCH
        body = {
            'unit_price': '900.01',
            'stock': 6,
        }
        expected = {
            'id': coke.id,
            'description': 'Coca-Cola 500ml',
            'unit_price': '900.01',
            'stock': 6,
        }
        response = self.client.patch(
            f'/api/products/update/{coke.id}/',
            body,
            'application/json'
        )
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_delete_product(self):
        coke = self.create_coke()
        response = self.client.delete(f'/api/products/delete/{coke.id}/')
        self.assertEquals(response.status_code, 405)
