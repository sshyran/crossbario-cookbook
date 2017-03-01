# Notes on the contents of `component.json`

The `component.json` file contains component meta-data

The following is a collection for what this meta-data could be for particular components, to get a feel fro what is required and what else makes sense in this context.


## Temperature sensor

```json
{
   "$schema": "http://com.crossbario/schemas/component",

   "title": "Temperature Monitor",
   "description": "Receive events about current temperature, configure an alert when a temperature threshold is exceeded.",
   "publisher": "Crossbar.io GmbH",

   "tags": ["sensor", "temperature", "iot", "ARM", "raspberrypi"],
   "version": "0.1",
   "license": ["MIT", "liberal"],

   "homepage": "https://github.com/crossbario/crossbar-examples/tree/master/iotcookbook/device/pi/tempmon",
   "support_addresses": ["https://groups.google.com/forum/#!forum/crossbario"],
   "docker_image_url": "https://placeholder.test",

   "interfaces": ["tempmon_interface.json"]
}
```

## Sample Player

```json
{
   "$schema": "http://com.crossbario/schemas/component",

   "title": "Sample Player",
   "description": "Play back existing samples and upload new samples to the device.",
   "publisher": "Record Evolution GmbH",

   "tags": ["actuator", "sound", "samples", "iot", "ARM", "raspberrypi"],
   "version": "0.1",
   "license": ["MIT", "liberal"],

   "homepage": "https://github.com/crossbario/crossbar-examples/tree/master/iotcookbook/device/pi/sampleplayer",
   "support_addresses": ["sven@record_evolution.com"],
   "docker_image_url": "https://placeholder.test",

   "interfaces": ["sampleplayer_interface.json"]
}
```


## Notes

* When hosted by us, the component meta-data includes a **component ID**. This is assigned by us during the component upload.
* **Tags** is quite generic, but also flexible. Things to cover here are
   * **Type of component**: sensor, actuator (other?)
   * Key words for **specific functionality** or **area of functionality** (e.g. "temperature", "weather")
   * **platforms** that the component can run on. Aay warrant an entry of its own.
* **License** could be just the identification of a particular license. This is somewhat beside what users require: They are less interested in whether a component is licensed under the MIT or three-clause-BSD license than in the more fundamental and general question of what they can do with the code. Having "liberal", "copyleft" and "commercial" as categories here allows this search.
* **Interfaces**: Having this as an array leaves open the possiblity that a component may offer multiple interfaces, e.g. a standard component management interface, a generic interface for sensors and a specific temperature sensor interface, which are described in separate interface files.
