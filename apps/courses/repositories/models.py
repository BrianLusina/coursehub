from typing import Dict
from sanctumlabs_dbkit.sql import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Course(BaseModel):
    """
    Course model represents a model for a course.
    """

    # The name of the course
    title: Mapped[str] = mapped_column(String(length=20), nullable=False)

    # A brief description of the course.
    overview: Mapped[str] = mapped_column(String(length=200), nullable=False)

    # The name of the author.
    author: Mapped[str] = mapped_column(String(length=50), nullable=False)

    # A hyperlink that opens the course’s homepage in a new tab.
    url: Mapped[str] = mapped_column(String(length=100), nullable=False)

    # A URL of the cover image.
    image_url: Mapped[str] = mapped_column(String(length=200), nullable=False)

    def to_dict(self) -> Dict[str, str]:
        """Generates dictionary key value pairs of this model

        Returns:
            Dict[str, str]: Dictionary mapping
        """
        return dict(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            updated_by=self.updated_by,
            deleted_at=self.deleted_at,
            title=self.title,
            overview=self.overview,
            image=self.image,
            url=self.url,
            author=self.author,
        )
