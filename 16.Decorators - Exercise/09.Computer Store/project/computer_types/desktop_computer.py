from math import log2

from project.computer_types.computer import Computer



class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                            "Intel Core i5-12600K": 600,
                            "Apple M1 Max": 1800}

    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        elif not log2(ram).is_integer() or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        super().configure_computer(processor, ram)
        self.price += self.AVAILABLE_PROCESSORS[processor]
        self.price += int(log2(ram)) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
