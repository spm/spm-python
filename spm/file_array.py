from mpython import MatlabClass
from spm._runtime import Runtime, RuntimeMixin


class file_array(RuntimeMixin, MatlabClass):
    def __init__(self, *args, **kwargs):
        r"""
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
            
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/file_array.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        super().__init__()

    def cat(self, *args, **kwargs):
        r"""
          Concatenate file_array objects.  The result is a non-simple object  
            that can no longer be reshaped.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/cat.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("cat", self._as_matlab_object(), *args, **kwargs)

    def ctranspose(self, *args, **kwargs):
        r"""
          Transposing not allowed  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/ctranspose.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("ctranspose", self._as_matlab_object(), *args, **kwargs)

    def disp(self, *args, **kwargs):
        r"""
          Display a file_array object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/disp.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("disp", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def display(self, *args, **kwargs):
        r"""
          Display a file_array object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/display.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def double(self, *args, **kwargs):
        r"""
          Convert to double precision  
            FORMAT double(fa)  
            fa - a file_array  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/double.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("double", self._as_matlab_object(), *args, **kwargs)

    def end(self, *args, **kwargs):
        r"""
          Overloaded end function for file_array objects.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/end.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("end", self._as_matlab_object(), *args, **kwargs)

    def fieldnames(self, *args, **kwargs):
        r"""
          Fieldnames of a file-array object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/fieldnames.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def full(self, *args, **kwargs):
        r"""
          Convert to numeric form  
            FORMAT full(fa)  
            fa - a file_array  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/full.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("full", self._as_matlab_object(), *args, **kwargs)

    def horzcat(self, *args, **kwargs):
        r"""
          Horizontal concatenation of file_array objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/horzcat.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("horzcat", self._as_matlab_object(), *args, **kwargs)

    def initialise(self, *args, **kwargs):
        r"""
          Initialise file on disk  
             
            This creates a file on disk with the appropriate size by explicitly  
            writing data to prevent a sparse file.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/initialise.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("initialise", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def isnan(self, *args, **kwargs):
        r"""
          Logical array containing true where the elements of file_array are NaN's  
            FORMAT isnan(fa)  
            fa - a file_array  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/isnan.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("isnan", self._as_matlab_object(), *args, **kwargs)

    def length(self, *args, **kwargs):
        r"""
          Overloaded length function for file_array objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/length.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("length", self._as_matlab_object(), *args, **kwargs)

    def loadobj(self, *args, **kwargs):
        r"""
          loadobj for file_array class  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/loadobj.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("loadobj", self._as_matlab_object(), *args, **kwargs)

    def ndims(self, *args, **kwargs):
        r"""
          Number of dimensions  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/ndims.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("ndims", self._as_matlab_object(), *args, **kwargs)

    def numel(self, *args, **kwargs):
        r"""
          Number of simple file arrays involved.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/numel.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("numel", self._as_matlab_object(), *args, **kwargs)

    def numeric(self, *args, **kwargs):
        r"""
          Convert to numeric form  
            FORMAT numeric(fa)  
            fa - a file_array  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/numeric.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("numeric", self._as_matlab_object(), *args, **kwargs)

    def permute(self, *args, **kwargs):
        r"""
          file_array objects can not be permuted  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/permute.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("permute", self._as_matlab_object(), *args, **kwargs)

    def reshape(self, *args, **kwargs):
        r"""
          Overloaded reshape function for file_array objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/reshape.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("reshape", self._as_matlab_object(), *args, **kwargs)

    def size(self, *args, **kwargs):
        r"""
          Method 'size' for file_array objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/size.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("size", self._as_matlab_object(), *args, **kwargs)

    def subsasgn(self, *args, **kwargs):
        r"""
          Overloaded subsasgn function for file_array objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/subsasgn.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        r"""
          SUBSREF Subscripted reference  
            An overloaded function...  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/subsref.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def transpose(self, *args, **kwargs):
        r"""
          file_array objects can not be transposed  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/transpose.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("transpose", self._as_matlab_object(), *args, **kwargs)

    def vertcat(self, *args, **kwargs):
        r"""
          Vertical concatenation of file_array objects.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/vertcat.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("vertcat", self._as_matlab_object(), *args, **kwargs)

    def _datatypes(self, *args, **kwargs):
        r"""
          Dictionary of datatypes  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/datatypes.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("datatypes", self._as_matlab_object(), *args, **kwargs)

    def _dim(self, *args, **kwargs):
        r"""
          file_array's dimension property  
            For getting the value  
            dat = dim(obj)  
             
            For setting the value  
            obj = dim(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/dim.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("dim", self._as_matlab_object(), *args, **kwargs)

    def _dtype(self, *args, **kwargs):
        r"""
          file_array's dtype property  
            FORMAT varargout = dtype(varargin)  
            For getting the value  
            dat = dtype(obj)  
             
            For setting the value  
            obj = dtype(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/dtype.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("dtype", self._as_matlab_object(), *args, **kwargs)

    def _file2mat(self, *args, **kwargs):
        r"""
          Function for reading from file_array objects  
            FORMAT val = file2mat(a,ind1,ind2,ind3,...)  
            a      - file_array object  
            indx   - indices for dimension x (int64)  
            val    - the read values  
             
            This function is normally called by file_array/subsref.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/file2mat.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("file2mat", self._as_matlab_object(), *args, **kwargs)

    def _fname(self, *args, **kwargs):
        r"""
          file_array's fname property  
            For getting the value  
            dat = fname(obj)  
             
            For setting the value  
            obj = fname(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/fname.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("fname", self._as_matlab_object(), *args, **kwargs)

    def _init(self, *args, **kwargs):
        r"""
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
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/init.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("init", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def _mat2file(self, *args, **kwargs):
        r"""
          Function for writing to file_array objects  
            FORMAT mat2file(a,val,ind1,ind2,ind3,...)  
            a      - file_array object  
            val    - values to write  
            indx   - indices for dimension x (int32)  
             
            This function is normally called by file_array/subsasgn.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/mat2file.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mat2file", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def _mystruct(self, *args, **kwargs):
        r"""
         __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/mystruct.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mystruct", self._as_matlab_object(), *args, **kwargs)

    def _offset(self, *args, **kwargs):
        r"""
          file_array's offset property  
            For getting the value  
            dat = offset(obj)  
             
            For setting the value  
            obj = offset(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/offset.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("offset", self._as_matlab_object(), *args, **kwargs)

    def _permission(self, *args, **kwargs):
        r"""
          file_array's permission property  
            For getting the value  
            dat = permission(obj)  
             
            For setting the value  
            obj = permission(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/permission.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("permission", self._as_matlab_object(), *args, **kwargs)

    def _resize_scales(self, *args, **kwargs):
        r"""
          Resize scalefactors   
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/resize_scales.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("resize_scales", self._as_matlab_object(), *args, **kwargs)

    def _scl_inter(self, *args, **kwargs):
        r"""
          file_array's scl_inter property  
            For getting the value  
            dat = scl_inter(obj)  
             
            For setting the value  
            obj = scl_inter(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/scl_inter.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("scl_inter", self._as_matlab_object(), *args, **kwargs)

    def _scl_slope(self, *args, **kwargs):
        r"""
          file_array's scl_slope property  
            For getting the value  
            dat = scl_slope(obj)  
             
            For setting the value  
            obj = scl_slope(obj,dat)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@file_array/private/scl_slope.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("scl_slope", self._as_matlab_object(), *args, **kwargs)
