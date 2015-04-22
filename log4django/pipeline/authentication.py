import hashlib

from django.utils.timezone import now

def is_logged(request):
    return request.user.is_authenticated()


def hash_login(request):
    h = hashlib.sha1(now().strftime('%d%m%Y')[::-1]).hexdigest()
    hash_session = request.session.get('password', None)
    hash_get = request.GET.get('hash', None)

    print hash_get, h

    if hash_session and hash_session == h:
        return True
    if hash_get and hash_get == h:
        request.session['hash'] = hash_get
        return True
