# Introduction
Every single tandem device is supposed to be described using one single JSON file. <br> 

#### Note on categorical data
Categorical data is whenever possible implemented as list of available options that can be selected rather. This tends to increase data quality compared to when using free text options. However, the suggested alternatives will never be exhaustive, so when your device is not covered by the available options, please feel free to define additional categories.
 

### Top level
The perovskite data file has one top level called “data”: {}. <br> 

???+ "data"
    The top level is named data. <br>
    The top level has one key-value pair and a variable number of subsections that can be added based on the type of available data.  


    ???+ "d_def"
        Should be: "perovskite_solar_cell_database.schema_packages.tandem.schema.PerovskiteTandemSolarCell" <br>
        This is needed to upload the file to the NOMAD database

    ???+ "subsections"
        Documentation to all subsections so far defines are found under "data" in the menu to the left. <br> Subsections can be deeply nested.  