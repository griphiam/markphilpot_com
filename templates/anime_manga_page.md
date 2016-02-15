Title: Anime | Manga
Date: 2014-04-10 22:48:08
Tags: anime, manga
Category: Anime
Slug: anime_manga
Summary: My Anime & Manga

<style>
.am_card_set {
    column-count: 5;
    column-gap: 0px;
    -webkit-column-count: 5;
    -webkit-column-gap:   0px;
    line-height: 0;
}
.am_card img {
    width: 100% !important;
    height: auto !important;
    border: 0 !important;
    padding: 0 !important;
}
.am_title {
    font-weight: bold;
    display: inline-block;
}
.am_element {
    display: inline-block;
}
</style>

<div class="am_header">
    <div class="am_title">Anime</div>
    <div class="am_element"><a href="#anime_watching">Watching</a></div>
    <div class="am_element"><a href="#anime_completed">Completed</a></div>
    <div class="am_title">Manga</div>
    <div class="am_element">Reading</div>
    <div class="am_element">Completed</div>
</div>

<div class="am_card_wrapper">
    <div id="anime_watching" class="am_title">Anime :: Watching</div>
    <div class="am_card_set">
        {% for a in anime.watching %}
        <div class="am_card"><a href="{{a[1]}}"><img src="{{a[0]}}" alt="{{a[2]}}" /></a></div>
        {% endfor %}
    </div>
</div>

<div class="am_card_wrapper">
    <div id="anime_completed" class="am_title">Anime :: Completed</div>
    <div class="am_card_set">
        {% for a in anime.completed %}
        <div class="am_card"><a href="{{a[1]}}"><img src="{{a[0]}}" alt="{{a[2]}}" /></a></div>
        {% endfor %}
    </div>
</div>