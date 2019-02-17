from logsensefluent import handler as l_handler, sender as l_sender
from logsense import sender


class LogSenseRecordFormatter(l_handler.FluentRecordFormatter, object):
    pass


class LogSenseHandler(l_handler.FluentHandler):
    def __init__(self,
                 customer_token,
                 logsense_host=None,
                 logsense_port=None,
                 timeout=3.0,
                 verbose=False,
                 buffer_overflow_handler=None,
                 msgpack_kwargs=None,
                 nanosecond_precision=False,
                 **kwargs):

        self._customer_token = customer_token
        self._logsense_host = logsense_host
        self._logsense_port = logsense_port

        l_handler.FluentHandler.__init__(self,
                                       'python',
                                       host=self._logsense_host,
                                       ssl_server_hostname=self._logsense_host,
                                       port=self._logsense_port,
                                       use_ssl=True,
                                       timeout=timeout,
                                       verbose=verbose,
                                       buffer_overflow_handler=buffer_overflow_handler,
                                       msgpack_kwargs=msgpack_kwargs,
                                       nanosecond_precision=nanosecond_precision)

    def getSenderClass(self):
        return sender.LogSenseSender

    @property
    def sender(self):
        if self._sender is None:
            self._sender = sender.LogSenseSender(customer_token=self._customer_token,
                                               tag='python',
                                               meta={},
                                               logsense_host=self._logsense_host,
                                               logsense_port=self._logsense_port)
        return self._sender
