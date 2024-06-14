from django.db.models import DateTimeField, Model, BigAutoField, UUIDField
from uuid import uuid4


class ModelDefault(Model):
    created_at = DateTimeField(auto_created=True, editable=False, auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def to_json(self):
        exclude_fields = []
        dictionary = {}
        for field in self._meta.concrete_fields:
            field_value = self.__getattribute__(field.name)
            if isinstance(field_value, object) and field.name not in exclude_fields:
                dictionary[field.name] = field_value if type(field_value) in [int, float, dict] \
                    else str(field_value) if field_value else None
            elif field.name not in exclude_fields:
                dictionary[field.name] = field_value
        return dictionary


class ModelBigIDBased(Model):
    id = BigAutoField(primary_key=True,editable=False)
    created_at = DateTimeField(auto_created=True, editable=False, auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def to_json(self):
        exclude_fields = []
        dictionary = {}
        for field in self._meta.concrete_fields:
            field_value = self.__getattribute__(field.name)
            if isinstance(field_value, object) and field.name not in exclude_fields:
                dictionary[field.name] = field_value if type(field_value) in [int, float, dict] \
                    else str(field_value) if field_value else None
            elif field.name not in exclude_fields:
                dictionary[field.name] = field_value
        return dictionary


class ModelUUIDBased(Model):
    id = UUIDField(primary_key=True,editable=False, default=uuid4)
    created_at = DateTimeField(auto_created=True, editable=False, auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def to_json(self):
        exclude_fields = []
        dictionary = {}
        for field in self._meta.concrete_fields:
            field_value = self.__getattribute__(field.name)
            if isinstance(field_value, object) and field.name not in exclude_fields:
                dictionary[field.name] = field_value if type(field_value) in [int, float, dict, bool] \
                    else str(field_value) if field_value else None
            elif field.name not in exclude_fields:
                dictionary[field.name] = field_value
        return dictionary

    @staticmethod
    def remove_keys(obj: dict, keys: list) -> dict:
        [obj.pop(k, None) for k in keys]
        return obj

    @staticmethod
    def rename_keys(obj: dict, keys: dict) -> dict:
        [obj.update({v: obj.pop(k, None)}) for k, v in keys.items()]
        return obj

    AUTO_FIELDS = ['created_at', 'updated_at']
