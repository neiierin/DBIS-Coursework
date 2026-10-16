#вихідні порти
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from fashion.domain.models import Brand, Collection, Designer, Garment
from fashion.application.dto import (
    CollectionFilterDto, CollaborationDto, SearchRequestDto, SearchResultDto,
)

T = TypeVar("T")

# Базовий CRUD-порт
class CrudRepository(ABC, Generic[T]):
    """Базовий CRUD-порт для всіх документних репозиторіїв."""
    @abstractmethod
    def create(self, entity: T) -> T: ...
    @abstractmethod
    def get_by_id(self, id: UUID) -> T | None: ...
    @abstractmethod
    def get_all(self, page: int = 0, size: int = 20) -> list[T]: ...
    @abstractmethod
    def update(self, id: UUID, entity: T) -> T: ...
    @abstractmethod
    def delete(self, id: UUID) -> None: ...


#MongoDB
class DesignerRepository(CrudRepository[Designer], ABC):
    pass


class BrandRepository(CrudRepository[Brand], ABC):
    @abstractmethod
    def find_by_style_category(self, style_category: str) -> list[Brand]: ...


class CollectionRepository(CrudRepository[Collection], ABC):
    @abstractmethod
    def find_by_filter(self, f: CollectionFilterDto) -> list[Collection]: ...
    @abstractmethod
    def find_by_brand_id(self, brand_id: UUID) -> list[Collection]: ...


class GarmentRepository(CrudRepository[Garment], ABC):
    @abstractmethod
    def find_by_collection_id(self, collection_id: UUID) -> list[Garment]: ...


#Neo4j
class RelationGraphRepository(ABC):
    """(Дизайнер)-[:РОЗРОБИВ]->(Колекція)-[:ПРЕДСТАВЛЕНА_БРЕНДОМ]->(Бренд)."""
    @abstractmethod
    def link_designer_to_collection(self, designer_id: UUID, collection_id: UUID) -> None: ...
    @abstractmethod
    def link_collection_to_brand(self, collection_id: UUID, brand_id: UUID) -> None: ...
    @abstractmethod
    def find_collaborations(self, designer_id: UUID) -> list[CollaborationDto]: ...
    @abstractmethod
    def delete_node(self, entity_id: UUID) -> None: ...


class RecommendationGraphRepository(ABC):
    @abstractmethod
    def find_similar_brand_ids(self, brand_id: UUID, limit: int = 5) -> list[UUID]: ...


#Elasticsearch
class SearchIndexRepository(ABC):
    @abstractmethod
    def search(self, request: SearchRequestDto) -> SearchResultDto: ...
    @abstractmethod
    def index_collection(self, collection: Collection) -> None: ...
    @abstractmethod
    def index_designer(self, designer: Designer) -> None: ...
    @abstractmethod
    def delete_from_index(self, entity_type: str, entity_id: UUID) -> None: ...


#Redis
class CacheRepository(ABC):
    @abstractmethod
    def get(self, key: str) -> object | None: ...
    @abstractmethod
    def put(self, key: str, value: object, ttl_seconds: int = 300) -> None: ...
    @abstractmethod
    def invalidate(self, prefix: str) -> None: ...