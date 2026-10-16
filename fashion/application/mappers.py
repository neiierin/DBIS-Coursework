from fashion.domain import models as m
from fashion.application import dto as d


#DesignerMapper
class DesignerMapper:
    @staticmethod
    def to_dto(entity: m.Designer) -> d.DesignerDto: ...
    @staticmethod
    def to_entity(dto: d.DesignerCreateDto) -> m.Designer: ...

#BrandMapper
class BrandMapper:
    @staticmethod
    def to_dto(entity: m.Brand) -> d.BrandDto: ...
    @staticmethod
    def to_entity(dto: d.BrandCreateDto) -> m.Brand: ...

#CollectionMapper
class CollectionMapper:
    @staticmethod
    def to_dto(entity: m.Collection) -> d.CollectionDto: ...
    @staticmethod
    def to_entity(dto: d.CollectionCreateDto) -> m.Collection: ...

#GarmentMapper
class GarmentMapper:
    @staticmethod
    def to_dto(entity: m.Garment) -> d.GarmentDto: ...
    @staticmethod
    def to_entity(dto: d.GarmentCreateDto) -> m.Garment: ...
