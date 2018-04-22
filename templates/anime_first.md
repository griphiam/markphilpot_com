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

![{{ show.title_romaji }}]({filename}/images/anime/{{ year }}/{{ season }}/{{ show.__pv_filename__ }} "{{ show.title_romaji }}"){: .center} 
![{% for studio in show.__page__.studio %}{{ studio.studio_name }}, {% endfor %}]({filename}/images/anime/studios/half/.png){: .studio}

<div class="studio">{% for studio in show.__page__.studio %}{{ studio.studio_name }}, {% endfor %}</div>

### [{{ show.title_romaji }}](https://anilist.co/anime/{{ show.id }})

> {{ show.__page__.description|replace('\r\n', '<br/>')|replace('\n', '<br/>') }}

{% endfor %}
