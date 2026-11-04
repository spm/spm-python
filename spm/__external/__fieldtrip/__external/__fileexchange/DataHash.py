from spm._runtime import Runtime


def DataHash(*args, **kwargs):
    r"""
      DATAHASH - Checksum for Matlab array of any type  
        This function creates a hash value for an input of any type. The type and  
        dimensions of the input are considered as default, such that UINT8([0,0]) and  
        UINT16(0) have different hash values. Nested STRUCTs and CELLs are parsed  
        recursively.  
         
        Hash = DataHash(Data, Opts...)  
        INPUT:  
          Data: Array of these built-in types:  
                  (U)INT8/16/32/64, SINGLE, DOUBLE, (real/complex, full/sparse)  
                  CHAR, LOGICAL, CELL (nested), STRUCT (scalar or array, nested),  
                  function_handle, string.  
          Opts: Char strings to specify the method, the input and theoutput types:  
                Input types:  
                   'array': The contents, type and size of the input [Data] are  
                            considered  for the creation of the hash. Nested CELLs  
                            and STRUCT arrays are parsed recursively. Empty arrays of  
                            different type reply different hashs.  
                   'file':  [Data] is treated as file name and the hash is calculated  
                            for the files contents.  
                   'bin':   [Data] is a numerical, LOGICAL or CHAR array. Only the  
                            binary contents of the array is considered, such that  
                            e.g. empty arrays of different type reply the same hash.  
                   'ascii': Same as 'bin', but only the 8-bit ASCII part of the 16-bit  
                            Matlab CHARs is considered.  
                Output types:  
                   'hex', 'HEX':      Lower/uppercase hexadecimal string.  
                   'double', 'uint8': Numerical vector.  
                   'base64':          Base64.  
                   'short':           Base64 without padding.  
                Hashing method:  
                   'SHA-1', 'SHA-256', 'SHA-384', 'SHA-512', 'MD2', 'MD5'.  
                   Call DataHash without inputs to get a list of available methods.  
         
                Default: 'MD5', 'hex', 'array'  
         
        OUTPUT:  
          Hash: String, DOUBLE or UINT8 vector. The length depends on the hashing  
                method.  
                If DataHash is called without inputs, a struct is replied:  
                  .HashVersion: Version number of the hashing method of this tool. In  
                     case of bugs or additions, the output can change.  
                  .Date: Date of release of the current HashVersion.  
                  .HashMethod: Cell string of the recognized hash methods.  
         
        EXAMPLES:  
        % Default: MD5, hex:  
          DataHash([])                      % 5b302b7b2099a97ba2a276640a192485  
        % MD5, Base64:  
          DataHash(int32(1:10), 'short', 'MD5')  % +tJN9yeF89h3jOFNN55XLg  
        % SHA-1, Base64:  
          S.a = uint8([]);  
          S.b = {{1:10}, struct('q', uint64(415))};  
          DataHash(S, 'SHA-1', 'HEX')       % 18672BE876463B25214CA9241B3C79CC926F3093  
        % SHA-1 of binary values:  
          DataHash(1:8, 'SHA-1', 'bin')     % 826cf9d3a5d74bbe415e97d4cecf03f445f69225  
        % SHA-256, consider ASCII part only (Matlab's CHAR has 16 bits!):  
          DataHash('abc', 'SHA-256', 'ascii')  
              % ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad  
        % Or equivalently by converting the input to UINT8:  
          DataHash(uint8('abc'), 'SHA-256', 'bin')  
         
        NOTES:  
          Function handles and user-defined objects cannot be converted uniquely:  
          - The subfunction ConvertFuncHandle uses the built-in function FUNCTIONS,  
            but the replied struct can depend on the Matlab version.  
          - It is tried to convert objects to UINT8 streams in the subfunction  
            ConvertObject. A conversion by STRUCT() might be more appropriate.  
          Adjust these subfunctions on demand.  
         
          MATLAB CHARs have 16 bits! Use Opt.Input='ascii' for comparisons with e.g.  
          online hash generators.  
         
          Matt Raum suggested this for e.g. user-defined objects:  
            DataHash(getByteStreamFromArray(Data))  
          This works very well, but unfortunately getByteStreamFromArray is  
          undocumented, such that it might vanish in the future or reply different  
          output.  
         
          For arrays the calculated hash value might be changed in new versions.  
          Calling this function without inputs replies the version of the hash.  
         
          The older style for input arguments is accepted also: Struct with fields  
            'Input', 'Method', 'OutFormat'.  
         
          The C-Mex function GetMD5 is 2 to 100 times faster, but obtains MD5 only:  
          http://www.mathworks.com/matlabcentral/fileexchange/25921  
         
        Tested: Matlab 2009a, 2015b(32/64), 2016b, 2018b, Win7/10  
        Author: Jan Simon, Heidelberg, (C) 2011-2019 matlab.2010(a)n(MINUS)simon.de  
         
        See also: TYPECAST, CAST.  
         
        Michael Kleder, "Compute Hash", no structs and cells:  
          http://www.mathworks.com/matlabcentral/fileexchange/8944  
        Tim, "Serialize/Deserialize", converts structs and cells to a byte stream:  
          http://www.mathworks.com/matlabcentral/fileexchange/29457  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/DataHash.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DataHash", *args, **kwargs)
