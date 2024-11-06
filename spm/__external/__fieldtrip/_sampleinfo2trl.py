from spm.__wrapper__ import Runtime


def _sampleinfo2trl(*args, **kwargs):
    """
      SAMPLEINFO2TRL constructs the trial definition from the sampleinfo, the time axes  
        and optionally from the trialinfo  
         
        Use as  
          trl = sampleinfo2trl(data)  
         
        See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/sampleinfo2trl.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sampleinfo2trl", *args, **kwargs)
