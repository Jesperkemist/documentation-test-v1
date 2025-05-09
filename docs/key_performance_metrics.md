# key performance metrics
This section stores the key performance metrics of the device. <br/>
This data is ideally automatically extracted from measurement data specified in detail in the measurement sections. <br>
From a data analytics perspective, it is however, convenient to have the key performance metrics collected in one section. 

### Stabilized efficiency
??? "power_conversion_efficiency_stabilized"
    Stabilized power conversion efficiency. Further details about the measurement in the dedicated measurement section

    * type: float
    * unit: %
    * example: 22.3

### IV metrics
From a representative measurement under standard illumination (AM1.5). Further details about the measurement in the dedicated measurement section

??? "power_conversion_efficiency"
    Power conversion efficiency. 

    * type: float
    * unit: %
    * example: 22.3

??? "short_circuit_current_density"
    Short-circuit current density. 

    * type: float
    * unit: mA/cm^2
    * example: 19.3   

??? "open_circuit_voltage"
    Open-circuit voltage. 

    * type: float
    * unit: V
    * example: 1.05   

??? "fill_factor"
    Fill factor. pce/(Voc*Jsc) Should be given as a number between 0 and 1.

    * type: float
    * unit: %
    * example: 0.76    

??? "maximum_power_point_voltage"
    Voltage at maximum power. 

    * type: float
    * unit: V
    * example: 1.02       

??? "maximum_power_point_current_density"
    Current at maximum power. 

    * type: float
    * unit: mA/cm^2
    * example: 19.3 

### Stability data
There are numerous different protocols by which device stability can be measured. For this section of key performance metrics, the following four are some of hte more commonly reported metrics. Additional metrics are found in the dedicated stability section. Further details about the measurement in the dedicated stability measurement section.

??? "pce_1000h_isos_l1"
    Power conversion efficiency after 1000 h under ISOS L1 conditions, 
        i.e. AM 1.5, Maximum powerpoint (or held at constant potential close to the Vmp), 
        room temperature, inert atmosphere. 

    * type: float
    * unit: %
    * example: 20.1   

??? "pce_1000h_isos_l3"
    Power conversion efficiency after 1000 h under ISOS L3 conditions, i.e. AM 1.5, Maximum powerpoint, 85°C and 50 % RH'. 

    * type: float
    * unit: %
    * example: 14.2       


??? "t80_1000h_isos_l1"
    Time to 80% of initial power conversion efficiency after 1000 h under ISOS L1 conditions.
    i.e. AM 1.5, Maximum powerpoint (or held at constant potential close to the Vmp), 
    room temperature, inert atmosphere. 

    * type: float
    * unit: h
    * example: 260       

??? "t80_1000h_isos_l3"
    Time to 80% of initial power conversion efficiency after 1000 h under ISOS L3 conditions, i.e. AM 1.5, Maximum powerpoint, 85°C and 50 % RH. 

    * type: float
    * unit: h
    * example: 150   