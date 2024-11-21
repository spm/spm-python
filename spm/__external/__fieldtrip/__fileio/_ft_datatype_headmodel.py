from spm.__wrapper__ import Runtime


def _ft_datatype_headmodel(*args, **kwargs):
    """
      FT_DATATYPE_HEADMODEL describes the FieldTrip MATLAB structure for a volume  
        conduction model of the head that can be used for forward computations of the EEG  
        potentials or the MEG fields. The volume conduction model represents the  
        geometrical and the conductive properties of the head. These determine how the  
        secondary (or impressed) currents flow and how these contribute to the model  
        potential or field.  
         
        A large number of forward solutions for the EEG and MEG are supported in FieldTrip,  
        each with its own specification of the MATLAB structure that describes the volume  
        conduction model of th ehead. It would be difficult to list all the possibilities  
        here. One common feature is that the volume conduction model should specify its  
        type, and that preferably it should specify the geometrical units in which it is  
        expressed (for example in mm, cm or m).  
         
        An example of an EEG volume conduction model with 4 concentric spheres is:  
         
        headmodel =  
               r: [86 88 94 100]  
               c: [0.33 1.79 0.042 0.33]  
               o: [0 0 0]  
            type: 'concentricspheres'  
            unit: 'mm'  
         
        An example of an MEG volume conduction model with a single sphere fitted to  
        the scalp with its center 4 cm above the line connecting the ears is:  
         
        headmodel =  
               r: [12]  
               o: [0 0 4]  
            type: 'singlesphere'  
            unit: 'cm'  
         
        For each of the methods XXX for the volume conduction model, a corresponding  
        function FT_HEADMODEL_XXX exists that contains all specific details and  
        references to literature that describes the implementation.  
         
        Required fields:  
          - type  
         
        Optional fields:  
          - unit  
         
        Deprecated fields:  
          - inner_skull_surface, source_surface, skin_surface, source, skin  
         
        Obsoleted fields:  
          - <none specified>  
         
        Revision history:  
         
        (2015/latest) Use the field name "pos" instead of "pnt" for vertex positions.  
         
        (2014) All numeric values are represented in double precision.  
         
        (2013) Always use the field "cond" for conductivity.  
         
        (2012) Use consistent names for the volume conductor type in the structure, the  
        documentation and for the actual implementation, e.g. bem_openmeeg -> openmeeg,  
        fem_simbio -> simbio, concentric -> concentricspheres. Deprecated the fields  
        that indicate the index of the innermost and outermost surfaces.  
         
        See also FT_PREPARE_HEADMODEL, FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP,  
        FT_DATATYPE_FREQ, FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE,   
        FT_DATATYPE_SPIKE, FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_datatype_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_headmodel", *args, **kwargs)
