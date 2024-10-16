# word-finder

![530540647816626308](https://github.com/user-attachments/assets/fb4ea319-e3fd-4adc-b4de-3c0fc4dd7881)

## setup

``` bash
brew install mecab mecab-ipadic

git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd/
./bin/install-mecab-ipadic-neologd -n

brew install poetry

```

``` bash
poetry install
```

## run
``` bash
python main.py
```


## References

- https://clrd.ninjal.ac.jp/unidic/
- https://github.com/neologd/mecab-ipadic-neologd/tree/master
- https://python-poetry.org/
- https://github.com/megagonlabs/ginza
