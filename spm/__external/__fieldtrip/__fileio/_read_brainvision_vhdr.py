from spm.__wrapper__ import Runtime


def _read_brainvision_vhdr(*args, **kwargs):
    """
      READ_BRAINVISION_VHDR reads the known items from the BrainVision EEG  
        header file and returns them in a structure.  
         
        Use as  
          vhdr = read_brainvision_vhdr(filename)  
         
        See also READ_BRAINVISION_EEG, READ_BRAINVISION_VMRK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_brainvision_vhdr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_brainvision_vhdr", *args, **kwargs)
