from spm._runtime import Runtime


def _artifact_level(*args, **kwargs):
    r"""
      This function is shared between FT_REJECTVISUAL, FT_BADCHANNEL,   
        FT_BADSEGMENT, and FT_BADDATA  
         
        Use as  
          level = artifact_level(dat, metric, mval, sd, connectivity)  
        where  
          dat           = nchan*ntime, data of a single trial  
          metric        = string, see below in the code  
          mval          = mean value over all trials  
          sd            = standard deviation over all trials  
          connectivity  = nchan*nchan connectivity matrix  
        and  
          level         = nchan*1 vector with values  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/artifact_level.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("artifact_level", *args, **kwargs)
