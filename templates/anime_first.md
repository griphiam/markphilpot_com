Title: Anime {{ season|capitalize }} {{ year }} First Impressions
Date: {{ timestamp }}
Tags: anime, first impressions
Category: anime
Slug: anime_{{ year }}_{{ season }}_first
Summary: First Impressions of the Anime {{ season|capitalize }} {{ year }} Season
status: draft

{% for show in shows %}

![{{ show.titles.canonical }}]({filename}/images/anime/{{ year}}/{{ season }}/{{ show.pv }} "{{ show.titles.canonical }}"){: .center}
![{{ show.titles.canonical }}]({{ show.poster_image }} "{{ show.titles.canonical }}"){: .center}
![$STUDIO]({filename}/images/anime/studios/_.png "$STUDIO"){: .studio}
Producers :: {{ show.producers|join(', ') if show.producers }}

### [{{ show.titles.canonical }}](https://hummingbird.me/anime/{{ show.slug }})

> {{ show.synopsis|replace('\r\n', '') }}

{% endfor %}
