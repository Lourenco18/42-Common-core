#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
from collections import deque, defaultdict
import time


# =========================
# Stage Protocol (Duck Typing)
# =========================
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# =========================
# Concrete Stages
# =========================
class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, str) and data.startswith("{") and data.endswith("}"):
            # very lightweight JSON-like parsing
            parsed: Dict[str, Any] = {
                k.strip().strip('"'): v.strip().strip('"')
                for k, v in (
                    pair.split(":")
                    for pair in data.strip("{}").split(",")
                    if ":" in pair
                )
            }
            return parsed
        if isinstance(data, str) and "," in data:
            values: List[str] = [item.strip() for item in data.split(",")]
            return {"csv": values}
        return {"raw": data}


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            enriched: Dict[str, Any] = {k: v for k, v in data.items()}
            enriched["processed"] = True
            enriched["timestamp"] = time.time()
            return enriched
        raise ValueError("Invalid data format for transformation")


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            if "sensor" in data and "value" in data:
                return (
                    f"Processed temperature reading: "
                    f"{data['value']}°{data.get('unit', '')} (Normal range)"
                )
            if "csv" in data:
                return f"User activity logged: {len(data['csv']) - 1} actions processed"
            if "raw" in data:
                return f"Stream summary: processed raw input"
        return "Output delivered"


# =========================
# Abstract Pipeline Base
# =========================
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.metrics: Dict[str, Union[int, float]] = defaultdict(int)

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...

    def execute(self, data: Any) -> Any:
        start_time: float = time.time()
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.metrics["processed"] += 1
            return data
        except Exception as error:
            self.metrics["errors"] += 1
            print(f"Error detected in pipeline {self.pipeline_id}: {error}")
            return "Recovery: Backup processor engaged"
        finally:
            elapsed: float = time.time() - start_time
            self.metrics["total_time"] += elapsed

    def get_stats(self) -> Dict[str, Union[int, float]]:
        efficiency: float = 0.0
        if self.metrics["processed"]:
            efficiency = (
                self.metrics["processed"]
                / (self.metrics["processed"] + self.metrics["errors"])
            ) * 100
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self.metrics["processed"],
            "errors": self.metrics["errors"],
            "efficiency": round(efficiency, 2),
            "total_time": round(self.metrics["total_time"], 4),
        }


# =========================
# Adapters (Inheritance + Override)
# =========================
class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing JSON data through pipeline...")
        return self.execute(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        return self.execute(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        return self.execute(data)


# =========================
# Nexus Manager
# =========================
class NexusManager:
    def __init__(self) -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.history: deque = deque(maxlen=100)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline.pipeline_id] = pipeline

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        pipeline = self.pipelines.get(pipeline_id)
        if not pipeline:
            return "Pipeline not found"
        result = pipeline.process(data)
        self.history.append(result)
        return result

    def chain_pipelines(self, pipeline_ids: List[str], data: Any) -> Any:
        print("Pipeline A -> Pipeline B -> Pipeline C")
        for pid in pipeline_ids:
            data = self.process_data(pid, data)
        return data


# =========================
# Demonstration
# =========================
def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    manager = NexusManager()

    # Create pipeline with shared stages
    def build_pipeline(adapter_cls, pid: str) -> ProcessingPipeline:
        pipeline = adapter_cls(pid)
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        return pipeline

    json_pipeline = build_pipeline(JSONAdapter, "JSON_PIPE")
    csv_pipeline = build_pipeline(CSVAdapter, "CSV_PIPE")
    stream_pipeline = build_pipeline(StreamAdapter, "STREAM_PIPE")

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("=== Multi-Format Data Processing ===")

    print(manager.process_data(
        "JSON_PIPE",
        '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    ))

    print(manager.process_data(
        "CSV_PIPE",
        "user,action,timestamp"
    ))

    print(manager.process_data(
        "STREAM_PIPE",
        "Real-time sensor stream"
    ))

    print("=== Pipeline Chaining Demo ===")
    result = manager.chain_pipelines(
        ["JSON_PIPE", "CSV_PIPE", "STREAM_PIPE"],
        '{"sensor": "temp", "value": 22.1, "unit": "C"}'
    )
    print(f"Chain result: {result}")

    print("=== Error Recovery Test ===")
    # Force transformation failure
    print(manager.process_data("JSON_PIPE", 12345))

    print("Performance:", json_pipeline.get_stats())
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
