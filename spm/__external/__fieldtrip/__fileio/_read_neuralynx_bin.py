from spm.__wrapper__ import Runtime


def _read_neuralynx_bin(*args, **kwargs):
    """
      READ_NEURALYNX_BIN  
         
        Use as  
          hdr = read_neuralynx_bin(filename)  
        or  
          dat = read_neuralynx_bin(filename, begsample, endsample)  
         
        This  is not a formal Neuralynx file format, but at the  
        F.C. Donders Centre we use it in conjunction with Neuralynx,  
        SPIKESPLITTING and SPIKEDOWNSAMPLE.  
         
        The first version of this file format contained in the first 8 bytes the  
        channel label as string. Subsequently it contained 32 bit integer values.  
         
        The second version of this file format starts with 8 bytes describing (as  
        a space-padded string) the data type. The channel label is contained in  
        the filename as dataset.chanlabel.bin.  
         
        The third version of this file format starts with 7 bytes describing (as  
        a zero-padded string) the data type, followed by the 8th byte which  
        describes the downscaling for the 8 and 16 bit integer representations.  
        The downscaling itself is represented as uint8 and should be interpreted as  
        the number of bits to shift. The channel label is contained in the  
        filename as dataset.chanlabel.bin.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_bin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_bin", *args, **kwargs)
