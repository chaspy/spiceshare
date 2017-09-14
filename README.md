# spiceshare
[![CircleCI](https://circleci.com/gh/takeshe12/spiceshare.svg?style=svg&circle-token=f0b56b2de1339b4ff5c7e9e68bf888d6308745f6)](https://circleci.com/gh/takeshe12/spiceshare)

platform for sharing recipi of spice-curry.

## Usage

* Run rest server
   
```
python app.py
```

* Show all items

```
curl localhost:5000/curry/v1/recipes
```

* Register item

```
curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '
        "title": "特製カレー",
        "abstract": "我が家の特製カレー",
        "category": "ドライカレー",
        "stuffs": {
            "ガラムマサラ": "5g",
            "クミン": "5g",
            "水": "200ml",
            "豚ひき肉": "200g"
        }
    ' localhost:5000/curry/v1/recipes
```

* Show item details

```
curl localhost:5000/v1/recipes/{recipe_id}
```

* Delete item

```
curl -X DELETE localhost:5000/v1/recipes/{recipe_id}
```
