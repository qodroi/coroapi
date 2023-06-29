   # Covid-19 Tracker API :microbe:

Provides up-to-date data about Coronavirus outbreak. Includes numbers about confirmed cases, deaths and recovered.

## Available data-sources:
Currently only 2 data-sources is available to retrieve the data:

- [Epidemic Stats](https://epidemic-stats.com/coronavirus/) - **All statistics data about coronavirus COVID-19 comes from World Health Organization and Johns Hopkins CSSE. Charts includes number of infected, deaths and recovered.**

- [Virusncov](https://virusncov.com/) - **All statistics data about coronavirus COVID-19 comes from World Health Organization**

## How it works

*The module emulates the browser actions by sending requests to the site server. The module doesn't load any type of files while sending requests to the site and that makes it faster. The module is scraping the website source code, and returning the final result.*

## Features

- Provides Fast, and Up-to-Date data about the Coronavirus outbreak
- A lot of supported countries (up to 100)

## Installation
- `pip3 install covid19-api`

**When there's new release, you need to update the package**
- `pip3 install covid19-api==1.0 --upgrade`

## Simple Usage

```python
# (1/22/2021)
# list of supported countries can be printed out | print(instance.countries)

import coroapi

instance = coroapi.Corona()

global_stats = instance.global_stats(text=False)
print(global_stats)

<< ['98135997', '2101562', '70548362', 'usa']
```