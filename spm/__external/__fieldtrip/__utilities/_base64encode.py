from spm.__wrapper__ import Runtime


def _base64encode(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/base64encode.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("base64encode", *args, **kwargs)
