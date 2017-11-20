# My 100% typical and standard CRUD app

Well.. my first django project, 2014/2015, left as-is,
everyone creates task magagement app, right?

## What gives

* Simple system for managing daily tasks (bonus: map view).
* Django, Leaflet, DataTables, MetroUI.
* No user tracking.
* Ajax avoided like fire. No real reason. Just wanted it to work this way.
* Next project will be SPA@REST

## Url structure

```
├── /
├── /info
│   ├── /
│   ├── about
│   ├── agreement
│   ├── support
│   ├── faq
├── /user
│   └── /<str: username>
├── /users
│   ├── /
│   ├── /logout
│   ├── /login
│   ├── /settings
│   └── /passwd
└── /tasks
    ├── /
    ├── /history/ not implemented yet.
    ├── /map
    ├── /new
    ├── /<int: task_id>/
    └── /<int: task_id>/edit/
```
