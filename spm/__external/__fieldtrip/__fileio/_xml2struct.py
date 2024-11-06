from spm.__wrapper__ import Runtime


def _xml2struct(*args, **kwargs):
    """
     Convert xml file into a MATLAB structure  
        [ s ] = xml2struct( file )  
         
        A file containing:  
        <XMLname attrib1="Some value">  
          <Element>Some text</Element>  
          <DifferentElement attrib2="2">Some more text</DifferentElement>  
          <DifferentElement attrib3="2" attrib4="1">Even more text</DifferentElement>  
        </XMLname>  
         
        Used to produce:  
        s.XMLname.Attributes.attrib1 = "Some value";  
        s.XMLname.Element.Text = "Some text";  
        s.XMLname.DifferentElement{1}.Attributes.attrib2 = "2";  
        s.XMLname.DifferentElement{1}.Text = "Some more text";  
        s.XMLname.DifferentElement{2}.Attributes.attrib3 = "2";  
        s.XMLname.DifferentElement{2}.Attributes.attrib4 = "1";  
        s.XMLname.DifferentElement{2}.Text = "Even more text";  
         
        Will produce (gp: to matche the output of xml2struct in XML4MAT, but note that Element(2) is empty):  
        Element: Some text   
        DifferentElement:  
           attrib2: 2   
           DifferentElement: Some more text   
        attrib1: Some value   
          
        Element:    
        DifferentElement:  
           attrib3: 2   
           attrib4: 1   
           DifferentElement: Even more text   
        attrib1:   
         
        Note the characters : - and . are not supported in structure fieldnames and  
        are replaced by _  
         
        Written by W. Falkena, ASTI, TUDelft, 21-08-2010  
        Attribute parsing speed increased by 40% by A. Wanner, 14-6-2011  
        2011/12/14 giopia: changes in the main function to make more similar to xml2struct of the XML4MAT toolbox, bc it's used by fieldtrip  
        2012/04/04 roboos: added the original license clause, see also http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=645#c11  
        2012/04/04 roboos: don't print the filename that is being read  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/xml2struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("xml2struct", *args, **kwargs)
