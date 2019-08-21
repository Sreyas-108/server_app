# Liquid Galaxy Controller Server Application

> API to handle request from Controller application for the LG Screen developed for Liquid Galaxy in GSoC 2019.

## Getting Started

This application is a server application which handles OSC requests from the [LG Controller Application](https://github.com/LiquidGalaxyLAB/lg_controller) for Liquid Galaxy setup.
Latest installation for [Liquid Galaxy setup.](https://github.com/LiquidGalaxyLAB/liquid-galaxy)

## Installation

**Install only on master machines.**

The installation script is present in `/scripts/install.sh`

Execute the installation file from any user folder.
```
bash <(curl -s https://raw.githubusercontent.com/Sreyas-108/server_app/master/scripts/install.sh)
```

Requirements : 
Please install the [KML Uploader](https://github.com/xemyst/liquid-galaxy-kml-uploader/) before proceeding.
This must be running successfully before running this server application.

### Run
Once execution has been executed successfully, run ``` chmod +x execute.sh``` in the '$HOME/api/server_app/scripts' folder.

Run ```./scripts/execute.sh``` to start the api. Enter the details accordingly. It will be present in the '$HOME/api/server_app' folder.

On successful initialization of the server application, configuration details will be displayed. These details are to be entered to connect the android application.

## Contributing

Please open an issue for discussion before sending a pull request. Please update the tests as required.

## License

[LICENSE](LICENSE)

