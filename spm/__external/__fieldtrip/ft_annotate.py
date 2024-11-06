from spm.__wrapper__ import Runtime


def ft_annotate(*args, **kwargs):
    """
      FT_ANNOTATE returns the same output data as the user has provided as input, but allows  
        to add comments to that data structure. These comments are stored along with the other  
        provenance information and can be displayed with FT_ANALYSISPIPELINE. Adding comments  
        is especially useful if you have manually (i.e. in plain MATLAB) modified the data  
        structure, whereby some provenance information is missing.  
         
        Use as  
          outdata = ft_annotate(cfg, indata)  
        where the input data structure can be any of the FieldTrip data structures and  
        the configuration structure should contain  
          cfg.comment    = string  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_ANALYSISPIPELINE, FT_MATH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_annotate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_annotate", *args, **kwargs)
