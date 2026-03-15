```json
{
    "memory/long_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from giskard import LangGraph

class NonStationaryDriftIndex(BaseModel):
    """Non-stationary drift index model"""
    drift_index: float
    stochastic_regime_switch: bool

class LongTermMemory:
    """Long-term memory management system"""
    def __init__(self, non_stationary_drift_index: NonStationaryDriftIndex):
        """
        Initialize long-term memory management system

        Args:
        - non_stationary_drift_index (NonStationaryDriftIndex): Non-stationary drift index model
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.lang_graph = LangGraph()

    def update_memory(self, new_data: List[Dict]) -> None:
        """
        Update long-term memory with new data

        Args:
        - new_data (List[Dict]): New data to update memory with

        Raises:
        - Exception: If update fails
        """
        try:
            logging.info('Updating long-term memory')
            self.lang_graph.update_state_graph(new_data)
            logging.info('Update successful')
        except Exception as e:
            logging.error(f'Update failed: {e}')
            raise

    def retrieve_memory(self, query: str) -> List[Dict]:
        """
        Retrieve long-term memory based on query

        Args:
        - query (str): Query to retrieve memory with

        Returns:
        - List[Dict]: Retrieved memory
        """
        try:
            logging.info(f'Retrieving long-term memory for query: {query}')
            retrieved_memory = self.lang_graph.query_state_graph(query)
            logging.info('Retrieval successful')
            return retrieved_memory
        except Exception as e:
            logging.error(f'Retrieval failed: {e}')
            return []

def simulate_rocket_science() -> None:
    """
    Simulate rocket science problem
    """
    non_stationary_drift_index = NonStationaryDriftIndex(drift_index=0.5, stochastic_regime_switch=True)
    long_term_memory = LongTermMemory(non_stationary_drift_index)
    new_data = [{'id': 1, 'data': 'rocket science data'}]
    long_term_memory.update_memory(new_data)
    retrieved_memory = long_term_memory.retrieve_memory('rocket science')
    print(retrieved_memory)

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized long_term_memory logic"
    }
}
```