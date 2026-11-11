from spm._runtime import Runtime


def _ft_convert_units(*args, **kwargs):
    r"""
      FT_CONVERT_UNITS changes the geometrical dimension to the specified SI unit.  
        The units of the input object is determined from the structure field  
        object.unit, or is estimated based on the spatial extend of the structure,  
        e.g. a volume conduction model of the head should be approximately 20 cm large.  
         
        Use as  
          [output] = ft_convert_units(input, target)  
         
        The following input data structures are supported  
          electrode or gradiometer array, see FT_DATATYPE_SENS  
          volume conductor, see FT_DATATYPE_HEADMODEL  
          anatomical mri, see FT_DATATYPE_VOLUME  
          segmented mri, see FT_DATATYPE_SEGMENTATION  
          source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL  
         
        The possible target units are 'm', 'cm ' or 'mm'. If no target units are specified,  
        this function will only determine the geometrical units of the input object.  
         
        See also FT_DETERMINE_UNITS, FT_DETERMINE_COORDSYS, FT_CONVERT_COORDSYS, FT_PLOT_AXES, FT_PLOT_XXX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ft_convert_units.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_convert_units", *args, **kwargs)
