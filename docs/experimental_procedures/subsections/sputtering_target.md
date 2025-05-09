#### Top level
??? "name"
    The common trade name of the substance.

    * type: str
    * examples: 
        * Au 
        * Ag 
        * ITO
        * NiO 

??? "substrate_distance"
    The distance between the substrate and the sputtering target

    * type: float
    * unit: cm
    * example: 15

??? "origin"
    The origin of the compound

    * type: str
    * options: 
        * commercial_supplier 
        * made_in_house 
        * made_by_collaborator
        * other        

#### Subsections
??? "identity"
    {% include "device_stack/subsections/compound_identity.md" %}

??? "supplier"
    {% include "device_stack/subsections/compound_supplier.md" %}

