#!/usr/bin/env python
# vim: set fileencoding=utf-8

import json
import logging
import random

from flask import Flask
from flask import request

application = Flask(__name__)

db = {}

# --- DEFAULT HANDLER ---


def default_handler(api_handler):
    try:
        # --- parsing request ---

        form = request.get_json()
        if not form:
            raise Exception('form is missing')

        logging.debug(
            'form: %s' % json.dumps(form, indent=2, ensure_ascii=False)
        )

        uuid = request.args.get('uuid')
        if not uuid:
            raise Exception('uuid is missing')

        # --- handling ---

        # TODO: Workround.
        # InvalidDocument: key u'requirements.smoking' must not contain '.'
        for slot, value in form.items():
            if slot.find('.'):
                del form[slot]
                slot = slot.replace('.', '__')
                form[slot] = value

        global db
        response = api_handler(db, form, uuid)

        for slot, value in form.items():
            if slot.find('__'):
                del form[slot]
                slot = slot.replace('__', '.')
                form[slot] = value

        # --- result ---

        response = json.dumps(response, indent=2, ensure_ascii=False)

        logging.debug("response: %s" % response)

        return response, 200, {
            'Access-Control-Allow-Origin': '*',
            'X-Content-Type-Options': 'nosniff',
            'Content-Type': 'application/json'
        }

    except Exception as exc:
        logging.exception(exc)
        return "Server error", 500, {
            'Access-Control-Allow-Origin': '*',
            'X-Content-Type-Options': 'nosniff',
            'Content-Type': 'text/plain'
        }

# --- HANDLERS ---


@application.route('/order_taxi', methods=["POST", "GET"])
def order_taxi():
    return default_handler(api_order_taxi)


@application.route('/get_status_taxi', methods=["POST", "GET"])
def get_status_taxi():
    return default_handler(api_get_status_taxi)


@application.route('/cancel_order_taxi', methods=["POST", "GET"])
def cancel_order_taxi():
    return default_handler(api_cancel_order_taxi)


# --- API ---


def api_order_taxi(db, form, uuid):
        location_from = form['location_from']
        location_to = form['location_to']
        when = form['when']

        # --- parameters validation ---

        if location_from == location_to:
            return {
                "actions": [{
                    "action": "nlg",
                    "id": "error__location_from__equals__location_to",
                    "form": form
                }]
            }

        if random.random() < 0.1:
            return {
                "actions": [{
                    "action": "nlg",
                    "id": "error__there_are_no_free_cars",
                    "form": form
                }]
            }

        # --- ordering taxi ---

        db[uuid] = form

        return {
            "actions": [{
                "action": "nlg",
                "id": "order_taxi_finished_successfully",
                "form": form
            }, {
                "action": "reset"
            }]
        }


def api_get_status_taxi(db, form, uuid):

        # --- ordering taxi ---

        form = db.get(uuid)

        if form is None:
            return {
                "actions": [{
                    "action": "nlg",
                    "id": "there_is_no_any_order",
                    "form": form
                }, {
                    "action": "reset"
                }]
            }

        if random.random() < 0.5:
            form['number'] = u'у123ух45'
            form['brand'] = u'хёндай солярис'
            form['color'] = u'жёлтый'
            form['phone'] = u'+79056665544'
            form['name'] = u'Вася Пупкин'
        else:
            form['number'] = u'е777кх77'
            form['brand'] = u'тесла'
            form['color'] = u'красная'
            form['phone'] = u'+79057777777'
            form['name'] = u'Сергей Иванов'

        return {
            "actions": [{
                "action": "nlg",
                "id": "get_status",
                "form": form
            }, {
                "action": "reset"
            }]
        }


def api_cancel_order_taxi(db, form, uuid):

        # --- ordering taxi ---

        form = db.get(uuid)

        if form is None:
            return {
                "actions": [{
                    "action": "nlg",
                    "id": "there_is_no_any_order",
                    "form": form
                }, {
                    "action": "reset"
                }]
            }

        del db[uuid]

        return {
            "actions": [{
                "action": "nlg",
                "id": "cancel",
                "form": form
            }, {
                "action": "reset"
            }]
        }


@application.route('/ping')
def ping():
    return "1", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    application.run(host="::", port=7777, debug=True)
