from spm.__wrapper__ import Runtime


def _sampleinfo2trl(*args, **kwargs):
  """  SAMPLEINFO2TRL constructs the trial definition from the sampleinfo, the time axes  
    and optionally from the trialinfo  
     
    Use as  
      trl = sampleinfo2trl(data)  
     
    See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/sampleinfo2trl.m)
  """

  return Runtime.call("sampleinfo2trl", *args, **kwargs)
