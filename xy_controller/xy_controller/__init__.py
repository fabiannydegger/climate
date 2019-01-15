class xy(object):
    """A XY controller.
    output = (out_max-out_min/in_max-in_min) * out_max + out_min

    Args:
        in_min (float): Lower output limit of x.
        in_max (float): Upper output limit of x.
        out_min (float): Lower output limit of y.
        out_max (float): Upper output limit of y.
        negate (bool): 0 = heater, 1 = cooler. (default=0)
        input_val (float): Sensor Value.
    """

    def __init__(self, in_min=float('-inf'), in_max=float('inf'),
            out_min=float('-inf'), out_max=float('inf'), type):
        if negate is None:
            negate = 0
        if in_min >= in_max:
            raise ValueError('in_min must be less than in_max')
        if out_min >= out_max:
            raise ValueError('out_min must be less than out_max')
        self._negate = negate
        self._in_min = in_min
        self._in_max = in_max
        self._out_min = out_min
        self._out_max = out_max

    def calc(self, input_val):
        """Adjusts the given setpoint.

        Args:
            input_val (float): The input value.

        Returns:
            Setpoint for further use.
        """

        if input_val < self._in_min:
            input_val = self._in_min
        elif input_val > self._in_max:
            input_val = self._in_max
        if self._negate == 0:
            m = -1
        else:
            m = 1
        x = self._in_max - self._in_min
        y = self._out_max - self._out_min

        setpoint = m * y/x * input_val + self._out_min

        return setpoint
