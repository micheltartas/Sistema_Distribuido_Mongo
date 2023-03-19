from uvicorn.workers import UvicornWorker


class UvicornWorkerWithoutAccesslogs(UvicornWorker):
    """
    Disabling Uvicorn's access log because Google automatically
    adds them *and* we manually log them too via a middleware
    """

    CONFIG_KWARGS = {"access_log": False}
