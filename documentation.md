# Notes on Component documentation

The component documentation is contained in the "README.md" which is a mandatory part of the component package.

It is written in markdown, and intended to be consumed both in this format and rendered into HTML.

## Audience & Purpose

The primary audience for the documentation are developers. The initial description should give non-developers an idea of what the component is intended for, but all other information can require a basic degree of technical knowledge and competence (though we should still make things as easy as possible).

The initial contact with the documentation is during a user's search for suitable components. The documentation needs to present the salient facts here upfront, so that a quick reading above the fold plus, potentially, a minimal amount of scrolling, should establish whether a component meets a particular set of requirements.


## Structure

An initial summary of the functionality is followed by an overview of the API.

Next are installation instructions, then the full API documentation.

Installation instructions come before the full API documentation since on initial contacts it is important to stress how simple the usage of the components is.


### Summary

The summary is intended to give the reader enough information to decide whether a particular component fulfills a particular function that she is looking for. For this it needs to describe e.g. the sensor the component interfaces with, what data it provides. The description should be as concise as possible.

An example for the Temperature Monitor Component could be:

> The Temperature Monitor Component allows the remote monitoring of a temperature sensor connected to a Raspberry Pi. Monitoring is via events published with the current temperature, and an alarm event when a configurable threshold temperature is exceeded.

An example for the Sample Player Component could be:

> The Sample Player Component allows triggering the playing of samples on a Rasperry Pi, and the upload of custom samples. Both the triggering and the upload is via WAMP calls.

### API Quick Reference

The API quick reference is intended to give the (developer) reader the information necessary to decide whether the required functionality is exposed in a way which meets the requirements of the user. It does not need to enable full use of the API - that's what the "API Full Reference" is for.

An example for the Temperature Monitor could be:

> Calls:    
>
> `toggle_publish` - start/stop the publication of temperature events
> `set_threshold`- set a temperature value - if this is exceeded, an alarm is published     
>
> Events:
>     
> `on_temperature` - current temperature    
> `on_threshold_exceeded` - set threshold is exceeded, contains temperature value

An example for the Sample Player could be:

> Calls:    
>
> `trigger_sample` - trigger the playback of a sample (identified by sample name)
> `stop_sample`- stop the playback of a sample (identified by sample name)     
> `add_sample`- upload a sample hosted at a given URL to the device  
>
> Events:
>     
> - none-

### Setup & Running

The setup section is there to provide all the information necessary for the deployment of the component. It should also clearly indicate that this is a simple process.

Instructions here will largely repeat across components.

Points to cover:

* The device or platform the component runs on.
* Hardware requirements (sensors, actuators)
* Software requirements (Crossbar.io, Docker installed, CB node paired with the CDC)
* Instantiating the component
* Basic configuration steps/simple configuration example

For the Temperature Monitor Component:

> This component is intended to run on a Raspberry Pi with an additional temperature sensor connected.   
>
> The component was developed usind the Adafruit Waterproof DS18B20 Digital temperature sensor. Other sensors may work as well.
>      
> Before running the component you must:    
> * connect a Adafruit Waterproof DS18B20 Digital temperature sensor (or compatible hardware) to pins 13 and 17 on the Raspberry Pi
> * install Docker on the device (instructions)    
> * install Crossbar.io on the device (instructions)
> * pair the Crossbar.io instance with the CDC
>
> To run the component, in the CDC CLI:
> * select the Crossbar.io node on the Pi as your context
> * create the component by doing     
>     `create component tempmon`    
>   This will download the Docker image of the component (if this is not already cached) and instantiate the component.    
> CLI feedback on success is:
> `Component instantiated. Default component ID: FGH-456-RED`
> * start the component with default values, just passing in a component id, the router and realm to connect to    
> `start component FGH-456-RED --router 192.168.1.34:8080/ws --realm test_01`    
> On a successful start, the CLI logs:    
> `Component FGH-456-RED started. Connected to router at 192.168.1.34:8080 and to realm 'test_01'`
>
> The component can now be integrated into your application using the component API.

-----------------
-- missing: what extra information can be passed into the component, e.g. different base URL, procedure and topic URLs, configurable thresholds etc.?
-----------------

#### Present State

For the time being, with the CDC infrastructure not in place, the instructions need to also cover.


### API Full Reference

All the information for the full API reference is contained in the interface definition files for the component.

Ideally, to avoid duplication of information, the reference section would be generated from these files.

> Wishlist: Allow interspersing blocks of additional information with the generated content, e.g. to give a hint to avoid a common error.

An example for an entry in the full API reference is:

- write me -
