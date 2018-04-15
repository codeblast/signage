# Digital Signage

This is a digital signage prototype web app.

We'll start with a very basic [Flight 
Information Display System](https://en.wikipedia.org/wiki/Flight_information_display_system) (FIDS)
feature: Check-in Counter Activation.

The initial architecture is super simple; four separate layers/technologies:

1. Front-end/UI:
	1. Admin: React/JS
	2. Signage displays: Static HTML/CSS/JS
2. Back-end:
	1. Database: Postgres
	2. API: Flask/Python

```
+------------------+     +------------------+     +------------------+
|Check-in counter  +---->|API back-end      +---->|Check-in counter  |
|activation/admin  |     |                  |     |signage display   |
|front-end UI      |     |                  |     |                  |
|(React SPA)       |     |(Python, Flask)   |     |(Plain HTML/JS)   |
+------------------+     +--------+---------+     +------------------+
                                  |
                                  V
                         +------------------+
                         |Database          |
                         |                  |
                         |                  |
                         |(PostgreSQL)      |
                         +------------------+
```

We'll take an iterative development
approach, i.e. by building a very simple prototype
and then gradually and slowly expand the
functionality until we have all the most common Check-in Counter FIDS features that
an airport might need.

Once that is done,
we'll add support for other display types, such as
the traditional arrivals/departures 
directory displays seen in any airport.
