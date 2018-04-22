---
title: 
category: twitter
date: "{{ date_field }}"
slug: "{{ filename }}"
TwitterId: "{{ tweet_id }}"
TweetUrl: "https://twitter.com/mark_philpot/status/{{ tweet_id }}"
{% if retweet_user %}ReTweetUser: {{ retweet_user }}{% endif %}
---
{{ markdown }}
