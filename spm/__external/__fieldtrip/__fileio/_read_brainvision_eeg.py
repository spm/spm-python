from spm._runtime import Runtime


def _read_brainvision_eeg(*args, **kwargs):
    r"""
      READ_BRAINVISION_EEG reads raw data from an EEG file and returns it as a Nchans x  
        Nsamples matrix.   
         
        Use as  
          dat = read_brainvision_eeg(filename, hdr, begsample, endsample)  
        where the header should be first read using READ_BRAINVISION_VHDR  
         
        See https://www.brainproducts.com/productdetails.php?id=21&tab=5 for the formal  
        specification.  
         
        See also READ_BRAINVISION_VHDR, READ_BRAINVISION_VMRK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_brainvision_eeg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_brainvision_eeg", *args, **kwargs)
