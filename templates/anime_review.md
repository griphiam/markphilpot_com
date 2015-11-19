Title: {{ titles.canonical }}
Date: {{ timestamp }}
Tags: anime, review
Category: anime
Slug: review_{{ slug|replace('-', '_') }}
Summary: Review of {{ titles.canonical }}
status: draft

![{{ titles.canonical }}]({filename}/images/{{ year }}/{{ slug|replace('-', '_') }}/pv.jpg "{{ titles.canonical }}"){: .center}
![{{ titles.canonical }}]({{ poster_image }} "{{ titles.canonical }}"){: .center}
![{{ studio.name }}]({filename}/{{ studio.logo }}){: .studio}
Producers :: {{ producers|join(', ') if producers }}

[{{ titles.canonical }}](https://hummingbird.me/anime/{{ slug }}) ![star]({filename}/images/rating/full_star.png){: .star}![star]({filename}/images/rating/full_star.png){: .star}![star]({filename}/images/rating/full_star.png){: .star}![star]({filename}/images/rating/full_star.png){: .star}![star]({filename}/images/rating/full_star.png){: .star} *{{ titles.english }}*

> {{ synopsis }}

## Story & Characters

## Animation

## Music & Sound

## Final Thoughts
