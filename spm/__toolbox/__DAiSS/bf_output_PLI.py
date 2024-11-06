from spm.__wrapper__ import Runtime


def bf_output_PLI(*args, **kwargs):
    """
      Generate a montage for source extraction, projects the sources one by  
        one and computes phase lag index on the fly, which is written out with no  
        need to call bf_write. Only one VOI allowed, which can be a sphere or a  
        mask image.  
         
        PLI computation using code published by Gerald Cooray (2010) Karolinska   
        Institutet: EFFECT OF DIABETES MELLITUS ON HUMAN BRAIN FUNCTION   
        (https://openarchive.ki.se/xmlui/bitstream/handle/10616/40241/ram_ber%C3%A4ttelse.pdf?sequence=1)  
        with a method based on Stam CJ, Nolte G, Daffertshofer A (Hum Brain Mapp 2007)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_PLI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_PLI", *args, **kwargs)
