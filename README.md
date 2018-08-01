# postcode-api

Endpoint: http://biggui.pythonanywhere.com/postcode

Post Request => fields:
- company
- city

Python Ex:
```
requests.post('http://biggui.pythonanywhere.com/postcode', data = {'company':'Red Lion', 'city': 'London'})
```

Response:
```
{
  "data": {
    "address": {
      "city": "London",
      "country": "UK",
      "map": "https://openstreetmap.org/way/100442829",
      "number": null,
      "postcode": "EC1V 4NA",
      "street": "St. John Street"
    },
    "city": "London",
    "company": "Red Lion"
  },
  "success": true
}
```

