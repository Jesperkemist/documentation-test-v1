### Numerical quantities
??? "time_in_solution"
    The total time of all the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "sample_temperature"
    The temperature of the sample during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "solution_temperature"
    The temperature of the solution during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "number_of_repetitions"
    The number of repetitions (dippings).

    * type: int
    * example: 5

??? "time_between_repetitions"
    The time between the repetitions. 

    * type: float
    * unit: minute
    * example: 4

### Categorical quantities
??? "drying_procedure"
    The method by which the liquid is removed from the sample after dipping.

    * type: str
    * options:
        * gas_blowing
        * self_drying
        * heating
        * tissue_paper
        * none
        * other

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "solution"
    Details about the solution.
    {% include "data_schemas/experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}      