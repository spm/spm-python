from spm.__wrapper__ import Runtime


def fil_io(*args, **kwargs):
    """
      Function handles for I/O, used by fil_train  
        FORMAT io = fil_io  
        io - Structure of function handles  
             io.init  - initialise  
             io.block - read in a block of data  
             io.patch - extract a patch from the read in block  
         
        FORMAT dat = io.block(dat,x0,y0,z0)  
        dat - data structure  
        x0  - x indices  
        y0  - y indices  
        z0  - z indices  
         
        FORMAT [X,J,C] = io.patch(dat,x0,y0,z0, r)  
        dat  - data structure  
        x0   - x indices  
        y0   - y indices  
        z0   - z indices  
        r    - search radius  
         
        FORMAT dat = io.init(varargin)  
        varargin - arrays of input filenames containing output from  
                   fil_push_train_data  
        dat      - data structure  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_io.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_io", *args, **kwargs)
