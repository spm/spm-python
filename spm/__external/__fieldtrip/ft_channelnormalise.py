from spm.__wrapper__ import Runtime


def ft_channelnormalise(*args, **kwargs):
    """
      FT_CHANNELNORMALISE shifts and scales all channels of the the input data.  
        The default behavior is to subtract each channel's mean, and scale to a  
        standard deviation of 1, for each channel individually.  
         
        Use as  
          [dataout] = ft_channelnormalise(cfg, data)  
         
        The configuration can contain  
          cfg.channel = 'all', or a selection of channels  
          cfg.trials  = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.demean  = 'yes' or 'no' (or boolean value) (default = 'yes')  
          cfg.scale   = scalar value used for scaling (default = 1)  
          cfg.method  = 'perchannel', or 'acrosschannel', computes the  
                          standard deviation per channel, or across all channels.  
                          The latter method leads to the same scaling across  
                          channels and preserves topographical distributions  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_COMPONENTANALYSIS, FT_FREQBASELINE, FT_TIMELOCKBASELINE  
         
        Copyright (C) 2010, Jan-Mathijs Schoffelen  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_channelnormalise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_channelnormalise", *args, **kwargs)
