from spm.__wrapper__ import Runtime


def _handle_atlas_input(*args, **kwargs):
    """
      HANDLE_ATLAS_INPUT handles user input to specify volumetric atlases in some coordinate. It  
        does two things: (1) call FT_READ_ATLAS to read the atlas from file, if it is specified as a  
        string input, and (2) if the optional second data input argument is provided, and it has a  
        coordsys and/or unit field, checks the coordinate systems and units of the atlas and the  
        input against each other.  
         
        This code was taken from ft_sourceplot to avoid duplication upon adding similar functionality  
        to ft_sourceplot_interactive.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/handle_atlas_input.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("handle_atlas_input", *args, **kwargs)
