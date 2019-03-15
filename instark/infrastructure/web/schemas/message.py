from marshmallow import Schema, fields


class MessageSchema(Schema):
    id = fields.Str(
        required=False, example="01f32c10-6d09-4145-98c5-56d4bf7c1329")
    backend_id = fields.Str(
        required=False, example="projects/instark/messages/0:154042575")
    recipient_id = fields.Str(
        required=True, example="9ec44c7c-73d6-4912-8f83-ccff9834132b")
    content = fields.Str(required=True, example="Hello World")
    kind = fields.Str(required=True, example="Direct")
   