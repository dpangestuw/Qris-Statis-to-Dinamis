import qrcode
import os

# Helper functions for padding and CRC16 calculation
def pad(num):
    return str(num).zfill(2)

def to_crc16(data):
    crc = 0xFFFF
    for char in data:
        crc ^= ord(char) << 8
        for _ in range(8):
            if (crc & 0x8000):
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return '{:04X}'.format(crc & 0xFFFF)

# Input data
qris = "00020101021126570011ID.DANA.WWW011893600915362751266202096275126620303UMI51440014ID.CO.QRIS.WWW0215ID10243193490550303UMI5204594553033605802ID5910dpangestuw6012Kab. Bandung6105402386304AC2C"
nominal = "5000"  # Transaction amount
taxtype = 'p'     # Tax type, 'r' for Rupiah, 'p' for Percentage
fee = "10"        # Fee amount, e.g., 10% for percentage

# Convert static QRIS to dynamic
qris2 = qris[:-4]  # Remove last 4 characters (CRC)
replace_qris = qris2.replace("010211", "010212")
pecah_qris = replace_qris.split("5802ID")

# Add amount and tax (if applicable)
uang = "54" + pad(len(nominal)) + nominal
tax = ""
if taxtype == 'p':
    tax = "55020357" + pad(len(fee)) + fee  # For percentage tax
elif taxtype == 'r':
    tax = "55020256" + pad(len(fee)) + fee  # For Rupiah tax

if len(tax) == 0:
    uang += "5802ID"
else:
    uang += tax + "5802ID"

# Create the dynamic QRIS data
output = pecah_qris[0].strip() + uang + pecah_qris[1].strip()
output += to_crc16(output)

# Output the final QRIS data
print("Generated QRIS Data:", output)

# Generate and save the QR code as an image
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

qr_img = qrcode.make(output)
qr_img.save(os.path.join(output_dir, 'qr_output.png'))

print("QR Code generated successfully and saved to output/qr_output.png")
