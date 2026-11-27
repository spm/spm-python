from mpython import MatlabClass
from spm._runtime import Runtime, RuntimeMixin


class gifti(RuntimeMixin, MatlabClass):
    def __init__(self, *args, **kwargs):
        r"""
          GIfTI Geometry file format class  
            Geometry format under the Neuroimaging Informatics Technology Initiative  
            (NIfTI):  
                            http://www.nitrc.org/projects/gifti/  
                                 http://nifti.nimh.nih.gov/  
           __________________________________________________________________________  
            
              Documentation for gifti  
                 doc gifti  
            
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/gifti.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        super().__init__()

    def display(self, *args, **kwargs):
        r"""
          Display method for GIfTI objects  
            FORMAT display(this)  
            this   -  GIfTI object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/display.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def export(self, *args, **kwargs):
        r"""
          Export a GIfTI object into specific MATLAB struct  
            FORMAT s = export(this,target)  
            this   - GIfTI object  
            target - string describing target output [default: MATLAB]  
            s      - a structure containing public fields of the object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/export.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("export", self._as_matlab_object(), *args, **kwargs)

    def fieldnames(self, *args, **kwargs):
        r"""
          Fieldnames method for GIfTI objects  
            FORMAT names = fieldnames(this)  
            this   -  GIfTI object  
            names  -  field names  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/fieldnames.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def isfield(self, *args, **kwargs):
        r"""
          Isfield method for GIfTI objects  
            FORMAT tf = isfield(this,field)  
            this   -  GIfTI object  
            field  -  string of cell array  
            tf     -  logical array  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/isfield.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("isfield", self._as_matlab_object(), *args, **kwargs)

    def plot(self, *args, **kwargs):
        r"""
          plot method for GIfTI objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/plot.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("plot", self._as_matlab_object(), *args, **kwargs)

    def save(self, *args, **kwargs):
        r"""
          Save GIfTI object in a GIfTI format file  
            FORMAT save(this,filename,encoding)  
            this      - GIfTI object  
            filename  - name of GIfTI file to be created [Default: 'untitled.gii']  
            encoding  - optional argument to specify encoding format, among  
                        ASCII, Base64Binary, GZipBase64Binary, ExternalFileBinary.  
                        [Default: 'GZipBase64Binary']  
            ordering  - optional argument to specify array element ordering, among  
                        ColumnMajorOrder, RowMajorOrder  
                        [Default: 'ColumnMajorOrder']  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/save.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("save", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def saveas(self, *args, **kwargs):
        r"""
          Save GIfTI object in external file format  
            FORMAT saveas(this,filename,format)  
            this      - GIfTI object  
            filename  - name of file to be created [Default: 'untitled.vtk']  
            format    - optional argument to specify encoding format, among  
                        VTK (.vtk,.vtp), Collada (.dae), IDTF (.idtf), Wavefront OBJ  
                        (.obj), JavaScript (.js), JSON (.json), FreeSurfer  
                        (.surf,.curv), MZ3 (.mz3) [Default: VTK]  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/saveas.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("saveas", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def struct(self, *args, **kwargs):
        r"""
          Struct method for GIfTI objects  
            FORMAT s = struct(this)  
            this   -  GIfTI object  
            s      -  a structure containing public fields of the object  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/struct.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("struct", self._as_matlab_object(), *args, **kwargs)

    def subsasgn(self, *args, **kwargs):
        r"""
          Subscript assignment for GIfTI objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/subsasgn.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        r"""
          Subscript referencing for GIfTI objects  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/subsref.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def _base64(self, *args, **kwargs):
        r"""
          Base64 binary-to-text encoding/decoding scheme  
            FORMAT y = zstream('encode',x)  
            x        - data stream to encode (uint8)  
            y        - Base64-encoded data stream (uint8)  
            FORMAT y = zstream('decode',x)  
            x        - data stream to decode (uint8)  
            y        - Base-64 decoded data stream (uint8)  
           __________________________________________________________________________  
             
            This C-MEX file is a wrapper around:  
              https://stackoverflow.com/a/37109258  
            by polfosol: https://stackoverflow.com/users/5358284/polfosol  
             
            >> char(base64('decode',base64('encode',uint8('Base64'))))  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/base64.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("base64", self._as_matlab_object(), *args, **kwargs)

    def _base64decode(self, *args, **kwargs):
        r"""
         BASE64DECODE Perform base64 decoding on a string.  
             
              BASE64DECODE(STR) decodes the given base64 string STR.  
             
              Any character not part of the 65-character base64 subset set is silently  
              ignored.  
             
              This function is used to decode strings from the Base64 encoding specified  
              in RFC 2045 - MIME (Multipurpose Internet Mail Extensions).  The Base64  
              encoding is designed to represent arbitrary sequences of octets in a form  
              that need not be humanly readable.  A 65-character subset ([A-Za-z0-9+/=])  
              of US-ASCII is used, enabling 6 bits to be represented per printable  
              character.  
             
              See also BASE64ENCODE.  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/base64decode.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("base64decode", self._as_matlab_object(), *args, **kwargs)

    def _base64encode(self, *args, **kwargs):
        r"""
         BASE64ENCODE Perform base64 encoding on a string.  
             
              BASE64ENCODE(STR, EOL) encode the given string STR.  EOL is the line ending  
              sequence to use; it is optional and defaults to '\n' (ASCII decimal 10).  
              The returned encoded string is broken into lines of no more than 76  
              characters each, and each line will end with EOL unless it is empty.  Let  
              EOL be empty if you do not want the encoded string broken into lines.  
             
              STR and EOL don't have to be strings (i.e., char arrays).  The only  
              requirement is that they are vectors containing values in the range 0-255.  
             
              This function may be used to encode strings into the Base64 encoding  
              specified in RFC 2045 - MIME (Multipurpose Internet Mail Extensions).  The  
              Base64 encoding is designed to represent arbitrary sequences of octets in a  
              form that need not be humanly readable.  A 65-character subset  
              ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits to be represented per  
              printable character.  
             
              Examples  
              --------  
             
              If you want to encode a large file, you should encode it in chunks that are  
              a multiple of 57 bytes.  This ensures that the base64 lines line up and  
              that you do not end up with padding in the middle.  57 bytes of data fills  
              one complete base64 line (76 == 57*4/3):  
             
              If ifid and ofid are two file identifiers opened for reading and writing,  
              respectively, then you can base64 encode the data with  
             
                 while ~feof(ifid)  
                    fwrite(ofid, base64encode(fread(ifid, 60*57)));  
                 end  
             
              or, if you have enough memory,  
             
                 fwrite(ofid, base64encode(fread(ifid)));  
             
              See also BASE64DECODE.  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/base64encode.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("base64encode", self._as_matlab_object(), *args, **kwargs)

    def _freesurfer_read(self, *args, **kwargs):
        r"""
          Low level reader of FreeSurfer file  
            FORMAT this = freesurfer_read(filename)  
            filename    - FreeSurfer file  
             
            Read ASCII triangle surface file and part of binary mgh file.  
            See https://surfer.nmr.mgh.harvard.edu/fswiki/FileFormats  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/freesurfer_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("freesurfer_read", self._as_matlab_object(), *args, **kwargs)

    def _getdict(self, *args, **kwargs):
        r"""
          Dictionary of GIfTI/NIfTI stuff  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/getdict.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("getdict", self._as_matlab_object(), *args, **kwargs)

    def _gifti_read(self, *args, **kwargs):
        r"""
          Low level reader of GIfTI 1.0 files  
            FORMAT this = read_gifti_file(filename, this)  
            filename    - XML GIfTI filename  
            this        - structure with fields 'metaData', 'label' and 'data'.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/gifti_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("gifti_read", self._as_matlab_object(), *args, **kwargs)

    def _isintent(self, *args, **kwargs):
        r"""
          Correspondence between fieldnames and NIfTI intent codes  
            FORMAT ind = isintent(this,intent)  
            this    -  GIfTI object  
            intent  -  fieldnames  
            a       -  indices of found intent(s)  
            b       -  indices of dataarrays of found intent(s)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/isintent.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("isintent", self._as_matlab_object(), *args, **kwargs)

    def _mvtk_read(self, *args, **kwargs):
        r"""
          Read VTK formatted data from disk  
            FORMAT M = mvtk_read(filename)  
             
            filename - VTK-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            VTK File Formats Specifications:  
            http://www.vtk.org/VTK/img/file-formats.pdf  
              
            Requirements: zstream, base64decode  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/mvtk_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mvtk_read", self._as_matlab_object(), *args, **kwargs)

    def _mvtk_write(self, *args, **kwargs):
        r"""
          Write geometric data on disk using VTK file format (legacy/XML,ascii/binary)  
            FORMAT mvtk_write(M,filename,format)  
              
            M        - data structure  
            filename - output filename [Default: 'untitled']  
            format   - VTK file format: legacy, legacy-ascii, legacy-binary, xml,  
                       xml-ascii, xml-binary [Default: 'legacy-ascii']  
           __________________________________________________________________________  
              
            VTK File Formats Specifications:  
            http://www.vtk.org/VTK/img/file-formats.pdf  
              
            Requirements: zstream, base64encode  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/mvtk_write.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mvtk_write", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def _mz3_read(self, *args, **kwargs):
        r"""
          Read MZ3-formatted data from disk  
            FORMAT M = mz3_read(filename)  
             
            filename - MZ3-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            MZ3 Format Specification:  
            https://github.com/neurolabusc/surf-ice/tree/master/mz3  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/mz3_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mz3_read", self._as_matlab_object(), *args, **kwargs)

    def _mz3_write(self, *args, **kwargs):
        r"""
          Write MZ3-formatted data from disk  
            FORMAT mz3_write(M,filename,fmt)  
             
            M        - data structure  
            filename - MZ3 output filename [Default: 'untitled']  
            fmt      - compress data [Default: false]  
           __________________________________________________________________________  
              
            MZ3 Format Specification:  
            https://github.com/neurolabusc/surf-ice/tree/master/mz3  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/mz3_write.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("mz3_write", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def _obj_read(self, *args, **kwargs):
        r"""
          Read Wavefront OBJ-formatted data from disk  
            FORMAT M = obj_read(filename)  
             
            filename - OBJ-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            Wavefront OBJ Format Specification:  
            https://en.wikipedia.org/wiki/Wavefront_.obj_file  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/obj_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("obj_read", self._as_matlab_object(), *args, **kwargs)

    def _off_read(self, *args, **kwargs):
        r"""
          Read OFF-formatted data from disk  
            FORMAT M = off_read(filename)  
             
            filename - OFF-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            OFF Format Specification:  
            https://en.wikipedia.org/wiki/OFF_(file_format)  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/off_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("off_read", self._as_matlab_object(), *args, **kwargs)

    def _ply_read(self, *args, **kwargs):
        r"""
          Read PLY-formatted data from disk  
            FORMAT M = ply_read(filename)  
             
            filename - PLY-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            Stanford Triangle Format Specification:  
            https://en.wikipedia.org/wiki/PLY_%28file_format%29  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/ply_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("ply_read", self._as_matlab_object(), *args, **kwargs)

    def _stl_read(self, *args, **kwargs):
        r"""
          Read STL-formatted data from disk  
            FORMAT M = stl_read(filename)  
             
            filename - STL-formatted file name  
            M        - data structure  
           __________________________________________________________________________  
              
            STL Format Specification:  
            https://en.wikipedia.org/wiki/STL_%28file_format%29  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/stl_read.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("stl_read", self._as_matlab_object(), *args, **kwargs)

    def _xml_parser(self, *args, **kwargs):
        r"""
          XML Parser  
            FORMAT tree = xml_parser(xml)  
            xml         - XML-encoded string or filename of an XML document  
            tree        - struct array representation of the XML document  
           __________________________________________________________________________  
             
            This C-MEX file is a wrapper around yxml:  
              https://dev.yorhel.nl/yxml  
            by Yoran Heling:  
              https://yorhel.nl/  
             
            A pure MATLAB implementation of a similar XML parser is available at:  
              https://github.com/gllmflndn/xmltree  
           __________________________________________________________________________  
             
            The tree representation of the XML document is stores as a struct array  
            with fields:  
             - type:       'element' or 'chardata'  
             - value:      tag name of an 'element' or content of a 'chardata'  
             - attributes: key/value struct array of element's attributes  
             - children:   array of uids of element's children  
             - uid:        unique identifier (index in the struct array)  
             - parent:     uid of parent ([] if root)  
             
            This corresponds to an XML string of the sort:  
            <value key="value">value</value>  
             
            Processing instructions and comments are not reported.  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/xml_parser.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("xml_parser", self._as_matlab_object(), *args, **kwargs)

    def _zstream(self, *args, **kwargs):
        r"""
          Compress/decompress stream of bytes using Deflate/Inflate  
            FORMAT Z = zstream('C',D)  
            D        - data stream to compress (converted to uint8 if needed)  
            Z        - compressed data stream (uint8 vector)  
            FORMAT D = zstream('D',Z)  
            Z        - data stream to decompress (uint8 vector)  
            D        - decompressed data stream (uint8 vector)  
             
            If action is upper case ('C','D'), a zlib stream is used (zlib header  
            with an adler32 checksum). Otherwise, if action is lower case ('c','d'),  
            a raw deflate stream is assumed.  
           __________________________________________________________________________  
             
            This C-MEX file relies on:  
            * miniz, by Rich Geldreich  
              https://github.com/richgel999/miniz  
            Fallback Java implementation is adapted from:  
            * dzip/dunzip, by Michael Kleder  
              https://www.mathworks.com/matlabcentral/fileexchange/8899  
           __________________________________________________________________________  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/@gifti/private/zstream.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("zstream", self._as_matlab_object(), *args, **kwargs)
