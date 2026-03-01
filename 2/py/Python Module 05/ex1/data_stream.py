#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.
    """

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data and return a summary string.
        """
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Default filtering behavior (returns all if no criteria).
        Can be overridden by subclasses.
        """
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Return basic stream statistics.
        """
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    """
    Specialized stream for environmental sensor data.
    Expected formats like: "temp:22.5", "humidity:65"
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_readings: List[str] = [
                item for item in data_batch if isinstance(item, str) and ":" in item
            ]

            temps: List[float] = [
                float(item.split(":")[1])
                for item in valid_readings
                if item.startswith("temp:")
            ]

            self.processed_count += len(valid_readings)

            avg_temp: float = sum(temps) / len(temps) if temps else 0.0

            return (
                f"Sensor analysis: {len(valid_readings)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception as error:
            return f"Sensor stream error: {error}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            return [
                item
                for item in data_batch
                if isinstance(item, str)
                and item.startswith("temp:")
                and float(item.split(":")[1]) > 30
            ]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """
    Specialized stream for financial transaction data.
    Expected formats like: "buy:100", "sell:150"
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            operations: List[str] = [
                item for item in data_batch if isinstance(item, str) and ":" in item
            ]

            net_flow: int = 0
            for op in operations:
                action, value = op.split(":")
                amount: int = int(value)
                if action == "buy":
                    net_flow -= amount
                elif action == "sell":
                    net_flow += amount

            self.processed_count += len(operations)

            return (
                f"Transaction analysis: {len(operations)} operations, "
                f"net flow: {net_flow:+d} units"
            )
        except Exception as error:
            return f"Transaction stream error: {error}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item
                for item in data_batch
                if isinstance(item, str)
                and ":" in item
                and int(item.split(":")[1]) > 100
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    """
    Specialized stream for system events.
    Example events: "login", "error", "logout"
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events: List[str] = [
                item for item in data_batch if isinstance(item, str)
            ]

            error_count: int = len(
                [event for event in events if event.lower() == "error"]
            )

            self.processed_count += len(events)

            return (
                f"Event analysis: {len(events)} events, "
                f"{error_count} error detected"
            )
        except Exception as error:
            return f"Event stream error: {error}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                item
                for item in data_batch
                if isinstance(item, str) and item.lower() == "error"
            ]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    """
    Manager class that handles multiple stream types polymorphically.
    """

    def process_streams(
        self, streams: List[DataStream], batches: List[List[Any]]
    ) -> None:
        for stream, batch in zip(streams, batches):
            print(stream.process_batch(batch))


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))

    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    print(transaction.process_batch(["buy:100", "sell:150", "buy:75"]))

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(event.process_batch(["login", "error", "logout"]))

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()

    streams: List[DataStream] = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002"),
    ]

    batches: List[List[Any]] = [
        ["temp:35", "temp:28"],
        ["buy:200", "sell:50", "sell:75", "buy:25"],
        ["login", "error", "logout"],
    ]

    processor.process_streams(streams, batches)

    print("Stream filtering active: High-priority data only")

    filtered_sensor = streams[0].filter_data(batches[0], "high")
    filtered_transaction = streams[1].filter_data(batches[1], "large")
    filtered_event = streams[2].filter_data(batches[2], "critical")

    print(f"Filtered results: {len(filtered_sensor)} critical sensor alerts, "
          f"{len(filtered_transaction)} large transactions")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()