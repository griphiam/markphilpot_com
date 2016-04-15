Title: Anime {{ season|capitalize }} {{ year }} First Impressions
Date: {{ timestamp }}
Tags: anime, first impressions
Category: anime
Slug: anime_{{ year }}_{{ season }}_first
Summary: First Impressions of the Anime {{ season|capitalize }} {{ year }} Season
Hero: background-image: url(/images/anime/{{year}}/{{season}}/hero.jpg);
status: draft

{% for show in shows %}

![{{ show.titles.canonical }}]({filename}/images/anime/{{ year}}/{{ season }}/{{ show.pv_filename }} "{{ show.titles.canonical }}"){: .center}
![$STUDIO]({filename}/images/anime/studios/.png){: .studio}
<div class="studio">{{ show.producers|join(', ') if show.producers }}</div>

### [{{ show.titles.canonical }}](https://hummingbird.me/anime/{{ show.slug }})

> {{ show.synopsis|replace('\r\n', '<br/>')|replace('\n', '<br/>') }}

{% endfor %}
