---
title: "Activity for {{key}}"
category: anilist_activity
date: "{{ date_field }}"
slug: "{{ key }}"
---

{% for a in activity %} {{a.status}} {{a.progress if a.progress else ''}} {{a.media.title.romaji}}

{% endfor %}
