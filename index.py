#!/usr/bin/env python
# -*- coding:utf-8 *-

import falcon


class HogeResource(object):
    def on_get(self, req, res):
        print(req.headers)
        print(req.params)
        print(req.cookies)
        res.status = falcon.HTTP_200
        res.body = 'Hello World'
        res.content_type = 'text/plain'

    def on_post(self, req, res):
        print(req.headers)
        print(req.method)
        print(req.protocol)
        print(req.content_type)
        print(req.stream.read())

        res.status = falcon.HTTP_200
        res.content_type = 'text/plain'
        res.body = 'post!!'

app = falcon.API()
app.add_route('/hoge_resoure', HogeResource())
