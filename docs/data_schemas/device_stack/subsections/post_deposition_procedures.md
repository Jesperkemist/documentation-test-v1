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
                * AtomicLayerDeposition
                * ChemicalBathDeposition
                * ChemicalVapourDeposition
                * Cleaning
                * DipCoating
                * DoctorBlading
                * Evaporation
                * Heating
                * InkjetPrinting
                * IonExchangeByDipping
                * IonExchangeByGasDiffusion
                * OzonTreatment
                * SlotDyeCoating
                * SpinCoating
                * SprayCoating
                * Sputtering
                * Storage
                * UVOzonTreatment
                * ...

        ???+ "Procedure dependent key-value pairs and subsections"
            ...

            ???+ warning "Note on nesting"
                In the NOMAD implementation, choosing a method dynamically modifies the data fields displayed, to capture that different procedures require rather different descriptions. 
                In this documentation, description for different deposition procedures are found under the headline "experimental_procedures" in the menu to the left. <br/>
                However, in the generated datafiles, those sections should be nested here.

    ??? "sample_history"
        A description of the conditions under which the sample have been stored between
        the finalization of the last layer and the deposition of this layer

        {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}    