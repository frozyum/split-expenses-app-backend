from authentication.authenticationfilters import JWTAuthentication


# TODO handle built in exceptions somehow
def base_auth_required(view):
    def wrap(request, *args, **kwargs):
        user, token = JWTAuthentication().authenticate(request)
        request.token = token
        request.user = user
        return view(request, *args, **kwargs)
    return wrap