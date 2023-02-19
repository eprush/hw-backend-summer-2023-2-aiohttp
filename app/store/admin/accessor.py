import typing
import uuid
import yaml
from typing import Optional
from app.base.base_accessor import BaseAccessor
from app.admin.models import Admin

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application", config_path: str = "\config.yml"):
        # TODO: создать админа по данным в config.yml здесь
        self.app = app
        if not self.app.database:
            with open(config_path, "r") as f:
                raw_config = yaml.safe_load(f)

            self.app.database.admins =  [await self.create_admin(
                raw_config["admin"]["email"],
                raw_config["admin"]["password"]
            )
            ]
        return

    async def disconnect(self, _: "Application"):
        self.app.database.admins = []

    async def get_by_email(self, email: str) -> Optional[Admin]:
        for admin in self.app.database.admins:
            if admin.email == email:
                return admin

    async def create_admin(self, email: str, password: str) -> Admin:
        return Admin(email= email, password= password, id= uuid.uuid4())

def setup_accessor(app : "Application"):
    app.accessor = AdminAccessor(app)