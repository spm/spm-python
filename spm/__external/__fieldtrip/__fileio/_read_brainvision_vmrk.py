from spm.__wrapper__ import Runtime


def _read_brainvision_vmrk(*args, **kwargs):
  """  READ_BRAINVISION_VMRK reads the markers and latencies  
    it returns the stimulus/response code and latency in ms.  
     
    Use as  
      event = read_brainvision_vmrk(filename)  
     
    See also READ_BRAINVISION_VHDR, READ_BRAINVISION_EEG  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_brainvision_vmrk.m)
  """

  return Runtime.call("read_brainvision_vmrk", *args, **kwargs)
