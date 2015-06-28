# My Little Organiser


### By Grzegorz Wójcicki


Domains:

* my-organiser.com
* little-organiser.com
* my-little-organiser.com

## What currently works/exists:

* Whole ORM done nicely
* Integrated with django auth engine
* Custom auth backend: login by mail or username
* Permission works (simple, for now.. later gonna use build in django stuff)
* Created every possible template and view (now... fill them up)


## Url structure

```
├── /
├── /info
│   ├── /
│   ├── about
│   ├── agreement
│   ├── support
│   ├── faq
├── /lists
│   ├── /<int: page_id>, default = 1
│   ├── /<str: username>
│   └── /search/<str: username>
├── /users
│   ├── /
│   ├── /logout
│   ├── /passwd
│   └── /login
└── /tasks
    ├── /<int: page_id>, default = 1
    ├── /history/<int: page_id>, default = 1
    ├── /map
    ├── /new
    ├── /edit/<int: task_id>
    └── /task
        ├── / (redirect to /tasks/)
        └── /<int: task_id>
```