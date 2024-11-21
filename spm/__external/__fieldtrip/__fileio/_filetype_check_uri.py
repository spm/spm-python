from spm.__wrapper__ import Runtime


def _filetype_check_uri(*args, **kwargs):
    """
      FILETYPE_CHECK_URI  
         
        Use as  
           status = filetype_check_uri(filename, type)  
         
        Supported URIs are  
          buffer://<host>:<port>  
          fifo://<filename>  
          global://<varname>  
          mysql://<user>:<password>@<host>:<port>  
          rfb://<password>@<host>:<port>  
          serial:<port>?key1=value1&key2=value2&...  
          shm://<filename>  
          tcp://<host>:<port>  
          udp://<host>:<port>  
          ftp://<user>@<host>/path  
          sftp://<user>@<host>/path  
         
        The URI schemes supproted by these function are not the official schemes.  
        See the documentation included inside this function for more details.  
        RFC4395 defines an IANA-maintained registry of URI Schemes. See also  
        http://www.iana.org/assignments/uri-schemes.html and  
        http://en.wikipedia.org/wiki/URI_scheme#Generic_syntax.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/filetype_check_uri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("filetype_check_uri", *args, **kwargs)
