from spm.__wrapper__ import Runtime


def _read_brainvision_eeg(*args, **kwargs):
    """
      READ_BRAINVISION_EEG reads raw data from an EEG file and returns it as a Nchans x  
        Nsamples matrix.   
         
        Use as  
          dat = read_brainvision_eeg(filename, hdr, begsample, endsample)  
        where the header should be first read using READ_BRAINVISION_VHDR  
         
        See https://www.brainproducts.com/productdetails.php?id=21&tab=5 for the formal  
        specification.  
         
        See also READ_BRAINVISION_VHDR, READ_BRAINVISION_VMRK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_brainvision_eeg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_brainvision_eeg", *args, **kwargs)
