from spm.__wrapper__ import Runtime


def _channelposition(*args, **kwargs):
    """
      CHANNELPOSITION computes the channel positions and orientations from the  
        MEG coils, EEG electrodes or NIRS optodes  
         
        Use as  
          [pos, ori, lab] = channelposition(sens)  
        where sens is an gradiometer, electrode, or optode array.  
         
        See also FT_DATATYPE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/channelposition.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("channelposition", *args, **kwargs)
