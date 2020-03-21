__all__ = ["{{ cookiecutter.class_name }}"]

import asyncio
from typing import Dict, Any, List

from yaqd_core import {{ cookiecutter.base_class }}, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class {{ cookiecutter.class_name }}({{ cookiecutter.base_class }}):
    _kind = "{{ cookiecutter.first_daemon_kind }}"
    traits: List[str] = []
    defaults: Dict[str, Any] = {}

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        # Perform any unique initialization
{% if cookiecutter.base_class == "Sensor" %}
        self.channel_names = ["channel"]
        self.channel_units = {"channel": "units"}
{% endif %}

    def _load_state(self, state):
        """Load an initial state from a dictionary (typically read from the state.toml file).

        Must be tolerant of missing fields, including entirely empty initial states.

        Parameters
        ----------
        state: dict
            The saved state to load.
        """
        super()._load_state(state)
        # This is an example to show the symetry between load and get
        # If no persistent state is needed, these unctions can be deleted
        self.value = state.get("value", 0)

    def get_state(self):
        state = super().get_state()
        state["value"] = self.value
        return state

{% if cookiecutter.base_class == "DiscreteHardware" %}
    def get_value(self):
        return self.value

    def set_value(self, value):
        ...
{% endif %}
{% if cookiecutter.base_class == "Sensor" %}
    async def _measure(self):
        return {"channel": 0}
{% endif %}
{% if "Hardware" in cookiecutter.base_class %}
    def _set_position(self, position):
        ...
{% endif %}

    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        # If there is no state to monitor continuously, delete this function
        while True:
            # Perform any updates to internal state
            self._busy = False
            # There must be at least one `await` in this loop
            # This one waits for something to trigger the "busy" state
            # (Setting `self._busy = True)
            # Otherwise, you can simply `await asyncio.sleep(0.01)`
            await self._busy_sig.wait()
