# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out for instructions on how to deploy this app to Heroku and also run it locally.

Alternatively, you can deploy it using this Heroku Button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

# Deploying
```
git push heroku main
heroku ps:scale web=1
heroku open
```

# Local dev
```
heroku local
```

# Actions
## Simulate completing a transaction
```
curl --location --request POST 'https://mighty-stream-68566.herokuapp.com/transactions/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "userId": "5398095040303673"
}'
```