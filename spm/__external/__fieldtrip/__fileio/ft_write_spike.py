from spm._runtime import Runtime


def ft_write_spike(*args, **kwargs):
    r"""
      FT_WRITE_SPIKE writes animal electrophysiology spike timestamps and/or waveforms  
        to file  
         
        Use as  
          ft_write_spike(filename, spike, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'dataformat'          string, see below  
          'fsample'             sampling frequency of the waveforms  
          'chanindx'            index of selected channels  
          'TimeStampPerSample'  number of timestamps per sample  
         
        The supported dataformats are  
          neuralynx_nse  
          neuralynx_nts  
          plexon_nex  
          matlab  
         
        See also FT_READ_SPIKE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_write_spike.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_write_spike", *args, **kwargs, nargout=0)
