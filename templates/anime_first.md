---
title: "Anime {{ season|capitalize }} {{ year }} First Impressions"
date: "{{ timestamp }}"
tags: [anime, first impressions]
category: anime
slug: anime_{{ year }}_{{ season }}_first
summary: First Impressions of the Anime {{ season|capitalize }} {{ year }} Season
Hero: "background-image: url(/images/anime/{{year}}/{{season}}/hero.jpg);"
status: draft
---

{% for show in shows %}

![{{ show.title.userPreferred }}]({filename}/images/anime/{{ year }}/{{ season }}/{{ show.__pv_filename__ }} "{{ show.title.userPreferred }}"){: .center} 
![{{ show.studios.nodes|map(attribute='name')|join(', ') }}]({filename}/images/anime/studios/half/.png){: .studio}

<div class="studio">{{ show.studios.nodes|map(attribute='name')|join(', ') }}</div>

### [{{ show.title.userPreferred }}]({{ show.siteUrl }})

> {{ show.description|replace('\r\n', '<br/>')|replace('\n', '<br/>') }}

{% endfor %}
