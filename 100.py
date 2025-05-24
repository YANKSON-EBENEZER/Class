import os
import platform
import subprocess

def get_gpu_name():
    """
    Retrieve the name of the GPU using the WMIC command on Windows.
    """
    try:
        result = subprocess.run(
            ["wmic", "path", "win32_videocontroller", "get", "name"],
            capture_output=True,
            text=True,
            check=True
        )

        lines = [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]
        if len(lines) > 1:
            return lines[1]  # The second line should contain the GPU name
        else:
            return "No GPU detected"
    except Exception as e:
        return f"Error detecting GPU: {str(e)}"

def get_system_specs():
    """
    Automatically retrieve the user's hardware specifications.
    """
    # Get CPU name
    cpu = platform.processor()

    # Get total RAM in GB
    ram = round(int(os.environ.get('NUMBER_OF_PROCESSORS', 0)) * 4)  # Approximation for Windows

    # Get GPU name
    gpu = get_gpu_name()

    return {"cpu": cpu, "ram": ram, "gpu": gpu}

def check_compatibility(game, user_hardware):
    """
    Check if the user's hardware meets the requirements for the specified game.
    """
    # Example game requirements (you can expand this dictionary)
    game_requirements = {
        "game1": {"cpu": "Intel Core i5", "ram": 8, "gpu": "NVIDIA GTX 1050"},
        "game2": {"cpu": "Intel Core i7", "ram": 16, "gpu": "NVIDIA GTX 1660"},
    }

    # Check if the game exists in the requirements dictionary
    if game.lower() in game_requirements:
        requirements = game_requirements[game.lower()]
        print(f"\nRequirements for {game}:")
        print(f"CPU: {requirements['cpu']}")
        print(f"RAM: {requirements['ram']} GB")
        print(f"GPU: {requirements['gpu']}")

        # Compare user hardware with game requirements
        compatible = True
        if user_hardware["ram"] < requirements["ram"]:
            print("Your RAM does not meet the requirements.")
            compatible = False
        if user_hardware["gpu"].lower() != requirements["gpu"].lower():
            print("Your GPU does not meet the requirements.")
            compatible = False
        if compatible:
            print("Your system is compatible with this game!")
        else:
            print("Your system is not compatible with this game.")
    else:
        print(f"Game '{game}' not found in the database.")

if __name__ == "__main__":
    # Automatically detect user hardware specs
    user_hardware = get_system_specs()

    print("Detected hardware specs:")
    for key, value in user_hardware.items():
        print(f"{key.upper()}: {value}")

    print("\nEnter the name of the game you want to check compatibility for:")
    game = input().strip()
    check_compatibility(game, user_hardware)