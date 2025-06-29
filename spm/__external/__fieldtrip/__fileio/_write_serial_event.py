from spm._runtime import Runtime


def _write_serial_event(*args, **kwargs):
    """
      WRITE_SERIAL_EVENT  
         
        changed A.Hadjipapas 2010  
         
        write to phyiscal serial port  
        serial port on windows or linux platform  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_serial_event.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_serial_event", *args, **kwargs, nargout=0)
