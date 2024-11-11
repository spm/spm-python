from spm.__wrapper__ import Runtime


def ft_combineplanar(*args, **kwargs):
    """
      FT_COMBINEPLANAR computes the planar gradient magnitude over both directions  
        combining the two gradients at each sensor to a single positive-valued number. This  
        can be done for single-trial/averaged planar gradient ERFs or single-trial/averaged  
        TFRs.  
         
        Use as  
          [data] = ft_combineplanar(cfg, data)  
        where data contains an averaged planar-gradient ERF or single-trial or  
        averaged TFRs.  
         
        The configuration can contain  
          cfg.method         = 'sum', 'svd', 'abssvd', or 'complex' (default = 'sum')  
          cfg.updatesens     = 'no' or 'yes' (default = 'yes')  
        and for timelocked input data (i.e. ERFs), the configuration can also contain  
          cfg.demean         = 'yes' or 'no' (default = 'no')  
          cfg.baselinewindow = [begin end]  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_MEGPLANAR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_combineplanar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_combineplanar", *args, **kwargs)
