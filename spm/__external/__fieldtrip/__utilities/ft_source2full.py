from spm._runtime import Runtime


def ft_source2full(*args, **kwargs):
    r"""
      FT_SOURCE2FULL recreates the grid locations outside the brain in the source  
        reconstruction, so that the source volume again describes the full grid.  
        This undoes the memory savings that can be achieved using FT_SOURCE2SPARSE  
        and makes it possible again to plot the source volume and save it to an  
        external file.  
         
        Use as  
          [source] = ft_source2full(source)  
         
        See also FT_SOURCE2SPARSE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_source2full.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_source2full", *args, **kwargs)
