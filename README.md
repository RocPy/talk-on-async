Josh's talk on AsyncIO
======================

Here are the main resources I used while learning [AsyncIO](https://docs.python.org/3/library/asyncio.html) for the talk

An excellent overview of what is actually going on behind the scenes:
[PYTHON ASYNCIO FROM THE INSIDE OUT](https://www.buzzcapture.com/en/2014/05/python-asyncio-inside/)

[A deep dive into PEP-3156 and the new asyncio module](http://www.slideshare.net/saghul/asyncio) - slides from a presentation by Saul Ibarra Corretge

[Tulip: Async I/O for Python 3](https://www.youtube.com/watch?v=1coLC-MUCJc) - A talk [Guido](https://www.python.org/~guido/) gave at the San Francisco Python User Group

[PEP-3156](http://legacy.python.org/dev/peps/pep-3156/) - The Python Enhancemnent Proposal (PEP) for AsyncIO. It's extremely helpful in understanding the intent of the module, though the order of items may seem a little random. I would recomend starting with the following
* [Abstract](http://legacy.python.org/dev/peps/pep-3156/#abstract) and [Introduction](http://legacy.python.org/dev/peps/pep-3156/#introduction) sections, though you can probably skip the Transports and Protocols initially within the Introduction section
* [Event Loop Policy: Getting and Setting the Current Event Loop](http://legacy.python.org/dev/peps/pep-3156/#event-loop-policy-getting-and-setting-the-current-event-loop)
* [Event Loop Methods Overview](http://legacy.python.org/dev/peps/pep-3156/#event-loop-methods-overview) and [Event Loop Methods](http://legacy.python.org/dev/peps/pep-3156/#event-loop-methods)
* [Futures](http://legacy.python.org/dev/peps/pep-3156/#futures)
* [Callback Style](http://legacy.python.org/dev/peps/pep-3156/#callback-style)
* [Coroutines and the Scheduler](http://legacy.python.org/dev/peps/pep-3156/#coroutines-and-the-scheduler)

An example of how to create an async web scraper: [Fast scraping in Python with AsyncIO](http://compiletoi.net/fast-scraping-in-python-with-asyncio.html)
