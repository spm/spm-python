from spm.__wrapper__ import Runtime


def ft_reproducescript(*args, **kwargs):
    """
      FT_REPRODUCESCRIPT is a helper function to clean up the script and intermediate  
        datafiles that are the result from using the cfg.reproducescript option. You should  
        call this function all the way at the end of your analysis. This function will look  
        at all intermediate files in the output directory, remove input and output files  
        that are the same and update the script accordingly.  
         
        Use as  
          ft_reproducescript(cfg)  
         
        The configuration structure should contain  
          cfg.reproducescript = string, directory with the script and intermediate data  
         
        See also FT_ANALYSISPIPELINE, FT_DEFAULTS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_reproducescript.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_reproducescript", *args, **kwargs, nargout=0)
