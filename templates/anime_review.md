Title: {{ titles.canonical }}
Date: {{ timestamp }}
Tags: anime, review
Category: anime
Slug: review_{{ slug|replace('-', '_') }}
Summary: Review of {{ titles.canonical }}
status: draft

![{{ titles.canonical }}]({filename}/images/{{ year }}/{{ slug|replace('-', '_') }}/{{ pv_filename }} "{{ titles.canonical }}"){: .center}
![$STUDIO]({filename}/images/anime/studios/_.png "$STUDIO"){: .center}
Producers :: {{ show.producers|join(', ') if show.producers }}

[{{ titles.canonical }}](https://hummingbird.me/anime/{{ slug }}) *{{ titles.english }}*

> {{ synopsis }}

## Story & Characters

## Animation

## Music & Sound

## Final Thoughts
