from dataclasses import dataclass
from hashlib import sha256
from typing import Optional
import uuid

@dataclass
class Admin:
    id: uuid.UUID
    email: str
    password: Optional[str] = None
