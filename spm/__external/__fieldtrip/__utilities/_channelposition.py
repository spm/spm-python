from spm._runtime import Runtime


def _channelposition(*args, **kwargs):
    r"""
      CHANNELPOSITION computes the channel positions and orientations from the  
        MEG coils, EEG electrodes or NIRS optodes  
         
        Use as  
          [pos, ori, lab] = channelposition(sens)  
        where sens is an gradiometer, electrode, or optode array.  
         
        See also FT_DATATYPE_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/channelposition.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("channelposition", *args, **kwargs)
