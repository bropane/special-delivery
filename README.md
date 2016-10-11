# Special Delivery

A battery powered GPS tracker designed to catch mail thieves. The "package" refers to the hardware
which will be disguised waiting in the mailbox. The server is the computer to store the information from
the package.

## Features
- Low power consumption
- Runs on Particle.IO Electron w/ Asset Tracker Shield & Heroku
- Purpose built to catch thieves!

## How to Use

To use this project, follow these steps:

1. Clone the repo
2. Install python dependencies $ pip install -r requirements.txt
3. WORK IN PROGRESS

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.
