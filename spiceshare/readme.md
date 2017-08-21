# SpiceShare
## Installation
1. Install vagrant. 
2. Install ansible higher than 2.2.
3. Edit hosts file (spiceshare/hosts) or ssh config file (~/.ssh/config)
4. Execute vagrant provision.

    vagrant provision
    
## Usage

    # Run rest server
    cd spiceshare
    python app.py
    # Show all items
    curl localhost:5555/curry/v1/recipes
    # Register item
    curl -X POST -H "ContentType: application/json" -H "Accept: application/json" -d '
        "title": "特製カレー",
        "abstract": "我が家の特製カレー",
        "category": "ドライカレー",
        "stuffs": {
            "ガラムマサラ": "5g",
            "クミン": "5g",
            "水": "200ml",
            "豚ひき肉": "200g"
        }
    ' localhost:5555/curry/v1/recipes
    # Show item details
    curl localhost:5555/v1/recipes/{recipe_id}
    # Delete item
    curl -X DELETE localhost:5555/v1/recipes/{recipe_id}
    