# Rename this file as your tool name - avoid generic names (i.e shopping_tool, product_tools) 
# You may need seperate files for different tools 
# Build your tool here   





#  API endpoint
# Product Availability API - Returns the stock quantity and price of products, looked up by name. 
# Endpoint: GET {LARAVEL_API_URL}/api/ai/products/availability


# Parameters: Required   Description
# name:        Yes       Product name, 2–255 characters. An exact name is matched first; otherwise products whose name contains 
#                        the text are returned.                                                                                
# limit:       No        Maximum number of results, 1–20 (default 5).
# 

# See two examples below:
#
# params = {"name": "Nike Summer Cotton T-Shirt"}   
# response = requests.get(
#     f"{LARAVEL_API_URL}/api/ai/products/availability",
#     params=params,
#     headers={"Accept": "application/json"},
#     timeout=10,
# )
# jsonResponse = response.json() 
# 
# jsonResponse will look like this: 
# 
# jsonResponse
# {
#   "success": true,
#   "found": true,
#   "match_type": "exact",
#   "count": 1,
#   "data": [{
#     "id": 6,
#     "name": "Nike Summer Cotton T-Shirt",
#     "qty": 120,
#     "in_stock": true,
#     "price": 25,
#     "offer_price": 20,
#     "is_on_sale": false,
#     "current_price": 25,
#     "url": "https://.../product?product=nike-summer-cotton-t-shirt"
#   }]
# }

# - found: false if no product matches (data is then empty).
# - match_type: exact, partial (the name only partly matched, so confirm with the user) or none.
# - current_price: the price the customer pays now (the offer price when a sale is active).



# params = {"name": "God of War"}   
# response = requests.get(
#     f"{LARAVEL_API_URL}/api/ai/products/availability",
#     params=params,
#     headers={"Accept": "application/json"},
#     timeout=10,
# )
# jsonResponse = response.json()  

# jsonResponse will look like this:
# jsonResponse
# {
#     "success": true,
#     "query": {
#         "name": "God of War",
#         "limit": 5
#     },
#     "found": true,
#     "match_type": "partial",
#     "count": 5,
#     "data": [
#         {
#             "id": 243,
#             "name": "Sony God of War 2 (2007) Disc",
#             "qty": 82,
#             "in_stock": true,
#             "price": 59,
#             "offer_price": 49,
#             "is_on_sale": false,
#             "current_price": 59,
#             "url": "https://...../product?product=sony-god-of-war-2-2007-disc"
#         },
#         {
#             "id": 67,
#             "name": "Sony God of War Ragnarok PS5 Game Disc",
#             "qty": 90,
#             "in_stock": true,
#             "price": 69,
#             "offer_price": 57,
#             "is_on_sale": false,
#             "current_price": 69,
#             "url": "https://...../product?product=sony-god-of-war-ragnarok-ps5-game-disc"
#         },
#         {
#             "id": 244,
#             "name": "Sony God of War 3 PS4 Hits Edition Game Disc",
#             "qty": 88,
#             "in_stock": true,
#             "price": 29,
#             "offer_price": 24,
#             "is_on_sale": false,
#             "current_price": 29,
#             "url": "https://...../product?product=sony-god-of-war-3-ps4-hits-edition-game-disc"
#         },
#         {
#             "id": 242,
#             "name": "Sony God of War PSP Ghost of Sparta Disc (2010)",
#             "qty": 70,
#             "in_stock": true,
#             "price": 69,
#             "offer_price": 58,
#             "is_on_sale": false,
#             "current_price": 69,
#             "url": "https://...../product?product=sony-god-of-war-psp-ghost-of-sparta-disc-2010"
#         },
#         {
#             "id": 241,
#             "name": "Sony God of War PS2 Chains of Olympus Disc (2008)",
#             "qty": 95,
#             "in_stock": true,
#             "price": 39,
#             "offer_price": 32,
#             "is_on_sale": false,
#             "current_price": 39,
#             "url": "https://...../product?product=sony-god-of-war-ps2-chains-of-olympus-disc-2008"
#         }
#     ]
# }