[![Build Status](https://travis-ci.org/markphilpot/markphilpot_com.svg?branch=master)](https://travis-ci.org/markphilpot/markphilpot_com)

# installation

```bash
brew install libjpeg optipng
yarn install

pyenv virtualenv 3.5.2 blog pip
pyenv activate blog

pip install -r requirements.txt
```

# twitter archive import

```bash
python scripts/process_twitter_archive.py -i $EXPORT_DIR
```

For Hero Images :: https://unsplash.com/

1920x1080
