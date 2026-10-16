#вихідні порти

#CrudRepository (базовий)
# create, get_by_id, get_all, update, delete
...

# --- MongoDB ---
#DesignerRepository
...
#BrandRepository
# find_by_style_category
...
#CollectionRepository
# find_by_filter, find_by_brand_id
...
#GarmentRepository
# find_by_collection_id
...

# --- Neo4j ---
#RelationGraphRepository
# link_designer_to_collection, link_collection_to_brand, find_collaborations, delete_node
...
#RecommendationGraphRepository
# find_similar_brand_ids
...

# --- Elasticsearch ---
#SearchIndexRepository
# search, index_collection, index_designer, delete_from_index
...

# --- Redis ---
#CacheRepository
# get, put, invalidate
...
