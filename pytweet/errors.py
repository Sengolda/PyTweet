"""
MIT License

Copyright (c) 2021 TheFarGG & TheGenocides

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class Unauthorized(Exception):
    """Raised when the Credentials you passed is invalid!"""

    pass


class NotFoundError(Exception):
    """Raised when the api return NotFoundError, meaning it cant find an object in the database."""

    pass


class TooManyRequests(Exception):
    """Raised when ratelimit exceeded and a request return status code: 429"""

    pass


class Forbidden(Exception):
    """Raised when a request return status code: 403"""

    pass


class PytweetException(Exception):
    """Raise whenever the client failed executing a function. This usually happen due to user input."""

    pass
