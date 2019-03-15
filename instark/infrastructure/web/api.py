from flask import Flask, jsonify

from ..resolver import Registry
from .resources import(RootResource, MessageResource, ChannelResource,
                       DeviceResource, SubscriptionResource)
from .spec import create_spec


def create_api(app: Flask, registry: Registry) -> None:

    # Restful API
    spec = create_spec()
    registry['spec'] = spec

    # Root Resource (Api Specification)
    root_view = RootResource.as_view('root', registry=registry)
    app.add_url_rule("/", view_func=root_view)

    # Message Resource
    spec.path(path="/message/", resource=MessageResource)
    message_view = MessageResource.as_view('message', registry=registry)
    app.add_url_rule("/message/", view_func=message_view)

    # Channel Resource
    spec.path(path="/channel/", resource=ChannelResource)
    channel_view = ChannelResource.as_view('channel', registry=registry)
    app.add_url_rule("/channel/", view_func=channel_view)

    # Device Resource
    spec.path(path="/device/", resource=DeviceResource)
    device_view = DeviceResource.as_view('device', registry=registry)
    app.add_url_rule("/device/", view_func=device_view)

    # Device Resource
    spec.path(path="/subsccription/", resource=SubscriptionResource)
    subscription_view = SubscriptionResource.as_view('subscription',
                                                     registry=registry)
    app.add_url_rule("/subscription/", view_func=subscription_view)
