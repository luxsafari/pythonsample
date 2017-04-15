# api.py

import falcon
import json

class HogeResource(object):
    def on_get(self, req, resp, id):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ 
                      "result": True, 
                      "message": "success!",
                    })

api = falcon.API()
hoge = HogeResource()

api.add_route('/hoge/{id}', hoge)
