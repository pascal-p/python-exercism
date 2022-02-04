""" Meltdown Mitigation exercise """

from typing import Union, Literal

IntOrFloat = Union[int, float]
Efficiency = Literal['green', 'orange', 'red', 'black']
Safety = Literal['LOW', 'NORMAL', 'DANGER']

TEMP_LIM = 800
NEU_EMIT_LIM = 500
TEMP_NEU_EMIT_LIM = 500_000


def is_criticality_balanced(temperature: IntOrFloat, neutrons_emitted: IntOrFloat) -> bool:
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return temperature < TEMP_LIM and neutrons_emitted > NEU_EMIT_LIM \
        and temperature * neutrons_emitted < TEMP_NEU_EMIT_LIM


def reactor_efficiency(voltage: IntOrFloat, current: IntOrFloat,
                       theoretical_max_power: IntOrFloat) -> Efficiency:
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    value = (voltage * current / theoretical_max_power) * 100.
    if value < 30.:
        return 'black'
    elif value < 60.:
        return 'red'
    elif value < 80.:
        return 'orange'
    else:
        return 'green'


def fail_safe(temperature: IntOrFloat,
              neutrons_produced_per_second: IntOrFloat,
              threshold: IntOrFloat) -> Safety:
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges == 'DANGER'
    """

    value = temperature * neutrons_produced_per_second
    if value < 0.9 * threshold:
        return 'LOW'
    elif value < 1.1 * threshold:  # value >= 0.9 * threshold
        return 'NORMAL'
    else:
        return 'DANGER'
