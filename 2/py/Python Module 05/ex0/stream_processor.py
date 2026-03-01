#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """
    Abstract base class defining the common processing interface.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a result string.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Default output formatting. Can be overridden by subclasses.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor specialized for numeric list data.
    """

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data.")

            numbers: List[Union[int, float]] = data
            total: float = float(sum(numbers))
            count: int = len(numbers)
            average: float = total / count if count > 0 else 0.0

            return f"Processed {count} numeric values, sum={int(total) if total.is_integer() else total}, avg={average}"
        except Exception as error:
            return f"Numeric processing error: {error}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        if not data:
            return False
        return all(isinstance(x, (int, float)) for x in data)


class TextProcessor(DataProcessor):
    """
    Processor specialized for text data.
    """

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data.")

            text: str = data
            char_count: int = len(text)
            word_count: int = len(text.split())

            return f"Processed text: {char_count} characters, {word_count} words"
        except Exception as error:
            return f"Text processing error: {error}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """
    Processor specialized for log entry data.
    Expected format: "LEVEL: message"
    """

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry.")

            log_entry: str = data
            level, message = log_entry.split(":", 1)
            level = level.strip().upper()
            message = message.strip()

            if level == "ERROR":
                return f"[ALERT] ERROR level detected: {message}"
            if level == "INFO":
                return f"[INFO] INFO level detected: {message}"
            return f"[{level}] {level} level detected: {message}"
        except Exception as error:
            return f"Log processing error: {error}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data

    def format_output(self, result: str) -> str:
        """
        Override default formatting to demonstrate method overriding.
        """
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    numeric_processor: DataProcessor = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print("Validation: Numeric data verified"
          if numeric_processor.validate(numeric_data)
          else "Validation failed")
    numeric_result: str = numeric_processor.process(numeric_data)
    print(numeric_processor.format_output(numeric_result))

    print("Initializing Text Processor...")
    text_processor: DataProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print("Validation: Text data verified"
          if text_processor.validate(text_data)
          else "Validation failed")
    text_result: str = text_processor.process(text_data)
    print(text_processor.format_output(text_result))

    print("Initializing Log Processor...")
    log_processor: DataProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print("Validation: Log entry verified"
          if log_processor.validate(log_data)
          else "Validation failed")
    log_result: str = log_processor.process(log_data)
    print(log_processor.format_output(log_result))

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    demo_data: List[Any] = [
        [1, 2, 3],
        "Hello Matrix",
        "INFO: System ready",
    ]

    for index, processor in enumerate(processors):
        result: str = processor.process(demo_data[index])
        print(f"Result {index + 1}: {result}")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()