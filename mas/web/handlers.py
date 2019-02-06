import json

from tornado.web import RequestHandler

from mas.services import favorite


class PingHandler(RequestHandler):
    _response = {
        'status': 'ok'
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()


class AddFavoriteHandler(RequestHandler):
    def initialize(self):
        body = json.loads(self.request.body)
        self.object_id = body.get('object_id')
        self.user_id = body.get('user_id')

    def prepare(self):
        if not self.object_id or not self.user_id:
            self.set_status(400)
            self.finish()

    async def post(self, *args, **kwargs):
        await favorite.add(
            user_id=self.user_id,
            object_id=self.object_id
        )
        self.set_status(204)
        self.finish()


class GetFavoriteHandler(RequestHandler):
    def initialize(self):
        body = json.loads(self.request.body)
        self.user_id = body.get('user_id')

    def prepare(self):
        if not self.user_id:
            self.set_status(400)
            self.finish()

    async def post(self, *args, **kwargs):
        favorite_objects = await favorite.get(
            user_id=self.user_id,
        )
        self.write({
            'favorite_objects': favorite_objects
        })
        self.set_status(200)
        self.finish()
