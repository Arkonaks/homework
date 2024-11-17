import inspect


def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
        'methods': [method for method in dir(obj) if method.startswith('__')],
        'module': obj.__class__.__module__ if hasattr(obj, '__class__') else None
    }
    return info


number_info = introspection_info(42)
print(number_info)
