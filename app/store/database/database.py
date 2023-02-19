from dataclasses import dataclass, field

from app.quiz.models import Theme
from app.quiz.models import Question
from app.admin.models import Admin

@dataclass
class Database:
    # TODO: добавить поля admins и questions
    questions: list[Question] = field(default_factory=list)
    admins:    list[Admin] = field(default_factory=list)
    themes:    list[Theme] = field(default_factory=list)

    @property
    def next_theme_id(self) -> int:
        return len(self.themes) + 1

    def clear(self):
        self.themes = []
