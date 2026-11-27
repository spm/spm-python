from spm._runtime import Runtime


def _fixsampleinfo(*args, **kwargs):
    r"""
      FIXSAMPLEINFO checks for the existence of a sampleinfo and trialinfo field in the  
        provided raw or timelock data structure. If present, nothing is done; if absent,  
        this function attempts to reconstruct them based on either an trl-matrix present in  
        the cfg-tree, or by just assuming the trials are segments of a continuous  
        recording.  
         
        See also FT_DATATYPE_RAW, FT_DATATYPE_TIMELOCK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fixsampleinfo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixsampleinfo", *args, **kwargs)
