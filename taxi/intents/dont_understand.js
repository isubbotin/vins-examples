
{
    "form": "dont_understand",
    "comment": "если команда не понятна, то активируется этот intent",
    "events": [
        {
            "event": "submit",
            "handler": "nlg",
            "phrase_id": "i_dont_undestand_you"
        }
    ],
    "slots": [
        {
          "slot": "utterance",
          "type": "string",
          "optional": true,
          "events": []
        }
    ]
}
