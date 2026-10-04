from typing import Generic, TypeVar

from pydantic import BaseModel, Field


T = TypeVar("T")


class PaginationParams(BaseModel):
    page: int = Field(default=1,ge=1)
    page_size: int = Field(default=20,ge=1,le=100)
    has_next: bool = Field(default=False)
    has_prev: bool = Field(default=False)

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        return self.page_size


class PaginationMeta(BaseModel, Generic[T]):
    page: int
    page_size: int
    has_next: bool
    has_prev: bool
    total: int
    total_pages: int
    items: list[T]