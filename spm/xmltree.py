from spm.__wrapper__ import Runtime, MatlabClassWrapper


class xmltree(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          XMLTREE/XMLTREE Constructor of the XMLTree class  
            FORMAT tree = xmltree(varargin)  
              
            varargin - XML filename or XML string  
            tree     - XMLTree Object  
             
                tree = xmltree;             % creates a minimal XML tree: '<tag/>'  
                tree = xmltree('foo.xml');  % creates a tree from XML file 'foo.xml'  
                tree = xmltree('<tag>content</tag>') % creates a tree from string  
           __________________________________________________________________________  
             
            This is the constructor of the XMLTree class.   
            It creates a tree of an XML 1.0 file (after parsing) that is stored   
            using a Document Object Model (DOM) representation.  
            See http://www.w3.org/TR/REC-xml for details about XML 1.0.  
            See http://www.w3.org/DOM/ for details about DOM platform.  
           __________________________________________________________________________  
            
              Documentation for xmltree  
                 doc xmltree  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@xmltree/xmltree.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("xmltree", *args, **kwargs)
            
        super().__init__(_objdict)

    def _struct2xml(self, *args, **kwargs):
        """
          STRUCT2XML Convert a structure to an XML tree object  
            FORMAT tree = struct2xml(s,rootname)  
             
            Convert the structure S into an XML representation TREE (an XMLTree  
            object) with ROOTNAME as the root tag, if provided. Only conventional  
            objects (char, numeric) are accepted in S's fields.  
             
            Example  
               report = struct('name','John','marks',...  
                               struct('maths',17,'physics',12));  
               tree = struct2xml(report);  
               save(tree,'report.xml');  
             
            See also XMLTREE.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@xmltree/private/struct2xml.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("struct2xml", *args, **kwargs)

    def _xml_findstr(self, *args, **kwargs):
        """
         XML_FINDSTR Find one string within another  
              K = XML_FINDSTR(TEXT,PATTERN) returns the starting indices of any   
              occurrences of the string PATTERN in the string TEXT.  
             
              K = XML_FINDSTR(TEXT,PATTERN,INDICE) returns the starting indices   
              equal or greater than INDICE of occurrences of the string PATTERN  
              in the string TEXT. By default, INDICE equals to one.  
             
              K = XML_FINDSTR(TEXT,PATTERN,INDICE,NBOCCUR) returns the NBOCCUR   
              starting indices equal or greater than INDICE of occurrences of  
              the string PATTERN in the string TEXT. By default, INDICE equals  
              to one and NBOCCUR equals to Inf.  
             
              Examples  
                  s = 'How much wood would a woodchuck chuck?';  
                  xml_findstr(s,' ') returns [4 9 14 20 22 32]  
                  xml_findstr(s,' ',10) returns [14 20 22 32]  
                  xml_findstr(s,' ',10,1) returns 14  
             
              See also STRFIND, FINDSTR  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@xmltree/private/xml_findstr.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("xml_findstr", *args, **kwargs)

    def _xml_parser(self, *args, **kwargs):
        """
          XML (eXtensible Markup Language) Processor  
            FORMAT tree = xml_parser(xmlstr)  
             
            xmlstr  - XML string to parse  
            tree    - tree structure corresponding to the XML file  
           __________________________________________________________________________  
             
            xml_parser.m is an XML 1.0 (http://www.w3.org/TR/REC-xml) parser.  
            It aims to be fully conforming. It is currently not a validating   
            XML processor.  
             
            A description of the tree structure provided in output is detailed in   
            the header of this m-file.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@xmltree/private/xml_parser.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("xml_parser", *args, **kwargs)
