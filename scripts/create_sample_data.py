from products.models import Category, Product
c1, _ = Category.objects.get_or_create(name='Libros', slug='libros')
c2, _ = Category.objects.get_or_create(name='Papelería', slug='papeleria')
c3, _ = Category.objects.get_or_create(name='Segunda Mano', slug='segunda-mano')
Product.objects.get_or_create(name='Aprende Django', defaults={'price': 19990, 'stock': 10, 'description': 'Un libro para aprender Django paso a paso.', 'category': c1})
Product.objects.get_or_create(name='Cuaderno A4 - 100 hojas', defaults={'price': 1990, 'stock': 50, 'description': 'Cuaderno para apuntes.', 'category': c2})
Product.objects.get_or_create(name='Libro usado: Clásicos', defaults={'price': 7990, 'stock': 3, 'description': 'Edición de segunda mano en buen estado.', 'category': c3})
print('Datos de ejemplo creados (si no existían)')
