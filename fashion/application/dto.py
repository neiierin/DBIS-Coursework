# DTO
from dataclasses import dataclass, field
from uuid import UUID


#Designer
@dataclass
class DesignerCreateDto:
    name: str
    biography: str
    style: str


@dataclass
class DesignerDto:
    id: UUID
    name: str
    biography: str
    style: str


@dataclass
class CollaborationDto:
    partner_designer: DesignerDto
    collection_id: UUID
    collection_title: str
    year: int


@dataclass
class DesignerDetailsDto:
    designer: DesignerDto
    collections: list["CollectionDto"] = field(default_factory=list)
    collaborations: list[CollaborationDto] = field(default_factory=list)


#Brand
@dataclass
class BrandCreateDto:
    name: str
    head_designer_id: UUID
    style_category: str


@dataclass
class BrandDto:
    id: UUID
    name: str
    head_designer_id: UUID
    style_category: str


@dataclass
class BrandDetailsDto:
    """Картка бренду: бренд -> головний дизайнер -> його колаборації."""
    brand: BrandDto
    head_designer: DesignerDto
    collaborations: list[CollaborationDto] = field(default_factory=list)


#Collection / Garment
@dataclass
class CollectionCreateDto:
    title: str
    season: str
    year: int
    concept_description: str
    press_release: str
    video_url: str
    brand_id: UUID
    designer_ids: list[UUID]


@dataclass
class CollectionDto:
    id: UUID
    title: str
    season: str
    year: int
    concept_description: str
    press_release: str
    video_url: str
    brand_id: UUID
    designer_ids: list[UUID]


@dataclass
class CollectionFilterDto:
    season: str | None = None
    year: int | None = None
    style: str | None = None
    page: int = 0
    size: int = 20


@dataclass
class GarmentCreateDto:
    collection_id: UUID
    type: str
    name: str
    material: str


@dataclass
class GarmentDto:
    id: UUID
    collection_id: UUID
    type: str
    name: str
    material: str


@dataclass
class CollectionDetailsDto:
    collection: CollectionDto
    brand: BrandDto
    designers: list[DesignerDto]
    garments: list[GarmentDto]


#Search
@dataclass
class SearchRequestDto:
    query: str
    entity_types: list[str] = field(default_factory=lambda: ["collection", "designer"])
    page: int = 0
    size: int = 20


@dataclass
class SearchHitDto:
    entity_type: str      # collection | designer
    entity_id: UUID
    title: str
    highlight: str
    score: float


@dataclass
class SearchResultDto:
    total: int
    hits: list[SearchHitDto] = field(default_factory=list)


@dataclass
class RecommendationDto:
    similar_brands: list[BrandDto] = field(default_factory=list)
    same_collection_garments: list[GarmentDto] = field(default_factory=list)
