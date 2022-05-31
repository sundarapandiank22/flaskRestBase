from http import HTTPStatus as httpStatusCode


class InternalServerError(Exception):
    pass


class MethodNotImplementedError(Exception):
    pass


class NoneTypeValueError(Exception):
    pass


class UnknownError(Exception):
    pass


def bad_request_error(error_msg):
    return Exception(error_msg, httpStatusCode.BAD_REQUEST)


def unauthorized_error(error_msg):
    return Exception(error_msg, httpStatusCode.UNAUTHORIZED)


errors = dict(
    MethodNotImplementedError=dict(
        message="The requested URL was not found on the server.",
        status=httpStatusCode.NOT_FOUND),
    NoneTypeValueError=dict(
        message="Value cannot be None.",
        status=httpStatusCode.BAD_REQUEST),
    InternalServerError=dict(
        message="Something went wrong",
        status=httpStatusCode.INTERNAL_SERVER_ERROR),
    UnknownError=dict(
        message="Unknown exception, please try again.",
        status=httpStatusCode.INTERNAL_SERVER_ERROR),
    ResourceNotFoundError=Exception("Resource does not exists."),
    UnhandledMethodNotImplementedError=Exception("The requested URL was not found on the server.",
                                                 httpStatusCode.NOT_FOUND),
    UnhandledError=Exception("Unknown exception, please try again.", httpStatusCode.INTERNAL_SERVER_ERROR),
    DataBaseTimeOutError=Exception("Server time out - when connecting to the database.",
                                   httpStatusCode.INTERNAL_SERVER_ERROR),
    HttpConnectionError=Exception("Unable to connect to remote server.", httpStatusCode.INTERNAL_SERVER_ERROR),
    UnhandledNoneTypeValueError=Exception("Value cannot be None.", httpStatusCode.BAD_REQUEST),
)
