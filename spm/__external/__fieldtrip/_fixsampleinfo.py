from spm.__wrapper__ import Runtime


def _fixsampleinfo(*args, **kwargs):
    """
      FIXSAMPLEINFO checks for the existence of a sampleinfo and trialinfo field in the  
        provided raw or timelock data structure. If present, nothing is done; if absent,  
        this function attempts to reconstruct them based on either an trl-matrix present in  
        the cfg-tree, or by just assuming the trials are segments of a continuous  
        recording.  
         
        See also FT_DATATYPE_RAW, FT_DATATYPE_TIMELOCK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixsampleinfo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixsampleinfo", *args, **kwargs)
