from spm.__wrapper__ import Runtime


def _ft_inside_headmodel(*args, **kwargs):
    """
      FT_INSIDE_HEADMODEL locates dipole locations inside/outside the source  
        compartment of a volume conductor model.  
         
        Use as  
          [inside] = ft_inside_headmodel(dippos, headmodel, ...)  
         
        The input should be  
          dippos      = Nx3 matrix with dipole positions  
          headmodel   = structure with volume conductor model  
        and the output is  
          inside      = boolean vector indicating for each dipole wether it is inside the source compartment  
         
        Additional optional input arguments should be given in key value pairs and can include  
          inwardshift = number  
          grad        = structure with gradiometer information, used for localspheres  
          headshape   = structure with headshape, used for old CTF localspheres strategy  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/ft_inside_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inside_headmodel", *args, **kwargs)
