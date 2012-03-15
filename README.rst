PuSH
====

A python PubSubHubbub library.

* Author: Bruno Renié and `contributors`_
* Licence: BSD
* Compatibility: Python 2.X where X >= 6

.. _contributors: https://github.com/brutasse/python-push/contributors

This library provides some helpers for implementing PubSubHubbub-enabled
applications in python.

Publishing
----------

Publishing some content is as easy as:

Declaring a hub
```````````````

This is done in your RSS/Atom feed::

    <?xml version="1.0"?>
    <atom:feed>
      <link rel="hub" href="http://hub.example.com/endpoint" />
    …

Pinging the hub
```````````````

Whenever the content is updated, issue a ping request to the hub you use::

    from push.pub import ping_hub, PingError

    try:
        ping_hub(topic_url, hub_url)
    except PingError as e:
        print "Error while pinging hub, more info available in e.response

Subscribing
-----------

Running a hub
-------------
