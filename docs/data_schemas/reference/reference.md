# Reference data

This section provides the reference information for the source of the data. <br/>

### Primary data
Information about the origin of the data and who is providing the data. 

??? "doi"
    The DOI number of the source of the data. <br/>
    If the DOI number is provided, additional data can be 
    populated automatically. <br/>

    * type: str
    * example: "10.1016/j.solener.2020.06.034"

??? "sample_id"
    ID of the device in the original data source (for traceability)

    * type: str
    * example: "device_a"

??? "data_entered_by_author"
    TRUE if the data is formatted by the person making the device or by one of the study's co-authors   

    * type: boolean
    * options: TRUE, FALSE

??? "name_of_person_entering_the_data"
    Name of the  person providing the data. For traceability-   

    * type: str
    * example: "T. Jesper Jacobsson"

??? "free_text_comment"
    Any additional description not captured by any other field.

    * type: str
    * example: "This is the control device"

??? "part_of_initial_dataset"
    TRUE if the data is part of the first initial data hunt. <br/>
    Primary relevant during project development

    * type: boolean
    * options: TRUE, FALSE

### Derived data
Useful quantities that automatically can be derived from other data

!!! tip "Tip : The following data can be populated automatically based on the DOI number and Crossref"  

??? "publication_date"
    The publication date. <br/> Can be populated based on the DOI number

    * type: datetime
    * example: 2020-07-08

??? "journal"
    The journal where the device is described. <br/> Can be populated based on the DOI number

    * type: str
    * example: Solar Energy

??? "publication_title"
    The title of the publication. <br/> Can be populated based on the DOI number

    * type: str
    * example: 2-Terminal CIGS-perovskite tandem cells: A layer by layer exploration

??? "publication_authors"
    Authors of the publication. <br/>
    Can be populated based on the DOI number

    * type: list of strings
    * example: ["T. Jesper Jacobsson", "Adam Hultqvist"]

### Metadata
Metadata that is added automatically if the device data is uploaded to NOMAD

??? "ID"
    Database ID in the Nomad database. Assigned automatically when a file is uploaded

    * type: int
    * example: 635


