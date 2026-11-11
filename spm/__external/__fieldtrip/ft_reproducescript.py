from spm._runtime import Runtime


def ft_reproducescript(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_reproducescript.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_reproducescript", *args, **kwargs, nargout=0)
