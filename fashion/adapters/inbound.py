#вхідні адаптери

#REST-контролери

#BrandController
# POST/GET/PUT/DELETE /api/brands
...
#DesignerController
# POST/GET/PUT/DELETE /api/designers
...
#CollectionController
# POST/GET/PUT/DELETE /api/collections, фільтр: season, year, style
...
#SearchController
# GET /api/search?q=
...
#RecommendationController
# GET /api/recommendations/brand/{id}, /collection/{id}
...

# --- Генератор даних ---
#DataGenerator
# run, generate_designer, generate_brand, generate_collection, generate_garment
...
