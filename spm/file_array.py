from spm.__wrapper__ import Runtime, MatlabClassWrapper


class file_array(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          Function for creating file_array objects.  
            FORMAT a = file_array(fname,dim,dtype,offset,scl_slope,scl_inter,permission)  
            a          - file_array object  
            fname      - filename  
            dim        - dimensions (default = [0 0] )  
            dtype      - datatype   (default = 'uint8-le')  
            offset     - offset into file (default = 0)  
            scl_slope  - scalefactor (default = 1)  
            scl_inter  - DC offset, such that dat = raw*scale + inter (default = 0)  
            permission - Write permission, either 'rw' or 'ro' (default = 'rw')  
           __________________________________________________________________________  
            
              Documentation for file_array  
                 doc file_array  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/file_array.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("file_array", *args, **kwargs)
            
        super().__init__(_objdict)

    def _datatypes(self, *args, **kwargs):
        """
          Dictionary of datatypes  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/datatypes.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("datatypes", *args, **kwargs)

    def _dim(self, *args, **kwargs):
        """
          file_array's dimension property  
            For getting the value  
            dat = dim(obj)  
             
            For setting the value  
            obj = dim(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/dim.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("dim", *args, **kwargs)

    def _dtype(self, *args, **kwargs):
        """
          file_array's dtype property  
            FORMAT varargout = dtype(varargin)  
            For getting the value  
            dat = dtype(obj)  
             
            For setting the value  
            obj = dtype(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/dtype.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("dtype", *args, **kwargs)

    def _file2mat(self, *args, **kwargs):
        """
          Function for reading from file_array objects  
            FORMAT val = file2mat(a,ind1,ind2,ind3,...)  
            a      - file_array object  
            indx   - indices for dimension x (int64)  
            val    - the read values  
             
            This function is normally called by file_array/subsref.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/file2mat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("file2mat", *args, **kwargs)

    def _fname(self, *args, **kwargs):
        """
          file_array's fname property  
            For getting the value  
            dat = fname(obj)  
             
            For setting the value  
            obj = fname(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/fname.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fname", *args, **kwargs)

    def _init(self, *args, **kwargs):
        """
          Initialise binary file on disk  
            FORMAT init(fname, nbytes[, opts])  
            fname   - filename  
            nbytes  - data size {bytes}  
            opts    - optional structure with fields:  
              .offset   - file offset {bytes} [default: 0]  
              .wipe     - overwrite existing values with 0 [default: false]  
              .truncate - truncate file if larger than requested size [default: true]  
             
            This function is normally called by file_array/initialise  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/init.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("init", *args, **kwargs, nargout=0)

    def _mat2file(self, *args, **kwargs):
        """
          Function for writing to file_array objects  
            FORMAT mat2file(a,val,ind1,ind2,ind3,...)  
            a      - file_array object  
            val    - values to write  
            indx   - indices for dimension x (int32)  
             
            This function is normally called by file_array/subsasgn.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/mat2file.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mat2file", *args, **kwargs, nargout=0)

    def _mystruct(self, *args, **kwargs):
        """
         __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/mystruct.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mystruct", *args, **kwargs)

    def _offset(self, *args, **kwargs):
        """
          file_array's offset property  
            For getting the value  
            dat = offset(obj)  
             
            For setting the value  
            obj = offset(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/offset.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("offset", *args, **kwargs)

    def _permission(self, *args, **kwargs):
        """
          file_array's permission property  
            For getting the value  
            dat = permission(obj)  
             
            For setting the value  
            obj = permission(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/permission.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("permission", *args, **kwargs)

    def _resize_scales(self, *args, **kwargs):
        """
          Resize scalefactors   
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/resize_scales.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("resize_scales", *args, **kwargs)

    def _scl_inter(self, *args, **kwargs):
        """
          file_array's scl_inter property  
            For getting the value  
            dat = scl_inter(obj)  
             
            For setting the value  
            obj = scl_inter(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/scl_inter.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("scl_inter", *args, **kwargs)

    def _scl_slope(self, *args, **kwargs):
        """
          file_array's scl_slope property  
            For getting the value  
            dat = scl_slope(obj)  
             
            For setting the value  
            obj = scl_slope(obj,dat)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@file_array/private/scl_slope.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("scl_slope", *args, **kwargs)
