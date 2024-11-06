from spm.__wrapper__ import Runtime


def _buffer_wait_dat(*args, **kwargs):
    """
      BUFFER_WAIT_DAT implementation that is also backwards compatibility with ft buffer version 1  
         
        Use as  
          available = buffer_wait_dat(selection, host, port)  
        where  
          selection(1) = nsamples, 0 indicates not to wait  
          selection(2) = nevents,  0 indicates not to wait  
          selection(3) = timeout in seconds  
         
        It returns a structure with the available nsamples and nevents.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/buffer_wait_dat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("buffer_wait_dat", *args, **kwargs)
