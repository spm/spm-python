from spm.__wrapper__ import Runtime


def ft_source2sparse(*args, **kwargs):
    """
      FT_SOURCE2SPARSE removes the grid locations outside the brain from the source  
        reconstruction, thereby saving memory.  
         
        This invalidates the fields that describe the grid, and also makes it  
        more difficult to make a plot of each of the slices of the source volume.  
        The original source structure can be recreated using FT_SOURCE2FULL.  
         
        Use as  
          [source] = ft_source2sparse(source)  
         
        See also FT_SOURCE2FULL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_source2sparse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_source2sparse", *args, **kwargs)
