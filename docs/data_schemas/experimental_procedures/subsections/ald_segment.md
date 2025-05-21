??? "time_of_segment"
    Time of the segment. 

    * type: float
    * unit: minute
    * example: 2

??? "chamber_pressure"
    The pressure in the reaction chamber 

    * type: float
    * unit: Pa
    * example: 200

??? "gases"
    Repeating section. Details about the gases in the mixture.
    {% include "data_schemas/experimental_procedures/subsections/gas_component.md" %}