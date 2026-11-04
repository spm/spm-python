from spm._runtime import Runtime


def _read_brainvision_vmrk(*args, **kwargs):
    r"""
      READ_BRAINVISION_VMRK reads the markers and latencies  
        it returns the stimulus/response code and latency in ms.  
         
        Use as  
          event = read_brainvision_vmrk(filename)  
         
        See also READ_BRAINVISION_VHDR, READ_BRAINVISION_EEG  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_brainvision_vmrk.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_brainvision_vmrk", *args, **kwargs)
