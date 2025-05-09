import asyncio
from pymodbus.client.asyncio import ModbusTcpClient

# Define the server address and port
server_address = "127.0.0.1"
port = 1502

async def run_async_client():
    """Async version of the Modbus client."""
    client = ModbusTcpClient(server_address, port=port)

    # Connect to the server
    connection = await client.connect()
    if connection:
        print(f"Connected to Modbus server at {server_address}:{port}")

        # Example: Read coils (binary outputs) starting from address 0
        result = await client.read_coils(0, 3)  # Address 0, 3 coils
        if result.isError():
            print(f"Error reading coils: {result}")
        else:
            print(f"Coils status: {result.bits}")

        # Example: Write a coil (set it to True/On) at address 0
        write_result = await client.write_coil(0, True)
        if write_result.isError():
            print(f"Error writing coil: {write_result}")
        else:
            print(f"Successfully wrote coil at address 0")

        # Example: Read holding registers starting from address 0
        result = await client.read_holding_registers(0, 2)  # Address 0, 2 registers
        if result.isError():
            print(f"Error reading registers: {result}")
        else:
            print(f"Holding registers: {result.registers}")

        # Close the connection
        await client.close()
    else:
        print(f"Failed to connect to {server_address}:{port}")

# Run the async client
asyncio.run(run_async_client())
