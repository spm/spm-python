from spm._runtime import Runtime


def ft_source2sparse(*args, **kwargs):
    r"""
      FT_SOURCE2SPARSE removes the grid locations outside the brain from the source  
        reconstruction, thereby saving memory.  
         
        This invalidates the fields that describe the grid, and also makes it  
        more difficult to make a plot of each of the slices of the source volume.  
        The original source structure can be recreated using FT_SOURCE2FULL.  
         
        Use as  
          [source] = ft_source2sparse(source)  
         
        See also FT_SOURCE2FULL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_source2sparse.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_source2sparse", *args, **kwargs)
