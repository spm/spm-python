from spm._runtime import Runtime


def _buffer_wait_dat(*args, **kwargs):
    r"""
      BUFFER_WAIT_DAT implementation that is also backwards compatibility with ft buffer version 1  
         
        Use as  
          available = buffer_wait_dat(selection, host, port)  
        where  
          selection(1) = nsamples, 0 indicates not to wait  
          selection(2) = nevents,  0 indicates not to wait  
          selection(3) = timeout in seconds  
         
        It returns a structure with the available nsamples and nevents.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/buffer_wait_dat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("buffer_wait_dat", *args, **kwargs)
