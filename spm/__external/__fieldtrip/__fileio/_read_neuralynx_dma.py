from spm.__wrapper__ import Runtime


def _read_neuralynx_dma(*args, **kwargs):
    """
      READ_NEURALYNX_DMA reads specified samples and channels data from a Neuralynx DMA log file  
         
        Use as  
           [hdr] = read_neuralynx_dma(filename)  
           [dat] = read_neuralynx_dma(filename, begsample, endsample)  
           [dat] = read_neuralynx_dma(filename, begsample, endsample, chanindx)  
         
        The channel specification can be a vector with indices, or a single string with the value  
           'all', 'stx', 'pid', 'siz', 'tsh', 'tsl',  
           'cpu', 'ttl', 'x01',  ...,  'x10'  
         
        This function returns the electrophysiological data in AD units  
        and not in uV. You should look up the details of the headstage and  
        the Neuralynx amplifier and scale the values accordingly.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_dma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_dma", *args, **kwargs)
