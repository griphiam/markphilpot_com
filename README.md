[![Build Status](https://travis-ci.org/markphilpot/markphilpot_com.svg?branch=master)](https://travis-ci.org/markphilpot/markphilpot_com)

# installation

```bash
brew install libjpeg optipng pyenv pyenv-virtualenv

pyenv install 3.5.2
pyenv virtualenv 3.5.2 blog pip
pyenv activate blog

pip install -r requirements.txt
```

# twitter archive import

```bash
python scripts/process_twitter_archive.py -i $EXPORT_DIR
```

# anime first impressions

```bash
python scripts/bootstrap_anime_first.py --season $SEASON --year $YEAR -o content/$YEAR/anime_$SEASON_first.md --save_images --client_id X --client_secret Y
```

For Hero Images :: https://unsplash.com/

1920x1080
