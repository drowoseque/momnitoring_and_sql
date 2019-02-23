import json

from tornado.web import RequestHandler

from mas.helpers.statsd import statsd_client
from mas.repositories import favorite


class PingHandler(RequestHandler):
    _response = {
        'status': 'ok'
    }

    @statsd_client.timer('ping-handler.execution-time')
    def get(self):
        statsd_client.incr(self.__class__.__name__ + '.request')
        self.write(self._response)
        self.set_status(200)
        self.finish()


class AddFavoriteHandler(RequestHandler):
    def initialize(self):
        body = json.loads(self.request.body)
        self.object_id = body.get('object_id')
        self.user_id = body.get('user_id')

    def prepare(self):
        if self.object_id is None or self.user_id is None:
            self.set_status(400)
            self.finish()

    async def post(self, *args, **kwargs):
        statsd_client.incr(self.__class__.__name__ + '.post')
        with statsd_client.timer(self.__class__.__name__ + '.post'):
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
        if self.user_id is None:
            self.set_status(400)
            self.finish()

    async def post(self, *args, **kwargs):
        statsd_client.incr(self.__class__.__name__ + '.post')
        with statsd_client.timer(self.__class__.__name__ + '.post'):
            favorite_objects = await favorite.get(
                user_id=self.user_id,
            )
            self.write({
                'favorite_objects': favorite_objects
            })
            self.set_status(200)
            self.finish()


class CreateTableHandler(RequestHandler):

    async def post(self, *args, **kwargs):
        statsd_client.incr(self.__class__.__name__ + '.post')
        with statsd_client.timer(self.__class__.__name__ + '.post'):
            await favorite.create()
