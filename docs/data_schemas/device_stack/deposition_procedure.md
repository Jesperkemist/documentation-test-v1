??? "deposition_procedure"
    The deposition procedure for the layer. The deposition of a layer could involve several deposition steps, or segments. 

    ## Top level
    ??? "substrate_layer"
        The layer on which the layer is deposited.
        The layer are ordered from bottom (furthest from the sun) to top (closest to the sun).
        Indicate if the layer was deposited on a layer that is below or above it in the device 
        (when the device is oriented with the top towards the sun)
        There are a few exceptions in that a layer can be a substrate, 
        it could be a layer that laminates two subcells, 
        and it could be a layer that is not deposited at all (like an air gap) 

        * type: str
        * options:
            * is_substrate
            * on_lower_layer
            * on_upper_layer
            * laminate_layers
            * not-deposited    

    ??? "origin"
        The place where the layer was deposited. i.e. was it deposited in the lab or was it bought. An example of a layer that often is bought is the ITO layer on glass substrates

        * type: str
        * options:
            * commercial_supplier
            * deposited_in_house
            * deposited_by_collaborator

    ??? "duration"
        The time it takes to deposit the layer from start to finish.

        * type: float
        * unit: minute
        * example: 15

    ??? "time_from_last_step"
        The time from the finalization of the last layer 
        and the start of the deposition of this.

        * type: float
        * unit: h
        * example: 0.5

    ??? "time_stamp"
        Date and time of the procedure

        * type: datetime
        * example: 2020-07-08

    ## Subsections
    ??? "segments"
        List of all deposition segments that is used to deposit the layer. 
        This will probably never be a compleat list of possible deposition procedures. However, using the methods described here as templates, it is possible define data schemas for new procedures. 

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
                * UVOzonTreatment
                * ...

        ???+ "Procedure dependent key-value pairs and subsections"
            ...

            ???+ warning "Note on nesting"
                In the NOMAD implementation, choosing a method dynamically modifies the data fields displayed, to capture that different procedures require rather different descriptions. 
                In this documentation, description for different deposition procedures are found under the headline "experimental_procedures" in the menu to the left. <br/>
                However, in the generated datafiles, those sections should be nested here.


    ??? "sample_history"
        A description of the conditions under which the sample have been stored between the finalization of the last segment and this segment

        {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}




