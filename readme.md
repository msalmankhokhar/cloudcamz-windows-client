# Cloudcamz Windows Client

## Overview
Cloudcamz Windows Client is a crucial component of the Cloudcamz CCTV camera backup solution. This client application runs as a Windows service, facilitating seamless communication between local CCTV cameras and the Cloudcamz cloud platform.

## Features
- Runs as a Windows service in the background
- Manages local CCTV camera connections
- Streams footage securely to Cloudcamz cloud storage
- Local HTTP server for camera interaction
- Automatic service recovery and reconnection
- Secure communication with Cloudcamz web platform

## Technical Details
- Built with Python Flask
- Operates as a local HTTP server on port 80
- Interfaces with cameras on local network
- Communicates with Cloudcamz web application
- Windows service integration

## Installation
1. Download the Cloudcamz Windows Client installer
2. Run the installer with administrator privileges
3. Follow the installation wizard
4. The service will automatically start after installation

## System Requirements
- Windows 10 or later
- Administrator privileges for installation
- .NET Framework 4.7.2 or later
- Python 3.8 or later (bundled with installer)
- Minimum 2GB RAM
- 500MB free disk space

## Configuration
The client can be configured through the Cloudcamz web interface at https://mydomain.com after installation.

## Troubleshooting
- Service status can be checked in Windows Services
- Logs are available in Windows Event Viewer
- For support, contact support@cloudcamz.com

## Security
- End-to-end encryption for video streams
- Secure communication with cloud servers
- Regular security updates
- Local network isolation

## License
Copyright © 2024 Cloudcamz. All rights reserved.
