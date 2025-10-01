class KeyWords:

    ACCESS_TOKEN = 'accessToken'
    ACCESS_TOKEN_TYPE = 'Bearer '
    AUTH_FIELD = 'Authorization'
    BUN = 'bun'
    DATA = 'data'
    EMAIL = 'email'
    FILLING = 'main'
    ID = '_id'
    INGREDIENTS = 'ingredients'
    MESSAGE = 'message'
    NAME = 'name'
    NUMBER = 'number'
    ORDER = 'order'
    PASSWORD = 'password'
    REFRESH_TOKEN = 'refreshToken'
    SAUCE = 'sauce'
    SUCCESS = 'success'
    TYPE = 'type'
    USER = 'user'


class StatusCodes:

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    ERROR_500 = 500


class ResponseMessages:

    USER_EXISTS = 'User already exists'
    EMPTY_FIELDS = 'Email, password and name are required fields'
    INCORRECT_EMAIL_OR_PASSWORD = 'email or password are incorrect'
    BURGER_WITH_NO_INGREDIENTS = 'Ingredient ids must be provided'
