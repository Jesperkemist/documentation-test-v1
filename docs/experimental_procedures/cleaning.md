
### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: minute
    * example: 60

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

??? "free_text_comment"
    Any additional description not captured by any other field.

    * type: str
    * example: "An elaborate cleaning protocol" 

### Subsections
??? "solution"
    Details about the solution.
    {% include "experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}      