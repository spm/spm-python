from spm.__wrapper__ import Runtime


def ft_source2grid(*args, **kwargs):
    """
      FT_SOURCE2GRID removes the fields from a source structure that are  
        not necessary to reuse the dipole grid in another source estimation.  
         
        Use as  
          [grid] = ft_source2grid(source);  
         
        The resulting grid can be used in the configuration of another  
        run of FT_SOURCEANALYSIS.  
         
        See also FTSOURCE2SPARSE, FT_SOURCE2FULL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_source2grid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_source2grid", *args, **kwargs)
