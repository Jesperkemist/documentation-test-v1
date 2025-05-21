#### Solution top level
??? "preparation_date"
    Date of preparation of the solution.

    * type: Datetime
    * example: 2025-01-15

??? "age"
    The time between preparation and the use of the solution.

    * type: float
    * unit: h
    * example: 24

??? "volume"
    The volume of the solution used.

    * type: float
    * unit: ml
    * example: 0.5   

??? "density"
    The density of the solution.

    * type: float
    * unit: g/ml
    * example: 1.05  

??? "viscosity"
    The viscosity of the solution.

    * type: float
    * unit: Pa*s
    * example: 1.5       

??? "temperature"
    The temperature of the solution.

    * type: float
    * unit: C
    * example: 25 

??? "temperature_max"
    The maximum temperature the solution has experienced.

    * type: float
    * unit: C
    * example: 85 

??? "colour"
    The colour of the solution.

    * type: str
    * example: yellow 

??? "stirred"
    True if the solution is stirred before use.

    * type: boolean
    * options: TRUE, FALSE 

??? "filtered"
    TRUE if the if the solution is filtered before use.

    * type: boolean
    * options: TRUE, FALSE 

??? "filter_pour_size"
    TRUE if the if the solution is filtered before use.

    * type: float
    * unit: µm
    * example: 100 

#### Solution subsections
??? "components"
    A repeating section detailing the substances in the solution.
    {% include "data_schemas/experimental_procedures/subsections/solution_component.md" %} 

??? "environmental_conditions_during_preparation"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %} 