from spm.__wrapper__ import Runtime


def dccnpath(*args, **kwargs):
    """
      DCCNPATH manages the filename and path for test files. It helps to locate and read  
        test file from Linux, Windows or macOS computers both inside and outside the DCCN.  
         
        Use as  
          filename = dccnpath(filename)  
        where the input filename corresponds to the test data on the DCCN cluster and the  
        output filename corresponds to the local file including the full path where the  
        test data is available.  
         
        The test data location on the DCCN cluster is '/home/common/matlab/fieldtrip/data'  
        and the specification of the input filename MUST start with this.  
         
        This function will search-and-replace the location on the DCCN cluster by the  
        location that applies to your computer. If needed, it will replace '/home' by 'H:'  
        and will replace forward by backward slashes.  
         
        In case you have a local copy of the data, or if you are inside the DCCN and have  
        mounted the '/home' drive on another letter than 'H:', you should override the  
        default location using  
           global ft_default  
           ft_default.dccnpath = '/your/copy';  
         
        If you do not have a local copy and do not define ft_default.dccnpath manually,  
        then dccnpath will automatically use a temporary directory and try to download the  
        data.  
         
        See also WHICH, WEBSAVE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/dccnpath.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dccnpath", *args, **kwargs)
