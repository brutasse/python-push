import requests

from .exceptions import PingError


def ping_hub(topic_url, hub_url):
    """Pings the hub to trigger an update. Returns the hub's HTTP response
    or raises `PingError`.

    :param topic_url: the URL of the feed that's just been updated.
    :param hub_url: the URL of the feed's hub to ping."""
    response = requests.post(hub_url, data={'hub.mode': 'publish',
                                            'hub.url': topic_url})
    if response.status_code != 204:
        raise PingError(response)
    return response
