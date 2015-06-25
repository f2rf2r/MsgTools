#    <OUTPUTFILENAME>
#    Created <DATE> from:
#        Messages = <INPUTFILENAME>
#        Template = <TEMPLATEFILENAME>
#        Language = <LANGUAGEFILENAME>
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from Messaging import Messaging
import Messaging as msg

class <MSGNAME> :
    ID = <MSGID>
    SIZE = <MSGSIZE>
    MSG_OFFSET = Messaging.hdrSize
    FIELDINFOS = <FIELDINFOS>
    
    @staticmethod
    def Create() :
        bytes = ctypes.create_string_buffer(<MSGNAME>.MSG_OFFSET + <MSGNAME>.SIZE)

        Messaging.hdr.SetSource(bytes, 0)
        Messaging.hdr.SetDestination(bytes, 0)
        Messaging.hdr.SetID(bytes, <MSGNAME>.ID)
        Messaging.hdr.SetLength(bytes, <MSGNAME>.SIZE)
        Messaging.hdr.SetPriority(bytes, 0)
        Messaging.hdr.SetType(bytes, 0)

        <INIT_CODE>
        return bytes

    @staticmethod
    def MsgName():
        return "<MSGNAME>"
    # Enumerations
    <ENUMERATIONS>
    # Accessors
    <ACCESSORS>

Messaging.Register("<MSGNAME>", <MSGNAME>.ID, <MSGNAME>)
