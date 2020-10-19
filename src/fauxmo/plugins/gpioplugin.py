"""gpioplugin.py :: Fauxmo plugin for gpio output.

Fauxmo plugin that makes simple gpio call in its `on` and `off` methods.
Comes pre-installed in Fauxmo as an example for user plugins.
"""
from fauxmo import logger
from fauxmo.plugins import FauxmoPlugin
import RPi.GPIO as GPIO

class GpioPlugin(FauxmoPlugin):

    def __init__(
        self,
        name: str,
        port: int,
        pin:int
    ) -> None:
        """Initialize a CommandLinePlugin instance.

        Args:
            name: Name for this Fauxmo device
            port: Port on which to run a specific CommandLinePlugin instance

        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        super().__init__(name=name, port=port)

    def on(self) -> bool:
        """Run on command.

        Returns:
            True if command seems to have run without error.

        """
        GPIO.output(self.pin, 0)
        return True

    def off(self) -> bool:
        """Run off command.

        Returns:
            True if command seems to have run without error.

        """
        GPIO.output(self.pin, 1)
        return True

    def get_state(self) -> str:
        """Get device state.

        NB: Return code of `0` (i.e. ran without error) indicates "on" state,
        otherwise will be off. making it easier to have something like `ls
        path/to/pidfile` suggest `on`. Many command line switches may not
        actually have a "state" per se (just an arbitary command you want to
        run), in which case you could just put "false" as the command, which
        should always return "off".

        Returns:
            "on" or "off"

        """

        state = GPIO.input(self.pin)
        if state == 0:
            return "on"
        else:
            return "off"
