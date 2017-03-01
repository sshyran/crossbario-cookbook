# Notes on the contents of `interface.json`

The `interface.json` file contains information about an interface that a component implements.

A component may implement several interfaces, e.g. a standard component management interface, a generic interface for sensors and a specific temperature sensor interface, which are described in separate interface files.

The following is a collection for what this information could be for particular interfaces, in the form of interface description JSON objects, to get a feel for what is required and what else makes sense in this context.


## Component Management Interface

An interface shared across components which permits common actions. (At this moment: limited to customizing the URLs used by the component).

```json
{
   "$schema": "http://com.crossbario/schemas/interface",

   "title": "Shared Component Management Interface",
   "description": "Perform generic component management actions such as setting custom URLs.",

   "tags": ["management", "URLs", "configuration"],
   "version": "0.1",
   "license": ["CC BY-ND 4.0", "attribution", "no-derivatives", "commercial"],

   "homepage": "https://github.com/crossbario/crossbar-examples/tree/master/iotcookbook/device/pi/tempmon#interface",

   "API": [
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.set_base_url",
          "type": "procedure",
          "title": "Set Base URL for Component API",
          "description": "Set a new base URL which is then used as part of all component API URLs",
          "parameters": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                        "id": "base_url",
                        "description": "The new base URL to use",
                        "type": "string",
                        "format": "URL"
                     }
                  ],
                  "required": ["base_url"]
             }
          },
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "boolean",
                          "title": "Success",
                          "description": "Successfully changed the base URL"
                     }
                  ]
             }
          },
          "events": [
             "io.crossbar.components.<id>.on_base_url_set"
          ],
          "errors": [
             "io.crossbar.components.<id>.not_a_url"             
          ]
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.on_base_url_set",
          "type": "topic",
          "title": "Set Base URL for Component API Set",
          "description": "A new base URL which is then used as part of all component API URLs has been set",
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "string",
                          "title": "New Base URL",
                          "description": "The new base URL.",
                          "format": "URL"
                     }
                  ]
             }
          }
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.set_action_url",
          "type": "procedure",
          "title": "Set Action URL for Component API Action",
          "description": "Set a new URL for a specified action (procedure or topic)",
          "parameters": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                        "id": "current_url",
                        "description": "The current action URL to change",
                        "type": "string",
                        "format": "URL"
                     },
                     {
                        "id": "new_url",
                        "description": "The action URL to use going forward",
                        "type": "string",
                        "format": "URL"
                     }
                  ],
                  "required": ["current_url", "new_url"]
             }
          },
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "string",
                          "title": "Updated URL",
                          "description": "The full URL used for the action going forward (including the current base URL part)",
                          "format": "URL"
                     }
                  ]
             }
          },
          "events": [
             "io.crossbar.components.<id>.on_action_url_set"
          ],
          "errors": [
             "io.crossbar.components.<id>.not_a_url"             
          ]
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.on_base_url_set",
          "type": "topic",
          "title": "Set Base URL for Component API Set",
          "description": "A new base URL which is then used as part of all component API URLs has been set",
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "string",
                          "title": "New Base URL",
                          "description": "The new base URL.",
                          "format": "URL"
                     }
                  ]
             }
          }
      }
   ]
}
```

## Questions

* Are there any interface licenses?
   * As far as I can tell none of the OSS licenses cover this satisfactorily.
   * A CC license may work, since this is for copyright generally, and tries to be broad in its terms.
* Should we announce the fact that the base URL has changed?
* Does the "format" attribute in addition to the "type" attribute make sense? For the above, it would actually need to be more specific:
   * The **baseURL** is a full URL - but with the <id> part in it, which the checker needs to accept
   * The **action URL part** is just a part of the URL, so checking here should be that this + the current base URL is a full URL

## Temperature Monitor Interface

```json
{
   "$schema": "http://com.crossbario/schemas/interface",

   "title": "Temperature Monitor Interface",
   "description": "Receive current temperature and an alarm when a configurable threshhold is exceeded",

   "tags": ["temperature", "monitoring"],
   "version": "0.1",
   "license": ["CC BY-ND 4.0", "attribution", "no-derivatives", "commercial"],

   "homepage": "https://github.com/crossbario/crossbar-examples/tree/master/iotcookbook/device/pi/tempmon#interface",

   "API": [
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.toggle_publish",
          "type": "procedure",
          "title": "Start/Stop the publication of current temperature values",
          "description": "Calling this either starts or stops the publication of the current temperature value",
          "parameters": {},
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "string",
                          "values": ["running", "stopped"],
                          "title": "Publication state",
                          "description": "Returns 'running' if the call started the publication, 'stopped' if it stopped is"
                     }
                  ],
                  "required": ["current_url", "new_url"]
             }
          },
          "events": [],
          "errors": []
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.on_temperature",
          "type": "topic",
          "title": "Current Temperature",
          "description": "Publication of the current temperature reading.",
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "type": "integer",
                          "title": "Current Temperature Value",
                          "description": "The current temperature value in degrees Celsius"
                     }
                  ]
             }
          }
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.set_threshold",
          "type": "procedure",
          "title": "Set threshold value for alarm",
          "description": "Set the threshold value for the temperature alarm. Whenever this is exceeded, an alarm is published",
          "parameters": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                        "id": "threshold_temperature",
                        "description": "The threshold temperature value in degrees Celsius",
                        "type": "integer"
                     }
                  ],
                  "required": ["threshold_temperature"]
             }
          },
          "result": {},
          "events": [],
          "errors": []
      },
      {
          "$schema": "http://wamp-proto.org/schema#",
          "uri": "io.crossbar.components.<id>.on_threshold_exceeded",
          "type": "topic",
          "title": "threshold exceeded",
          "description": "The configured temperature threshold has been exceeded.",
          "result": {
             "args": {
                  "type": "array",
                  "items": [
                     {
                          "id": "threshold",
                          "type": "integer",
                          "title": "Threshold Temperature",
                          "description": "The currently configured threshold temperature"
                     },
                     {
                          "id": "temperature",
                          "type": "integer",
                          "title": "Current Temperature",
                          "description": "The currently measured temperature"
                     }
                  ]
             }
          }
      }
   ]
}
```

## Sample Player Interface
