from spm._runtime import Runtime


def _sampleinfo2trl(*args, **kwargs):
    r"""
      SAMPLEINFO2TRL constructs the trial definition from the sampleinfo, the time axes  
        and optionally from the trialinfo  
         
        Use as  
          trl = sampleinfo2trl(data)  
         
        See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/sampleinfo2trl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sampleinfo2trl", *args, **kwargs)
