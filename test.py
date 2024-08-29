


def configure_moon_sensors(data):
        moon_sensors = {}

        #logging.debug(f"Processing moonraker sensors: {data}")
        for x in data['sensors'].values():
            moon_sensors[x['id']] = x['values']
        #logging.debug(f"Moonraker sensors: {self.moon_sensors}")

data = {'result': {'sensors': {'tasmota_power1': {'id': 'tasmota_power1', 'friendly_name': 'tasmota_power1', 'type': 'mqtt', 'values': {'energy': 1.378, 'voltage': 239, 'power': 23, 'current': 0.164}}, 'tasmota_power': {'id': 'tasmota_power', 'friendly_name': 'tasmota_power', 'type': 'mqtt', 'values': {'energy': 1.378, 'voltage': 239, 'power': 23, 'current': 0.164}}}}}

configure_moon_sensors(data)