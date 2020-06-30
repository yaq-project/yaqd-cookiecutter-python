__all__ = ["{{ cookiecutter.class_name }}"]

import asyncio
from typing import Dict, Any, List

from yaqd_core import {{ cookiecutter.base_class }}


class {{ cookiecutter.class_name }}({{ cookiecutter.base_class }}):
    _kind = "{{ cookiecutter.first_daemon_kind }}"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        # Perform any unique initialization
{% if cookiecutter.base_class == "Sensor" %}
        self._channel_names = ["channel"]
        self._channel_units = {"channel": "units"}

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
