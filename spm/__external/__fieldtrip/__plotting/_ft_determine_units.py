from spm.__wrapper__ import Runtime


def _ft_determine_units(*args, **kwargs):
    """
      FT_DETERMINE_UNITS tries to determine the units of a geometrical object by  
        looking at its size and by relating this to the approximate size of the  
        human head according to the following table:  
          from  0.050 to   0.500 -> meter  
          from  0.500 to   5.000 -> decimeter  
          from  5.000 to  50.000 -> centimeter  
          from 50.000 to 500.000 -> millimeter  
         
        Use as  
          [output] = ft_determine_units(input)  
         
        The following input data structures are supported  
          electrode or gradiometer array, see FT_DATATYPE_SENS  
          volume conduction model, see FT_DATATYPE_HEADMODEL  
          source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL  
          anatomical mri, see FT_DATATYPE_VOLUME  
          segmented mri, see FT_DATATYPE_SEGMENTATION  
          anatomical or functional atlas, see FT_READ_ATLAS  
         
        This function will add the field 'unit' to the output data structure with the  
        possible values 'm', 'cm ' or 'mm'.  
         
        See also FT_CONVERT_UNITS, FT_DETERMINE_COODSYS, FT_CONVERT_COORDSYS, FT_PLOT_AXES, FT_PLOT_XXX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/ft_determine_units.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_determine_units", *args, **kwargs)
