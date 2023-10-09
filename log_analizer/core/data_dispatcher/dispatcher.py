
class Dispatcher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    @staticmethod
    def get_data(data, meta: dict):

    @staticmethod
    def update_meta(method):
        def wrapper(cls, *args, **kwargs):
            if not hasattr(cls, '_meta'):
                raise Exception("Нет атрибута _meta")

            cls._meta = cls._meta | META_SCHEMA.get_meta(cls)

            result = method(cls, *args, **kwargs)
            return result

        return wrapper


class META_SCHEMA:
    COMPONENTS = {"db_manager", "data_dispatcher", "log_engine",
                  "middlewares", "metrics", "api"}
    @staticmethod
    def __change_cls(component) -> str:
        return component.__class__.__name__

    @staticmethod
    def __change_method(component) -> str:
        return component.__name__

    @staticmethod
    def __change_target(component) -> list:
        method_name = component.__name__
        parts = method_name.split('_')
        target_keywords = [part.lower() for part in parts]
        return target_keywords

    @staticmethod
    def get_meta(component):
        meta = {
                "cls": META_SCHEMA.__change_cls(component),
                "method": META_SCHEMA.__change_method(component),
                "target": META_SCHEMA.__change_target(component),
                }
        return meta

    @staticmethod
    def interpretate_target() -> str:  # class name




