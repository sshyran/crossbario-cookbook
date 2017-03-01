# Component API notes

With different component functionality, component APIs will differe widely regarding what they expose on a component and what events they provide. There is, however, functionality for administrating the component which is common to all components.

These notes give some thoughts on what common API features could be. They further list API features of particular components as an overview of how specifc functionality may be made accessible.

## Base URL

Each component needs to be individually addressable. A user may start multiple instances of a component within an application, and more than one instance may run on the same machine.

The base URL for all calls to the component, and for any events it emits, needs to include a unique identifier. This cannot be identifying information from the device the component is running on (such as a device serial number, MAC address), but needs to be specific to the component.

The identifier will most usually be assigned during the component instantiation, and then passed into the component (e.g. as an environment variable). Absent such assignment, it could be created within the component (random id with sufficient entropy to assure uniqueness).

A base URL for a component could be

    io.crossbar.components.<id>.<component_name>


## Custom URLs

Within an application, an API with semantic naming based on the structure of the application helps clarity and reduces errors. Users will not want to break from this when using components.

Custom URLs are a necessary option to allow users to seamlessly integrate components into their applications.

There are two levels for this:

* customizing the base URL
* customizing individual action URLs

### Custom Base URL

A custom base URL applies across all API URLs, e.g. for a temperature monitor component, the standard URLs for temperature publication events and for temperature alarms

    io.crossbar.components.component_34787829.tempmon.on_temperature
    io.crossbar.components.component_34787829.tempmon.on_threshold_exceeded

with a base URL of

   io.crossbar.components.component_34787829.tempmon

after a setting of a new base URL

    com.buildingmanagement.building_01.floor_11.temp_sensor_23

would become

    com.buildingmanagement.building_01.floor_11.temp_sensor_23.on_temperature
    com.buildingmanagement.building_01.floor_11.temp_sensor_23.on_threshold_exceeded

This allows a quick adaptation of the component to the namespace used in the applciation.

The changing of the base URL may occur via two mechanisms:

* information passed in during instantiation of the component
* via a component management API call

The component management API call could be in the form of a call

    <baseURL>.set_base_url

where the argument is a new base URL as a string.

### Custom Action URLs

In some cases the semantics of the component actions (procedures and events) may differ from those used in an application. In this case it would be advantageous to be able to configure not just the base URL, but the action part as well.

In the above example for a temperature sensor, "on_temperature" could e.g. be renamed to "present_temperature".

The component management API call to configure this could be in the form

    <baseURL>.set_action_url

with the current part of the respective URL (excluding the base URL part) and the new part of the URL as arguments (both strings).

### Questions

* Should it also be possible to configure completely freeform URLs for actions, without a shared base URL?


## Particular Component APIs


### Pi Temperature Monitor

#### Calls

- `<baseURL>.tempmon.toggle_publish`- start/stop publishing the periodic temperature readings
- `<baseURL>.tempmon.set_threshold` - threshold temp as int - alarm is published when this is exceeded

#### Events

- `<baseURL>.tempmon.on_temperature` - periodic publishing of current temperature reading
- `<baseURL>.tempmon.on_threshold_exceeded` - alarm when the configured threshold is exceeded


### Pi Sample Player

#### Calls

- `<baseURL>.sample_player.trigger_sample` - name of sample as argument
- `<baseURL>.sample_player.stop_sample` - name of sample as argument
- `<baseURL>.sample_player.add_sample`- URL to download sample file from, name to be assigned to it

#### Events

- none
