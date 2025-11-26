from api.models import MenuItem

items = [
    {"name":"Masala Dosa","price":80,"desc":"Crispy dosa with masala","image":"https://b.zmtcdn.com/data/dish_photos/5ca/d42e43fc1cadc7cca5719efdf519f5ca.jpg","category":"South Indian","available":True},
    {"name":"Idli Sambhar","price":50,"desc":"Soft idlis with sambhar","image":"https://b.zmtcdn.com/data/dish_photos/b1c/a49196225ef505bfe67f7d67a114ab1c.jpg","category":"South Indian","available":True},
    {"name":"Vada Plate","price":45,"desc":"Crispy vada with chutney","image":"https://b.zmtcdn.com/data/dish_photos/6fa/2a3c3d7ce5373fe4d36e4b197ccae6fa.jpg","category":"South Indian","available":True},
    {"name":"Paneer Roll","price":70,"desc":"Spicy paneer stuffed roll","image":"https://b.zmtcdn.com/data/dish_photos/349/96c95ca87c7a6a98bb24dc05ad88e349.jpg","category":"Snacks","available":True},
    {"name":"Veg Sandwich","price":55,"desc":"Fresh vegetable sandwich","image":"https://b.zmtcdn.com/data/dish_photos/5ac/5a04056e80c695dd4a32541d62e5c5ac.jpg","category":"Snacks","available":True},
    {"name":"French Fries","price":60,"desc":"Crispy salted fries","image":"https://b.zmtcdn.com/data/dish_photos/4d4/d4bb4c63cc3cf34a1fbec628e4cab4d4.jpg","category":"Snacks","available":True},
    {"name":"Veg Burger","price":75,"desc":"Crispy veg patty burger","image":"https://b.zmtcdn.com/data/dish_photos/7ae/1ed8b5a4a7e65e6dffcaf8420abc67ae.jpeg","category":"Snacks","available":True},
    {"name":"White Sauce Pasta","price":120,"desc":"Creamy Alfredo pasta","image":"https://b.zmtcdn.com/data/dish_photos/595/41075c8a92f88340cdadc346c63b1595.jpg","category":"Special","available":True},
    {"name":"Red Sauce Pasta","price":115,"desc":"Spicy arrabiata pasta","image":"https://b.zmtcdn.com/data/dish_photos/a99/fc433c6869b8f4fcf1c6ba8dd0b8ca99.jpeg","category":"Special","available":True},
    {"name":"Fried Rice","price":90,"desc":"Chinese style fried rice","image":"https://b.zmtcdn.com/data/dish_photos/158/5a787875ad2e5032c94a295e39e2c158.jpeg","category":"Main Course","available":True},
    {"name":"Veg Noodles","price":85,"desc":"Street style noodles","image":"https://b.zmtcdn.com/data/dish_photos/051/8007eda030340c59b981ced35606b051.jpeg","category":"Main Course","available":True},
    {"name":"Paneer Fried Rice","price":110,"desc":"Spicy paneer fried rice","image":"https://b.zmtcdn.com/data/dish_photos/14c/272e2547ba2d71696bf352865d24614c.jpg","category":"Main Course","available":True},
    {"name":"Chole Kulche","price":80,"desc":"Punjabi chole with kulche","image":"https://b.zmtcdn.com/data/dish_photos/6c3/846bb33b73a750bf7a1a69dc32f766c3.jpg","category":"North Indian","available":True},
    {"name":"Rajma Chawal","price":90,"desc":"Classic rajma & rice","image":"https://b.zmtcdn.com/data/dish_photos/7fd/563e8ec6f6b1a1137126ff789bfd17fd.jpg","category":"North Indian","available":True},
    {"name":"Mini Thali","price":100,"desc":"Roti, sabji, dal, rice","image":"https://b.zmtcdn.com/data/dish_photos/4ed/5091f07de02e5dcfe1fe5c1a47b9d4ed.jpeg","category":"North Indian","available":True},
    {"name":"Aloo Paratha","price":60,"desc":"Stuffed paratha with achar","image":"https://b.zmtcdn.com/data/dish_photos/620/ac3d2dafc35724b21d6f281363597620.jpeg","category":"Indian Bread","available":True},
    {"name":"Paneer Paratha","price":75,"desc":"Paneer stuffed paratha","image":"https://b.zmtcdn.com/data/dish_photos/953/4db51d3454cb1bf2d490e93a36f18953.jpg","category":"Indian Bread","available":True},
    {"name":"Cold Coffee","price":50,"desc":"Refreshing iced coffee","image":"https://b.zmtcdn.com/data/dish_photos/bac/b46159e38d60c4fd4a3ac406a3853bac.jpg","category":"Beverages","available":True},
    {"name":"Hot Coffee","price":30,"desc":"Strong milk coffee","image":"https://b.zmtcdn.com/data/pictures/1/96341/9fe7b9dd6d9d530b0165565fcaa3b062_o2_featured_v2.jpg","category":"Beverages","available":True},
    {"name":"Masala Chai","price":20,"desc":"Hot spiced tea","image":"https://b.zmtcdn.com/data/dish_photos/513/0b32b07a4643e1409456c86b6f618513.jpg","category":"Beverages","available":True},
    {"name":"Oreo Shake","price":90,"desc":"Creamy Oreo milkshake","image":"https://b.zmtcdn.com/data/dish_photos/162/fd5af289df9ed1022ae040b082979162.jpg","category":"Beverages","available":True},
    {"name":"Fruit Salad","price":60,"desc":"Fresh mixed fruits","image":"https://b.zmtcdn.com/data/dish_photos/1cd/e26950c9b695b512229a9b8a78db11cd.jpg","category":"Healthy","available":True},
    {"name":"Veg Momos","price":70,"desc":"Steamed momos & chutney","image":"https://b.zmtcdn.com/data/dish_photos/933/c894e2b0b6b4c3ee2bdeb58afe151933.jpg","category":"Snacks","available":True},
    {"name":"Spring Roll","price":65,"desc":"Crispy veg rolls","image":"https://b.zmtcdn.com/data/dish_photos/5ab/45a30925023cfa512d65bca8c68375ab.jpg","category":"Snacks","available":True},
    {"name":"Chocolate Brownie","price":50,"desc":"Soft and fudgy brownie","image":"https://b.zmtcdn.com/data/dish_photos/d81/81f919a79f183d5c59b19e5635781d81.jpeg","category":"Desserts","available":True},
    {"name":"Grilled Cheese Sandwich","price":65,"desc":"Cheesy grilled sandwich","image":"https://b.zmtcdn.com/data/dish_photos/7dc/649e5c8fb74c8d1573a13092c70787dc.jpg","category":"Snacks","available":True},
    {"name":"Veg Wrap","price":69,"desc":"Grilled veg wrap","image":"https://b.zmtcdn.com/data/pictures/6/21378166/2305aea1f7b151f00bb131250bf44069_o2_featured_v2.jpg","category":"Snacks","available":True},
    {"name":"Iced Latte","price":70,"desc":"Cold latte with ice","image":"https://b.zmtcdn.com/data/dish_photos/6f7/6fdaa755619639ea984558a001c206f7.jpg","category":"Beverages","available":True},
    {"name":"Chocolate Shake","price":85,"desc":"Thick chocolate shake","image":"https://b.zmtcdn.com/data/dish_photos/708/253d492774347ba61569904c5d21d708.png","category":"Beverages","available":True},
    {"name":"Fruit Bowl","price":65,"desc":"Refreshing fruit bowl","image":"https://b.zmtcdn.com/data/dish_photos/115/6a801547c37a584c3943c3caea6cd115.jpg","category":"Healthy","available":True}
]

for it in items:
    MenuItem.objects.create(**it)

print('Inserted sample menu items')
