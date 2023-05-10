from shorter.models import Url


def get_by_id(id_string):
    try:
        obj = Url.objects.get(id=id_string)
    except:
        obj = None
    return obj

def get_by_custom_name(id_string):
    try:
        obj = Url.objects.get(custom_name=id_string)
    except:
        obj = None
    return obj

def get_url_obj(id_string):
    obj = get_by_id(id_string)
    if not obj:
        obj = get_by_custom_name(id_string)
    return obj