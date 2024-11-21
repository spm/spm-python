from spm.__wrapper__ import Runtime


def ft_create_buffer(*args, **kwargs):
    """
      FT_CREATE_BUFFER starts the thread with the TCP server attached to the local  
        MATLAB instance. The TCP server will listen to the specified network  
        port, and accept incoming read and write requests.  
         
        Use as  
          ft_create_buffer(port)  
        where port is the TCP port to which the server listens. The default port   
        number is 1972.  
          
        See also FT_DESTROY_BUFFER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_create_buffer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_create_buffer", *args, **kwargs, nargout=0)
