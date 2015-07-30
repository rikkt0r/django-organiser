# My Little Organiser


### By Grzegorz Wójcicki


Domains:

* my-organiser.com
* little-organiser.com
* my-little-organiser.com

## WTF

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