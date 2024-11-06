from spm.__wrapper__ import Runtime


def _mat2ades(*args, **kwargs):
    """
      write in the current folder ADES and DAT files from matrix in MATLAB workspace  
        data = matrix of data (nbchannel * time points) - the data have to be in microVolt  
        fileName = string of the output files without extension ; the ades and dat files will have the same name  
        FS = sampling rate  
        labels = cell-array with channel labels  
        labelType : 'EEG' or 'MEG'  
         
        Data are stored in a binary file which name is exactly the same than the header file except the extension: .dat  
        The samples are stored as float, 4 bytes per sample, little endian. The channels are multiplexed.  
         
        Sophie Chen - January 2014  
        Modified by Robert Oostenveld - February 2019  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/mat2ades.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mat2ades", *args, **kwargs, nargout=0)
