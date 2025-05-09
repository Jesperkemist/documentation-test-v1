### Numerical quantities
??? "time_in_solution"
    The total time of all the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "substrate_temperature"
    The temperature of the substrate during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "solution_temperature"
    The temperature of the solution during the activity. 

    * type: float
    * unit: C
    * example: 35

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
    {% include "experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}      