```json
{
    "memory/short_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from giskard import LangGraph

class NonStationaryDriftIndex(BaseModel):
    """Non-stationary drift index model"""
    drift_index: float
    stochastic_regime_switch: bool

class ShortTermMemory:
    """Short-term memory management system"""
    def __init__(self, non_stationary_drift_index: NonStationaryDriftIndex):
        """
        Initialize short-term memory management system

        Args:
        - non_stationary_drift_index (NonStationaryDriftIndex): Non-stationary drift index model
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.lang_graph = LangGraph()

    def update_memory(self, new_data: List[Dict]) -> None:
        """
        Update short-term memory with new data

        Args:
        - new_data (List[Dict]): New data to update memory with

        Returns:
        - None
        """
        try:
            logging.info('Updating short-term memory')
            self.lang_graph.update_state_graph(new_data)
            logging.info('Short-term memory updated successfully')
        except Exception as e:
            logging.error(f'Error updating short-term memory: {e}')

    def retrieve_memory(self) -> List[Dict]:
        """
        Retrieve short-term memory

        Returns:
        - List[Dict]: Retrieved short-term memory
        """
        try:
            logging.info('Retrieving short-term memory')
            memory = self.lang_graph.get_state_graph()
            logging.info('Short-term memory retrieved successfully')
            return memory
        except Exception as e:
            logging.error(f'Error retrieving short-term memory: {e}')
            return []

def simulate_rocket_science(non_stationary_drift_index: NonStationaryDriftIndex) -> None:
    """
    Simulate rocket science problem

    Args:
    - non_stationary_drift_index (NonStationaryDriftIndex): Non-stationary drift index model

    Returns:
    - None
    """
    short_term_memory = ShortTermMemory(non_stationary_drift_index)
    new_data = [{'id': 1, 'value': 10}, {'id': 2, 'value': 20}]
    short_term_memory.update_memory(new_data)
    retrieved_memory = short_term_memory.retrieve_memory()
    logging.info(f'Retrieved memory: {retrieved_memory}')

if __name__ == '__main__':
    non_stationary_drift_index = NonStationaryDriftIndex(drift_index=0.5, stochastic_regime_switch=True)
    simulate_rocket_science(non_stationary_drift_index)
",
        "commit_message": "feat: implement specialized short_term_memory logic"
    }
}
```