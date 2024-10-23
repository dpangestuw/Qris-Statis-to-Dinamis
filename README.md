# QRIS Static to Dynamic Converter

This Python script converts a static QRIS (Quick Response Code Indonesian Standard) into a dynamic QRIS, allowing users to input transaction amounts and optional service fees (in Rupiah or percentage). The script also generates a QR code image from the resulting dynamic QRIS data.

## Features

- Converts static QRIS to dynamic QRIS by adding transaction amounts.
- Supports optional service fees in either Rupiah or percentage format.
- Generates a QR code image for the dynamic QRIS.
- Calculates and appends a CRC16 checksum to the QRIS for data integrity.

## Requirements

- Python 3.x
- Required Python packages:
  - `qrcode`

## Installation

1. Clone this repository or download the script file.
2. Install the required Python packages:

   ```bash
   pip install qrcode[pil]
   ```
3. (Optional) You may also need to install the Pillow library if it's not installed automatically:
   ```bash
   pip install pillow
   ```
## usage
  **Set your data on qris = "your qris"**

  ```bash
   git clone https://github.com/dpangestuw/Qris-Statis-to-Dinamis.git
   ```
  ```bash
   cd Qris-Statis-to-Dinamis
   ```
  ```bash
   python qris.py
   ```

