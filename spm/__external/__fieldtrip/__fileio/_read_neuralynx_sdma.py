from spm.__wrapper__ import Runtime


def _read_neuralynx_sdma(*args, **kwargs):
    """
      READ_NEURALYNX_SDMA read specified channels and samples from a Neuralynx splitted DMA dataset  
         
        Use as  
           [hdr] = read_neuralynx_sdma(dataset)  
           [dat] = read_neuralynx_sdma(dataset, begsample, endsample, chanindx)  
         
        The splitted DMA dataset is not a formal Neuralynx format, but at  
        the FCDC we use it in conjunction with SPIKEDOWNSAMPLE. The dataset  
        directory contains files, one for each channel, each containing a  
        8-byte header followed by the binary values for all samples. Commonly  
        the binary values are represented as int32, but it is possible to use  
        int16 or other numeric representations. The 8-byte header specifies the  
        numeric representation and the bitshift that should be applied (in case  
        of integer representations).  
         
        This function returns the electrophysiological data in AD units  
        and not in uV. You should look up the details of the headstage and  
        the Neuralynx amplifier and scale the values accordingly.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_sdma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_sdma", *args, **kwargs)
