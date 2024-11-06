from spm.__wrapper__ import Runtime


def _write_brainvision_eeg(*args, **kwargs):
    """
      WRITE_BRAINVISION_EEG exports continuous EEG data to a BrainVision *.eeg  
        and corresponding *.vhdr file. The samples in the exported file are  
        multiplexed and stored in ieee-le float32 format.  
         
        Use as  
          write_brainvision_eeg(filename, hdr, dat, evt)  
         
        See also READ_BRAINVISION_EEG, READ_BRAINVISION_VHDR, READ_BRAINVISION_VMRK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_brainvision_eeg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_brainvision_eeg", *args, **kwargs, nargout=0)
