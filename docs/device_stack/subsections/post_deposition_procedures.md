??? "post_deposition_procedure"
    Post deposition procedure. This refer to any operation done on the sample after a layer have been completely formed, but before the deposition of the next. 

    ### Top level sections
    ??? "duration"
        The time it takes to deposit the layer from start to finish.

        * type: float
        * unit: minute
        * example: 15

    ??? "time_from_last_step"
        The time from the finalization of the last layer 
        and the start of this process.

        * type: float
        * unit: h
        * example: 0.5

    ??? "time_stamp"
        Date and time of the procedure

        * type: datetime
        * example: 2020-07-08
    
    ### Subsections
    ??? "segments"
        The segments of the procedure.

        ??? "method"
            The type of process

            * type: str
            * options:
                * atomic_layer_deposition
                * chemical_bath_deposition
                * chemical_vapour_deposition
                * dip_coating
                * doctor_blading
                * evaporation
                * heating
                * inkjet_printing
                * ion_exchange_by_dipping
                * ion_exchange_by_gas_diffusion
                * ozon_treatment
                * slot_dye_coating
                * spin_coating
                * spray_coating
                * sputtering
                * storage
                * uv_ozon_treatment
                * other

            ???+ warning "Note on nesting"
                In the NOMAD implementation, the choice of method dynamically modify the data fields displayed. This is because different procedures require rather different descriptions. <br/>
                In this documentation, description for different procedures are found under the top level headline "experimental_procedures". <br/>
                In the generated datafiles, those sections should, however, be nested here.

    ??? "sample_history"
        A description of the conditions under which the sample have been stored between
        the finalization of the last layer and the deposition of this layer

        {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}    