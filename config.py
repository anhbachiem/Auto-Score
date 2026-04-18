# ===== CONFIGURATION FILE FOR AUTO-SCORE SYSTEM =====

# ===== COMMON CONFIGURATION =====
BAUD_RATE = 9600
UART_TIMEOUT = 5

# ===== NODE CONFIGURATION =====
NODE_IDS = {
    1: "NODE_1",
    2: "NODE_2",
    3: "NODE_3",
    4: "NODE_4",
    5: "NODE_5",
}

# GPIO Pins for Node (RPI Nano 2W)
NODE_GPIO_ENABLE = 20  # GPIO pin to enable/disable target

# MCP3204 Configuration
MCP3204_CS = 8      # Chip Select pin
MCP3204_CLK = 11    # Clock pin
MCP3204_MOSI = 10   # Master Out Slave In
MCP3204_MISO = 9    # Master In Slave Out

# ADC Channel mapping (Piezoelectric sensors)
ADC_CHANNELS = {
    'A': 0,  # Bottom-left (-50, -50)
    'B': 1,  # Top-left (-50, 50)
    'C': 2,  # Top-right (50, 50)
    'D': 3,  # Bottom-right (50, -50)
}

# Sensor positions (in cm, centered at 0:0)
SENSOR_POSITIONS = {
    'A': (-50, -50),   # Bottom-left
    'B': (-50, 50),    # Top-left
    'C': (50, 50),     # Top-right
    'D': (50, -50),    # Bottom-right
}

# ===== CONTROLLER CONFIGURATION (RPI 5) =====
CONTROLLER_GPIO_PINS = {
    'NODE_1': 2,
    'NODE_2': 3,
    'NODE_3': 4,
    'NODE_4': 5,
    'NODE_5': 6,
    'NODE_ALL': 7,
    'CLEAR_SCREEN': 8,
}

# Scoring configuration
SCORING_RINGS = {
    10: 3.25,    # 10 points: radius <= 3.25 cm
    9: 10.75,    # 9 points: radius <= 10.75 cm
    8: 18.25,    # 8 points: radius <= 18.25 cm
    7: 25.75,    # 7 points: radius <= 25.75 cm
    6: 33.25,    # 6 points: radius <= 33.25 cm
    5: 40.75,    # 5 points: radius <= 40.75 cm
    4: 48.25,    # 4 points: radius <= 48.25 cm
    3: 50.0,     # 3 points: radius <= 50.0 cm (edge of target)
    0: float('inf'),  # 0 points: beyond target
}

# Timeout for each round
ROUND_TIMEOUT = 60  # 60 seconds

# Number of shots per round
SHOTS_PER_ROUND = 3

# ===== LORA CONFIGURATION =====
LORA_FREQUENCY = 915000000  # 915 MHz (adjust based on your region)
LORA_BANDWIDTH = 125000     # 125 kHz
LORA_SPREADING_FACTOR = 7
LORA_CODING_RATE = 5
LORA_POWER = 20

# ===== UART CONFIGURATION FOR LORA =====
# Node: UART 1 for LoRa
# Controller: UART 1 for LoRa
LORA_UART_PORT_RPI = '/dev/ttyAMA1'    # RPI 5 UART 1
LORA_UART_PORT_NANO = 1                # RPI Nano 2W UART 1
