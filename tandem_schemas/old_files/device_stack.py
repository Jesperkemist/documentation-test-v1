from ase.data import chemical_symbols
from nomad.datamodel.data import ArchiveSection
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    Filter,
    SectionProperties,
)
from nomad.datamodel.metainfo.basesections import PubChemPureSubstanceSection
from nomad.metainfo import MEnum, Quantity, Datetime, Section, SubSection
from nomad.metainfo.metainfo import SchemaPackage

from perovskite_solar_cell_database.composition import PerovskiteCompositionSection

m_package = SchemaPackage()


### Chemicals and materials
class EnvironmentalConditionsDeposition(ArchiveSection):
    """
    Environmental conditions during the activity.
    """
    ambient_conditions = Quantity(
        description='TRUE if the activity is occurring in in uncontrolled ambient conditions. FALSE otherwise',
        type=bool,
        a_eln=ELNAnnotation(component='BoolEditQuantity'),
    )

    atmosphere = Quantity(
        description='Atmosphere during the activity.',
        type=MEnum(['air', 'dry_air', 'N2', 'Ar', 'He', 'O2', 'H2', 'vacuum', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity')
    )

    pressure = Quantity(
        description='The atmospheric pressure during the activity.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )

    in_glove_box = Quantity(
        type=bool,
        shape=[],
        description="""True if the the activity was performed in a glove box, False otherwise.
            """,
        a_eln=dict(component='BoolEditQuantity'),
    )
    
    ambient_temperature = Quantity(
        description='Ambient temperature during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )

    relative_humidity = Quantity(
        description='Relative humidity during the activity.',
        type=float,
        unit='%',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='%'),
    )

    # substrate_temperature = Quantity(
    #     description='The temperature of the substrate during the activity.',
    #     type=float,
    #     unit='C',
    #     a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    # )

    oxygen_concentration = Quantity(
        description='The oxygen concentration during the activity.',
        type=float,
        unit='%',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='%'),
    ) 


class ChemicalComponentIdentity(PubChemPureSubstanceSection):
    """
    PubChem functionality for pure substances.
    """
    
    def normalize(self, archive, logger):
        # Fix for non-defined molecular_formula in PureSubstance v2.py
        # self.molecular_formula = self.formula
        super().normalize(archive, logger)


class ChemicalComponentAmount(ArchiveSection):
    """
    This is the section for the amount of a chemical component in a layer.
    """
    mass_fraction = Quantity(
        description='The mass fraction of the substance.',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )
    
    molar_fraction = Quantity(
        description='The molar fraction of the substance.',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    volume_fraction = Quantity(
        description='The volume fraction of the substance.',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )
     
    molar_concentration = Quantity(
        description='The molarity of the substance.',
        type=float,
        unit='mol/l',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mol/l'),
    )
    
    mass_concentration = Quantity(
        description='The mass concentration of the substance.',
        type=float,
        unit='g/l',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mg/ml'),
    )

    mass = Quantity(
        description='The mass of the substance.',
        type=float,
        unit='g',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='g'),
    )

    volume = Quantity(
        description='The volume of the substance.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    amount = Quantity(
        description='The amount of the substance.',
        type=float,
        unit='mol',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mol'),
    )

    partial_pressure = Quantity(
        description='The partial pressure of the compound.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )


class NanostructureInformation(ArchiveSection):
    """
    This is the section for the nanostructure information of a chemical component.
    """
    shape = Quantity(
        description='The nanostructure of the compound',
        type=MEnum(
            [
                'nanoparticle',
                'quantum_dot',
                'nanorod',
                'disc',
                'sheet',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )    
    
    diameter = Quantity(
        description='diameter.',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    width = Quantity(
        description='width.',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    length = Quantity(
        description='length.',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )


class SupplierInformation(ArchiveSection):
    """
    This is the section for the supplier information of a chemical component.
    """
    supplier = Quantity(
        type=str,
        shape=[],
        description='The name of the supplier.',
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    product_number = Quantity(
        type=str,
        shape=[],
        description="The supplier's product number of the substance.",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    batch_number = Quantity(
        type=str,
        shape=[],
        description="The suppliers batch number of the substance bought.",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    purity = Quantity(
        description='The purity of the substance.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    delivery_date = Quantity(
        description='Date of delivery of the substance.',
        type=Datetime,
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )


class SynthesisInformation(ArchiveSection):
    """
    Synthesis of substances not sourced from commercial suppliers.
    """
    synthesis_method = Quantity(
        type=str,
        shape=[],
        description='The synthesis method used to make the substance.',
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    synthesis_date = Quantity(
        description='Date of synthesis of the substance.',
        type=Datetime,
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )
    
    free_text_comment = Quantity(
        type=str,
        shape=[],
        description="""
            Any additional description not captured by any other field.                    
            """,
        a_eln=dict(component='RichTextEditQuantity'),
    )


class Component(ArchiveSection):
    """
    This is the section for a chemical component in a layer.
    """
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the material.
        examples: TiO2-mp, PEDOT:PSS, Spiro-MeOTAD, SLG, ITO""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    abbreviation = Quantity(
        type=str,
        shape=[],
        description="""Standard arreviation of the compound.""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    functionality = Quantity(
        description='The primary functionality of the compound in the layer',
        type=MEnum(
            [
                'majority_phase',
                'secondary_phase',
                'additive',
                'dopant',
                'impurity',
                'solvent',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    aggregation_state = Quantity(
        description='The aggregation state of the compound',
        type=MEnum(
            [
                'solid',
                'liquid',
                'gas',
                'solution',
                'suspension',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    origin = Quantity(
        description='The origin of the compound',
        type=MEnum(
            [
                'commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'collected_in_nature',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    nanostructured = Quantity(
        description='TRUE if the compound is nanostructured, e.g. nanoparticles, nanorods etc.',
        type=bool,
        a_eln=ELNAnnotation(component='BoolEditQuantity'),
    )

    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )
    
    # Amount of the compound in the layer
    amount = SubSection(
        section_def=ChemicalComponentAmount,
        description='The amount of the compound in the layer.',
    )
    
    # Supplier information
    Supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )
    
    # Nanostructure information
    nanostructuration = subSection(
        section_def=NanostructureInformation,
        description='The nanostructure information of the compound.',
    )
    
    # Synthesis information
    synthesis = SubSection(
        section_def=SynthesisInformation,
        description='Synthesis of substances not sourced from commercial suppliers.',
    )


class SputteringTarget(ArchiveSection):
    """
    Section for a sputtering target.
    """
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the material.
        examples: Au, Ag, ITO, NiO""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    substrate_distance = Quantity(
        description='The distance between the substrate and the sputtering target.',
        type=float,
        unit='cm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm'),
    )

    origin = Quantity(
        description='The origin of the compound',
        type=MEnum(['commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'other',]),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )

    # Supplier information
    Supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )


class EvaporationSource(ArchiveSection):
    """
    This is the section for a evaporation source.
    """
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the material.
        examples: Au, Ag, C60, PCBM60, LiF, MoO3""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    amount = Quantity(
        description='The amount of the compound in the evaporation source.',
        type=float,
        unit='g',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='g'),
    )

    substrate_distance = Quantity(
        description='The distance between the substrate and the evaporation source.',
        type=float,
        unit='cm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm'),
    )

    aggregation_state = Quantity(
        description='The aggregation state of the compound',
        type=MEnum(['solid','liquid','other',]),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    crucible_material = Quantity(
        description='The material of the evaporation boat/vessel',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    origin = Quantity(
        description='The origin of the compound',
        type=MEnum(['commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'collected_in_nature',
                'other',]),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )

    # Supplier information
    Supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )
    
    # Synthesis information
    synthesis = SubSection(
        section_def=SynthesisInformation,
        description='Synthesis of substances not sourced from commercial suppliers.',
    )


class LigandsAndDyes(ArchiveSection):
    """
    This is the section for a ligands or dyes.
    """
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the material.
        examples: TiO2-mp, PEDOT:PSS, Spiro-MeOTAD, SLG, ITO""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    abbreviation = Quantity(
        type=str,
        shape=[],
        description="""Standard arreviation of the compound.""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    origin = Quantity(
        description='The origin of the compound',
        type=MEnum(
            [
                'commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'collected_in_nature',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )    

    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )
    
    # Supplier information
    Supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )
    
    # Synthesis information
    synthesis = SubSection(
        section_def=SynthesisInformation,
        description='Synthesis of substances not sourced from commercial suppliers.',
    )


class GasComponent(ArchiveSection):
    """
    Section for a chemical component in gas phase.
    """    
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the substance.
        examples: methylamine, I2, H2O""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )       

    functionality = Quantity(
        description='The role of this specific substance in the gas mixture.',
        type=MEnum(['reactant', 'product', 'carrier_gas', 'none', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    origin = Quantity(
        description='The origin of the substance.',
        type=MEnum([
                'commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'collected_in_nature',
                'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    partial_pressure = Quantity(
        description='The partial pressure of the gas.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )

    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )
   
    # Supplier information
    supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )

    # Synthesis information
    synthesis = SubSection(
        section_def=SynthesisInformation,
        description='Synthesis of substances not sourced from commercial suppliers.',
    )


class SolutionComponent(ArchiveSection):
    """
    Section for a chemical component in a solution.
    """
    ## Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description="""The common trade name of the substance.
        examples: DMF, DMSO, TiO2-mp, PEDOT:PSS, Spiro-MeOTAD""",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )    
   
    functionality = Quantity(
        description='The role of this specific substance in the solution.',
        type=MEnum(['solvent', 'solute', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )
    
    origin = Quantity(
        description='The origin of the substance.',
        type=MEnum([
                'commercial_supplier',
                'made_in_house',
                'made_by_collaborator',
                'collected_in_nature',
                'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    nanostructured = Quantity(
        description='TRUE if the compound is nanostructured, e.g. nanoparticles, nanorods etc.',
        type=bool,
        a_eln=ELNAnnotation(component='BoolEditQuantity'),
    )
    
    ## Subsections
    # PubChem pure substance section
    identity = SubSection(
        section_def=ChemicalComponentIdentity,
        description='The identity of the compound.'
    )
    
    # Amount of the compound in the layer
    amount = SubSection(
        section_def=ChemicalComponentAmount,
        description='The amount of the compound in the layer.',
    )
    
    # Supplier information
    supplier = SubSection(
        section_def=SupplierInformation,   
        description='The supplier information of the compound.',
    )
    
    # Nanostructure information
    nanostructuration = subSection(
        section_def=NanostructureInformation,
        description='The nanostructure information of the compound.',
    )
    
    # Synthesis information
    synthesis = SubSection(
        section_def=SynthesisInformation,
        description='Synthesis of substances not sourced from commercial suppliers.',
    )


class Solution(ArchiveSection):
    """
    Description of a solution
    """
    preparation_date = Quantity(
        description='Date of preparation of the solution.',
        type=Datetime,
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )    
    
    age = Quantity(
        description='The time between preparation and the use of the solution.',
        type=float,
        unit='h',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='h'),
    )

    volume = Quantity(
        description='The volume of the solution used.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )    

    density = Quantity(
        description='The density of the solution.',
        type=float,
        unit='g/ml',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='g/ml'),
    ) 

    viscosity = Quantity(
        description='The viscosity of the solution.',
        type=float,
        unit='Pa*s',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='Pa*s'),
    ) 

    temperature = Quantity(
        description='The temperature of the solution.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='celsius'),
    )    

    temperature_max = Quantity(
        description='The maximum temperature the solution has experienced.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='celsius'),
    )  
    
    colour = Quantity(
        description='The colour of the solution.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    ) 

    stirred = Quantity(
        description="""True if the solution is stirred before use.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )

    filtered = Quantity(
        description="""TRUE if the if the solution is filtered before use.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )

    filter_pour_size = Quantity(
        description="""TRUE if the if the solution is filtered before use.""",
        type=float,
        unit='µm',
        shape=[],
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='µm'),
    )    
    
    # Subsections
    # Compounds in the solution
    components = SubSection(
        section_def=SolutionComponent,
        description='The substances in the solution.',
        repeats=True,
    )
    
    # Environmental conditions
    environmental_conditions_during_preparation = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )    


### Photoabsorbers
class PhotoabsorberPerovskite(ArchiveSection):
    """
    This is the section for a perovskite photoabsorber.
    """
    # origin = Quantity(
    #     description='If the perovskite was made in house, by a collaborator, or bought commercially',
    #     type=MEnum(
    #         [
    #             'commercial_supplier',
    #             'deposited_in_house',
    #             'deposited_by_collaborator', 
    #         ]
    #     ),
    #     a_eln=ELNAnnotation(component='EnumEditQuantity'),
    # )

    lead_free = Quantity(
        description="""True if the perovskite does not contain any lead.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )  
    
    inorganic = Quantity(
        description="""True if the perovskite is inorganic.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )

    double_perovskite = Quantity(
        description="""True if it is a double perovskite structure. 
        A double perovksite is strictly not a perovskite, but as if 
        in terms of PV development often is treated as a perovskite, 
        it is worth including it but with a flag indicating the structure.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )
    
    has_a_2D_perovskite_capping_layer = Quantity(
        description="""True if the perovskite has a thin capping layer of a 2D perovskite.""",
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )

    # Subsections
    composition = SubSection(
        section_def=PerovskiteCompositionSection,
        description='The composition of the perovskite.',
    )


class PhotoabsorberSilicon(ArchiveSection):
    """
    This is the section for a silicon photoabsorber.
    """
    cell_type = Quantity(
        description='The type of silicon cell.',
        type=MEnum(
            [
                'AL-BSF',
                'c-type ',
                'HIT',
                'Homojunction',
                'n-type',
                'p-type',
                'PERC',
                'SC/nFAB',
                'PERL',
                'heterojunction',
                'TopCon',
                'other'
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    doping_sequence = Quantity(
        description='Description of the doping sequence.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class PhotoabsorberCIGS(ArchiveSection):
    """
    This is the section for a CIGS photoabsorber.
    """
    Cu = Quantity(
        description='The stoichiometric coefficient for Cu',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    In = Quantity(
        description='The stoichiometric coefficient for In',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    Ga = Quantity(
        description='The stoichiometric coefficient for Ga',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )
    
    Se = Quantity(
        description='The stoichiometric coefficient for Se',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    # Derived quantities
    molecular_formula = Quantity(
        description='The molecular formula. Can be derived automatically based on the stoichiometric coefficients',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # TODO add functionality for populating the derived quantities
    def normalize(self, archive, logger):
        super().normalize(archive, logger)    


class PhotoabsorberCZTS(ArchiveSection):
    """
    This is the section for a CZTS photoabsorber.
    """
    Cu = Quantity(
        description='The stoichiometric coefficient for Cu',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    Zn = Quantity(
        description='The stoichiometric coefficient for Zn',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    Sn = Quantity(
        description='The stoichiometric coefficient for Sn',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )
    
    S = Quantity(
        description='The stoichiometric coefficient for S',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    # Derived quantities
    molecular_formula = Quantity(
        description='The molecular formula. Can be derived automatically based on the stoichiometric coefficients',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # TODO add functionality for populating the derived quantities
    def normalize(self, archive, logger):
        super().normalize(archive, logger)  
    

class PhotoabsorberOPV(ArchiveSection):
    """
    This is the section for a organic photoabsorber.
    """
    blend = Quantity(
        description='The name of the OPV blend. Often in the form - "name of acceptor:"name of donor"',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    cell_type = Quantity(
        description='The type of opv cell',
        type=MEnum(
            [
                'singel_layer',
                'bilayer',
                'heterojunction',
                'bulk_heterojunction',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    peak_absorption_wavelength = Quantity(
        description='The wavelength at maximum absorption',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    ) 

    molar_extinction_coefficient = Quantity(
        description='The molar extinction coefficient',
        type=float,
        unit='L*mol^1*cm^-1',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='L*mol^1*cm^-1'),
    ) 
 
    homo_level = Quantity(
        description='The energy of the HOMO level',
        type=float,
        unit='eV',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='eV'),
    )  
    
    lumo_level = Quantity(
        description='The energy of the LUMO level',
        type=float,
        unit='eV',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='eV'),
    )      
  
  
class PhotoabsorberDSSC(ArchiveSection):
    """
    This is the section for a organic photoabsorber.
    """
    peak_absorption_wavelength = Quantity(
        description='The wavelength at maximum absorption',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    ) 

    molar_extinction_coefficient = Quantity(
        description='The molar extinction coefficient',
        type=float,
        unit='L*mol^1*cm^-1',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='L*mol^1*cm^-1'),
    ) 
 
    homo_level = Quantity(
        description='The energy of the HOMO level',
        type=float,
        unit='eV',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='eV'),
    )  
    
    lumo_level = Quantity(
        description='The energy of the LUMO level',
        type=float,
        unit='eV',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='eV'),
    )    
    
    oxidation_potential = Quantity(
        description='The oxidation potential vs the normal hydrogen electrode',
        type=float,
        unit='V',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='V'),
    )      
 
    # subsections
    dye = SubSection(
        section_def=LigandsAndDyes,
        description='The components.',
        repeats=True,
    )        


class PhotoabsorberQD(NanostructureInformation):
    """
    This is the section for a quantum dot photoabsorbers.
    """
    material = Quantity(
        description='The material of the quantum dots. e.g PbS',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
       
    # subsections
    ligands = SubSection(
        section_def=LigandsAndDyes,
        description='The components.',
        repeats=True,
    )     
    
### Material and layer properties
class Area(ArchiveSection):
    value = Quantity(
        description='The area of the layer',
        type=float,
        unit='cm^2',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm^2'),
    ) 


class BandGap(ArchiveSection):
    value = Quantity(
        description='The band gap of the layer',
        type=float,
        unit='eV',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='eV'),
    )
    
    graded = Quantity(
        description='TRUE if the band gap varies as a function of the vertical position in the layer',
        type=bool,
        a_eln=ELNAnnotation(component='BoolEditQuantity'),
    )
    
    determined_by = Quantity(
        description="""The method by which the band gap was estimated.
        The band gap can be estimated from absorption data, 
        EQE-data, UPS-data, or it can be estimated based on literature values 
        for the recipe, or it could be inferred from the composition and what 
        we know of similar but not identical compositions.""",
        type=MEnum(
            [
                'absorption',
                'absorption_Tauc-plot',
                'composition',
                'eqe',
                'literature',
                'ups',
                'xps',
                'other',
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )


class Conductivity(ArchiveSection):
    value = Quantity(
        description='The conductivity of the layer',
        type=float,
        unit='S/m',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='S/m'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class Crystallinity(ArchiveSection):
    value = Quantity(
        description='The crystallinity of the layer',
        type=MEnum(['amorphous', 'polycrystalline', 'single_crystal', 'nanoparticles', 'nanorods', 'qunatum_dots', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    average_grain_size = Quantity(
        description='The average grain size',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class ElectronMobility(ArchiveSection):
    value = Quantity(
        description='The electron mobility of the layer',
        type=float,
        unit='cm**2/(V*s)',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm**2/(V*s)'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class HoleMobility(ArchiveSection):
    value = Quantity(
        description='The hole mobility of the layer',
        type=float,
        unit='cm**2/(V*s)',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm**2/(V*s)'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class Photoluminesence(ArchiveSection):
    """
    This is the section for the photoluminesence of a layer.
    """
    pl_max = Quantity(
        description='The wavelength of the maximum PL intensity',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class RefractiveIndex(ArchiveSection):
    refractive_index = Quantity(
        description='The real part of the refractive index of the layer',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    extinction_coefficient = Quantity(
        description='The imaginary part of the refractive index of the layer',
        type=float,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )    
    

class SheetResistance(ArchiveSection):
    value = Quantity(
        description='The sheet resistance of the layer',
        type=float,
        unit='ohm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ohm'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
 
    
class SurfaceRoughness(ArchiveSection):
    value = Quantity(
        description='The root mean square value of the surface roughness',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    
class Thickness(ArchiveSection):
    value = Quantity(
        description='The thickness of the layer',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    determined_by = Quantity(
        description='The measurement or estimation method used to determine the property.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
 
    
class LayerProperties(ArchiveSection):
    """
    A section storing general properties of a layer.
    """
    area = SubSection(
        description='The area of the layer',
        section_def=Area,
    )
    
    band_gap = SubSection(
        description='The band gap of the layer',
        section_def=BandGap,
    )
    
    conductivity = SubSection(
        description='The conductivity of the layer',
        section_def=Conductivity,
    )   
    
    crystallinity = SubSection(
        description='The crystallinity of the layer',
        section_def=Crystallinity,
    )
    
    electron_mobility = SubSection(
        description='The electron mobility of the layer',
        section_def=ElectronMobility,
    )
    
    hole_mobility = SubSection(
        description='The hole mobility of the layer',
        section_def=HoleMobility,
    )
  
    photoluminesence = SubSection(
        description='The photoluminesence of the layer',
        section_def=Photoluminesence,
    )
    
    refractive_index = SubSection(
        description='The refractive index of the layer',
        section_def=RefractiveIndex,
    )
    
    sheet_resistance = SubSection(
        description='The sheet resistance of the layer',
        section_def=SheetResistance,
    )
    
    thickness = SubSection(
        description='The thickness of the layer',
        section_def=Thickness,
    )
      

### Deposition procedures general sections

class DepositionStep(ArchiveSection):
    """
    This is the section for a deposition step of a layer.
    """
    # # Deposition method
    # method = Quantity(
    #     description='The method used to deposit the layer.',
    #     type=MEnum(
    #         [
    #             'spin_coating',
    #             'doctor_blade',
    #             'slot_die',
    #             'spray_coating',
    #             'inkjet_printing',
    #             'screen_printing',
    #             'dip_coating',
    #             'thermal_evaporation',
    #             'sputtering',
    #             'CVD',
    #             'ALD',
    #             'other',
    #         ]
    #     ),
    #     a_eln=ELNAnnotation(component='EnumEditQuantity'),
    # )

    # time_from_last_step = Quantity(
    #     description="""The time from the finalization of the last step 
    #     and the start of this step. If this is the first step, this would be 0.""",
    #     type=float,
    #     unit='minute',
    #     a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    # )

    # # Environmental conditions
    # environmental_conditions = SubSection(
    #     section_def=EnvironmentalConditionsDeposition,
    #     description='Environmental conditions during the activity.',
    # )
    pass


### Synthetic procedures
class ALDStep(ArchiveSection):
    """
    ALD steps
    """
    time_of_step = Quantity(
        description='The length of the step.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    chamber_pressure = Quantity(
        description='The pressure in the reaction chamber.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )

    gases = SubSection(
        section_def=GasComponent,
        description='The gases in the mixture',
        repeats=True
    )


class SpinCoatingSteps(ArchiveSection):
    """
    A spin-coating program can be composed of several different steps. 
    This is a repeating section for describing all the spin-coating steps
    """
    duration = Quantity(
        description='The length of the step.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    speed_start = Quantity(
        description='The spin speed of the start of the step.',
        type=float,
        unit='rpm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='rpm'),
    )

    speed_end = Quantity(
        description='The spin speed of the end of the step.',
        type=float,
        unit='rpm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='rpm'),
    )

    acceleration = Quantity(
        description='The acceleration of the rotations.',
        type=float,
        unit='rpm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='rpm/s'),
    )


class Dipping(ArchiveSection):
    """
    Details for a dipping treatment.
    """
    time_in_solution = Quantity(
        description='The time of the dipping.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    drying_procedure = Quantity(
        description='The methode by which the liquid is removed from the sample after dipping.',
        type=EMum([
                'gas_blowing',
                'self_drying',
                'heating',
                'tissue_paper',
                'none',
                'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )


class TemperatureStep(ArchiveSection):
    """
    Details for heaating steps
    """
    time_of_step = Quantity(
        description='Time of the step.',
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    )

    temperature_start = Quantity(
        description='Temperature at the start of the step.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )    

    temperature_end = Quantity(
        description='Temperature at the end of the step.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )      

    temperature_acceleration = Quantity(
        description='Temperature acceleration',
        type=float,
        unit='C/min',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C/min'),
    )  


class SputteringStep(ArchiveSection):
    """
    Details for heaating steps
    """
    time_of_step = Quantity(
        description='Time of the step.',
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    )

    deposition_rate = Quantity(
        description='The rate of deposition.',
        type=float,
        unit='nm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm/s'),
    )

    target_power = Quantity(
        description='The power driving the target.',
        type=float,
        unit='J/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='J/s'),
    )

    chamber_pressure = Quantity(
        description='The pressure in the reaction chamber.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )
 

class AntiSolventDetails(ArchiveSection):
    """
    Details for an antisolvent treatment.
    """
    volume = Quantity(
        description='The volume of the antisolvent.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    start_time = Quantity(
        description='Time of the start of the dispensing in seconds after the start of the spin-coating program.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )

    dispense_speed = Quantity(
        description='The dispense speed of the precursor solution.',
        type=float,
        unit='ml/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml/s'),
    )

    distance_between_tip_and_substrate = Quantity(
        description='Distance between the pipet tip and the substrate',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    # Subsections
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )


class GasQuenchingDetails(ArchiveSection):
    """
    Details for a gas quenching treatment.
    """
    gas = Quantity(
        description='The gas used for the quenching.',
        type=MEnum(['air', 'dry_air', 'N2', 'Ar', 'He', 'O2', 'H2', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )
    
    start_time = Quantity(
        description='Time of the start of the dispensing in seconds after the start of the spin-coating program.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )

    duration = Quantity(
        description='The length of the qas quenching',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    pressure = Quantity(
        description='The pressure of the gas.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )

    temperature = Quantity(
        description='The temperature of the gas.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    distance_between_nozzle_and_substrate = Quantity(
        description='Distance between the nozzle and the substrate',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )    


class PostDepositionProcedure(DepositionStep):
    """
    Post deposition procedure. 
    """
    # Top level sections
    time_stamp = Quantity(
        description='Date of the operation',
        type=Datetime,
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )

    duration = Quantity(
        type=float,
        description='The time if the operation from start to finish.',
        unit='minute',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='minute'
        ),
    )
    
    time_from_last_step = Quantity(
        description="""The time from the finalization of the last layer 
        and the start of the deposition of this.""",
        type=float,
        unit='h',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='h'),
    )

    # Subsections
    steps = SubSection(
        section_def=DepositionStep,
        description='The steps of the deposition procedure.',
        repeats=True,
    )

    # Environmental conditions
    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )
    
    sample_history = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description="""A description of the conditions under which the sample have been stored between
        the finalization of the device and the described measurement.""",
    )


class AtomicLayerDeposition(DepositionStep):
    """
    Details for an ALD process.
    """
    # Numerical qunatities
    duration = Quantity(
        description='The total time of the procedure.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    ) 

    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )

    flow_rate = Quantity(
        description='The flow rate.',
        type=float,
        unit='sccm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='sccm'),
    ) 

    number_of_cycles = Quantity(
        description='The number of deposition cycles.',
        type=int,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    ) 

    # Categorical qunatities
    carrier_gas = Quantity(
        description='The carrier gas.',
        type=MEnum(['air', 'dry_air', 'N2', 'Ar','other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),    
    )
    
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    steps = SubSection(
        section_def=ALDStep,
        description='Details about the four ALD steps.',
        repeats=True,  
    ) 

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'atomic_layer_deposition' 


class ChemicalBathDeposition(DepositionStep):
    """
    Details for a chemical bath deposition process.
    """
    # Numerical quantities
    time_in_solution = Quantity(
        description='The time of the dipping.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )    

    # Categorical quantities
    drying_procedure = Quantity(
        description='The method by which the liquid is removed from the sample after dipping.',
        type=EMum([
                'gas_blowing',
                'self_drying',
                'heating',
                'tissue_paper',
                'none',
                'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )
    
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    # Subsection    
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'chemical_bath_deposition'      


class Cleaning(DepositionStep):
    """
    Cleaning procedures
    """
    # Numerical quantities
    duration = Quantity(
        description='The time of the evaporation.',
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    )

    # Categorical quantities
    equipment = Quantity(
        description='Brand name and model of the spin-coater.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    free_text_comment = Quantity(
        type=str,
        shape=[],
        description="""
            Any additional description not captured by any other field.                    
            """,
        a_eln=dict(component='RichTextEditQuantity'),
    )
            
    # Subsections
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )
    
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'cleaning'  


class DipCoating(DepositionStep):
    """
    Details for a dip coating process.
    """
    # Numerical quantities
    time_in_solution = Quantity(
        description='The time of the dipping.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )    
     
    number_of_repetitions = Quantity(
        description='The number of repetitions (dippings).',
        type=int,
        a_eln=ELNAnnotation(component='IntegerEditQuantity'),
    )
    
    time_between_repetitions = Quantity(
        description='The time between the repetitions.',
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    )
    
    # Categorical quantities
    drying_procedure = Quantity(
        description='The methode by which the liquid is removed from the sample after dipping.',
        type=EMum([
                'gas_blowing',
                'self_drying',
                'heating',
                'tissue_paper',
                'none',
                'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    # Subsection    
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'dip_coating'  


class DoctorBlading(DepositionStep):
    """
    Details for a doctor blading process.
    """
    # Numerical quantities
    duration = Quantity(
        description='The time of the doctor blading.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    blade_speed = Quantity(
        description='The speed of the blade.',
        type=float,
        unit='mm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm/s'),
    )

    blade_angle = Quantity(
        description='The angle of the blade.',
        type=float,
        unit='degree',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='degree'),
    )

    blade_height = Quantity(
        description='The height of the blade.',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    ink_volume = Quantity(
        description='The volume of the ink used.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )     
    
    # categorical quantities
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    # Subsections
    ink = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'doctor_blading'  


class Evaporation(DepositionStep):
    """
    Details for a evaporation process.
    """
    # Numerical quantities
    number_of_sources = Quantity(
        description='The number of sources used for the evaporation.',
        type=int,
        a_eln=ELNAnnotation(component='IntegerEditQuantity'),
    )
    
    duration = Quantity(
        description='The time of the evaporation.',
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='minute'),
    )
    
    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    substrate_rotation_speed = Quantity(
        description='The rotation speed of the substrate during the activity.',
        type=float,
        unit='rpm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='rpm'),
    )
    
    deposition_rate = Quantity(
        description='The rate of deposition.',
        type=float,
        unit='nm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm/s'),
    )

    chamber_pressure = Quantity(
        description='The pressure in the reaction chamber.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    )

    # Categorical qunatities 
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    sources = SubSection(
        section_def=EvaporationSource,
        description='Details about the evaporation sources.',
        repeats=True,
    )
    
    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description="""Environmental conditions during the activity. 
        Mostly relevant if the evaporation not is done in a vaccuum chamber""",
    )
    
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'evaporation'  


class Heating(DepositionStep):
    """
    Details for a heating process.
    """
    # Numerical quantities
    duration = Quantity(
        description='The duration of the process.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )    

    # categorical quantities
    heating_medium = Quantity(
        description='The way by which the temperature is controlled',
        type=MEnum(['hotplate', 'furnace', 'liquid_bath', 'gas', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )    
    
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    
    # Subsections
    temperature_steps = SubSection(
        section_def=TemperatureStep,
        description='Details about the temperature steps.',
        repeats=True,  
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'heating'    
    

class InkjetPrinting(DepositionStep):
    """
    Details for a inkjet printing process.
    """
    # Numerical qunatities
    duration = Quantity(
        description='The total time of the procedure.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    ) 
        
    drop_volume = Quantity(
        description='Drop volume.',
        type=float,
        unit='µl',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='µl'),
    )

    print_resolution = Quantity(
        description='The print resolution.',
        type=float,
        unit='dpi',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='dpi'),
    )

    print_speed = Quantity(
        description='The speed of the printer head.',
        type=float,
        unit='mm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm/s'),
    )

    print_heigth = Quantity(
        description='The distance from the nozzle and the substrate.',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )  
     
    ink_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )  
     
    # categorical qunatities
    equipment = Quantity(
        description='Brand name and model of the spin-coater.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    ink = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )  
      
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'inkjet_printing'     


class IonExchangeByDipping(DipCoating):
    """
    Details for a process where ions in a perovksite is exchanged by 
    dipping it in a solution 
    
    """
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'ion_exchange_by_dipping'  


class IonExchangeByGasDiffusion(DepositionStep):
    """
    Details for a process where ions in a perovksite is exchanged by 
    a gas diffusion process 
    
    """
    # Numerical quantities
    duration = Quantity(
        description='The total time of the procedure.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )     

    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    gas_temperature = Quantity(
        description='The temperature of the reaction gas during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )

    # Categorical qunatities
    equipment = Quantity(
        description='Brand name and model of the spin-coater.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    gases = SubSection(
        section_def=GasComponent,
        description='The gases in the mixture',
        repeats=True
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'ion_exchange_by_gas_diffusion'  


class SlotDyeCoating(DepositionStep):
    """
    Details for a slot dye coatig process
    """
    # Numerical qunatities
    duration = Quantity(
        description='The time of the doctor blading.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    blade_speed = Quantity(
        description='The speed of the blade.',
        type=float,
        unit='mm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm/s'),
    )

    blade_angle = Quantity(
        description='The angle of the blade.',
        type=float,
        unit='degree',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='degree'),
    )

    blade_height = Quantity(
        description='The height of the blade.',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    ink_volume = Quantity(
        description='The volume of the ink used.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )     
    
    # Categorical qunatities
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
   
    # Subsectinos 
    ink = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'slot_dye_coating'  


class SpinCoating(DepositionStep):
    """
    This is the section for a spin coating step of a layer.
    """
    # Boolean quantities
    dynamic_spin_coating = Quantity(
        description="""
            TRUE if the if the liquid is added on a spinning substrate. FALSE if the liquid is applied before the substrate starts spinning.',
            """,
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )
    
    antisolvent = Quantity(
        description="""
            True if an antisolvent is used during spin-coating.',
            """,
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )

    gas_quenching = Quantity(
        description="""
            True if an gas quenching is used during spin-coating.',
            """,
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )      
    
    # Numeric quantities
    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )

    solvent_volume = Quantity(
        description='volume of the precursor solution used for spin coating.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    duration = Quantity(
        description='The total time of all the spin-coating procedure.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )

    dispense_start_time = Quantity(
        description="""Time of the start of the dispensing in seconds after the start of the spin-coating program.
        For static spin-coating where the solution is added before the spinning starts, this is 0.""",
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )

    dispense_speed = Quantity(
        description='The dispense speed of the precursor solution.',
        type=float,
        unit='ml/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml/s'),
    )

    distance_between_tip_and_substrate = Quantity(
        description='Distance between the pipet tip and the substrate.',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    # Categorical quantities
    equipment = Quantity(
        description='Brand name and model of the spin-coater.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    spin_coating_steps = SubSection(
        section_def=SpinCoatingSteps,
        description='Description of each spin-coating step.',
        repeats=True,   
    )
    
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    antisolvent_details = SubSection(
        section_def=AntiSolventDetails,
        description='Details about the antisolvent treatment.',
    )
    
    gas_quenching_details = SubSection(
        section_def=GasQuenchingDetails,    
        description='Details about the gas quenching treatment.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'spin-coating'  


class SprayCoating(DepositionStep):
    """
    Details for a spray coating process
    """
    # Numerical qunatities
    duration = Quantity(
        description='The time of the doctor blading.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    nozzle_speed = Quantity(
        description='The speed of the nozzle.',
        type=float,
        unit='mm/s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm/s'),
    )

    nozzle_angle = Quantity(
        description='The angle of the nozzle.',
        type=float,
        unit='degree',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='degree'),
    )

    nozzle_height = Quantity(
        description='The distance between thesample and the nozzle.',
        type=float,
        unit='mm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='mm'),
    )

    solution_volume = Quantity(
        description='The volume of the ink used.',
        type=float,
        unit='ml',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='ml'),
    )

    solution_temperature = Quantity(
        description='The temperature of the solution during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    ) 

    sample_temperature = Quantity(
        description='The temperature of the sample during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    sample_area = Quantity(
        description='The area of the samples being sprayed.',
        type=float,
        unit='cm^2',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='cm^2'),
    )    

    gas_pressure = Quantity(
        description='The gas pressure.',
        type=float,
        unit='Pa',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='Pa'),
    ) 
    
    # categorical qunatities
    carrier_gas = Quantity(
        description='The carrier gas.',
        type=MEnum(['air', 'dry_air', 'N2', 'Ar', 'He', 'O2', 'H2', 'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),    
    )
  
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
   
    # Subsectinos 
    solution = SubSection(
        section_def=Solution,
        description='Details about the solution.',
    )

    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'slot_dye_coating'  


class Sputtering(DepositionStep):
    """
    Details for a sputtering process
    """
    # Numerical qunatities  
    duration = Quantity(
        description='The total time of the process.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )
    
    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )
    
    substrate_rotation_speed = Quantity(
        description='The rotation speed of the substrate during the activity.',
        type=float,
        unit='rpm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='rpm'),
    )

    # Categorical qunatities
    type_of_sputering = Quantity(
        description="The type of sputtering process",
        type=MEnum(['DC_sputtering', 
                    'RF_sputtering', 
                    'Magnetron_sputtering', 
                    'Reactive_sputtering', 
                    'Pulsed_DC_sputtering',  
                    'other']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),           
    )
    
    equipment = Quantity(
        description='Brand name and model of the equipment used for the process.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    steps = SubSection(
        section_def=SputteringStep,
        description='Details about the sputtering steps.',
        repeats=True,  
    )    
    
    target = SubSection(
        section_def=SputteringTarget,
        description='Details about the sputtering target.',
    )
  
    gases = SubSection(
        section_def=GasComponent,
        description='The gases in the mixture. For reactive sputtering',
        repeats=True
    )  
  
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'sputtering'  


class UVOzonTreatment(DepositionStep):
    """
    UVOzon treatment
    """
    # Boolean qunatities
    uv_illuminated = Quantity(
        description="""
            TRUE if the if the samples is illuminated by UV-light. FALSE if samples only are treated with ozone.',
            """,
        type=bool,
        shape=[],
        a_eln=dict(component='BoolEditQuantity'),
    )
    
    # Numerical quantities
    duration = Quantity(
        description='The total time of the procedure.',
        type=float,
        unit='s',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='s'),
    )     

    substrate_temperature = Quantity(
        description='The temperature of the substrate during the activity.',
        type=float,
        unit='C',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='C'),
    )

    uv_wavelength = Quantity(
        description='The wavelength of the UV light.',
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='nm'),
    )

    uv_intensity = Quantity(
        description='Intensity of the illumination.',
        type=float,
        unit='W/m^2',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='W/m^2'),
    )

    # Categorical qunatities
    equipment = Quantity(
        description='Brand name and model of the spin-coater.',
        type=str,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    # Subsections
    environmental_conditions = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description='Environmental conditions during the activity.',
    )
    
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        self.method = 'uv_ozon_treatment'      


### Deposition procedures top sections
class DepositionProcedure(ArchiveSection):
    """
    This is the section for the deposition procedure of a layer.
    """
    ## Top layer quantities
    substrate_layer = Quantity(
        description="""The layer on which the layer is deposited.
        The layer are ordered from bottom (furthest from the sun) to top (closest to the sun).
        Indicate if the layer was deposited on a layer that is below or above it in the device 
        (when the device is oriented with the top towards the sun)
        There are a few exceptions in that a layer can be a substrate, 
        it could be a layer that laminates two subcells, 
        and it could be a layer that is not deposited at all (like an air gap) 
        """,
        type=MEnum(
            ['is_substrate',
             'on_lower_layer',
             'on_upper_layer',
             'laminate_layers',
             'not-deposited']),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )
         
    origin = Quantity(
        description='The place where the layer was deposited. i.e. was it deposited in the lab or was it bought. An example of a layer that often is bought is the ITO layer on glass substrates',
        type=MEnum(
            [
                'commercial_supplier',
                'deposited_in_house',
                'deposited_by_collaborator', 
            ]
        ),
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )

    time_stamp = Quantity(
        description='Date the layer was deposited',
        type=Datetime,
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )
    
    duration = Quantity(
        type=float,
        description='The time it takes to deposit the layer from start to finish.',
        unit='minute',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity', defaultDisplayUnit='minute'
        ),
    )
    
    time_from_last_step = Quantity(
        description="""The time from the finalization of the last layer 
        and the start of the deposition of this.""",
        type=float,
        unit='h',
        a_eln=ELNAnnotation(component='NumberEditQuantity', defaultDisplayUnit='h'),
    )
    
    ## Subsections
    # Deposition steps
    steps = SubSection(
        section_def=DepositionStep,
        description='The steps of the deposition procedure.',
        repeats=True,
    )
    
    # Sample history
    sample_history = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description="""A description of the conditions under which the sample have been stored between
        the finalization of the last layer and the deposition of this layer.""",
    )


### Layers
class StackSummary(ArchiveSection):
    """
    This is the summary of the device stack.
    """

    # Number of layers in the stack
    n_layers = Quantity(
        description='Number of layers in the stack.',
        type=int,
        shape=[],
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    # Stack sequence
    stack_sequence = Quantity(
        description="""A list of the materials in the layers of the stack. <br/>  
        If a proper device stack section is provided, the stack sequence can be generated from that one.

        * Start with the layer in the bottom of the device (i..e that is furthest from the sun) and work up from that.
        * If two materials, e.g. A and B, are mixed in one layer, list the materials in alphabetic order and separate them with semicolons, as in (A; B)
        * The perovskite layer is stated as “Perovskite”, regardless of composition, mixtures, dimensionality etc. Those details are provided elsewhere. 
        * Use common abbreviations when possible but spell them out when there is risk for confusion. 
            """,
        type=str,
        shape=['*'],
        a_eln=ELNAnnotation(component='StringEditQuantity'),  
    )


class Layer(ArchiveSection):
    """
    This is the section for a layer in the device stack.
    """
    # Top level quantities
    name = Quantity(
        type=str,
        shape=[],
        description=""" A sensible name for the layer. A good default is the trade 
        name of the material, possibly with an addition of the microstructure.
        examples: 
        * TiO2-mp
        * PEDOT:PSS
        * Spiro-MeOTAD
        * SLG
        * ITO
        """,
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    sub_device_identity = Quantity(
        type=int,
        shape=[],
        description="""
            If the device not is monolithic, this describes which individual subcell the layer belongs to.  

            - 0 = the layer belongs to a monolithic device 
            - 1 = the layer belongs to the bottom subcell, 
            - 2 = the layer belongs to the second subcell (top cell in a 2-junction device)
            - 3 = the layer belongs to the third subcell (top cell in a 3-junction device
            """,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )

    functionality = Quantity(
        type=MEnum([''
            'air_gap',
            'anti_reflection',
            'back_contact',
            'buffer_layer',
            'edge_sealing',
            'electrolyte',
            'encapsulation',
            'electron_transport_layer',
            'front_contact',
            'hole_transport_layer',
            'interface_modifier',
            'mesoporous_scaffold',
            'middle_contact',
            'optical_spacer',
            'photoabsorber',
            'recombination_layer',
            'refractive_index_matching',
            'self_assembled_monolayer',
            'substrate',
            'other']),
        shape=[],
        description="The primary functionality of the layer in the device stack.",
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )

    ### Subsections
    ## Photoabsorbers 
    perovskite = SubSection(
        section_def=PhotoabsorberPerovskite,
        description='Perovskite specific information.',
    )
    
    silicon = SubSection(
        section_def=PhotoabsorberSilicon,
        description='Silicon specific information.',
    )
    
    CIGS = SubSection(
        section_def=PhotoabsorberCIGS,
        description='CIGS specific information.',
    )   
    
    CZTS = SubSection(
        section_def=PhotoabsorberCZTS,
        description='CZTS specific information.',
    )   
    
    OPV = SubSection(
        section_def=PhotoabsorberOPV,
        description='OPV specific information.',
    )
    
    DSSC = SubSection( 
        section_def=PhotoabsorberDSSC,
        description='DSSC specific information.',
    )   
    
    quantum_dot = SubSection(
        section_def=PhotoabsorberQD,
        description='Quantum dot specific information.',
    )
    
    ## Other subsections
    # Compounds in the layer
    components = SubSection(
        section_def=Component,
        description='The components in the layer.',
        repeats=True,
    )

    # Deposition procedure
    deposition_procedure = SubSection(
        section_def=DepositionProcedure,
        description='The deposition procedure of the layer.',
    )

    # Post deposition procedure
    post_deposition_procedure = SubSection(
        section_def=PostDepositionProcedure,    
        description='Post deposition procedure.',
    )

    ## Properties of the layer
    properties = SubSection(
        section_def=LayerProperties,
        description='Properties of the layer.',
    )

    # Sample history
    sample_history = SubSection(
        section_def=EnvironmentalConditionsDeposition,
        description="""A description of the conditions under which the sample have been stored between
        the finalization of the last layer and the deposition of this layer.""",
    )

    # Derived quantities
    layer_index = Quantity(
        type=int,
        shape=[],
        description="""The position in the device stack for the layer. Counted from the bottom. Can be populated automatically """,
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )    
    
    # TODO add functionality for populating the layer index
     
    def normalize(self, archive, logger):
        super().normalize(archive, logger)

### Master class putting everything together
class DeviceStack(StackSummary):
    """
    This is the master class for the device stack. It contains all the layers in the device stack.
    """
    
    ## Subsections
    layers = SubSection(
        section_def=Layer,
        description='The stack of layers in the device starting from the bottom.',
        repeats=True,
    )
  
    # TODO add functionality for populating the summary section with the data from the layers
     
    def normalize(self, archive, logger):
        super().normalize(archive, logger)

m_package.__init_metainfo__()