# My Little Organiser


### By Grzegorz Wójcicki


Domains:

* my-organiser.com
* little-organiser.com
* my-little-organiser.com


## Url structure

```
├── /
├── /info
│   ├── /
│   ├── about
│   ├── agreement
│   ├── faq
├── /lists
│   ├── /
│   └── /<str: url_name>
├── /user
│   ├── /
│   ├── /logout
│   ├── /passwd
│   └── /login
└── /tasks
    ├── /
    ├── /history
    ├── /map
    ├── /overview
    ├── /new
    ├── /edit
    └── /show
        ├── / (redirect to /tasks/overview)
        └── /<int: task_id>
```