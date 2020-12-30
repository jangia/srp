# Single responsibility principle

This repository was made to find the best solution which does not violate SRP.

> It started with these 2 tweets: [@testdrivenio](https://twitter.com/testdrivenio/status/1338958991037247489?s=20) and [jangiacomelli](https://twitter.com/jangiacomelli/status/1343676834085543936?s=20)

## Specifications
Let's say we have a forum for Python professionals. We have users which are monthly charged for the subscription and banned for 7 days if they misbehave.

### SRP-violating pseudo-solution
```python
import datetime


class User:
    def __init__(self, username, banned_until):
        self.username = username
        self.banned_until = banned_until

    def save(self):
        print('I am saving to PostgreSQL')

    def ban(self):
        self.banned_until = datetime.datetime.today() + datetime.timedelta(days=7)

    def charge(self):
        print('Charge credit card of user using Stripe')

```

## Goal
We're trying to find the best solution that complies with SRP.

## Setup
To install requirements:
```sh
(venv)$ pip install -r requirements.txt
```

To run tests:
```sh
(venv)$ pytest tests
```