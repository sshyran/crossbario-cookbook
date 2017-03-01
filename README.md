# Crossbar.io IoT Cookbook

## Intro

The IoT Cookbook is a collection of components which encapsulate typical, generic functionality of IoT applications (sensors and actuators).

All components are packaged in Docker images with a standardized set of meta-data, and are launched via a Crossbar.io instance on the target device. The connection of this instance to Crossbar.io Fabric allows remote management of the components.

Initially, the target platform for components is the Raspberry Pi, but components for other SBCs or even desktop-class devices are possible.

## Motivation

IoT applications employ recurring, generic functionality. As an example, a temperature sensor needs to be able to transmit the current temperature data, and this functionality is the same regardless of where the temperature is being measured.

The Cookbook aims to provide such basic function blocks, with standard packaging and easy-to-use APIs.

Developers can use these function blocks in their applications and concentrate on designing the combinations of functionality and the creating the connecting code which creates value for the particular target user.

## How Does it Work?

The components are centrally registered with Crossbar.io Fabric, the online management service for Crossbar.io routers. The set of information submitted allows the automatic display of a human-readable description (README.md), as well as containing all information necessary for deployment (chief among this the location of the Docker file).

A Crossbar.io node runs on the Raspberry Pi. This node is connected to Crossbar.io Fabric, and a particular management realm within it.

A developer with the necessary permissions on the management realm can then remotely launch components by selecting both the component and the node/device to deploy the component on. This can be done programmatically via the a management API which Crossbar.io Fabric makes accessible, or via the command line shell that we provide.

>Note: The above does not yet work, but it should soon.

The launch command is communicated to the node via the node management API. If the docker image is not yet locally cached this is downloaded. It is possible to pass information into the Docker container at this point, e.g. an identifier to use as part of component API URLs.

All interaction with the component after launch is via the WAMP API which the component provides.

> The same API may be provided by multiple components, so that it is possible to transparently exchange e.g. a component running on an ARM-architecture device with one running on a x86-architecture device.

## Component Parts

A component has the following required parts:

* Docker file
* README.md
* component.json
* interface.json
* Makefile

> Note: The text below is a work in progress and any feedback is welcome!


### Docker File

The `Dockerfile` contains a complete build recipe for the user component (such as the IoT cookbook speech output component).

It will usually derive from one of our Docker Autobahn base images, by starting with a line like this:

    FROM crossbario/autobahn-python-armhf:cpy2-minimal-tx-0.16.1

This will derive the component from the CPython 2 base image with Autobahn 0.16.1 and Twisted installed (but nothing else, and stripped down to the minimum) - and of of that for **ARM architecture** (as would be required if the component is supposed to run on the Pi for example).

A component will usually require more (Python) packages, such as for accessing GPIO or for rendering speech from text etc. The installation of these additional requirement will then follow the above line in the `Dockerfile`.

#### Open issues

##### Multiple archs/targets

A question remaining is how to handle multiple CPU architectures or target platforms.

For example, Crossbar.io and Autobahn are available now for both x86-64 and ARM, eg:

* **x86-64**: crossbario/crossbar:community-16.10.1
* **armhf**: crossbario/crossbar-armhf:community-16.10.1

##### Configuration

Another question is how to forward configuration to the component (technically). A Docker container can receive configuration at least via:

* environment variables
* by reading from stdin
* by reading from a (host) file

##### Uplink Router

The component will need to connect to a upstream Crossbar.io router. Probably, even a list of router transports of different kind and to different routers might be wished for.

Probably this information is best provided or selected by user at deployment time (when the component has been selected, but the target of where to instantiate the component needs to be specified).

But again at least the question remains of how to technically transmit this information to within inside the Docker container where the (Autobahn based) component runs (and needs to connect to Crossbar.io).

### README.md

Human-readable documentation for the component, in GitHub-flavored Markdown.

The rendered document should look visually appealing, using code syntax highlighting and so forth. It can make use of Markdown rich formatting features and can contain links to external resources.

> Images can only be "embedded" by using fully qualified URLs (not relative) and hosting the images externally - as uploading of user Web resources during publishing of a component will not be supported.



### component.json

A JSON or YAML file with component meta-data

* title
* description
* tags
* version
* license
* homepage
* list of interfaces implemented
* docker image URL
* config schema


### interface.json

A JSON (YAML) file with interface metadata

* title
* description
* tags
* version
* license
* homepage
* API schema

> A component may be instantiated multiple times by a user within the same application. The API and deployment process needs to take this into consideration in order to avoid duplicate topics and failed procedure registrations.

> Initial notes on the API description can be found in "api.md", a sample API definition in "api.json" in this directory.

### Makefile

For automating tasks like building, registering and publishing interfaces and components.

It is supposed to work on Linux and provide the following targets:

* image_clean: scratch everything related to Docker image building.
* image_build: build the component Docker image.
* image_publish: publish the component Docker image to Dockerhub.

## Development Process

Crossbar.io Fabric is under development, and some parts necessary for the full deployment process are not there yet.

For the time being we can run components under development locally, i.e. just manually start the Docker image with the required configuration data.
