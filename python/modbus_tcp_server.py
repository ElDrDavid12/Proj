import logging
import sys
from pymodbus.client import ModbusSerialClient
from pymodbus.server.async import StartTcpServer  # Use 'async' instead of 'sync'
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.exceptions import ModbusException
import threading

# Set up logging
logging.basicConfig(level=logging.INFO)

# ==========================
# Modbus RTU Client Setup
# ==========================
def modbus_rtu_client():
    # Create Modbus RTU client
    client = ModbusSerialClient(
        method='rtu',
        port='/dev/ttyUSB0',  # Update with your serial port
        baudrate=9600,
        timeout=3,
        parity='N',  # None (N), Even (E), Odd (O)
        stopbits=1,
        bytesize=8
    )

    # Connect to the Modbus RTU server
    if client.connect():
        print("Modbus RTU client connected successfully!")
    else:
        print("Failed to connect to Modbus RTU server!")
        sys.exit()

    try:
        # Read Holding Registers (example: address 100, count 2)
        response = client.read_holding_registers(address=100, count=2, slave=1)
        if response.isError():
            print(f"Error reading registers: {response}")
        else:
            print(f"Registers: {response.registers}")
            
            # Decode data if necessary (example: 32-bit float)
            decoder = BinaryPayloadDecoder.fromRegisters(
                response.registers,
                byteorder=Endian.Big,
                wordorder=Endian.Big
            )
            decoded_value = decoder.decode_32bit_float()
            print(f"Decoded value: {decoded_value}")

    except ModbusException as e:
        print(f"Modbus error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Write to Holding Registers (example: address 200)
    try:
        builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
        builder.add_32bit_float(123.45)  # Example value to write
        payload = builder.to_registers()
        response = client.write_registers(address=200, values=payload, slave=1)
        
        if response.isError():
            print(f"Error writing registers: {response}")
        else:
            print("Write successful!")

    except ModbusException as e:
        print(f"Modbus error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Close the connection
    client.close()


# ==========================
# Modbus TCP Server Setup
# ==========================
def modbus_tcp_server():
    # Define Modbus datastore and slave context
    slave_context = ModbusSlaveContext(
        hr={100: 10, 200: 1234},  # Holding register values, for example
        di={},                    # Digital inputs (if needed)
        co={},                    # Coils (if needed)
        ir={}                     # Input registers (if needed)
    )
    context = ModbusServerContext(slaves={1: slave_context}, single=True)

    # Start the Modbus TCP server
    print("Starting Modbus TCP server...")
    StartTcpServer(context, address=("0.0.0.0", 5020))


# ==========================
# Main Function to Run Both
# ==========================
if __name__ == '__main__':
    # First start the Modbus TCP server (in a separate process or thread)
    server_thread = threading.Thread(target=modbus_tcp_server)
    server_thread.start()

    # Now start the Modbus RTU client to communicate with the server
    modbus_rtu_client()
