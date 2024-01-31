# FamPay Backend Task

[You can also Checkout the documentation here](https://shiny-chauffeur-91e.notion.site/FamPay-Backend-Task-3e370ff4fa584341b16abb2815c104d7?pvs=4)

# Try the API
[Try the API Here](https://fampay-backend-task-nishchay.onrender.com)
```shell
curl 'https://fampay-backend-task-nishchay.onrender.com/videos?page=1'
Adjust the page number as per your need

curl 'https://fampay-backend-task-nishchay.onrender.com/ping'
Try this to test if the API is active
```

# Application Structure

- 📂`Main`
    - 📂`core`
        - 📝`fetch_videos.py`
    - 📂`routes`
        - 📝`videos.py`
    - 📂`utils`
        - 📝`config.py`
        - 📝`db.py`
        - 📝`scheduler.py`
    - 📝`app.py(Entrypoint)`

# Environment Variables

```jsx
MONGO_URI = "mongodb+srv://<Fill Based on your deployment>"
COLLECTION_NAME = "<Create and Fill Based on your deployment>"
GOOGLE_API_KEYS=API_KEY_1,API_KEY_2,API_KEY_3
QUERY = "Enter Query to Search"
TIME_DELTA = 10
TIME_DELAY = 10
```

This is how an actual env file would look like

```jsx
MONGO_URI = "mongodb+srv://XXXXXXXX.mongodb.net/XXXXXXX?retryWrites=true&w=majority"
COLLECTION_NAME = "r2d2"
GOOGLE_API_KEYS = AIzXXXXXXXXXXyfP_XL-_yOC0KgFUb39Y,AIzaXXXXXXXXXTUq7P0i-AHgQxVJZKwHEc,AIzaSXXXXXXXXXX9X2Y-JmjFlWHh63ns
QUERY = "surfing"
TIME_DELTA = 604800
TIME_DELAY = 10
```

# Getting Started

Lets get started! to set you up with running the code

### Installing Dependencies

if using gunicorn then:

```bash
Navigate to the source folder and execute the following command:

pip3 install -r requirements.txt
```

If using docker then:

```bash
Edit your .env beforehand(Instructions Below)

docker build -t <Enter Name of Image> .

run the docker image according to your setup
```

### Setting up the API and Database

We need to setup 2 different services that were used to finish this assignment, 

### MongoDB Atlas Setup

After setting up your atlas account navigate to the following menu to create a new project

![Screenshot 2024-01-31 at 5.45.47 PM.png](docs/Screenshot_2024-01-31_at_5.45.47_PM.png)

After creating and naming a project, you will need to create a deployment

![Untitled](docs/Untitled.png)

For our demo purpose, we’ll be creating a free instance

![Untitled](docs/Untitled%201.png)

Once done, you can set up the access control for the deployment, Create a password and username for yourself(you will need this later to setup the .env file)

![Untitled](docs/Untitled%202.png)

In the next section you’ll have to setup the IP access list for your application

if you have a static IP address then setting up for a local environment with the default ip is going to be good enough 

![Untitled](docs/Untitled%203.png)

Otherwise press finish and close and access the network access page

![Untitled](docs/Untitled%204.png)

press add ip address and select the allow traffic from anywhere option(or enter 0.0.0.0/0)

![Untitled](docs/Untitled%205.png)

this is not a secure method to handle IP access control

Once done, create a new database, click add data

![Untitled](docs/Untitled%206.png)

and navigate to create database

![Untitled](docs/Untitled%207.png)

name according to your use case 

![Untitled](docs/Untitled%208.png)

once done go to the overview tab and select the connect option

and select drivers

![Untitled](docs/Untitled%209.png)

![Untitled](docs/Untitled%2010.png)

Select python and copy the given url

![Untitled](docs/Untitled%2011.png)

in this URL do remember to add your Password as created above and add the database name at the end of the URL right before the parameters

```bash
mongodb+srv://nishchayspace:D4t0pN3OB4i74FWb@slompy.h63rafj.mongodb.net/cricket?retryWrites=true&w=majority
```

This is a sample URI that we need to add to the env

### Youtube Data API

Create a Google Cloud account, once done create a new project from the following menu 

![Untitled](docs/Untitled%2012.png)

Once you create and switch over to the new project you will be greeted with the following page

![Untitled](docs/Untitled%2013.png)

Click on enable apis and services and search for youtube data api v3 

![Untitled](docs/Untitled%2014.png)

![Untitled](docs/Untitled%2015.png)

Once you enable to the top right you will see an option to create credentials

![Untitled](docs/Untitled%2016.png)

and you will then be greeted with your credentials 

### Adding Environment Variables

Now we can finally fill the .env file, 

```bash
MONGO_URI = mongodb+srv://<Enter Based on instruction above>
COLLECTION_NAME = <Create and Fill Based on your deployment>
GOOGLE_API_KEYS = <Enter Based on instruction above>#add multiple comma separated
QUERY = "Enter Query to Search"
TIME_DELTA = "Videos range time" #if 10 then api will search for videos uploaded
#in the last 10 seconds
TIME_DELAY = "Delay between each schedule"
```

# Execution

run this command to execute the code

```bash
gunicorn app:app
```

# Results

Here is a small demo of how the endpoint works

![Untitled](docs/Untitled%2017.png)

as you can see the api appropriately paginates video objects in a reverse chronological order

```json
[
    {
        "_id": "k9ljP1vdnes",
        "title": "Small waves are better than no waves I guess #surfing",
        "description": "",
        "publishedAt": "2024-01-31T07:29:37Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/k9ljP1vdnes/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/k9ljP1vdnes/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/k9ljP1vdnes/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "0SNY124r5To",
        "title": "Surfing Picture Perfect, Clean Burleigh Heads! Pt One. Taj Burrow &amp; The Locals",
        "description": "Surfing Pumping, Clean Burleigh, 20th March 2017 Pt1. Taj Burrow, Shaun Martin, Toby Johnston, Toby Mossop, Jarrod ...",
        "publishedAt": "2024-01-31T04:01:16Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/0SNY124r5To/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/0SNY124r5To/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/0SNY124r5To/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "qXqFygCZqMQ",
        "title": "Would You Surf On Ice?",
        "description": "Credit: nikguehrs/tt https://www.tiktok.com/t/ZT8nhYyp8/ Credit: adrienraza/tt https://www.tiktok.com/t/ZT8nh1NMk/ Check out my ...",
        "publishedAt": "2024-01-31T03:18:19Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/qXqFygCZqMQ/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/qXqFygCZqMQ/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/qXqFygCZqMQ/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "P7nmSOF_Zno",
        "title": "Bingin Glass #surfing #balisurf #surfers",
        "description": "SUBSCRIBE for daily surf videos: https://bit.ly/2Tu1Poz FIND US HERE Website: https://surfersofbali.com/ Facebook: ...",
        "publishedAt": "2024-01-30T23:00:26Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/P7nmSOF_Zno/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/P7nmSOF_Zno/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/P7nmSOF_Zno/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "kXnDB73NgNA",
        "title": "Glassy Pipeline Barrel 😮 #shorts #surfing",
        "description": "Welcome to Waves of the World We are not your typical surfing channel. Our dedicated filmers from around the world produce the ...",
        "publishedAt": "2024-01-30T21:00:33Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/kXnDB73NgNA/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/kXnDB73NgNA/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/kXnDB73NgNA/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "zMHz7eD4mYw",
        "title": "How to Face Your Fears Surfing Big Waves: Pipeline W/ Griffin Colapinto",
        "description": "How Pro Surfers FACE FEAR and prepare the mind for BRUTAL Pipeline w/ Griffin Colapinto and Koa Smith. The Power of setting ...",
        "publishedAt": "2024-01-30T18:38:27Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/zMHz7eD4mYw/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/zMHz7eD4mYw/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/zMHz7eD4mYw/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "DIhhhivZsv4",
        "title": "Hawai&#39;i, As Told By Kimo Leong | Yeti x WSL",
        "description": "Kimo Leong's legacy as a prominent and influential Hawaiian is known across the Islands for taking care of his home. Leong and ...",
        "publishedAt": "2024-01-30T17:02:16Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/DIhhhivZsv4/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/DIhhhivZsv4/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/DIhhhivZsv4/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "Ri3WESyXDQQ",
        "title": "A Really Long Wave At Uluwatu #surfing #balisurf #surfers",
        "description": "SUBSCRIBE for daily surf videos: https://bit.ly/2Tu1Poz FIND US HERE Website: https://surfersofbali.com/ Facebook: ...",
        "publishedAt": "2024-01-29T23:00:26Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/Ri3WESyXDQQ/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/Ri3WESyXDQQ/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/Ri3WESyXDQQ/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "kxmGcO6joug",
        "title": "PIPE PRO &#39;24 Super Session Warmup: World&#39;s Best Surf LARGE Pipeline Leading Up to Contest",
        "description": "Some of the best evening pipe of the year! Barron Mamiya, Seth Moniz, Kala Grace, Ezekiel Lau, Koa Smith, Miguel Pupo, ...",
        "publishedAt": "2024-01-29T22:00:22Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/kxmGcO6joug/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/kxmGcO6joug/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/kxmGcO6joug/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    },
    {
        "_id": "j5rY4Z_xTEg",
        "title": "Official Surfline Forecast: Big Swell, Better Wind 1/31 Looking Likely For Lexus Pipe Pro",
        "description": "The 2024 Championship Tour book is now open as we turn the page to the Lexus Pipe Pro presented by Yeti. With large WNW ...",
        "publishedAt": "2024-01-29T22:00:18Z",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/j5rY4Z_xTEg/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/j5rY4Z_xTEg/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/j5rY4Z_xTEg/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        }
    }
]
```
