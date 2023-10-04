import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')  # Replace 'your_project_name' with your actual project name
django.setup()

# Import the Menu model
from restaurant.models import Menu

# Sample menu items data
menu_items_data = [
    {
        'name': 'Classic Lemonade',
        'price': 2.99,
        'menu_item_description': 'Our signature lemonade made with freshly squeezed lemons and a hint of sweetness.'
    },
    {
        'name': 'Lemon Meringue Pie',
        'price': 5.99,
        'menu_item_description': 'A delightful lemon meringue pie with a flaky crust and fluffy meringue topping.'
    },
    {
        'name': 'Lemon Herb Salmon',
        'price': 12.99,
        'menu_item_description': 'Grilled salmon fillet seasoned with a zesty lemon and herb marinade.'
    },
    {
        'name': 'Lemon Garlic Shrimp Pasta',
        'price': 11.99,
        'menu_item_description': 'Linguine pasta tossed with succulent shrimp, roasted garlic, and a lemon cream sauce.'
    },
    {
        'name': 'Lemon Poppy Seed Pancakes',
        'price': 7.99,
        'menu_item_description': 'Fluffy pancakes infused with lemon zest and poppy seeds, served with maple syrup.'
    },
    {
        'name': 'Lemon Berry Cheesecake',
        'price': 6.99,
        'menu_item_description': 'Creamy cheesecake with a lemon-infused berry compote on top.'
    },
    {
        'name': 'Lemon Buttered Asparagus',
        'price': 4.99,
        'menu_item_description': 'Fresh asparagus spears sautéed in lemon butter for a zesty side dish.'
    },
    {
        'name': 'Lemon Sorbet',
        'price': 3.49,
        'menu_item_description': 'A refreshing lemon sorbet to cleanse your palate.'
    },
    {
        'name': 'Lemon Chicken Wrap',
        'price': 8.99,
        'menu_item_description': 'Grilled chicken, mixed greens, and lemon aioli wrapped in a soft tortilla.'
    },
]
# Create sample menu items
for item_data in menu_items_data:
    menu_item = Menu.objects.create(
        name=item_data['name'],
        price=item_data['price'],
        menu_item_description=item_data['menu_item_description']
    )
    print(f"Created menu item: {menu_item.name}")

print("Sample menu items created successfully!")
