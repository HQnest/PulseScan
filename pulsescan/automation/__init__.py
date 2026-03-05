"""
Workflow automation module for building diagnostic pipelines.
"""

from typing import Dict, Any, Callable, List
import time


class DiagnosticWorkflow:
    """
    Framework for creating and executing automated diagnostic workflows.
    """

    def __init__(self):
        self.steps: Dict[str, Callable] = {}
        self.results: Dict[str, Any] = {}

    def add_step(self, name: str, function: Callable) -> None:
        """
        Add a step to the workflow.

        Args:
            name: Unique name for the step
            function: Callable to execute for this step
        """
        self.steps[name] = function

    def run(self) -> Dict[str, Any]:
        """
        Execute all workflow steps in order.

        Returns:
            Dictionary of results from each step
        """
        self.results = {}
        for name, func in self.steps.items():
            try:
                start_time = time.time()
                result = func()
                end_time = time.time()
                self.results[name] = {
                    "result": result,
                    "duration": end_time - start_time,
                    "status": "success"
                }
            except Exception as e:
                self.results[name] = {
                    "result": None,
                    "duration": 0,
                    "status": "error",
                    "error": str(e)
                }
        return self.results

    def get_step_result(self, name: str) -> Any:
        """
        Get the result of a specific step.

        Args:
            name: Step name

        Returns:
            Result of the step or None if not found
        """
        return self.results.get(name, {}).get("result")

    def get_failed_steps(self) -> List[str]:
        """
        Get list of steps that failed during execution.

        Returns:
            List of failed step names
        """
        return [name for name, data in self.results.items() if data["status"] == "error"]