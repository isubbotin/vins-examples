{
  "form": "order_taxi",
  "events": [{
    "event": "submit",
    "handler": "rest",
    "url": "http://[2a03:b0c0:2:d0::67:7001]:7777/order_taxi"
  }],
  "slots": [{
    "slot": "location_from",
    "type": "geo",
    "optional": false,
    "events": [{
      "event": "ask",
      "handler": "nlg",
      "phrase_id": "ask__location_from"
    }]
  }, {
    "slot": "location_to",
    "type": "geo",
    "optional": false,
    "events": [{
      "event": "ask",
      "handler": "nlg",
      "phrase_id": "ask__location_to"
    }]
  }, {
    "slot": "when",
    "type": "datetime",
    "optional": false,
    "events": [{
      "event": "ask",
      "handler": "nlg",
      "phrase_id": "ask__when"
    }]
  }, {
    "slot": "requirements.child",
    "type": "boolean",
    "optional": true,
    "events": []
  }, {
    "slot": "requirements.animals",
    "type": "boolean",
    "optional": true,
    "events": []
  }, {
    "slot": "requirements.conditioner",
    "type": "boolean",
    "optional": true,
    "events": []
  }, {
    "slot": "requirements.smoking",
    "type": "boolean",
    "optional": true,
    "events": []
  }]
}