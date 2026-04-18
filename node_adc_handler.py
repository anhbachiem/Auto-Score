class MCP3204Handler:
    def __init__(self, spi, chip_select_pin):
        self.spi = spi
        self.chip_select_pin = chip_select_pin
        self.channels = 4

    def read_channel(self, channel):
        if channel < 0 or channel >= self.channels:
            raise ValueError("Channel must be between 0 and 3.")
        # Activate chip select
        self.chip_select_pin.low()
        # Send the start bit and channel number
        command = 0b11000000 | (channel << 2)
        self.spi.writebyte(command)
        # Read the data
        data = self.spi.readbytes(2)
        # Deactivate chip select
        self.chip_select_pin.high()
        # Convert to voltage (assuming 3.3V reference)
        value = ((data[0] & 0x0F) << 8) | data[1]
        return value * (3.3 / 4095)  # Normalize to voltage

    def read_all_channels(self):
        return [self.read_channel(i) for i in range(self.channels)]

    def read_multiple_samples(self, channel, num_samples):
        if channel < 0 or channel >= self.channels:
            raise ValueError("Channel must be between 0 and 3.")
        samples = [self.read_channel(channel) for _ in range(num_samples)]
        return samples
