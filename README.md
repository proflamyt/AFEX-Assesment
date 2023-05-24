# Novel Search Engine

A Django Novel search engine that allows users to efficiently search for novels based on user query using elasticsearch.
It uses the BM25 for similarity ranking (relevancy), ranks the result based on the frequency of the query in the content and uses an english language stemmer for stemming to ensure the search engine finds documents that contain variations of the query keywords. It uses the multi match query to match texts across multiple fields of the novel which are :

<b> *'overview' (short detail about the novel ),*

*'authors.username' (author's username),*

*'title' (title of the novel).* 
</b>

# Local Development (Getting Started)

Create and Activate Virtual Environment (windows)

```
$ python3 -m venv venv

$ ./venv/scripts/activate
```

Install Requirements

```
$ pip install -r requirements.txt
```

Populate Database 

```
$ python manage.py populate_db
```

Run Elastic Search with docker in detached mode

```
$ docker run -d -p 9200:9200 -p 9300:9300 -e 'discovery.type=single-node' elasticsearch:7.17.10 
```

Create Search Index (This is already handled by signals)

```
$ python manage.py search_index --rebuild

```

Run server

```
$ python manage.py runserver
```




# Or Activate Using Docker Compose

```
docker-compose up -d
```



# Run Search 

```
curl http://afex.onrender.com/novels/search?q='of the' -H 'Content-Type: application/json'
```

```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "The Journey",
            "overview": "the vampire lord of the nightmare land. But with only a captive of the Vistani woman and an untrustworthy of the ghost for allies",
            "genre": [
                {
                    "name": "fantacy"
                },
                {
                    "name": "horror"
                },
                {
                    "name": "romance"
                }
            ],
            "authors": [
                {
                    "id": 3,
                    "username": "author3"
                }
            ],
            "chapters": []
        },
        {
            "title": "Game of Throne",
            "overview": "Gaming are thrones with gangs and the man of the hsjjs",
            "genre": [
                {
                    "name": "fantacy"
                },
                {
                    "name": "horror"
                },
                {
                    "name": "romance"
                }
            ],
            "authors": [
                {
                    "id": 1,
                    "username": "author1"
                },
                {
                    "id": 2,
                    "username": "author2"
                }
            ],
            "chapters": []
        },
        {
            "title": "The Life",
            "overview": "The life is a story of a love life between angelina and joe",
            "genre": [
                {
                    "name": "fantacy"
                },
                {
                    "name": "horror"
                },
                {
                    "name": "romance"
                }
            ],
            "authors": [
                {
                    "id": 3,
                    "username": "author3"
                }
            ],
            "chapters": []
        },
        {
            "title": "Knight of Black roses",
            "overview": "On the fabled world of Krynn, Lord Soth finally learns that there is a price to pay for his long history of evil deeds, a price even an undead warrior might find horrifying.",
            "genre": [
                {
                    "name": "fantacy"
                },
                {
                    "name": "horror"
                },
                {
                    "name": "romance"
                }
            ],
            "authors": [
                {
                    "id": 3,
                    "username": "author3"
                }
            ],
            "chapters": []
        }
    ]
}
```
