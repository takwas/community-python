from ..blueprint import api
from middleware import token_verification


@api.route('/me')
@token_verification
def me():
    return 'me'
