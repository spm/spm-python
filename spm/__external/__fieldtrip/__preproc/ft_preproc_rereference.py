from spm.__wrapper__ import Runtime


def ft_preproc_rereference(*args, **kwargs):
    """
      FT_PREPROC_REREFERENCE computes the average reference over all EEG channels  
        or rereferences the data to the selected channels  
         
        Use as  
          [dat] = ft_preproc_rereference(dat, refchan, method, handlenan, leadfield)  
        where  
          dat        data matrix (Nchans X Ntime)  
          refchan    vector with indices of the new reference channels, or 'all'  
          method     string, can be 'avg', 'median', or 'rest'  
          handlenan  boolean, can be false (default) or true  
          leadfield  leadfield matrix (required for REST, otherwise empty)  
         
        If the new reference channel(s) are not specified, the data will be  
        rereferenced to the average of all channels.  
         
        If the data that is used to compute the new reference contains NaNs,  
        these will spread to all output channels, unless the handlenan flag has  
        been set to true.  
         
        For REST the leadfield should be a matrix (channels X sources)  
        which is calculated by using the forward theory, based on  
        the electrode montage, head model and equivalent source  
        model.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_rereference.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_rereference", *args, **kwargs)
