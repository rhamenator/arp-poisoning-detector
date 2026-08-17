<p align="center">
  <img src=".github/assets/logo.png" alt="ARP Poisoning Detector logo" width="220">
</p>

# ARP Poisoning Detector

This is a simple command-line program that runs the `arp -a` command and checks for potential ARP poisoning by looking for duplicate IP addresses with different MAC addresses.

## Features

- Checks for duplicate IP addresses with different MAC addresses.
- Saves the IP-MAC mapping to a JSON file.
- Prints one or more warning messages if ARP poisoning is detected.
- Prints a message indicating no ARP poisoning if the scan is negative.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/rhamenator/arp-poisoning-detector.git
    cd arp-poisoning-detection
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script:

```sh
python arp_detection.py
