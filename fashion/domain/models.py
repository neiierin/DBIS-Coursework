# Доменні моделі
from dataclasses import dataclass, field
from uuid import UUID

# Designer
@dataclass
class Designer:
    id: UUID
    name: str
    biography: str
    style: str

# Brand
@dataclass
class Brand:
    id: UUID
    name: str
    head_designer_id: UUID
    style_category: str

# Collection
@dataclass
class Collection:
    id: UUID
    title: str
    season: str
    year: int
    concept_description: str
    press_release: str
    video_url: str
    brand_id: UUID
    designer_ids: list[UUID] = field(default_factory=list)

# Garment
@dataclass
class Garment:
    id: UUID
    collection_id: UUID
    type: str
    name: str
    material: str