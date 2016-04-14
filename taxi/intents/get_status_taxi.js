{
  "form": "get_status_taxi",
  "events": [{
    "event": "submit",
    "handler": "rest",
    "url": "http://[2a03:b0c0:2:d0::67:7001]:7777/get_status_taxi"
  }],
  "slots": [{
    "slot": "color",
    "type": "string",
    "optional": true,
    "events": []
  }, {
    "slot": "brand",
    "type": "string",
    "optional": true,
    "events": []
  }, {
    "slot": "number",
    "type": "string",
    "optional": true,
    "events": []
  }, {
    "slot": "name",
    "type": "string",
    "optional": true,
    "events": []
  }, {
    "slot": "phone",
    "type": "string",
    "optional": true,
    "events": []
  }]
}
