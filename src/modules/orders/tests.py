from django.test import Client, TestCase

from modules.inventory.models import Product

from .models import Order


class OrdersTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.coke = Product.objects.create(
            description="Coca-Cola",
            unit_price=500,
            stock=10,
        )
        self.chips = Product.objects.create(
            description="Potato Chips",
            unit_price=1000,
            stock=10,
        )

    def get_request_body(self):
        return {
            'items': [
                {
                    "id": self.coke.id,
                    "quantity": 1,
                },
                {
                    "id": self.chips.id,
                    "quantity": 2,
                },
            ]
        }

    def create_order(self):
        response = self.client.post(
            '/api/orders/',
            self.get_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)

        data = response.json()
        order = Order.objects.get(id=data['id'])
        return order

    def test_list_orders(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        order = self.create_order()
        expected = [
            {
                'id': order.id,
                'items': [
                    {
                        'description': 'Coca-Cola',
                        'quantity': 1,
                        'unit_price': 500,
                        'total': 500,
                    },
                    {
                        'description': 'Potato Chips',
                        'quantity': 2,
                        'unit_price': 1000,
                        'total': 2000,
                    }
                ],
                'total': 2500,
            }
        ]
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_create_order(self):
        self.assertEqual(Order.objects.count(), 0)

        response = self.client.post(
            '/api/orders/',
            self.get_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)

        order = Order.objects.get()
        expected = {
            'id': order.id,
            'items': [
                {
                    'description': 'Coca-Cola',
                    'quantity': 1,
                    'unit_price': 500,
                    'total': 500,
                },
                {
                    'description': 'Potato Chips',
                    'quantity': 2,
                    'unit_price': 1000,
                    'total': 2000,
                }
            ],
            'total': 2500,
        }
        self.assertEqual(response.json(), expected)

        self.coke.refresh_from_db()
        self.assertEqual(self.coke.stock, 9)

        self.chips.refresh_from_db()
        self.assertEqual(self.chips.stock, 8)

    def test_get_order(self):
        order = self.create_order()
        expected = {
            'id': order.id,
            'items': [
                {
                    'description': 'Coca-Cola',
                    'quantity': 1,
                    'unit_price': 500,
                    'total': 500,
                },
                {
                    'description': 'Potato Chips',
                    'quantity': 2,
                    'unit_price': 1000,
                    'total': 2000,
                }
            ],
            'total': 2500,
        }
        response = self.client.get(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_get_order_after_editing_products(self):
        order = self.create_order()
        expected = {
            'id': order.id,
            'items': [
                {
                    'description': 'Coca-Cola',
                    'quantity': 1,
                    'unit_price': 500,
                    'total': 500,
                },
                {
                    'description': 'Potato Chips',
                    'quantity': 2,
                    'unit_price': 1000,
                    'total': 2000,
                }
            ],
            'total': 2500,
        }

        response = self.client.get(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

        self.coke.description = "Coca-Cola 500ml"
        self.coke.unit_price = 800
        self.coke.save()

        self.chips.description = "Potato Chips 100gr"
        self.chips.unit_price = 900
        self.chips.save()

        response = self.client.get(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_update_order(self):
        order = self.create_order()

        # Test HTTP PUT
        response = self.client.put(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 405)

        # Test HTTP PATCH
        response = self.client.patch(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 405)

    def test_delete_order(self):
        order = self.create_order()
        response = self.client.delete(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, 405)
