import socket
from . import socks
ProxyConnectionError = socks.ProxyConnectionError
GeneralProxyError = socks.GeneralProxyError
ProxyError = socks.ProxyError
AuthError = socks.SOCKS5AuthError
Socks5Error = socks.SOCKS5_ERRORS
serror = socket.error

