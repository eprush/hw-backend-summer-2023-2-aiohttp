from aiohttp.web_response import json_response
from app.web.app import View

class AdminLoginView(View):
    async def post(self):
        data  = await self.request.json()
        admin = await self.request.app.accessor.create_admin(
            email=    data["email"],
            password= data["password"]
        )
        self.request.app.database.admins.append(admin)
        return json_response(data= { "id": admin.id, "email": admin.email})


class AdminCurrentView(View):
    async def get(self):
        cookie = list(self.request.cookies)[0]
        app    = self.request.app
        if cookie == app.config.session.key:
            config = app.config.admin
            admin  = await app.accessor.get_by_email(config.email)
            return json_response(data= {"id": admin.id, "email": admin.email})
        else:
            return